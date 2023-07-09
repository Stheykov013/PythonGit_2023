## Iniciar un Diccionario vacio
    # Estructura
        # nombre_diccionario = {}
        # print(nombre_diccionario)

jugador = {} # Se crea el Diccionario vacio
print(jugador)

## Agregamos llaves y valor al diccionario vacio

jugador["nombre"] = "Felipe" # En este caso al diccionario jugador le creamos la llave nombre y se asignamos el valor Felipe
jugador["apellido"] = "Gutierrez"
jugador["email"] = "Felipe.madrid@yahoo.es"
jugador["nickname"] = "Stheykov"

print(jugador)

    # Resultado
        # {'nombre': 'Felipe', 'apellido': 'Gutierrez', 'email': 'Felipe.madrid@yahoo.es', 'nickname': 'Stheykov'}

print(jugador.get("apellido")) # Accedo al valor por medio del metodo .get
print(jugador.get("" , "No Existe esa llave : valor")) # Forma de evaluar cuando la llave no existe
print(jugador["apellido"]) # Acceso al valor sin metodos

## Iteradores en el Dicionario

for llave , valor in jugador.items(): # nombre_diccionario.items() evalua el elemento de la llave y el elememnto del valor
    print(f"Esta es la llave {llave}", f"Este es el valor {valor}")
        # Resultado 
            # Esta es la llave nombre Este es el valor Felipe
            # Esta es la llave apellido Este es el valor Gutierrez
            # Esta es la llave email Este es el valor Felipe.madrid@yahoo.es
            # Esta es la llave nickname Este es el valor Stheykov
 
## Eliminar llaves Diccionario. Con solo eliminar las llaves, tambien se eliminan los valores.
    
del jugador["nombre"]        
del jugador["apellido"]        
del jugador["email"]        
del jugador["nickname"] 

print(jugador)       
        
## Dict que tiene una Key con valor de una lista

tupla = ("Felipe",546789,"TB")
lista = ["C#","SQL","MngoDB", "Python"]
dict = {"Nombre" : "Felipe", "Edad" : 38, "Lenguajes" : lista} # la Key Lenguajes tiene el valor de una lista (lista = ["C#","SQL","MngoDB",2345])
print(dict)

# Como acceder a una elemento de la { "Key" : ["valor1","valor2","valor3"]}

tupla = ("Felipe",546789,"TB")
lista = ["C#","SQL","MngoDB", "Python"]
dict = {"Nombre" : "Felipe", "Edad" : 38, "Lenguajes" : lista} # la Key Lenguajes tiene el valor de una lista (lista = ["C#","SQL","MngoDB",2345])
print(dict["Lenguajes"][3]) # Imprime el valor de la lista en la posicion 3
        