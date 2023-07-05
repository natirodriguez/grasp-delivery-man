from GreedyRandom import GreedyRandom
from LocalSearch import LocalSearch

class Grasp:
    def __init__(self, matriz, porcentajeRandom, vecindad, corteGrasp):
        self.matriz = matriz
        self.porcentajeRandom = porcentajeRandom
        self.vecesRepetidasVecindad = vecindad 
        self.corteGrasp = corteGrasp

    def solucionGRASP(self):
        scoreCamino = 0
        caminoRandomizado = None
        solucionesRegistradasGRASP = []

        for i in range(0,self.corteGrasp):
            print("--- GRASP ", i, " ---")

            #matriz del mismo len q antes pero de diferentes numeros. Los score son los de findbest
            greedyRandom = GreedyRandom(self.matriz, self.porcentajeRandom)
            caminoRandomizado, scoreCamino = greedyRandom.repartidorRandom()

            localSearch = LocalSearch(self.matriz, caminoRandomizado, scoreCamino, self.vecesRepetidasVecindad)

            mejorScore, secuencia = localSearch.findBest()
                
            if (mejorScore < scoreCamino):
                print("Score: ", scoreCamino, " -> ", mejorScore)
                scoreCamino = mejorScore
            
            solucionesRegistradasGRASP.append([i, secuencia])
                    
        return solucionesRegistradasGRASP