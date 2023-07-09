# Se crea un archivo mimodulo.py y se agrega una funcion
    # def greeting(name):
    #   print("Hello, " + name)

# se importa el archivo mimodulo y se accede a la funcion greeting
  
import mimodulo20

mimodulo20.greeting("Andres")
    # Resultado
        # Hello, Andres
 
# lista lo nombres de los metodos de modulo        
print(dir(mimodulo20)) 
    # Resultado
        # ['greeting']