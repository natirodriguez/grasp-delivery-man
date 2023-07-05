from Grasp import Grasp 
from GreedyRandom import GreedyRandom
from LocalSearch import LocalSearch
from Plotter import Plotter 
import Grafos30x30 
import Grafos100nodos


grafoEjemplo = [[-1, 10, 15, 20, 8], 
         [10, -1, 35, 25, 5], 
         [15, 35, -1, 30, 14], 
         [20, 25, 30, -1, 23],
         [8, 5, 14, 23,-1]]

test_graph = [
[0,   456, 605, 859, 328, 611, 289, 982, 286, 938],
[456, 0,   302, 535, 553, 101, 801, 929, 605, 901],
[605, 302, 0,   158, 919, 57,  687, 226, 949, 948],
[859, 535, 158, 0,   261, 344, 757, 262, 744, 283],
[328, 553, 919, 261, 0,   890, 431, 19,  793, 271],
[611, 101, 57,  344, 890, 0,   18,  181, 832, 871],
[289, 801, 687, 757, 431, 18,  0,   581, 71,  977],
[982, 929, 226, 262, 19,  181, 581, 0,   107, 309],
[286, 605, 949, 744, 793, 832, 71,  107, 0,   991],
[938, 901, 948, 283, 271, 871, 977, 309, 991, 0]
]

#Se comenta el greedy random y el local search ya que internamente el grasp llama n veces a esas dos clases
#Para un solo elemento se puede coentar el grasp para que no corra tanto y ver el resultado particular de ambos
"""
greedyRandom = GreedyRandom(Grafos200x200.grafo1, 10) #agarro este porcentaje para que pueda traer mas de un elem random
caminoRandomizado, scoreCamino = greedyRandom.repartidorRandom()

localSearch = LocalSearch(Grafos200x200.grafo1, caminoRandomizado, scoreCamino, 5)
mejorScore, secuencia = localSearch.findBest()
"""

#30

grasp = Grasp(Grafos30x30.grafo30v1, 10)
solucionesRegistradas = grasp.solucionGRASP()

plotter = Plotter()
plotter.solucion_plot(solucionesRegistradas)
