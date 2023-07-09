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
    
## LLenar una lista con un range
# Ejemplo con puertos tcp/udp de un pc 
list = []
ports = range(1,65536)
for port in ports:
  list.append(port)
print(list)    

## llemar una lista y luego invertir el orden de la lista
# Ejemplo con puertos tcp/udp de un pc 
lista = []
list_know_OK = []
list_register_ports = []
list_private_ports = []
ports = range(1,65536)
for port in ports:
  lista.append(port)
  
  if port <= 1023:
    list_know_OK.append(port)
  elif port >= 1024 and port <= 49151:
    list_register_ports.append(port)
  elif port >= 49152 and port <= 65535:
    list_private_ports.append(port)
  else:
    print("Exit")      
print(f"Rango de Puertos: {lista}\r\n")
print(f"Puertos Conocidos: {list_know_OK}\r\n")
print(f"Puertos Registrados: {list_register_ports}\r\n")
print(f"Puertos Conocidos: {list_private_ports}\r\n")

# inversa de lista
lista.reverse()
list_know_OK.reverse()
list_register_ports.reverse()
list_private_ports.reverse()
      
print(f"Rango de Puertos invertido: {lista}\r\n")
print(f"Puertos Conocidos invertido: {list_know_OK}\r\n")
print(f"Puertos Registrados invertido: {list_register_ports}\r\n")
print(f"Puertos Privados invertido: {list_private_ports}\r\n")
         