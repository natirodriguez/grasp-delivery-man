class SecuenciaScore:
    """ mantiene la relacion entre una lista de NamedSequence y un score """
    def __init__(self, secuencias, score):
        self.secuencias = secuencias
        self.score = score

    def __str__(self):
        return "Score: " + str(self.score) + ", secuencia: " + str(self.secuencias)

    def __repr__(self):
        return "Score: " + str(self.score) + ", secuencia: " + str(self.secuencias)
