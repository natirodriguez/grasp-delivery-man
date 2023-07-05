from SecuenciaScore import SecuenciaScore 

class LocalSearch:
    def __init__(self, matriz, caminoGenerado, scoreGenerado, vecesRepeticionVecindad):
        self.matriz = matriz
        #Parametro usado para no seguir buscando scores en caso de no encontrar mejorias
        self.vecesPermitidasUnScore = 20
	    #Parametro usado para poner un corte en caso de que se encuentre siempre una mejor solucion
        self.limiteBusLocal = 10
        self.caminoGenerado = caminoGenerado
        self.scoreGenerado = scoreGenerado
        self.vecesRepeticionVecindad = vecesRepeticionVecindad

    def findBest(self):

        mejorCamino = self.caminoGenerado 
        mejorScore = self.scoreGenerado
        
        secuenciasScoresList = []
        secuenciasScoresList.append(SecuenciaScore(0, mejorScore)) #arbol greedy
        print (0, mejorScore)
        for c in range(0,self.vecesRepeticionVecindad):
            contadorMejorScore = 0
            busLocal = 0
            while busLocal < self.limiteBusLocal and contadorMejorScore < self.vecesPermitidasUnScore:
                nuevoScore, nuevoCamino = self.busquedaVecindad(mejorCamino, mejorScore)
                secuenciasScoresList.append(SecuenciaScore(c+1, nuevoScore))

                if nuevoScore < mejorScore: 
                    print("Local search: ", busLocal, " Mejor Score: ", mejorScore, " Nuevo Score: ", nuevoScore)
                    mejorScore = nuevoScore
                    mejorCamino = nuevoCamino
                    contadorMejorScore += 1
                
                busLocal += 1

        return mejorScore, secuenciasScoresList

    def busquedaVecindad(self, mejorCamino, mejorScore):
        mejorIndice = 0

        for c in range(len(mejorCamino)): 
            nuevoScore = self.moverAristaConScoreResultante(c, mejorCamino, mejorScore)
            
            if nuevoScore < mejorScore: 
                mejorIndice = c
                mejorScore = nuevoScore

        #Se copia la solucion, y actualizo las aristas gracias al mejor camino encontrado
        mejorVecindad = self.copiarMejorVencidad(mejorIndice, mejorCamino)
        
        return mejorScore, mejorVecindad
    
    def copiarMejorVencidad(self, indiceCambiario, mejorCamino):
        longMatriz = len(mejorCamino) -1
        nuevaSolucion = mejorCamino.copy()
        
        if (indiceCambiario == 0):
            indiceCambiarioAnterior = longMatriz
            indiceCambiarioPosterior = indiceCambiario + 1
        else:
            indiceCambiarioAnterior = indiceCambiario -1
            if (indiceCambiario != longMatriz):
                indiceCambiarioPosterior = indiceCambiario +1
            else:
                indiceCambiarioPosterior = 0

        #Elemento a swapear, el elemento posterior y anterior al mismo. 
        primerElemento = mejorCamino[indiceCambiarioAnterior]; 
        elementoCambiario = mejorCamino[indiceCambiario] 
        ultimoElemento = mejorCamino[indiceCambiarioPosterior];

        #Swapeo los tres elementos(cambiario, anterior y posterior)
        nuevaSolucion[indiceCambiarioAnterior] = [primerElemento[0], elementoCambiario[1]]
        nuevaSolucion[indiceCambiario] = [elementoCambiario[1], elementoCambiario[0]]
        nuevaSolucion[indiceCambiarioPosterior] = [elementoCambiario[0], ultimoElemento[1]]

        return nuevaSolucion 

    def moverAristaConScoreResultante(self, indiceCambiario, mejorCamino, mejorScore):
        longMatriz = len(mejorCamino) -1
        nuevoScore = mejorScore
        
        if (indiceCambiario == 0):
            indiceCambiarioAnterior = longMatriz
            indiceCambiarioPosterior = indiceCambiario + 1
        else:
            indiceCambiarioAnterior = indiceCambiario -1
            if (indiceCambiario != longMatriz):
                indiceCambiarioPosterior = indiceCambiario +1
            else:
                indiceCambiarioPosterior = 0

        #Elemento a swapear, el elemento posterior y anterior al mismo. 
        primerElemento = mejorCamino[indiceCambiarioAnterior]; 
        elementoCambiario = mejorCamino[indiceCambiario] 
        ultimoElemento = mejorCamino[indiceCambiarioPosterior]

        #Resto al score los valores del mismo
        nuevoScore -= self.matriz[primerElemento[0]][primerElemento[1]]
        nuevoScore -= self.matriz[elementoCambiario[0]][elementoCambiario[1]]
        nuevoScore -= self.matriz[ultimoElemento[0]][ultimoElemento[1]]


        #Sumo al score los valores de los elementos cambiarios
        nuevoScore += self.matriz[primerElemento[0]][elementoCambiario[1]]
        nuevoScore += self.matriz[elementoCambiario[1]][elementoCambiario[0]]
        nuevoScore += self.matriz[elementoCambiario[0]][ultimoElemento[1]]

        return nuevoScore 
