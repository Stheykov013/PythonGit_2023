import time

inicio = time.time()

# Variables Enteras / Int
numero = int(5)
print("Este es un Numero Entero",type(numero)) # type() me muestra que tipo de variable es lo que hay entre ()
    # Resultado
        # Este es un Numero Entero <class 'int'>
    
# Variables Decimales / Float
decimal = float(5.4321)
print("Este es un Numero Float",type(decimal)) # type() me muestra que tipo de variable es lo que hay entre ()
    # Resultado
        # Este es un Numero Float <class 'float'>
        
# Variable String o Caracter
caracter = str(30)
print("Este es un Caracter",type(caracter)) # type() me muestra que tipo de variable es lo que hay entre ()
    # Resultado
        # Este es un Caracter <class 'str'>

caracter = True
print("Este es un Booleano",type(caracter)) # type() me muestra que tipo de variable es lo que hay entre ()
    # Resultado
        # Este es un Caracter <class 'bool'>       
        
fin = time.time()

tiempo_ejecucion = fin - inicio

print(f"Tiempo de ejecucion {tiempo_ejecucion:.5f} segundos")  
    # Respuesta 
        #Tiempo de ejecucion 0.00007 segundos