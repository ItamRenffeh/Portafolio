import re
import os
import sys
import json
import csv
import time
import requests
import argparse
from pathlib import Path
from datetime import datetime

# ==========================================
# 1. FUNCIONES DE EXTRACCIÓN
# ==========================================
def extract_timestamps(text):
    date = r"\d{4}(?:-\d{2}-\d{2}|/\d{2}/\d{2})"
    time_pattern = r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d"
    timezone = r"(?:Z|[+-](?:[01]\d|2[0-3]):?[0-5]\d)?"
    pattern = rf"(?<!\w){date}[ T]{time_pattern}{timezone}(?![\w.:+-])"

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

def extraer_iocs(texto_log):
    octet = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    patron_ip = rf"(?<![\d.]){octet}(?:\.{octet}){{3}}(?!\d|\.\d)"
    patron_email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"

    ips = list(set(re.findall(patron_ip, texto_log)))
    emails = list(set(re.findall(patron_email, texto_log)))
    fechas = extract_timestamps(texto_log)
    
    return ips, emails, fechas

# ==========================================
# 2. ENRIQUECIMIENTO CON ABUSEIPDB
# ==========================================
def enriquecer_ips(lista_ips, api_key):
    ips_enriquecidas = []
    print("\n🔍 Consultando inteligencia de amenazas en AbuseIPDB...")
    
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    url = "https://api.abuseipdb.com/api/v2/check"
    
    for ip in lista_ips:
        if ip.startswith(("192.168.", "10.", "127.", "172.")):
            ips_enriquecidas.append({
                "IP": ip, 
                "Pais": "Red Local", 
                "ISP": "Privado", 
                "Peligro": "Limpia (0%)"
            })
            continue
            
        try:
            parametros = {'ipAddress': ip, 'maxAgeInDays': '90'}
            res = requests.get(url, headers=headers, params=parametros, timeout=10)
            res.raise_for_status()
            
            datos = res.json()['data']
            score = datos.get('abuseConfidenceScore', 0)
            pais = datos.get('countryCode', 'Desc.')
            isp = datos.get('isp', 'Desc.')
            
            if score == 0:
                nivel = "Limpia (0%)"
            elif score < 50:
                nivel = f"Sospechosa ({score}%)"
            else:
                nivel = f"Maliciosa ({score}%)"
                
            ips_enriquecidas.append({
                "IP": ip,
                "Pais": pais,
                "ISP": isp,
                "Peligro": nivel
            })
            
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error al consultar {ip}: {e}")
            ips_enriquecidas.append({"IP": ip, "Pais": "Error", "ISP": "Error", "Peligro": "Desconocido"})
            
    return ips_enriquecidas

# ==========================================
# 3. EXPORTACIÓN DE DATOS
# ==========================================
def exportar_csv(datos_ips, emails, ruta_salida):
    try:
        with open(f"{ruta_salida}_ips.csv", "w", encoding="utf-8", newline="") as arch:
            if datos_ips:
                columnas = ["IP", "Pais", "ISP", "Peligro"]
                escritor = csv.DictWriter(arch, fieldnames=columnas)
                escritor.writeheader()
                escritor.writerows(datos_ips)
        print(f"✅ Reporte CSV de IPs guardado en: {ruta_salida}_ips.csv")
    except Exception as e:
        print(f"❌ Error al guardar CSV: {e}")

def exportar_json(datos_ips, emails, fechas, ruta_salida):
    try:
        reporte_maestro = {
            "metadatos": {
                "eventos_totales": len(fechas),
                "emails_detectados": emails
            },
            "indicadores_red": datos_ips
        }
        
        with open(f"{ruta_salida}.json", "w", encoding="utf-8") as arch:
            json.dump(reporte_maestro, arch, indent=4)
        print(f"✅ Reporte JSON maestro guardado en: {ruta_salida}.json")
    except Exception as e:
        print(f"❌ Error al guardar JSON: {e}")

# ==========================================
# 4. MOTOR PRINCIPAL CLI
# ==========================================
def main():
    parser = argparse.ArgumentParser(description="Analizador de IoCs con AbuseIPDB")
    parser.add_argument("archivo", help="Ruta al archivo de log (.txt)")
    parser.add_argument("--formato", choices=['csv', 'json', 'ambos'], default='ambos')
    # Ya no es required=True, damos la opción de usar la variable de entorno
    parser.add_argument("--apikey", help="API Key de AbuseIPDB (o usar variable de entorno ABUSEIPDB_KEY)")
    args = parser.parse_args()

    # LÓGICA DE SEGURIDAD: Priorizar argumento, sino buscar en entorno
    api_key = args.apikey or os.environ.get("ABUSEIPDB_KEY")
    
    if not api_key:
        print("❌ Error: No se proporcionó API key.")
        print("💡 Solución: Usar el argumento --apikey o definir la variable de entorno ABUSEIPDB_KEY.")
        sys.exit(1)

    ruta_log = Path(args.archivo)

    if not ruta_log.is_file():
        print(f"❌ Error: El archivo '{ruta_log}' no existe.")
        sys.exit(1)

    print(f"📂 Leyendo el archivo: {ruta_log.name}...")
    try:
        with open(ruta_log, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except Exception as e:
        print(f"❌ No se pudo leer el archivo. Error: {e}")
        sys.exit(1)

    ips, emails, fechas = extraer_iocs(texto)
    print(f"🎯 Extraídos: {len(ips)} IPs únicas, {len(emails)} Emails, {len(fechas)} Marcas de tiempo validadas.")

    ips_enriquecidas = enriquecer_ips(ips, api_key)

    nombre_salida = ruta_log.stem + "_reporte"
    
    if args.formato in ['csv', 'ambos']:
        exportar_csv(ips_enriquecidas, emails, nombre_salida)
    
    if args.formato in ['json', 'ambos']:
        exportar_json(ips_enriquecidas, emails, fechas, nombre_salida)
        
    print("\n🚀 ¡Análisis completado con éxito!")

if __name__ == "__main__":
    main()