## Leer o capturar datos 
    # Estructura
        # captura = input(valor) # Todo valor que ingrese en input, se guarda en la variable captura

nombre = input("Cual es tu nombre? : \r\n") # \r\n generan un salto de linea en la Terminal

print(f"Hola, Bienvenido {nombre}")


edad = input("Cual es tu edad? : \r\n") # Ingresan edad. Como edad es un numero, se debe convertir a entero

edad = int(edad) # convierte la edad en entero.

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")    
    
## RETO ############################################## 

# Pregunta 1
pregunta1 = input("1. Cuanto es 2 + 2 ? : \r\n")
pregunta1 = int(pregunta1)
puntaje = 0

print(f"Tu respuesta fue {pregunta1}")

if pregunta1 == 4:
    print(f"Correcto tu respuesta fue {pregunta1}")
    puntaje += 1
else: 
    print(f"Incorrecto tu respuesta fue {pregunta1}")

# Pregunta 2
pregunta2 = input("2. Que lenguaje estamos aprendiendo ? : \r\n")
pregunta2 = str(pregunta2.lower())

print(f"Tu respuesta fue {pregunta2}")

if pregunta2 == "python":
    print(f"Correcto tu respuesta fue {pregunta2}")
    puntaje += 1
else: 
    print(f"Incorrecto tu respuesta fue {pregunta2}")

# Pregunta 3    
pregunta3 = input("3. Como se llama tu Hija? : \r\n")
pregunta3 = str(pregunta3.lower())

print(f"Tu respuesta fue {pregunta3}")

if pregunta3 == "luciana":
    print(f"Correcto tu respuesta fue {pregunta3}")
    puntaje += 1
else: 
    print(f"Incorrecto tu respuesta fue {pregunta3}")    
    
print("Cada pregunta tenia un puntaje \r\n")
print(f"Puntaje total {puntaje} puntos")           

     
    
    
    