# class Restaurante:
    
#     def __init__(self,nombre,telefono,direccion): # Este codigo se ejecuta automaticamente gracias al __init__
#         self.nombre = nombre # Atributo
#         self.telefono = telefono
#         self.direccion = direccion
    
#     def mostrar_informacion(self):
#         print("\r") 
#         print(f"Nombre: {self.nombre}")    
#         print(f"Telefono: {self.telefono}")    
#         print(f"Direccion: {self.direccion}") 
#         print("\r")   
                
# restaurante = Restaurante("IlForno",604,"Superior")
# restaurante.mostrar_informacion()
# restaurante2 = Restaurante("Rancherito",604,"Copacabana")
# restaurante2.mostrar_informacion()

### Pilares de OOP

## ABSTRACCION
    # Son los datos necesarios de una Clase
    
## ENCAPSULAMIENTO  
    # Este permite restringir u ocultar el acceso a los datos dentro de la misma clase, del mundo exterior
    
        # DEFAULT : PUBLIC = quiere decir que  se puede modificar en cualquier parte de la aplicacion
            # Resultado
                # class Restaurante:
    
                    # def __init__(self,nombre,telefono,direccion): 
                    #     self.nombre = nombre   # DEFAULT : PUBLIC
                    #     self.telefono = telefono # DEFAULT : PUBLIC
                    #     self.direccion = direccion # DEFAULT : PUBLIC
                    
        # PROTECTED = se agreda al atributo un guion al piso despues del punto SE PUEDE MODIFICAR EN LA MISMA CLASE PERO NO EN CUALQUIER PARTE DE LA APLICACION
            # Resultado
                # class Restaurante:
    
                    # def __init__(self,nombre,telefono,direccion): 
                    #     self.nombre = nombre   # DEFAULT : PUBLIC
                    #     self._telefono = telefono # PROTECTED
                    #     self._direccion = direccion # PROTECTED
                    
        # PRIVATE = Se agrega doble guion al piso despues del punto. NO SERA POSIBLE MODIFICAR
            # Resultado
                # class Restaurante:
    
                    # def __init__(self,nombre,telefono,direccion): 
                    #     self.nombre = nombre   # DEFAULT : PUBLIC
                    #     self._telefono = telefono # PROTECTED
                    #     self.__direccion = direccion # PRIVATE . En caso de que se requiera modificar, se debe de hacer por medio de un METODO GET-SET

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
restaurante.telefono = 601 # Esto se llama como encapsulamiento
restaurante.mostrar_informacion()
restaurante2 = Restaurante("Rancherito",604,"Copacabana")
restaurante2.mostrar_informacion()  
