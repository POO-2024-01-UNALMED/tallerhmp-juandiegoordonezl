class Deportista():
    def __init__(self,nombre,edad,altura,sexo,deporte,añosPracticando):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte 
        self._añosPracticando=añosPracticando 
    
    def getDeporte(self):
        return self._deporte 
    
    def setDeporte(self,deporte):
        self._deporte=deporte 
        
    def getAños_Practicando(self):
        return self._añosPracticando
    
    def setAños_Practicando(self,año):
        self._añosPracticando=año 