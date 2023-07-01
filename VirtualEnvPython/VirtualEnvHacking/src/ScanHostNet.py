## Todos los paquetes quedaran instalados en el Entorno Virtual
## Instalar el paquete nmap desde el Terminal con el siguiente comando pip install python-nmap

import nmap
import time

inicio = time.time() # inicializo la variable inicio con el tiempo actual

# Aqui va el codigo que queremos medir

nm = nmap.PortScanner()
    
    # Especificar el rango
ip_range = "192.168.1.0/24"
    
    # Realiza el Scaneo de la Red
nm.scan(ip_range,arguments='-sn') #An option is required for -s, most common are -sT (tcp scan), -sS (SYN scan), -sF (FIN scan), -sU (UDP scan) and -sn (Ping scan)'
print(nm.all_hosts())             #con el Argumento '-sn' son solo 3 seg... sin argumento son 154 seg

fin = time.time() # inicializo la variable fin con el tiempo actual
Tiempo_Ejecucion = fin - inicio
print(f"Tiempo de Ejecucion: {Tiempo_Ejecucion:.5f} segundos") # ".5f" significas 5 cifras decimales despues del punto

## Tiempo de Ejecucion: 3.15018 segundos