

def es_ip_valida(ip):
    # Divide la IP en sus cuatro partes usando el punto como separador.
    partes = ip.strip().split(".")

    # Una IPv4 debe tener exactamente cuatro partes.
    if len(partes) != 4:
        return False

    # Todas las partes deben estar formadas únicamente por dígitos.
    if any(not parte.isdigit() for parte in partes):
        return False

    # Convierte cada parte de texto a un número entero.
    octetos = [int(parte) for parte in partes]

    # Cada octeto debe estar dentro del rango permitido: 0 a 255.
    return all(0 <= octeto <= 255 for octeto in octetos)

def cantidad_apariciones(Lista_ip):
    # Crea un diccionario vacío donde la IP será la clave y las apariciones
    # serán el valor asociado a esa clave.
    diccionario_ips = {}

    # Recorre cada IP recibida en la lista.
    for ip in Lista_ip:
        # Elimina espacios al principio o al final para que, por ejemplo,
        # " 8.8.8.8 " se cuente como "8.8.8.8".
        ip = ip.strip()

        # Solo agrega al diccionario las IPs que cumplen las reglas de IPv4.
        if es_ip_valida(ip):
            # get() devuelve la cantidad actual o 0 si la IP todavía no existe.
            # Luego suma una aparición y guarda el resultado en el diccionario.
            diccionario_ips[ip] = diccionario_ips.get(ip, 0) + 1

    # Devuelve el diccionario con las IPs válidas y sus cantidades.
    return diccionario_ips
            
       
def mostrar_resultado(diccionario_ips):
    # items() obtiene pares en la forma (clave, valor), por ejemplo:
    # ("8.8.8.8", 3).
    # sorted() recibe esos pares y crea una nueva lista ordenada.
    # key indica qué parte de cada par se usará para ordenar.
    # lambda x: x[1] es una función pequeña: recibe un par x y devuelve
    # su segundo elemento, que en este caso es la cantidad de apariciones.
    # reverse=True ordena de mayor a menor cantidad.
    ordenado = sorted(diccionario_ips.items(), key=lambda x: x[1], reverse=True)

    # Recorre la lista ya ordenada y separa cada par en ip y cantidad.
    for ip, cantidad in ordenado:
        print(f"{ip}: {cantidad} veces")
        
        
def ip_mas_repetida(diccionario_ips):
    # Si no hay IPs, no se puede calcular un máximo.
    if not diccionario_ips:
        return []

    # values() obtiene solo las cantidades y max() encuentra la mayor.
    max_valor = max(diccionario_ips.values())

    # Devuelve todas las IPs cuya cantidad coincide con la mayor cantidad.
    return [ip for ip, cant in diccionario_ips.items() if cant == max_valor]

if __name__ == "__main__":
    # Caso de prueba: incluye IPs repetidas, un empate, límites permitidos,
    # espacios, partes faltantes o sobrantes, letras y valores fuera de rango.
    ips = [
        "192.168.1.10", "10.0.0.5", "192.168.1.10", "45.170.23.11",
        "10.0.0.5", "192.168.1.10", "45.170.23.11", "45.170.23.11",
        "8.8.8.8", "45.170.23.11", " 8.8.8.8 ",
        "0.0.0.0", "0.0.0.0", "255.255.255.255",
        "192.168.1", "192.168.1.1.1", "192.168.one.1",
        "256.168.1.1", "192.168.1.256", "-1.168.1.1",
        "192..1.1", "",
    ]

    # Cuenta únicamente las IPs válidas de la lista.
    diccionario_ips = cantidad_apariciones(ips)

    # Muestra las IPs desde la más frecuente hasta la menos frecuente.
    mostrar_resultado(diccionario_ips)

    # Obtiene todas las IPs que tienen la mayor cantidad de apariciones.
    top = ip_mas_repetida(diccionario_ips)

    print(f"\nIP(s) más repetida(s): {', '.join(top)}")



