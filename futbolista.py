from deportista import Deportista
from persona import Persona


class Futbolista(Deportista,Persona):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre,edad,altura,sexo,"Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    # Métodos get
    def get_goles_marcados(self):
        return self._golesMarcados

    def get_tarjetas_rojas(self):
        return self._tarjetasRojas

    def get_pierna_habil(self):
        return self._piernaHabil
    
    @classmethod
    def getListaFutbolistas(cls):
        return Futbolista.listasFutbolistas

    # Métodos set
    def set_goles_marcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def set_tarjetas_rojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def set_pierna_habil(self, piernaHabil):
        self._piernaHabil = piernaHabil
     
    @classmethod   
    def setListaFutbolistas(cls,listaFutbolistas):
        cls.listaFutbolistas=listaFutbolistas

    # Método str
    def __str__(self):
        return f"Mi nombre es "+str(self.get_nombre())+" soy profesional en el deporte "+ str(self.getDeporte()) + " Tengo "+ str(self.get_edad()) + " años de edad y llevo "+ str(self.getAños_Practicando()) + " años en el deporte"
    
