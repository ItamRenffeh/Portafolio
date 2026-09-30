import sys
import requests
import xml.etree.ElementTree as ET
import webbrowser
from pathlib import Path
import bs4 

def obtener_cotizaciones_html():
    tipos_dolar = {
        "Oficial": "https://dolarapi.com/v1/dolares/oficial",
        "Blue": "https://dolarapi.com/v1/dolares/blue",
        "MEP": "https://dolarapi.com/v1/dolares/bolsa"
    }
    
    html = '<div class="tarjeta cotizaciones"><h2>💵 Cotizaciones del Día</h2><ul>'
    
    try:
        for nombre, url in tipos_dolar.items():
            res = requests.get(url, timeout=5)
            res.raise_for_status()
            datos = res.json()
            
            # Formateamos los números para que queden prolijos
            compra = f"${datos['compra']:.0f}"
            venta = f"${datos['venta']:.0f}"
            
            html += f'<li><strong>Dólar {nombre}:</strong> Compra {compra} / Venta {venta}</li>'
            
        html += '</ul></div>'
        return html
    except Exception as e:
        return f'<div class="tarjeta error"><h2>💵 Cotizaciones</h2><p>Error al cargar: {e}</p></div>'

def obtener_github_html():
    url = "https://github.com/trending/python?since=daily"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        repositorios = soup.select('article.Box-row')
        
        html = '<div class="tarjeta github"><h2>🐍 GitHub Trending (Python)</h2><ul>'
        
        for repo in repositorios[:5]:
            enlace = repo.select_one('h2 a')
            # Buscamos la etiqueta <p> que contiene la descripción
            etiqueta_desc = repo.select_one('p')
            
            if enlace:
                titulo = enlace.getText().strip().replace(' ', '').replace('\n', '')
                link = f"https://github.com{enlace.get('href')}"
                
                # Algunas veces los repositorios no le ponen descripción, hay que atajar ese error
                descripcion = etiqueta_desc.getText().strip() if etiqueta_desc else "Sin descripción proporcionada."
                
                # Armamos el bloque de HTML separando título de descripción
                html += f'<li style="margin-bottom: 16px;">'
                html += f'<a href="{link}" target="_blank" style="font-weight: 600; font-size: 1.05rem;">{titulo}</a><br>'
                html += f'<span style="font-size: 0.85rem; color: #a0a0a0; display: block; margin-top: 4px;">{descripcion}</span>'
                html += f'</li>'
                
        html += '</ul></div>'
        return html
    except Exception as e:
        return f'<div class="tarjeta error"><h2>🐍 GitHub</h2><p>Error al cargar: {e}</p></div>'

def obtener_clima_html(ciudad="Bahia Blanca"):
    try:
        url = f"https://wttr.in/{ciudad}?format=j1"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        
        datos = res.json()
        condicion = datos['current_condition'][0]
        hoy = datos['weather'][0]
        
        html = f"""
        <div class="tarjeta clima">
            <h2>📍 Clima en {ciudad.title()}</h2>
            <p><strong>🌡️ Actual:</strong> {condicion['temp_C']}°C</p>
            <p><strong>📉 Mín / Máx:</strong> {hoy['mintempC']}°C / {hoy['maxtempC']}°C</p>
            <p><strong>💨 Viento:</strong> {condicion['windspeedKmph']} km/h</p>
            <p><strong>🌧️ Prob. Lluvia:</strong> {hoy['hourly'][4]['chanceofrain']}% (Tarde)</p>
        </div>
        """
        return html
    except Exception as e:
        return f'<div class="tarjeta error"><h2>📍 Clima</h2><p>Error al cargar: {e}</p></div>'

def obtener_noticias_html(titulo_seccion, url_rss, limite=5):
    try:
        res = requests.get(url_rss, timeout=10)
        res.raise_for_status()
        arbol = ET.fromstring(res.content)
        articulos = arbol.findall('.//item')
        
        html = f'<div class="tarjeta noticias"><h2>📰 {titulo_seccion}</h2><ul>'
        for articulo in articulos[:limite]:
            titulo = articulo.find('title').text
            link = articulo.find('link').text
            html += f'<li><a href="{link}" target="_blank">{titulo}</a></li>'
        html += '</ul></div>'
        
        return html
    except Exception as e:
        return f'<div class="tarjeta error"><h2>📰 {titulo_seccion}</h2><p>Error al cargar: {e}</p></div>'

def main():
    ciudad = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Bahia Blanca"
    
    # 1. Recopilar todos los bloques
    bloque_clima = obtener_clima_html(ciudad)
    bloque_cotizaciones = obtener_cotizaciones_html()
    bloque_github = obtener_github_html()
    bloque_thn = obtener_noticias_html("The Hacker News", "https://feeds.feedburner.com/TheHackersNews")
    bloque_ciberseguridad = obtener_noticias_html("ESET Ciberseguridad", "https://www.welivesecurity.com/la-es/feed/")
    bloque_argentina = obtener_noticias_html("Argentina", "https://news.google.com/rss?hl=es-419&gl=AR&ceid=AR:es-419")
    bloque_global = obtener_noticias_html("Globales", "https://news.google.com/rss/headlines/section/topic/WORLD?hl=es-419&gl=AR&ceid=AR:es-419")

    # 2. Ensamblar la página web
    pagina_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Resumen Diario</title>
        <style>
            /* MANTENÉ TU CSS ANTERIOR ACÁ Y AGREGÁ ESTOS COLORES: */
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #121212;
                color: #e0e0e0;
                margin: 0;
                padding: 20px;
            }}
            h1 {{ text-align: center; color: #ffffff; margin-bottom: 30px; }}
            .contenedor {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
                gap: 20px;
                max-width: 1200px;
                margin: 0 auto;
            }}
            .tarjeta {{
                background-color: #1e1e1e;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                border-top: 4px solid #4da6ff;
            }}
            /* COLORES DE LOS BORDES */
            .clima {{ border-top-color: #ff9900; }}
            .cotizaciones {{ border-top-color: #00cc66; }} /* Verde billete */
            .github {{ border-top-color: #999999; }} /* Gris código */
            .error {{ border-top-color: #ff3333; }}
            
            h2 {{ margin-top: 0; font-size: 1.2rem; border-bottom: 1px solid #333; padding-bottom: 10px; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 12px; line-height: 1.4; }}
            a {{ color: #66b3ff; text-decoration: none; transition: color 0.2s; }}
            a:hover {{ color: #99ccff; text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>Tablero de Control Diario</h1>
        <div class="contenedor">
            {bloque_clima}
            {bloque_cotizaciones}
            {bloque_github}
            {bloque_thn}
            {bloque_ciberseguridad}
            {bloque_argentina}
            {bloque_global}
        </div>
    </body>
    </html>
    """

    ruta_archivo = Path(__file__).parent / "resumen_generado.html"
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(pagina_html)

    ruta_segura = ruta_archivo.absolute().as_uri()
    webbrowser.open(ruta_segura)

if __name__ == "__main__":
    main()