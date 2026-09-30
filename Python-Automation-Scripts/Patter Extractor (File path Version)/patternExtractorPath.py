import re
import sys
from datetime import datetime
from pathlib import Path


def extract_ips(text):
    octet = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    ipv4_pattern = rf"(?<![\d.]){octet}(?:\.{octet}){{3}}(?![\d.])"
    return re.findall(ipv4_pattern, text)


def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def extract_timestamps(text):
    date = (
        r"\d{4}(?:-\d{2}-\d{2}|/\d{2}/\d{2})"
    )
    time = r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d"
    timezone = r"(?:Z|[+-](?:[01]\d|2[0-3]):?[0-5]\d)?"
    pattern = rf"(?<!\w){date}[ T]{time}{timezone}(?![\w.:+-])"

    timestamps = []
    for match in re.finditer(pattern, text):
        timestamp = match.group()
        date_format = "%Y-%m-%d" if timestamp[4] == "-" else "%Y/%m/%d"
        try:
            datetime.strptime(timestamp[:10], date_format)
        except ValueError:
            continue
        timestamps.append(timestamp)

    return timestamps


def main():
    log_path = Path(__file__).with_name("log.txt")

    try:
        with open(log_path, "r", encoding="utf-8") as file:
            log_text = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error: could not read {log_path}: {error}", file=sys.stderr)
        return 1

    print("IPs found:")
    for ip in extract_ips(log_text):
        print(f"  - {ip}")

    print("\nEmails found:")
    for email in extract_emails(log_text):
        print(f"  - {email}")

    print("\nTimestamps found:")
    for timestamp in extract_timestamps(log_text):
        print(f"  - {timestamp}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())