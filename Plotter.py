import matplotlib.pyplot as plt
#pip install matplotlib

class Plotter:
    def solucion_plot(self, soluciones):
        for sols in soluciones:
            indice = soluciones.index(sols)
            solucion_id = str(indice + 1)
            xs = []
            ys = []

            for sol in sols[1]:
                xs.append(sol.secuencia)
                ys.append(sol.mejorScore)

            plt.plot(xs, ys, label="line " + solucion_id, marker='o')

        plt.xlabel('Solucion ID')
        plt.ylabel('Score')
        plt.title('GRASP - Repartidor')
        plt.legend()
        plt.show()