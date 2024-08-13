class Deportista():
        def __init__(self, nombre, edad, altura, sexo, deporte, años_practicando):

            super().__init__(nombre, edad, altura, sexo)       
            self._deporte = deporte
            self._años_practicando = años_practicando
       


        # Métodos get
        def get_deporte(self):
            return self._deporte

        def get_años_practicando(self):
            return self._años_practicando

        # Métodos set
        def set_deporte(self, deporte):
            self._deporte = deporte

        def set_años_practicando(self, años_practicando):
            self._años_practicando = años_practicando
