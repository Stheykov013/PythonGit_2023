### POLIMORFISMO

    # Para este caso la Clase padre se llama Restaurante
class Restaurante: # Clase Padre
    
    def __init__(self,nombre,telefono,direccion): 
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
    
    def monstrar_informacion(self):
        print("\r")
        print(f"Nombre: {self.nombre}")
        print(f"Telefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")
        print("\r")
    
restaurante = Restaurante("IlForno",604,"Poblado")
restaurante.monstrar_informacion()

restaurante2 = Restaurante("Rancherito",604,"Copacabana")
restaurante2.monstrar_informacion()


## Clase Hijo(Hotel) de clase Padre (Restaurante)
    # Estructura
        # class Hotel(Restaurante):
        #    def __init__(self, nombre, telefono, direccion):
        #        super().__init__(nombre, telefono, direccion)
    
        # hotel = Hotel("Hotel Rancherito",604,"Caldas")

        # hotel.monstrar_informacion()

class Hotel(Restaurante):
    def __init__(self, nombre, telefono, direccion,calificacion): # 1. Polimorfismo. Heredamos de la clase padre los atributos, pero podemos agregar nuevos, en este caso calificacion
        super().__init__(nombre, telefono, direccion)
        self.calificacion = calificacion                          # 2. se coloca el atributo de la clase self.calificacion = calificacion
    # Se reescribe el metodo en el hijo para mostrar calificacion 
    def monstrar_informacion(self):
        print("\r")
        print(f"Nombre: {self.nombre}")
        print(f"Telefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")
        print(f"Calificacion: {self.calificacion}")               # 3. Se muestra el polimorfismo calificacion
        print("\r")    
    
hotel = Hotel("Hotel Rancherito",604,"Caldas","5 Estrellas")
hotel.monstrar_informacion()
hotel2 = Hotel("Hotel IlForno",604,"Belen","2 Estrellas")
hotel2.monstrar_informacion()



