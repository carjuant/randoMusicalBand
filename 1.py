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
            print(self.musicos[i])
        #Se toman los instrumentos random
        for i in range (len(self.musicos)):
            self.instrumentos.append(random.choice(misInstrumentos))
            self.instrumentos[i].sonar()
        #Creamos la banda y cumplimos la dependencia del uml por medio de un diccionario
        for i in range(len(self.musicos)):
            self.asignarMusico(self.musicos[i],self.instrumentos[i])
        for clave, valor in self.banda.items():
             print(f"{clave}: {valor}")

             
    def asignarMusico(self,musico,instrumento):
        self.banda[musico]=instrumento

        

mibanda=Banda()
'''    
musicos=[]
instrumentos=[]
#Creo un numero aleatorio de musicos
for i in range (random.randint(1, 10)):
    musicos.append(Musico(f"Musico_{i}",random.randint(18,50),3000000000+random.randint(1,20)))
    print(musicos[i])
#Aca llamo instrumentos aleatorios, preguntar de donde sale el none a la hora de imprimir
for i in range (len(musicos)):
    instrumentos.append(random.choice(misInstrumentos))
    print(instrumentos[i].sonar())

mibanda=Banda(musicos,instrumentos)
#Preguntar si deberia trabajar con metodos o si en el constructor deberia asignar los valores a mi diccionario
'''