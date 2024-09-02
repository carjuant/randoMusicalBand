from abc import ABC,abstractmethod



class Instrumento(ABC):
    @abstractmethod
    def sonar():
        pass

class Guitarra(Instrumento):
    def sonar(self):
        print("Sonido de Guitarra")
    
    
class Acordeon(Instrumento):
    def sonar(self):
        print ("Sonido de Acordeon")

class Trompeta(Instrumento):
    def sonar(self):
        print("Sonido de Trompeta")

class Maracas (Instrumento):
    def sonar(self):
        print ("Sonido de Maracas")

misInstrumentos=[Guitarra(),Acordeon(),Trompeta(),Maracas()]