class Musico:
    def __init__(self,nombre,edad,telefono):
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, telefono: {self.telefono}"