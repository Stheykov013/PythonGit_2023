# Libreria os diseñada para manejar archivo
import os

# defino el codigo dentro de una funcion
CARPETA = "Contactos/"
EXTENSION =".txt"

class Contacto:
    def __init__(self,nombre,celular,email):
        self.nombre = nombre
        self.celular = celular
        self.email = email
        

def app():
    
    crear_directorio()
    mostrar_menu()
    
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion :\r\n")
        opcion = int(opcion)
        if opcion == 6:
            print("Adios!!:")
            preguntar = False
        elif opcion == 1:
            print("Agregar Contacto:")
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print("Editar Contacto:")
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print("Ver Contacto:")
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            print("Buscar Contacto:")
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            print("Eliminar Contacto:")
            eliminar_contacto()
            preguntar = False
        else:
            print("Opcion no valida, intente de nuevo") 

def eliminar_contacto():
    nombre = input("Ingrase el nombre que desea Eliminar: \r\n")
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print("\r\n Eliminado correctamente \r\n")
    except IOError:
        print("No Existe ese contacto: \r\n")    
    # Asi se Reinicia la app cuando en contacto ya este creado
    app()            

def buscar_contacto():
    nombre = input("Ingrase el nombre que desea buscar: \r\n")
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\nInformacion del contacto: \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("El archivo no existe")
        print("IOError")        
    # Asi se Reinicia la app cuando en contacto ya este creado
    app()
            
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")               
    # Asi se Reinicia la app cuando en contacto ya este creado
    app()
    
def editar_contacto():
    nombre_anterior = input("Nombre del contacto que desea editar: \r\n")
    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_conacto(nombre_anterior)
    
    if existe:
        print("Puedes Editar: ")
        with open(CARPETA + nombre_anterior + EXTENSION,"w") as archivo:
            # Agregar campos a editar
            nombre_contacto = input("Ingresa el nuevo nombre: \r\n")
            celular_contacto = input("Ingresar el nuevo Celular : \r\n")
            email_contacto = input("Ingresar el nuevo Email : \r\n")   
            
            #Instanciar
            contacto = Contacto(nombre_contacto,celular_contacto,email_contacto) 
            
            # Esribir en el archivo
            archivo.write("Nombre :" + contacto.nombre + "\r\n")
            archivo.write("Celular :" + contacto.celular + "\r\n")
            archivo.write("Email:" + contacto.email + "\r\n")
            
            # Renombrar en archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION) 
            
            print("Contacto Editado con Exito: \r\n")  
    else:
        print("Ese contacto no existe: ")    
        
    # Asi se Reinicia la app cuando en contacto ya este creado
    app()

def agregar_contacto():
    print("Escribre los datos para agregar el nuevo contacto")
    nombre_contacto = input("Nombre: \r\n")  
    
    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_conacto(nombre_contacto)
    if not existe:
    
        with open(CARPETA + nombre_contacto + EXTENSION,"w") as archivo:
            celular_contacto = input("Ingresar Celular : \r\n")
            email_contacto = input("Ingresar Email : \r\n")
            
            contacto = Contacto(nombre_contacto,celular_contacto,email_contacto)
            
            archivo.write("Nombre :" + contacto.nombre + "\r\n")
            archivo.write("Celular :" + contacto.celular + "\r\n")
            archivo.write("Email:" + contacto.email + "\r\n")
            
            print("\r\n Contacto creado")
    else:
        print("Ese Contacto ya existe")
        
    # Asi se Reinicia la app cuando en contacto ya este creado
    app()    
            
def crear_directorio():
    # Si el direcctorio no existe 
    if not os.path.exists(CARPETA):
        # cree "Contactos/"
        os.makedirs(CARPETA)
     
def mostrar_menu(): 
    print("Seleccione del Menù lo que desea hacer: \r\n")
    print("1) Agregar Nuevo Contacto \r\n")  
    print("2) Editar Contacto \r\n")
    print("3) Ver Contacto \r\n")
    print("4) Buscar Contacto \r\n")
    print("5) Eliminar Contacto \r\n")
    print("6) Salir \r\n")
# Esta funcion me retorna un valor Boolerano True/False
def existe_conacto (nombre_contacto):
    return os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

app()