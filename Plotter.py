import matplotlib.pyplot as plt
#pip install matplotlib

class Plotter:
    def solucion_plot(self, soluciones):
        
        for s in soluciones:
            solucion_id = str(soluciones.index(s) + 1)
            xs = []
            ys = []
       
            xs.append(solucion_id)
            ys.append(s.score)
            plt.plot(ys, xs, label="# linea " + solucion_id, marker='o')

        plt.xlabel('Solucion ID')
        plt.ylabel('Score')
        plt.title('GRASP - Repartidor')
        plt.legend()
        plt.show()