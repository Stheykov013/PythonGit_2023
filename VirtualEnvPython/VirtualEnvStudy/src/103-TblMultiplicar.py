print("Tabla de Multiplicar un numero X por numeros el 1-10")
numeroX = int(input("Digite un numero X:\r\n"))
numeroY = 0
while numeroY <= 10:
  resultado = numeroX * numeroY
  print(str(numeroX) + "X" + str(numeroY) + "=" + str(resultado))
  numeroY += 1