from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    
    def __init__(self,nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil) -> None:

        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self.añosPracticando = añosPracticando
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
    
    def getGolesMarcados(self):
        return self.golesMarcados

    def getTarjetasRojas(self):
        return self.edad

    def getPiernaHabil(self):
        return self.piernaHabil
        
    def setGolesMarcados(self, golesMarcados):
        self.golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self.piernaHabil = piernaHabil

    def __str__(self) -> str:
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"