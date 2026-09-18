import re


def extract_ips(text):
    octet = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    ipv4_pattern = rf"\b{octet}(?:\.{octet}){{3}}\b"
    return re.findall(ipv4_pattern, text)


def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def extract_timestamps(text):
    date = (
        r"\d{4}(?:-\d{2}-\d{2}|/\d{2}/\d{2})"
    )
    time = r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d"
    pattern = rf"\b{date}(?:[ T]){time}(?:Z|[+-]\d{{2}}:?\d{{2}})?(?!\w)"
    return re.findall(pattern, text)


if __name__ == "__main__":
    log_text = """
    2026-09-08 02:14:10 - Failed login attempt from 45.170.23.11
    2026-09-08 02:15:01 - Success: user j.gomez_log logged in from 45.170.23.11
    Contact: soporte@empresa.com for questions
    2026-09-08 03:12:45 - Alert sent to admin.security@empresa.com
    Unrelated line without any pattern.
    Internal IP 10.0.2.50 attempted login at 2026-09-08 08:05:00
    """

    print("IPs found:")
    for ip in extract_ips(log_text):
        print(f"  - {ip}")

    print("\nEmails found:")
    for email in extract_emails(log_text):
        print(f"  - {email}")

    print("\nTimestamps found:")
    for timestamp in extract_timestamps(log_text):
        print(f"  - {timestamp}")

    edge_cases = """
    Text without patterns: normal service restart.
    ISO: 2026-09-08T08:05:00Z
    Slash format: 2026/09/08 08:05:00
    Invalid date: 2026-13-40 25:61:99
    Valid boundary time: 2026-12-31 23:59:59
    Invalid IP: 999.300.1.2
    Invalid email: user@company
    """

    print("\nNoisy input tests:")
    print("IPs:", extract_ips(edge_cases))
    print("Emails:", extract_emails(edge_cases))
    print("Timestamps:", extract_timestamps(edge_cases))