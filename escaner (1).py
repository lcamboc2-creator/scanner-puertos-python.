import socket
from datetime import datetime

def escanear_puertos():
    print("=" * 40)
    print("      ESCÁNER DE PUERTOS TCP BÁSICO      ")
    print("=" * 40)
    
    # 1. Ingresar dirección IP
    ip_objetivo = input("1. Ingrese la dirección IP a escanear: ").strip()
    
    try:
        # 2 y 3. Ingresar puerto inicial y final
        puerto_inicio = int(input("2. Ingrese el puerto inicial (ej. 20): "))
        puerto_fin = int(input("3. Ingrese el puerto final (ej. 100): "))
    except ValueError:
        print("\n[!] Error: Los puertos deben ser números enteros.")
        return

    # 4. Realizar el escaneo
    print(f"\n[+] Iniciando escaneo en {ip_objetivo} del puerto {puerto_inicio} al {puerto_fin}...")
    tiempo_inicio = datetime.now()
    
    puertos_abiertos = []

    try:
        for puerto in range(puerto_inicio, puerto_fin + 1):
            # Crear socket TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4) # Tiempo de espera para agilizar el escaneo
            
            # connect_ex devuelve 0 si la conexión fue exitosa (puerto abierto)
            resultado = s.connect_ex((ip_objetivo, puerto))
            
            if resultado == 0:
                puertos_abiertos.append(puerto)
                # 5. Mostrar los puertos abiertos en tiempo real
                print(f" -> Puerto {puerto}: ABIERTO")
            
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Escaneo interrumpido por el usuario.")
    except socket.gaierror:
        print("\n[!] Error: La dirección IP no es válida o no se pudo resolver.")
        return
    except socket.error:
        print("\n[!] Error: No se pudo conectar alfanuméricamente con el servidor.")
        return

    tiempo_fin = datetime.now()
    duracion = tiempo_fin - tiempo_inicio

    # 6. Mostrar un resumen de los resultados
    print("\n" + "=" * 40)
    print("          RESUMEN DE RESULTADOS          ")
    print("=" * 40)
    print(f"[*] IP Objetivo: {ip_objetivo}")
    print(f"[*] Tiempo total de escaneo: {duracion}")
    if puertos_abiertos:
        print(f"[*] Puertos abiertos encontrados ({len(puertos_abiertos)}):")
        print(f"    {puertos_abiertos}")
    else:
        print("[*] No se encontraron puertos abiertos en el rango especificado.")
    print("=" * 40)

if __name__ == "__main__":
    escanear_puertos()
