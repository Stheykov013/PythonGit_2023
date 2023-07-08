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
