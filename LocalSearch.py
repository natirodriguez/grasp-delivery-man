from SecuenciaScore import SecuenciaScore

class LocalSearch:
    def __init__(self, matriz, caminoGenerado, scoreGenerado):
        self.matriz = matriz
        #Parametro usado para no seguir buscando scores en caso de no encontrar mejorias
        self.vecesPermitidasUnScore = 1
	    #Parametro usado para poner un corte en caso de que se encuentre siempre una mejor solucion
        self.limiteBusLocal = 50
        self.caminoGenerado = caminoGenerado
        self.scoreGenerado = scoreGenerado

    def findBest(self):
        contadorMejorScore = 0
        chances = 0

        #Camino y score del resultado de greedy
        mejorCamino = self.caminoGenerado 
        mejorScore = self.scoreGenerado

        #Plotter
        solucionesRegistradas = [];

        best_solution = SecuenciaScore(self.caminoGenerado, self.scoreGenerado)
        solucionesRegistradas.append(best_solution)

        print ("Camino generado: ", mejorCamino);
        print ("Score: ", mejorScore);

        while chances < self.limiteBusLocal and contadorMejorScore < self.vecesPermitidasUnScore:
            for c in range(len(self.caminoGenerado)): 
                print("Swap: ",  c)
                #Mover arista debe de recibir la mejorSolucion, si ve que el score es mejor actualizo
                # mejorSolucion con el valor.
                nuevoCamino, nuevoScore = self.moverAristaConScoreResultante(c, mejorCamino, mejorScore) #nuevaSolucion,nuevoScore
                best_solution = SecuenciaScore(nuevoCamino, nuevoScore)
                solucionesRegistradas.append(best_solution)

                print("Nueva solucion: ", nuevoCamino)
                print("Nuevo score: ", nuevoScore)
                if nuevoScore < mejorScore: 
                    print("Local search: ", chances, " Mejor Score: ", mejorScore, " Nuevo Score: ", nuevoScore)
                    mejorScore = nuevoScore
                    mejorCamino = nuevoCamino
                    contadorMejorScore = 0
                else: 
                    contadorMejorScore += 1
                    
                chances += 1

        return mejorCamino, mejorScore, solucionesRegistradas
    
    def moverAristaConScoreResultante(self, indiceCambiario, mejorCamino, mejorScore):
        longMatriz = len(mejorCamino) -1
        nuevaSolucion = mejorCamino.copy()
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
        #Resto al score los valores del mismo
        primerElemento = mejorCamino[indiceCambiarioAnterior]; 
        nuevoScore -= self.matriz[primerElemento[0]][primerElemento[1]]

        elementoCambiario = mejorCamino[indiceCambiario] 
        nuevoScore -= self.matriz[elementoCambiario[0]][elementoCambiario[1]]

        ultimoElemento = mejorCamino[indiceCambiarioPosterior];
        nuevoScore -= self.matriz[ultimoElemento[0]][ultimoElemento[1]]

        #Swapeo los tres elementos(cambiario, anterior y posterior)
        #Sumo al score los valores de los elementos cambiarios
        nuevaSolucion[indiceCambiarioAnterior] = [primerElemento[0], elementoCambiario[1]]
        nuevoScore += self.matriz[primerElemento[0]][elementoCambiario[1]]

        nuevaSolucion[indiceCambiario] = [elementoCambiario[1], elementoCambiario[0]]
        nuevoScore += self.matriz[elementoCambiario[1]][elementoCambiario[0]]

        nuevaSolucion[indiceCambiarioPosterior] = [elementoCambiario[0], ultimoElemento[1]]
        nuevoScore += self.matriz[elementoCambiario[0]][ultimoElemento[1]]

        return nuevaSolucion, nuevoScore 
