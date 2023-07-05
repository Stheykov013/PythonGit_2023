# Es importante crear una funcion que contenga la aplicacion, en este caso es app
    # Estructura 
        # def app(): # 1. se declara la funcion
        #   print("Hola Mundo") # Codigo
        # app() # 2. Se llama la funcion
        
# casillero = {} # diccionario vacio
# casillero ["Nombre"] = [] # Lista vacia para poner el nombre del casillero
        
# def app(): 
    
#     nombre_casillero = input("Digita el nombre del casillero: \r\n")
    
#     casillero["Nombre_casillero"] = nombre_casillero
    
#     print(f"Este es el nombre del Casillero : {nombre_casillero} \r\n") 
    
    
# app()

casillero = {} # diccionario vacio
casillero["Items_Casillero"] = [] # Lista vacia para poner el nombre del casillero

def app():

# Agregar Casillero con Nombre:

    agregar_casillero = True # inicializo el while 
    
    while agregar_casillero:
        nombre_casillero = input("Digita 'cerrar' para salir de Nombrar el Casillero\r\n"+"Digita el Nombre del Casillero: \r\n")
        
        if nombre_casillero == "cerrar":
            print("Adios!!")
            agregar_casillero = False
        else:
            casillero["Nombre"] = nombre_casillero
            print(f"Este es el Diccionario creado : {casillero} \r\n")
            print(f"Su Casillero se llama : {nombre_casillero} \r\n")
            add_Items_Casillero()
            
# Agregar Items al Casillero

def add_Items_Casillero():
    add_Items = True
    
    while add_Items:
        Casillero_Name = casillero["Nombre"]
        items_casillero = input("Digita 'cerrar01' para salir de Nombrar Items del Casillero\r\n"+f"Agregar Nombre de Items Casillero  al Casillero {Casillero_Name}:\r\n")
        if items_casillero == "cerrar01":
            print("Adios de Nombrar Items del Casillero \r\n!!")
            mostar_resumen()
        #    print(f"Este es el Casillero Nombre : {casillero}\r\n")
        #    print(f"Este es el Casillero Nombre : {casillero}\r\n"+f" Este es el Item del Casillero {items_casillero}")
            add_Items = False
        else:
            casillero["Items_Casillero"].append(items_casillero) # Agrego un item nuevo a la lista con el .append
            print(f"Este es el Casillero Nombre : {Casillero_Name}\r\n")
            print(f"Este es el Item del Casillero : {casillero['Items_Casillero']}")

def mostar_resumen():
    Casillero_Nombre = casillero["Nombre"]
    Items_Casillero = casillero["Items_Casillero"]
    print(f"Este es el nombre de Casillero {Casillero_Nombre} \r\n")
    print("Items Casillero : \r\n")
    for item in  Items_Casillero:
        print(item)
                   

app()    

