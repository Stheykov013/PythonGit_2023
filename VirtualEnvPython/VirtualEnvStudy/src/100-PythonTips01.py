# ## Llenar una lista y luego inverir el orden de la lista

# # Ejemplo con puertos tcp/udp de un pc 
# lista = []
# list_know_OK = []
# list_register_ports = []
# list_private_ports = []
# ports = range(1,65536)
# for port in ports:
#   lista.append(port)
  
#   if port <= 1023:
#     list_know_OK.append(port)
#   elif port >= 1024 and port <= 49151:
#     list_register_ports.append(port)
#   elif port >= 49152 and port <= 65535:
#     list_private_ports.append(port)
#   else:
#     print("Exit")      
# print(f"Rango de Puertos: {lista}\r\n")
# print(f"Puertos Conocidos: {list_know_OK}\r\n")
# print(f"Puertos Registrados: {list_register_ports}\r\n")
# print(f"Puertos Conocidos: {list_private_ports}\r\n")

# # inversa de lista
# lista.reverse()
# list_know_OK.reverse()
# list_register_ports.reverse()
# list_private_ports.reverse()
      
# print(f"Rango de Puertos invertido: {lista}\r\n")
# print(f"Puertos Conocidos invertido: {list_know_OK}\r\n")
# print(f"Puertos Registrados invertido: {list_register_ports}\r\n")
# print(f"Puertos Privados invertido: {list_private_ports}\r\n")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Crear un Archivo Forma1 open/close y excribir en el archivo
# # Abrir archivo 
# archivo = open("Data.txt","w") # "w" significa que si no existe, crea el archivo. Pero si existe, lo sobreescribe en blanco (como nuevo)
# # Cerar archivo
# archivo.close()

# # Abrir archivo 
# archivo = open("Data.txt","a") # "a" significa que el archivo ya existe, lo abriremos y vamos a escribir en el.
# archivo.write("Contenido a escribir en el archivo linea1 ") # Agregamos una linea1 que dice "Contenido a escribir en el archivo" en el archivo "Data.txt" 
# archivo.write("Contenido al lado de linea1") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# # Cerar archivo
# archivo.close()


# # Cuando el archivo ya esta creado y se requiere escribir lineas nuevas 
# # Abrir archivo 
# archivo = open("Data.txt","a") # "a" significa que el archivo ya existe, lo abriremos y vamos a escribir en el.
# archivo.write("\r\nContenido a escribir en el archivo linea1 \r\n") # Agregamos una linea1 que dice "Contenido a escribir en el archivo" en el archivo "Data.txt" 
# archivo.write("Contenido en linea2 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# archivo.write("Contenido en linea3 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# archivo.write("Contenido en linea4 con \\r\\n'\r\n") # Coloca al lado de la linea1 "Contenido al lado de linea1" 
# # Cerar archivo
# archivo.close()

# # Para ler el contenido total de un archivo
# # Abrir archivo 
# archivo = open("Data.txt","r") # "r" Significa que vamos a leer el conenido de un archivo existente
# print(archivo.read())
# # Cerrar archivo 
# archivo.close()

# # Leer archivo linea por linea
# # Abrir el archivo
# archivo = open("Data.txt","r")

# linea = archivo.readline()

# while linea != "":
#   print(linea)
#   linea = archivo.readline()
# # Cerar archivo
# archivo.close()

# # Leer archivo linea por linea con un FOR
# # Abrir el archivo
# archivo = open("Data.txt","r")

# for linea in archivo.readline():
#   print(linea)

# # Cerar archivo
# archivo.close() 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
