print("Calculadora de 2 numeros: \r\n")
numero1 = int(input("Ingresa el Primer numero: \r\n"))
numero2 = int(input("Ingresa el Segundo numero: \r\n"))
print("Que tipo de operacion deseas realizar: \r\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
operador = int(input("Escriba una opcion: \r\n"))
if operador == 1:
    totalSuma = numero1 + numero2
    print(f"Esta es la suma del primer numero {numero1} + el segundo numero {numero2}: Resultado {totalSuma} \r\n")
elif operador == 2:
    totalResta = numero1 - numero2
    print(f"Esta es la resta del primer numero {numero1} - el segundo numero {numero2}: Resultado {totalResta} \r\n")
elif operador == 3:
    totalMultiplicacion = numero1 * numero2
    print(f"Esta es la multiplicacion del primer numero {numero1} * el segundo numero {numero2}: Resultado {totalMultiplicacion} \r\n")    
elif operador == 4:
    if numero2 != 0:
        totaldivision = numero1 / numero2
        print(f"Esta es la division del primer numero {numero1} / el segundo numero {numero2}: Resultado {totaldivision} \r\n")
    else:
        print("Segundo numero no valido: \r\n")
else:
    print("Numero no valido") 

