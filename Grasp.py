from GreedyRandom import GreedyRandom
from LocalSearch import LocalSearch

class Grasp:
    def __init__(self, matriz, porcentajeRandom):
        self.matriz = matriz
        self.porcentajeRandom = porcentajeRandom
        self.vecesRepetidasVecindad = 7

    def solucionGRASP(self):
        contador = 0
        scoreCamino = 0
        corteGrasp = 100
        caminoRandomizado = None
        solucionesRegistradasGRASP = []
        solucionesPlotter = []

        for i in range(0,corteGrasp):
            print("--- GRASP ", contador, " ---")

                #matriz del mismo len q antes pero de diferentes numeros. Los score son los de findbest
            greedyRandom = GreedyRandom(self.matriz, self.porcentajeRandom)
            caminoRandomizado, scoreCamino = greedyRandom.repartidorRandom()

            localSearch = LocalSearch(self.matriz, caminoRandomizado, scoreCamino, self.vecesRepetidasVecindad)

            mejorScore, secuencia = localSearch.findBest()
                
            if (mejorScore < scoreCamino):
                print("GRASP: ", contador, ", Score: ", scoreCamino, " -> ", mejorScore)
                scoreCamino = mejorScore
            
            solucionesRegistradasGRASP.append([contador, secuencia])
                    
            contador += 1

        return solucionesRegistradasGRASP