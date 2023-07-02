def suma(a = 0,b = 0): # se coloca por default variable = 0 en caso de que no ingresen un argumento a ese parametro 
    print(a + b)

def resta(a = 0 , b = 0):
    print(a-b)

def multiplicacion(a = 0 , b = 1 ):
    print(a * b)

def divicion(a = 0 , b = 1): # b = 1 para evitar la divicion por 0 por default
    print(a/b)

suma(2,4)    
suma(2,4.7) #suma de enteros y flotantes/decimales
resta(2,4)
multiplicacion(2,4)
divicion(2,4)
