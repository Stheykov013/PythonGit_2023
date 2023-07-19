codigo = ["001","002"]
nombre = ["Felipe Gutierrez","Andres Madrid"]
puesto = ["SysAdmin","Ing. Datos"]
telefono = [605,604]



def app():
    print("\r\n Opciones del Menu:\r\n")
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
            vista_planilla()
            opcion = False
        elif menuppal == 2:
            print("Vista de Insertar Persona\r\n")
            insertar_persona()
            opcion = False
        elif menuppal == 3:
            print("Vista de Eliminar Persona\r\n")
            eliminar_persona()
            opcion = False
        elif menuppal == 4:
            print("Vista de Editar Persona\r\n")
            editar_persona()
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
    code = str(input("Ingresa tu Codigo: \r\n"))
    codigo.append(code)
    print(f"Tu codigo es: {codigo}\r\n")
    job = str(input("Ingresa tu Job title: \r\n"))
    puesto.append(job)
    print(f"Tu puesto es: {puesto}\r\n")
    tel = str(input("Ingresa tu Telefono: \r\n"))
    telefono.append(tel)
    print(f"Tu nombre es: {telefono}\r\n")
    app()
 
def vista_planilla():
    print("Vista Datos de Planilla ")
    for item in range(len(codigo)): # len da el numero de items en el objeto
        print (codigo[item] , nombre[item] , puesto[item] , telefono[item]) # muestra el contenido de las listas segun la posicion item
    app()    

def eliminar_persona():
    print("Eliminar usuario por Codigo")
    code = input("Escriba el codigo del usuario a eliminar :\r\n")
    code = str(code)
    #print(type(codigo[1]))
    #print(type(code))
    for item in range(len(codigo)-1,-1,-1):
        if codigo[item] == code:
            codigo.pop(item)
            nombre.pop(item)
            puesto.pop(item)
            telefono.pop(item)
            print("Persona Eliminada")       
    app()

def editar_persona():
    print("Editar usuario por Codigo")
    code = input("Escriba el codigo del usuario a editar :\r\n")
    code = str(code)
    for item in range(len(codigo)):
        if codigo[item] == code:
            nombre[item] = input("Digite nuevo nombre: \r\n")
            puesto[item] = input("Digite nuevo Job Title: \r\n")
            telefono[item] = input("Digite nuevo Telefono: \r\n")
            print("Codigo editado correctamente")       
    app()    
                
app()    