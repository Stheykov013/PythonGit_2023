# importamos libreria de Expresiones Regulares
import  re 
# importamos lib para poner colores al Script
from colorama import Fore
# importamos libreria de prticiones HTTPS a webpage
import requests
# pagina a Scraping
webpage_scraping = "https://www.crunchyroll.com/"
# Extraer del HTTPS
resultado = requests.get(webpage_scraping)
# Convertir en Texto resultado
content = resultado.text
# print(content)
# Patron
patron = r"/es/series/[\w-]*" # /entry/[\w-]*
# Filtramos repetido
series_repetidas = re.findall(patron,str(content))
print(series_repetidas)
# Creamos una lista Sin duplicados
sin_duplicados = list(set(series_repetidas))

series_final = []
for i in sin_duplicados:
     nombre_serie = i.replace("/es/series/","")
     series_final.append(nombre_serie)
     print(nombre_serie)
