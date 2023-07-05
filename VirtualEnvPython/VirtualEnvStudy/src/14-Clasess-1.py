## OOP Programacion Orientada a Objetos
    # Estructura
        # class Nombre_Clase: # 1. Se crea la Clase
        #   Codigo
        # nombre_clase = Nombre_Clase() # Se Instacia la clase

# Isntacia = Es el Objeto que es creado al llamar una clase.
# Atributo de clase = Es una propiedad que tendran todos los objetos creados en nuentra clase (darle forma a los datos)
# Metodo = es una funcion que existe dentro de una clase         
        
## Cuando se crean clases , por nomenclatura se debe de colocar la primera letra en mayuscula        
        
class Restaurante:  # 1. Se crea la clase 
    def agregar_restaurante(self, nombre, telefono, direccion,): # 3. Una Funcion dentro de una clase se le conoce como METODO
        self.nombre = nombre # Esto se conoce como atributo de la clase
        self.telefono = int(telefono)
        self.direccion = direccion
    
    def mostrar_informacion(self):
        print("\r")
        print(f"Nombre: {self.nombre}")    
        print(f"Telefono: {self.telefono}")    
        print(f"Direccion: {self.direccion}")  
        print("\r")  
                
restaurante = Restaurante() # 2. Se instacia la clase
restaurante.agregar_restaurante("IlForno", 604, "Superior") # 4. Se llama el metodo
restaurante.mostrar_informacion()
        
        
restaurante2 = Restaurante() # Se instancia la clase en una nueva variable
restaurante2.agregar_restaurante("Rancherito",604,"Copacabana")
restaurante2.mostrar_informacion()
         
        
        