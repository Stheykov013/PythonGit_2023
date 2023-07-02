## Es ejecutar un codigo un numero de veces hasta que una condicion se cunpla o se deje de cumplir
    # Estructura
        # lenguages = ["Español","Ingles","Ruso","Aleman","Portugues","Chino","Frances","Italiano"]
        # Iterador
        # for lenguage in lenguages # para cada lenguage(singular) en la lista lenguages(plural)
        
lenguages = ["Español","Ingles","Ruso","Aleman","Portugues","Chino","Frances","Italiano"]

for lenguaje in lenguages:
    print(lenguaje)

## Iterador que escriba numeros desde N hasta M
    # Estructura
        # for numero in range(N,M):
        # print(numero)
    
for numero in range(0,20): # En este caso se generan numeros de 0 a 19
    print(numero)  
    
## Iterador que escriba numeros desde N hasta M con incrementos de x
    # Estructura
        # for numero in range(N,M,x):
        # print(numero)
    
for numero in range(0,20,2): # En este caso se generan numeros de 0 a 19 con incrementos de 2 en dos
    print(numero)             