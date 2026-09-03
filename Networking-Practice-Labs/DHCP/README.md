# DHCP Lab

Lab de Packet Tracer configurando un pool DHCP en un router Cisco, 
verificando bindings y leases desde router y cliente, y relay DHCP 
cuando corresponde.

## Archivos
- DHCPproyecto.pkt — proyecto de Packet Tracer
- Respuesta.txt — respuestas a la consigna de la actividad

## Verificación
- `show ip dhcp binding` → lista los leases DHCP activos en el router
- `show running-config | section dhcp` → muestra la configuración del pool
- En el cliente: se verifica IP asignada y gateway por defecto

## Qué aprendí
- Configuración básica de un servidor DHCP en Cisco IOS
- Cómo verificar y diagnosticar problemas comunes (exclusiones 
  faltantes, gateway incorrecto)

## Próximo desafío
Agregar una reservation DHCP para una MAC específica.

