## Un Objeto permite agupar diferentes tipos de datos en Python se conoce como DICIONARIOS
    # Para acceder a un elemento del Objeto/Dics se usa una llave (Key).

    # # Estructura
    #     # nombre_diccionario = {
    #         "llave1" : "valor1" ,
    #         "llave2" : "valor2" ,
    #         "llave3" : "valor3"
    #     }


cancion = {
    "artista" : "Metallica", # llave : valor
    "cancion" : "Enter Sandman",
    "lanzamiento" : 1992,
    "likes" : 3000
}

print(cancion) # con esto imprimimos todo el diccionario

print(cancion["artista"]) # Con esto accedemos al elemento, que hay en artista, del diccionario.
print(cancion["lanzamiento"]) # Con esto accedemos al elemento, que hay en lanzamiento, del diccionario.
 
## Para mezclar con strings se recomienda guardar en elemento en una variable y luego imprimirlo

artista = cancion["artista"]  # Guardamos elemento en variable

print(f"Estoy escuchando a {artista}")

## Agregar nuevos valores al Diccionario
    #Estructura 
    #   nombre_diccionario["nueva_llave"] = "nuevo_valor"

print(f"Este es el diccionario original {cancion}")

cancion["playlist"] = "Heavy Metal" # Agregamos al diccionario cancion la llave playlist y el valor Heavy Metal

print(f"Esta es el diccionario con la nueva llave y valor {cancion}")

    # Resultado
        # Este es el diccionario original                   {'artista': 'Metallica', 'cancion': 'Enter Snadman', 'lanzamiento': 1992, 'likes': 3000}
        # Esta es el diccionario con la nueva llave y valor {'artista': 'Metallica', 'cancion': 'Enter Snadman', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}

## Reemprazar valores en el Diccionario

print(f"Este es el Diccionario original {cancion}")

cancion["cancion"] = "Seek & Destroy" # En la llave cancion, reemplaza Enter Sandman por Seek & Destroy

print(f"Este es el nuevo Diccionario con el reemplazo de la nueva cancion {cancion}")

    # Resultado
        # Este es el Diccionario original                                   {'artista': 'Metallica', 'cancion': 'Enter Sandman', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}
        # Este es el nuevo Diccionario con el reemplazo de la nueva cancion {'artista': 'Metallica', 'cancion': 'Seek & Destroy', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}

cancion["cancion"] = "Enter Sandman" # Se deja el Diccionario como el original # En la llave cancion, reemplaza Seek & Destroy por Enter Sandman

print(f"Este es el Diccionario original {cancion}")

    # Resultado
        # Este es el Diccionario original                                   {'artista': 'Metallica', 'cancion': 'Enter Sandman', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}
        # Este es el nuevo Diccionario con el reemplazo de la nueva cancion {'artista': 'Metallica', 'cancion': 'Seek & Destroy', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}
        # Este es el Diccionario original                                   {'artista': 'Metallica', 'cancion': 'Enter Sandman', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'} 
    
## Eminiar valores en el Diccionario

del cancion["playlist"] 

print(f"Esta es el diccionario eliminando llave y valor playlist {cancion}")
    
    # # Resultado
    #     Este es el diccionario original                           {'artista': 'Metallica', 'cancion': 'Enter Snadman', 'lanzamiento': 1992, 'likes': 3000}
    #     Esta es el diccionario con la nueva llave y valor         {'artista': 'Metallica', 'cancion': 'Enter Snadman', 'lanzamiento': 1992, 'likes': 3000, 'playlist': 'Heavy Metal'}
    #     Esta es el diccionario eliminando llave y valor playlist  {'artista': 'Metallica', 'cancion': 'Enter Snadman', 'lanzamiento': 1992, 'likes': 3000}
    
 
 
    
    
    