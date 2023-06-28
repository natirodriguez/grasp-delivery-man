import random
#pip install matplotlib
class GreedyRandom:
    def __init__(self, grafo):
        self.grafo = grafo
        self.VALOR_MAXIMO = 99999; 
    
    def repartidorRandom(self): 
        longGrafo = len(self.grafo)
        nodosARandomizar = longGrafo // 2
        scoreCamino = 0

        nodoRandom = random.choice(range(0, longGrafo)) #el ultimo no cuenta

        #filas
        valorFilaActual = nodoRandom

        elementosVisitados = [0] * longGrafo
        primerElemento = nodoRandom
        elementosVisitados[primerElemento]=1
        elementosRandomizados = [nodoRandom]
       
        caminoGenerado = []
        print("Nodo del que inicio: ", nodoRandom)

        while(elementosVisitados.__contains__(0)):
            primerosElemsOrdenadosIndice = list(self.ElementosOrdenadosPorIndice(valorFilaActual, elementosRandomizados))
            elemRandom = random.choice(primerosElemsOrdenadosIndice)
            caminoGenerado.append([valorFilaActual, elemRandom])
            scoreCamino += self.grafo[valorFilaActual][elemRandom]
            valorFilaActual = elemRandom
            elementosVisitados[elemRandom] = 1
            elementosRandomizados.append(elemRandom)

        #seteo el ultimo elemento
        scoreCamino += self.grafo[valorFilaActual][primerElemento]
        caminoGenerado.append([valorFilaActual, primerElemento]);

        return caminoGenerado, scoreCamino # devolver tmb la suma maxima de todo el arbol para la busqueda local

    def ElementosOrdenadosPorIndice(self, indice, elementosRandomizados):
        longGrafo = len(self.grafo);

        dictionary = {}
        #filtro y me quedo con aquellos nodos que no fueron visitados
        for i in range(longGrafo):
            if i < longGrafo and not elementosRandomizados.__contains__(i): 
                dictionary.__setitem__(i, self.grafo[indice][i])

        #de los nodos no visitados los ordeno 
        diccionarioOrdenado= sorted(dictionary.items(), key=lambda x:x[1])
        #y me quedo con el 10% de los mismos
        primerosDosElementosDiccionario = diccionarioOrdenado[:2] #TODO

        converted_dict = dict(primerosDosElementosDiccionario)

        return converted_dict.keys()