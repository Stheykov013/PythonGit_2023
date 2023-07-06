## Codigo propio 01 
    # Que hace:
        #  Solicita un nombre para el archivo, crea el archivo.txt con el nombre y lo llena con Numero : 0-19 
        #  Si usar WHIT OPEN()
# Tiempo de Ejecucion
import time

# Iniciamos el reloj
inicio = time.time()

archivo_name = {}
archivo_name["nombre_archivo"] = "default.txt"
archivo_name["Ejecut_Time"] = 0

# app01
def app01():
    
    #variable para while
    pregunta1 = True
    # se crea el ciclo while
    while pregunta1:
        archivo_name["nombre_archivo"] = input("Escriba 'cerrar' para terminar \r\n"+"Escriba el nombe del archivo que tendra formato .txt \r\n")
        if archivo_name["nombre_archivo"] == "cerrar": 
            pregunta1 = False # se cierra el while
        else:
            archivo = open(f"{archivo_name['nombre_archivo']}.txt","w") # se cre el archivo con en nombre digitado. 1. Cerrar el Open
            for item in range (0,20):   # En el archivo crea numeros en el rango del 0 al 19
                archivo.write(f"Numero: {str(item)}\r\n") # Escribre Numero: 0 - 19 en el archivo y es de tipo string 
            archivo.close()    # 2. Open cerrado
            mostrar_contenido()
            
def mostrar_contenido():
    pregunta2 = True
    while pregunta2:
        contenido = input("Escriba 'yes' / 'no' para mostrar contenido\r\n")
        
        if contenido == "yes":
            archivo_name_str = str(archivo_name["nombre_archivo"])
            print(archivo_name_str)
            with open(f"{archivo_name_str}.txt","r") as contenido_archivo:
                for item in contenido_archivo:
                    print(item.rstrip()) # Este comando me elimina los saltos de linea al leer el archivo
                      
        elif contenido == "no":
            print("modo de lectura Cerrado:\r\n")          
            pregunta2 = False    

         
app01()

#finalizamos el reloj
fin = time.time()
# calculamos en timepo de ejecucion
tiempo_ejecucion = fin - inicio
# imprimimos el tiempo de ejecucion
print(f"Este es el tiempo de ejecucion {tiempo_ejecucion:.5f} segundos") # {tiempo_ejecucion:.5f} .5f = 5 cifras despues del . 


