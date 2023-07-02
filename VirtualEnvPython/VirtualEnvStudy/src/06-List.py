## list es como lo que se conoce comunmente como Array

# Estructura del List/Array
    # meses = ["Enero","Febrero","Marzo","Abril"]
    
lenguages = ["Español","Ingles","Ruso","Aleman","Portugues","Chino","Frances","Italiano"]

print(lenguages) # Muestra todo la lista

## Posiciones en positivo

print(lenguages[0]) # Muestra los que contine Lenguages en la posicion [0] # Resultado Español
print(lenguages[3]) # Muestra los que contine Lenguages en la posicion [3] # Resultado Aleman
print(lenguages[7]) # Muestra los que contine Lenguages en la posicion [7] # Resultado Italiano

## Posiciones en negativo

print(lenguages[-1]) # Muestra los que contine Lenguages en la posicion [0] # Resultado Italiano
print(lenguages[-3]) # Muestra los que contine Lenguages en la posicion [3] # Resultado chino
print(lenguages[-7]) # Muestra los que contine Lenguages en la posicion [7] # Resultado Ingles

# usando el metodo .sort para ordenar alfabeticamente la lista

lenguages.sort()
print(lenguages)
    # antes 
        # ['Español', 'Ingles', 'Ruso', 'Aleman', 'Portugues', 'Chino', 'Frances', 'Italiano']
    # Resultado
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']     
    
## Acceder a un elemento dentro de un texto

aprendiendo = f"Estoy Aprendiendo {lenguages[4]} "

print(aprendiendo)

## Modificando valores en una Lista
    # Estructura
        # lenguajes[n] = "nuevo"  # En la lista Lenguajes, en la posicion N, reemplazarlo por nuevo

print(f"Esta es la lista  original sin modificar \r\n {lenguages}")

lenguages[7] = "Turco" # Reemplazamos lo que hay en la posicion 7 de la lista (RUSO) y colocamos (Turco) 

print(f"Esta es la lista modificada \r\n {lenguages}")

lenguages[7] = "Ruso"

print(f"Se deja la lista como la original \r\n {lenguages}")

## Agregar elementos a una lista
    # Estructura
        # lenguages.append("Elemento_a_Agregar")

print(f"Lista original \r\n {lenguages}")

lenguages.append("Mandarin")

print(f"Esta es la lista modificada con append agregando a la lista \r\n {lenguages}")     # Con en metodo .append se agrega el elemento Mandarin a la lista. Este se agrega al final de la lista

    # Resultado 
        # Lista original 
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']
        # Esta es la lista modificada con append agregando a la lista 
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso', 'Mandarin']
 

## Eliminar elementos de una Lista en una posicion especifica
    # Estructura
        # del lenguajes[N] # Elimina el elemento de la posicion N   

del lenguages[8]
print(f"Esta es la lista modificada con del eliminando de la lista la posicion 8 \r\n {lenguages}")
    # Resultado
        # Lista original 
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']
        # Esta es la lista modificada con append agregando a la lista 
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso', 'Mandarin']
        # Esta es la lista modificada con del eliminando de la lista la posicion 8 
        # ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']
              
## Elemiminar con POP
    # Eliminar el ultimo elemento de la lista con POP
        # Estructura
            # lenguages.pop() # Elimina el ultimo elemento de la lista
            
print(f"Lista original \r\n {lenguages}")

lenguages.append("Mandarin")     

print(f"Esta es la lista modificada con append agregando a la lista \r\n {lenguages}")     # Con en metodo .append se agrega el elemento Mandarin a la lista. Este se agrega al final de la lista

lenguages.pop(8)
print(f"Esta es la lista modificada con POP eliminando de la lista la posicion 8 \r\n {lenguages}")
    # Resultado
        # Lista original 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']
        # Esta es la lista modificada con append agregando a la lista 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso', 'Mandarin']
        # Esta es la lista modificada con POP eliminando de la lista la posicion 8 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']

 ## Eliminar por Nombre
    # Estructura
        # lenguages.remove("Nombre_a_Eliminar")     
 
print(f"Lista original \r\n {lenguages}")

lenguages.append("Mandarin")     

print(f"Esta es la lista modificada con append agregando a la lista \r\n {lenguages}")     # Con en metodo .append se agrega el elemento Mandarin a la lista. Este se agrega al final de la lista
       
lenguages.remove("Mandarin") 

print(f"Esta es la lista modificada con .remove eliminando de la lista en nombre Mandarin \r\n {lenguages}")

    # Resultado
        # Lista original 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']
        # Esta es la lista modificada con append agregando a la lista 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso', 'Mandarin']
        # Esta es la lista modificada con .remove eliminando de la lista en nombre Mandarin 
        #  ['Aleman', 'Chino', 'Español', 'Frances', 'Ingles', 'Italiano', 'Portugues', 'Ruso']

         