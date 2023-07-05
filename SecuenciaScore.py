class SecuenciaScore:
    """ mantiene la relacion entre una lista de NamedSequence y un score """
    def __init__(self, numeroSecuencia, mejorScore):
        self.secuencia = numeroSecuencia
        self.mejorScore = mejorScore

    def __str__(self):
        return "Secuencia: " + str(self.secuencia) + ", Score: " + str(self.mejorScore)

    def __repr__(self):
        return "Secuencia: " + str(self.secuencia) + ", Score: " + str(self.mejorScore)