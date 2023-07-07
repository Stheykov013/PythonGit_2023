import re # Libreria de Expresiones Regulares
from colorama import Fore # Color al Script
import requests # Para hacer peticiones HTTPS a una webpage

# Almacenar el link de la url a scraping en una variable
website_scraping = "https://www.vulnhub.com"
# Extraer del HTTPS
resultado = requests.get(website_scraping)
# Convertir en formato texto resultado
content = resultado.text
# imprimimos contenido
# print(content) # Todo el contenido HTML de la webpage
# Las constantes de cadena pueden precederse de una r que significa raw (en inglés); algo así como cruda o literal en español.
patron = r"/entry/[\w-]*" # Constante de cadena r"/entry/[\w-]*" literal tomara todo talcual /entry/[\w-]*
maquinas_repetidas = re.findall(patron,str(content)) # Buscamos en content lo que tenga ese patron repetido despues de /entry/
#print(maquinas_repetidas)

sin_duplicados = list(set(maquinas_repetidas)) # Crea una lista sin duplicados

# print(sin_duplicados)

maquina_final = []

for i in sin_duplicados:
    nombre_maquina = i.replace("/entry/","")
    maquina_final.append(nombre_maquina)
    print(nombre_maquina)    


