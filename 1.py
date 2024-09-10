import random
from Musico import Musico
from Instrumentos import misInstrumentos


class Banda():
    def __init__(self):
        self.musicos=[]
        self.instrumentos=[]
        self.banda={}
        for i in range (random.randint(1, 10)):
            self.musicos.append(Musico(f"Musico_{i}",random.randint(18,50),3000000000+random.randint(1,20)))
        #Se toman los instrumentos random
        for i in range (len(self.musicos)):
            self.instrumentos.append(random.choice(misInstrumentos))
        #Creamos la banda y cumplimos la dependencia del uml por medio de un diccionario
        for i in range(len(self.musicos)):
            self.asignarMusico(self.musicos[i],self.instrumentos[i])
        #Imprime
        for clave, valor in self.banda.items():
             print(f"{clave}: {valor}")


    def asignarMusico(self,musico,instrumento):
        self.banda[musico]=instrumento

        
aux=int(input("Que desea realizar: \n 1: Crear una banda aleatoria \n 2: Salir del programa\n"))
while aux!=2:
    mibanda=Banda()
    aux=int(input("Que desea realizar: \n 1: Crear una banda aleatoria \n 2: Salir del programa\n"))

