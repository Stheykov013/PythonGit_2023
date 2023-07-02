## Evaluar si una condicion es mayor a > con IF

balance = 500
if balance > 0:
    print("Tienes Saldo")



## Evaluar si una condicion es mayor a > con IF y ELSE

balance = 500
if balance > 0:
    print("Tienes Saldo")
else:
    print("No Tienes Saldo")

## Evaluar una condicion con texto con IF y ELSE   

lenguaje = "Python" 
if lenguaje == "Python": # Se Evalua si Lenguaje es igual a Python
    print(f"Correcto {lenguaje} es la mejor desicion")
else:
    print(f"{lenguaje} tambien es Bueno")
    
## Evaluar una condicion DIFERENTE(not) con texto con IF y ELSE   
    # Estructura
        # if not Variable == Argumento
        
lenguaje = "Python" 
if not lenguaje == "Python": # Se Evalua si Lenguaje NO es igual a Python
    print(f"Correcto {lenguaje} es la mejor desicion")
else:
    print(f"{lenguaje} tambien es Bueno")  
    
## Evaluar un Boolean

usuario_autenticado = True # Evalua si usuario_autenticado es verdadero, entonces Acceso al Sistema. 
                           # Cuando Cambir usurario_autenticado a False, entonces Debe Iniciar Sesion
if usuario_autenticado:
    print("Acceso al Sistema")
else:
    print("Debe Iniciar Sesion")  
    
## Evaluar un elemento de una lista
    # Estructura
        # if elemento in Lista:
        #     print(elemento)
        # else:
        #     print("No esta en la lista")    

lenguages = ["Español","Ingles","Ruso","Aleman","Portugues","Chino","Frances","Italiano"]

if "Aleman" in lenguages:
    print("Aleman si existe")
else:
    print("No, no existe en la lista")    
               
## IF anidados

usuario_autenticado = False # Evalua si usuario_autenticado es verdadero, entonces Acceso al Sistema. 
                           # Cuando Cambia usurario_autenticado a False, entonces Debe Iniciar Sesion
usuario_administrador = False # Evalua si usuario_administrador es verdadero, entonces Acceso de administrador. 
                           # Cuando Cambia usurario_administrador a False, entonces solo Acceso al Sistema
                           
if usuario_autenticado:
    if usuario_administrador:
        print("Acceso de Administrador")
    else:
        print("Acceso al Sistema")
else:
    print("Debe Iniciar Sesion")
    
    
    
    
    
                   