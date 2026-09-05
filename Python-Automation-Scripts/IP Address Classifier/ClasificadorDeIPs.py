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

def es_ip_privada(ip):
    # Primero comprobamos que la IP esté bien escrita y tenga valores válidos.
    if not es_ip_valida(ip):
        return False

    # Divide la IP en sus cuatro partes usando el punto como separador.
    partes = ip.strip().split(".")

    # Convierte cada parte de texto a un número entero.
    octetos = [int(parte) for parte in partes]

    # Todas las IP que comienzan por 10 son privadas.
    if octetos[0] == 10:
        return True

    # En el rango 172, solo son privadas las IP de 172.16 a 172.31.
    elif octetos[0] == 172 :
        if 16 <= octetos[1] <= 31:
            return True

    # Las IP que comienzan por 192.168 son privadas.
    elif octetos[0] == 192 and octetos[1] == 168:
        return True

    # Si no pertenece a ninguno de los rangos anteriores, es pública.
    return False

def clasificar_ip(ip):
    if not es_ip_valida(ip):
        return "IP inválida"
    elif es_ip_privada(ip):
        return "IP privada"
    else:
        return "IP pública"

# Pregunta cuántas IPs quiere ingresar el usuario.
cantidad_ips = int(input("¿Cuántas IPs quieres revisar? "))

# Repite el proceso hasta recibir la cantidad de IPs indicada.
for numero in range(cantidad_ips):
    ip = input(f"Ingresa la IP número {numero + 1}: ")
    print(ip, "->", clasificar_ip(ip))






