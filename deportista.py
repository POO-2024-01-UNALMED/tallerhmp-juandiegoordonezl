class Deportista():
    def __init__(self,nombre,edad,altura,sexo,deporte,años_Practicando):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte 
        self._añosPracticando=años_Practicando 
    
    def getDeporte(self):
        return self._deporte 
    
    def setDeporte(self,deporte):
        self._deporte=deporte 
        
    def getAños_Practicando(self):
        return self._años_Practicando
    
    def setAños_Practicando(self,año):
        self._años_Practicando=año 