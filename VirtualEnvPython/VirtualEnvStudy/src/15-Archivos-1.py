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