import re
import sys
import pyperclip
from datetime import datetime
from pathlib import Path

def extract_ips(text):
    octet = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    # Cambiamos el lookahead final de (?![\d.]) a (?!\d|\.\d)
    ipv4_pattern = rf"(?<![\d.]){octet}(?:\.{octet}){{3}}(?!\d|\.\d)"
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
    # 1. Evaluar si el usuario pasó un archivo por consola
    if len(sys.argv) > 1:
        # Se pasó un argumento (ej: python analizador.py "C:\mis_logs\servidor.txt")
        log_path = Path(sys.argv[1])
        try:
            with open(log_path, "r", encoding="utf-8") as file:
                log_text = file.read()
            print(f"--- Analizando archivo: {log_path.name} ---\n")
        except (OSError, UnicodeDecodeError) as error:
            print(f"Error: no se pudo leer {log_path}: {error}", file=sys.stderr)
            return 1
            
    # 2. Si no se pasó ningún archivo, usamos el portapapeles
    else:
        print("--- No se indicó archivo. Analizando el portapapeles ---\n")
        log_text = pyperclip.paste()
        if not log_text.strip():
            print("El portapapeles está vacío. Por favor, copiá un texto o pasá un archivo.")
            return 1

    # La salida ya imprime directo en consola como solicitaste
    print("IPs encontradas:")
    for ip in extract_ips(log_text):
        print(f"  - {ip}")

    print("\nEmails encontrados:")
    for email in extract_emails(log_text):
        print(f"  - {email}")

    print("\nTimestamps encontrados:")
    for timestamp in extract_timestamps(log_text):
        print(f"  - {timestamp}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())