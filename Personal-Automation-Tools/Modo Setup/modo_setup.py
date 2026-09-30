import webbrowser
import time
import os

print("Iniciando Modo Setup...")

# 1. ABRIR GITHUB DESKTOP
# Buscamos la ruta automática donde se instala GitHub Desktop en Windows
ruta_github = os.path.join(os.environ['LOCALAPPDATA'], 'GitHubDesktop', 'GitHubDesktop.exe')

try:
    # startfile() le hace "doble clic" invisible al programa
    os.startfile(ruta_github)
    print("GitHub Desktop abriendo...")
except FileNotFoundError:
    print("Error: No se encontró GitHub Desktop en tu PC.")
    print(f"Ruta buscada: {ruta_github}")

# Hacemos una pausa de 1 segundo para dejar que la PC respire 
# mientras arranca GitHub antes de abrir el navegador
time.sleep(1)

# 2. ABRIR EL NAVEGADOR
paginas = [
    'https://music.youtube.com',
    'https://www.google.com',  # Pestaña en blanco/buscador
    'https://gemini.google.com'
    
]

print("Abriendo pestañas...")
for url in paginas:
    webbrowser.open(url)
    time.sleep(0.5) 

print("¡Setup completado!")