codigo = []
nombre = []
puesto = []
telefono = []



def app():
    print("Opciones del Menu:\r\n")
    print("1. Ver Planilla: \r\n")
    print("2. Insertar Persona: \r\n")   
    print("3. Eliminar Persona: \r\n")
    print("4. Editar Persona: \r\n")
    print("5. Salir: \r\n")
    opcion = True
    while opcion:
        menuppal = int(input("Digite una opcion: \r\n"))
        if menuppal == 1:
            print("Vista de Planilla \r\n")
            opcion = False
        elif menuppal == 2:
            print("Vista de Insertar Persona\r\n")
            insertar_persona()
            opcion = False
        elif menuppal == 3:
            print("Vista de Eliminar Persona\r\n")
            opcion = False
        elif menuppal == 4:
            print("Vista de Editar Persona\r\n")
            opcion = False
        elif menuppal == 5:
            print("Adios!!!")
            opcion = False
        else:
            print("Opcion no valida!!\r\n")                

def insertar_persona():
    name = str(input("Ingresa tu nombre: \r\n"))
    nombre.append(name)
    print(f"Tu nombre es: {nombre}\r\n")
    app()
                
app()    