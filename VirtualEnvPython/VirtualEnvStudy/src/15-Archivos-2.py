# Abrir y cerrar un archivo de forma Automatica con WITH OPEN("ARCHIVO.TXT")
    # Estructura

        
def app ():
    
    with open("archivo.txt","r") as archivo: # con la palabra AS se crea un alias
        for contenido in archivo: # iteramos con el for los elementos del archivo
            # print(contenido)
            print(contenido.rstrip()) # Este comando me elimina los saltos de linea al leer el archivo

app()        
