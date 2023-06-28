from Grasp import Grasp 
from GreedyRandom import GreedyRandom
from LocalSearch import LocalSearch
from Plotter import Plotter 

grafoEjemplo = [[-1, 10, 15, 20, 8], 
         [10, -1, 35, 25, 5], 
         [15, 35, -1, 30, 14], 
         [20, 25, 30, -1, 23],
         [8, 5, 14, 23,-1]]

#Se comenta el greedy random y el local search ya que internamente el grasp llama n veces a esas dos clases
#Para un solo elemento se puede coentar el grasp para que no corra tanto y ver el resultado particular de ambos


greedyRandom = GreedyRandom(grafoEjemplo)
caminoRandomizado, scoreCamino = greedyRandom.repartidorRandom()

localSearch = LocalSearch(grafoEjemplo, caminoRandomizado, scoreCamino)
mejorResultado, mejorScore, solucionesRegistradas = localSearch.findBest()

plotter = Plotter()
plotter.solucion_plot(solucionesRegistradas)
"""

grasp = Grasp(grafoEjemplo)
grasp.solucionGRASP()
"""