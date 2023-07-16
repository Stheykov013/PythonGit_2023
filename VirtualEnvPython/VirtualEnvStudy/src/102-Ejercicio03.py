####Calculadora Sin Funciones
# 
# print("Calculadora de 2 numeros: \r\n")
# numero1 = int(input("Ingresa el Primer numero: \r\n"))
# numero2 = int(input("Ingresa el Segundo numero: \r\n"))
# print("Que tipo de operacion deseas realizar: \r\n")
# print("1. Suma")
# print("2. Resta")
# print("3. Multiplicacion")
# print("4. Division")
# operador = int(input("Escriba una opcion: \r\n"))
# if operador == 1:
#     totalSuma = numero1 + numero2
#     print(f"Esta es la suma del primer numero + el segundo numero: {totalSuma} \r\n")
# elif operador == 2:
#     totalResta = numero1 - numero2
#     print(f"Esta es la resta del primer numero - el segundo numero: {totalResta} \r\n")
# elif operador == 3:
#     totalMultiplicacion = numero1 * numero2
#     print(f"Esta es la multiplicacion del primer numero * el segundo numero: {totalMultiplicacion} \r\n")    
# elif operador == 4:
#     if numero2 != 0:
#         totaldivision = numero1 / numero2
#         print(f"Esta es la division del primer numero / el segundo numero: {totaldivision} \r\n")
#     else:
#         print("Segundo numero no valido: \r\n")
# else:
#     print("Numero no valido") 

###Calculadora Con Funciones

# print("Calculadora de 2 numeros: \r\n")
# numero1 = int(input("Ingresa el Primer numero: \r\n"))
# numero2 = int(input("Ingresa el Segundo numero: \r\n"))
# def app():
    
#     print("Que tipo de operacion deseas realizar: \r\n")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicacion")
#     print("4. Division")
#     operador = int(input("Escriba una opcion: \r\n"))
#     if operador == 1:
#         suma()
#     elif operador == 2:
#         resta()
#     elif operador == 3:
#         multiplicacion()    
#     elif operador == 4:
#         division()
#     else:
#         print("Numero no valido")  


# def suma():
#     totalSuma = numero1 + numero2
#     print(f"Esta es la suma del primer numero + el segundo numero: {totalSuma} \r\n")        
# suma()    
    

# def resta():
#     totalResta = numero1 - numero2
#     print(f"Esta es la resta del primer numero - el segundo numero: {totalResta} \r\n")
# resta()

# def multiplicacion():
#     totalMultiplicacion = numero1 * numero2
#     print(f"Esta es la multiplicacion del primer numero * el segundo numero: {totalMultiplicacion} \r\n")
# multiplicacion()

# def division():
#     if numero2 != 0:
#         totaldivision = numero1 / numero2
#         print(f"Esta es la division del primer numero / el segundo numero: {totaldivision} \r\n")       
#     else:
#         print("Segundo numero no valido: \r\n")             
# division()
 
# app()

#Codigo con While


def app():
    print("\r\nCalculadora de 2 numeros: \r\n")
    calculadora = True
    
    while calculadora:
        menu()
        operador = int(input("\r\nEscriba una opcion: \r\n"))
        if operador == 1:
            suma()
            calculadora = False
        elif operador == 2:
            resta()
            calculadora = False
        elif operador == 3:
            multiplicacion()
            calculadora = False    
        elif operador == 4:
            division()
            calculadora = False
        elif operador == 5:
            print("Adios")
            calculadora = False
        else:
            print("Numero no valido")  


def suma():
    numero1 = int(input("Ingresa el Primer numero: \r\n"))
    numero2 = int(input("Ingresa el Segundo numero: \r\n"))
    totalSuma = numero1 + numero2
    print(f"Esta es la suma del primer numero {numero1} + el segundo numero {numero2} : {totalSuma} \r\n")        
    app()

def resta():
    numero1 = int(input("Ingresa el Primer numero: \r\n"))
    numero2 = int(input("Ingresa el Segundo numero: \r\n"))
    totalResta = numero1 - numero2
    print(f"Esta es la resta del primer numero {numero1} - el segundo numero {numero2} : {totalResta} \r\n")
    app()

def multiplicacion():
    numero1 = int(input("Ingresa el Primer numero: \r\n"))
    numero2 = int(input("Ingresa el Segundo numero: \r\n"))
    totalMultiplicacion = numero1 * numero2
    print(f"Esta es la multiplicacion del primer numero {numero1} * el segundo numero {numero2} : {totalMultiplicacion} \r\n")
    app()

def division():
    numero1 = int(input("Ingresa el Primer numero: \r\n"))
    numero2 = int(input("Ingresa el Segundo numero: \r\n"))
    if numero2 != 0:
        totaldivision = numero1 / numero2
        print(f"Esta es la division del primer numero {numero1} / el segundo numero {numero2} : {totaldivision} \r\n")       
    else:
        print("Segundo numero no valido: \r\n")
    app()    
        
def menu():
    print("Que tipo de operacion deseas realizar: \r\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")                    
     
app()



