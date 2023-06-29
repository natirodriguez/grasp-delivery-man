from GreedyRandom import GreedyRandom
from LocalSearch import LocalSearch

class Grasp:
    def __init__(self, matriz, porcentajeRandom):
        self.matriz = matriz
        self.corteGrasp = 50 #da un corte en el grasp para que no se ejecute infinitas veces
        self.porcentajeRandom = porcentajeRandom

    def solucionGRASP(self):
        contador = 0
        mejorScoreActual = 0
        mejorCamino = None
        solucionesRegistradas = []

        while contador < self.corteGrasp:
            print("--- GRASP ", contador, " ---")
            greedyRandom = GreedyRandom(self.matriz, self.porcentajeRandom)
            caminoRandomizado, scoreCamino = greedyRandom.repartidorRandom()

            localSearch = LocalSearch(self.matriz, caminoRandomizado, scoreCamino)

            if (mejorCamino == None): # la primera vez que entra aqui
                mejorCamino = caminoRandomizado
                mejorScoreActual = scoreCamino
            
            nuevoCamino, scoreNuevaSolucion, solucionesRegistradas = localSearch.findBest()

            if (mejorScoreActual < scoreNuevaSolucion):
                print("GRASP: ", contador, ", Score: ", mejorScoreActual, " -> ", scoreNuevaSolucion)
                mejorScoreActual = scoreNuevaSolucion
                mejorCamino = nuevoCamino

            contador += 1
        
        print("Solucion definitiva: ", mejorCamino)
        print("Score : ", mejorScoreActual)

        return mejorCamino 