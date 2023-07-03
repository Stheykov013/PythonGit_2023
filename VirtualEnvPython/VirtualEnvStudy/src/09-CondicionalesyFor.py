lenguages = ["Español","Ingles","Ruso","Aleman","Portugues","Chino","Frances","Italiano"]

for lenguage in lenguages: # Recorre cada elemento de la lista lenguages y va guardando cada elemento en lenguaje
    if lenguage == "Aleman": # Luego evalua si el elemento guardado es igual a Aleman.
        print( f"Excelente {lenguage.upper()}!!!") # en caso de ser verdadero imprime Excelente ALEMAN!!!
    else: # en caso de no cumplirse
        print(lenguage) # imprima el elemento guardado en lenguaje

## El FOR anterior se ejecuta hasta que se cumplan todos los lementos de la lista.        
    
    
    