def app ():
    # Crear un Archivo 
        # 1. Siempre que se usa open se debe cerrar
    archivo = open("archivo.txt","w") # w es permiso de escritura, si no existe lo crea
    
    # Generar numeros en el archivo
    for item in range(0,20):
        archivo.write(f"Numero: {str(item)}\r\n")
    
    # Cerrar Archivo
        # 2. Cerrar Archivo
    archivo.close()
    
app()

## Codigo propio 01 

# Tiempo de Ejecucion
import time
# Iniciamos el reloj
inicio = time.time()

def app01():
    
    #variable para while
    pregunta1 = True
    # se crea el ciclo while
    while pregunta1:
        nombre_archivo = input("Escriba 'cerrar' para terminar \r\n"+"Escriba el nombe del archivo que tendra formato .txt \r\n")
        if nombre_archivo == "cerrar": 
            pregunta1 = False # se cierra el while
        else:
            archivo = open(f"{nombre_archivo}.txt","w") # se cre el archivo con en nombre digitado. 1. Cerrar el Open
            for item in range (0,20):   # En el archivo crea numeros en el rango del 0 al 19
                archivo.write(f"Numero: {str(item)}\r\n") # Escribre Numero: 0 - 19 en el archivo y es de tipo string 
            archivo.close()    # 2. Open cerrado
            
app01()

#finalizamos el reloj
fin = time.time()
# calculamos en timepo de ejecucion
tiempo_ejecucion = fin - inicio
print(f"Este es el tiempo de ejecucion {tiempo_ejecucion:.5f} segundos") # {tiempo_ejecucion:.5f} .5f = 5 cifras despues del . 


# Escribir en un Archivo Forma1 open/close

# Abrir archivo 
archivo = open("Data.txt","a") # "a" significa que el archivo ya existe, lo abriremos y vamos a escribir en el.
archivo.write("Contenido a escribir en el archivo linea1") # Agregamos una linea1 que dice "Contenido a escribir en el archivo" en el archivo "Data.txt" 
archivo.write("Contenido al lado de linea1") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# Cerar archivo
archivo.close()


# Crear un Archivo Forma1 open/close y excribir en el archivo
# Abrir archivo 
archivo = open("Data.txt","w") # "w" significa que si no existe, crea el archivo. Pero si existe, lo sobreescribe en blanco (como nuevo)
# Cerar archivo
archivo.close()

# Abrir archivo 
archivo = open("Data.txt","a") # "a" significa que el archivo ya existe, lo abriremos y vamos a escribir en el.
archivo.write("Contenido a escribir en el archivo linea1 ") # Agregamos una linea1 que dice "Contenido a escribir en el archivo" en el archivo "Data.txt" 
archivo.write("Contenido al lado de linea1") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# Cerar archivo
archivo.close()


# Cuando el archivo ya esta creado y se requiere escribir lineas nuevas 
# Abrir archivo 
archivo = open("Data.txt","a") # "a" significa que el archivo ya existe, lo abriremos y vamos a escribir en el.
archivo.write("\r\nContenido a escribir en el archivo linea1 \r\n") # Agregamos una linea1 que dice "Contenido a escribir en el archivo" en el archivo "Data.txt" 
archivo.write("Contenido en linea2 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
archivo.write("Contenido en linea3 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
archivo.write("Contenido en linea4 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# Cerar archivo
archivo.close()

# Para ler el contenido total de un archivo
# Abrir archivo 
archivo = open("Data.txt","r") # "r" Significa que vamos a leer el conenido de un archivo existente
print(archivo.read())
# Cerrar archivo 
archivo.close()

# Leer archivo linea por linea
# Abrir el archivo
archivo = open("Data.txt","r")

linea = archivo.readline()

while linea != "":
  print(linea)
  linea = archivo.readline()
# Cerar archivo
archivo.close()

# Leer archivo linea por linea con un FOR
# Abrir el archivo
archivo = open("Data.txt","r")

for linea in archivo.readline():
  print(linea)

# Cerar archivo
archivo.close() 