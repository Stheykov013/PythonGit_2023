## While y For
    # FOR se ejecuta determinado numero de ocasiones segun sean los elementos de una lista
    # WHILE se ejecuta mientras que la condicion sea verdadera 
    
    # Estructura
        # variable_while = True # se crea esta variable con la condicion verdadera para el WHILE
        # pregunta1 = input("Digite 'cerrar' para salir \r\n "+ "Entrada valor \r\n")
        # while variable_while: # Mientras el While sea verdadero se ejuta el codigo
            
        #     if pregunta1 == "cerrar": # Para salir del While, Preguntamos si pregunta 1 es igual a cerrar , si es cerrar se sale, si no, continua con el codigo
        #       variable_while = False
        #     else:    
        #       pregunta1 = "Entrada Valor"
        #       print(continuar con el codigo)

        #           (Codigo identado para el while)
                
                  
                
var_while = True # se crea esta variable con la condicion verdadera para el WHILE

while var_while:
    
    pregunta1 = input("Digita un numero: \r\n"+"Escribre 'cerrar' para salir de la app \r\n")
     
    print(f"El numero digitado es: {pregunta1}\r\n")
     
    if pregunta1 == "cerrar":
        var_while = False
    else:    
        pregunta1 = int(pregunta1)
        
        if pregunta1 % 2 == 0:
            print(f"El numero {pregunta1} es par ")
        else:
            print(f"El numero {pregunta1} es impar ")
                         
                  
            
            
    
