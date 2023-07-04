## Tip de WHILE para evital ciclos infinitos
    # Recordar siempre cortar el el ciclo ejemplo break
    
numero = 0

while numero <= 10:
    print(numero)
    numero += 1 

# IF dentro del While

numero = 0

while numero <= 10:
    if numero == 5:
        print("Cincoooo!!!")
    else:
        print(numero)
    numero += 1        