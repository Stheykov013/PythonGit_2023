## CONSTRUCTOR es una funcion que se ejecuta automaticamente al crear un nuevo objeto por medio de una clase
    # Estructura
    #   def __init__(self):
    #   print("Yo me ejecuto automaticamente")

# class Restaurante:  # 1. Se crea la clase
    
#     def __init__(self):
#         print("Yo me ejecuto automaticamente")
     
#     def agregar_restaurante(self, nombre, telefono, direccion,): # 3. Una Funcion dentro de una clase se le conoce como METODO
#         self.nombre = nombre # Esto se conoce como atributo de la clase
#         self.telefono = int(telefono)
#         self.direccion = direccion
    
#     def mostrar_informacion(self):
#         print("\r")
#         print(f"Nombre: {self.nombre}")    
#         print(f"Telefono: {self.telefono}")    
#         print(f"Direccion: {self.direccion}")  
#         print("\r")  
                
# restaurante = Restaurante() # 2. Se instacia la clase
# restaurante.agregar_restaurante("IlForno", 604, "Superior") # 4. Se llama el metodo
# restaurante.mostrar_informacion()
        
        
# restaurante2 = Restaurante() # Se instancia la clase en una nueva variable
# restaurante2.agregar_restaurante("Rancherito",604,"Copacabana")
# restaurante2.mostrar_informacion()
         
class Restaurante:
    
    def __init__(self,nombre,telefono,direccion): # Este codigo se ejecuta automaticamente gracias al __init__
        self.nombre = nombre # Atributo
        self.telefono = telefono
        self.direccion = direccion
    
    def mostrar_informacion(self):
        print("\r") 
        print(f"Nombre: {self.nombre}")    
        print(f"Telefono: {self.telefono}")    
        print(f"Direccion: {self.direccion}") 
        print("\r")   
                
restaurante = Restaurante("IlForno",604,"Superior")
restaurante.mostrar_informacion()
restaurante2 = Restaurante("Rancherito",604,"Copacabana")
restaurante2.mostrar_informacion()

### Pilares de OOP

## ABSTRACCION
    # Son los datos necesarios de una Clase
##     


      