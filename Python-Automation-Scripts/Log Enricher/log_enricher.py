import re
import ipaddress
import time
import requests
from bs4 import BeautifulSoup

# Expresiones regulares para extracción
IPV4_REGEX = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

def obtener_ips_desde_web(url: str) -> set:
    """
    Realiza web scraping sobre una URL para extraer texto y parsear IPs únicas.
    """
    print(f"[*] Obteniendo datos desde: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ThreatHunting-Script/1.0"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Error al consultar la URL: {e}")
        return set()

    # Parsear HTML / Texto con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    texto_plano = soup.get_text()

    # Extraer todas las coincidencias de IPs
    coincidencias = re.findall(IPV4_REGEX, texto_plano)
    
    # Filtrar IPs públicas válidas (descartando rangos privados como 192.168.x.x, 10.x.x.x, 127.0.0.1)
    ips_publicas = set()
    for ip in coincidencias:
        try:
            ip_obj = ipaddress.ip_address(ip)
            if not ip_obj.is_private and not ip_obj.is_loopback and not ip_obj.is_multicast:
                ips_publicas.add(ip)
        except ValueError:
            continue

    print(f"[+] Se encontraron {len(ips_publicas)} IPs públicas únicas.")
    return ips_publicas

def enriquecer_ip(ip: str) -> dict:
    """
    Consulta la API gratuita de IP-API para obtener metadatos de red y geolocalización.
    """
    # Solicitamos campos específicos: país, ciudad, ISP, ASN, si es hosting/proxy y estado
    api_url = f"http://ip-api.com/json/{ip}?fields=status,message,country,city,isp,as,hosting,query"
    
    try:
        res = requests.get(api_url, timeout=5)
        if res.status_code == 200:
            datos = res.json()
            if datos.get("status") == "success":
                return {
                    "ip": datos.get("query"),
                    "pais": datos.get("country", "Desconocido"),
                    "ciudad": datos.get("city", "Desconocido"),
                    "isp": datos.get("isp", "Desconocido"),
                    "asn": datos.get("as", "Desconocido"),
                    "es_datacenter_hosting": datos.get("hosting", False)
                }
    except requests.RequestException:
        pass
    
    return {"ip": ip, "error": "No se pudo enriquecer"}

def main():
    # URL de ejemplo: Feed público de Abuse.ch (Feodo Tracker - IPs activas de C2 / Botnets)
    # También puedes usar URLs con texto plano de honeypots o logs públicos.
    url_feed = "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

    ips = obtener_ips_desde_web(url_feed)

    # Limitar a las primeras 5 IPs para la demostración (evita superar rate limits de la API)
    ips_a_analizar = list(ips)[:5]

    print("\n[+] Enriqueciendo IPs con datos de Threat Intelligence & Red:\n")
    print(f"{'IP':<16} | {'PAÍS':<15} | {'CIUDAD':<15} | {'HOSTING/DC':<10} | {'ISP/ORG'}")
    print("-" * 85)

    for ip in ips_a_analizar:
        info = enriquecer_ip(ip)
        if "error" not in info:
            print(f"{info['ip']:<16} | {info['pais']:<15} | {info['ciudad']:<15} | {str(info['es_datacenter_hosting']):<10} | {info['isp'][:25]}")
        else:
            print(f"{ip:<16} | Error en consulta")
        
        # Pausa para respetar el rate limit de la API pública (máx 45 req/min)
        time.sleep(1.4)

if __name__ == "__main__":
    main()