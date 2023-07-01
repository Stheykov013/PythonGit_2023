## Instalar el paquete nmap desde el Terminal con el siguiente comando pip install python-nmap

import nmap #libreria de scaneo de red 
import json # libreria json
import time

inicio=time.time()

def get_open_ports(target):
    scanner = nmap.PortScanner()
    # realiza un scanneo desde 1 - 65535
    scanner.scan(target,
                 arguments='-p- --open')
    open_ports = {}
    #recorre todos los host detectados en la red
    for host in scanner.all_hosts():
        #recorre todos los puertos del host actual
        for proto in scanner[host].all_protocols():
            #consultamos en numero de puerto
            ports = scanner[host][proto].keys()
            open_ports[host] = list(ports)
    return open_ports




#rango de ips
target_host = '192.168.1.1-254'
open_ports = get_open_ports(target_host)

print(f'los puertos abiertos en {target_host} son:')

print(json.dumps(open_ports,indent=10))


fin=time.time()
Tiempo_Ejecucion=fin-inicio
print(f"Tiempo de Ejecucion {Tiempo_Ejecucion:.5f} Segundos")

## Tiempo de Ejecucion 493.79678 Segundos