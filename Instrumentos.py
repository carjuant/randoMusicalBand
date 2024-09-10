from abc import ABC,abstractmethod



class Instrumento(ABC):
    @abstractmethod
    def sonar():
        pass

class Guitarra(Instrumento):
    def sonar(self):
        print("Sonido de Guitarra")
    def __str__(self):
        return "Instrumento: Guitarra"
    
class Acordeon(Instrumento):
    def sonar(self):
        print ("Sonido de Acordeon")
    def __str__(self):
        return "Instrumento: Acordeon"

class Trompeta(Instrumento):
    def sonar(self):
        print("Sonido de Trompeta")
    def __str__(self):
        return "Instrumento: Trompeta"

class Maracas (Instrumento):
    def sonar(self):
        print ("Sonido de Maracas")
    def __str__(self):
        return "Instrumento: Maracas"

misInstrumentos=[Guitarra(),Acordeon(),Trompeta(),Maracas()]