import sys
import random

def write_graph(filename, nodes):
    matrix = [[str(0) for x in range(nodes)] for y in range(nodes)]
    for i in range(0, nodes):
        for j in range (i+1, nodes):
            value = str(random.randint(1, 1000)) 
            matrix[i][j] = value
            matrix[j][i] = value

    matrix = map(lambda row: ', '.join(row), matrix)

    tasks = [str(random.randint(1, 100)) for y in range(nodes)]
    tasks = ' '.join(tasks)

    graph_file = open(filename,"w")
    #graph_file.write(str(nodes) + "\n")
    graph_file.write("[")
    for row in matrix:
        graph_file.write("[" + row + "], \n")
    #graph_file.write(tasks)
    graph_file.write("]")
    graph_file.close()
    
def read_graph(filename):
    with open(filename) as f:
        matrix = []         #Lista que contiene cada fila
        num_rows = int(f.readline())
        for row_index in range(num_rows):
            line = f.readline()
            row = [int(x) for x in line.split()] # Split en whitespace y castear cada elemento a int
            matrix.append(row)
        tasks = f.readline()
        tasks = [int(x) for x in tasks.split()]
    print(matrix)
    print(tasks)
    
"""
if __name__ == "__main__":
    filename = sys.argv[1]
    nodes = int(sys.argv[2])
    
    write_graph(filename, nodes)
    read_graph(filename)
"""
write_graph("Grafos100nodos.py", 100)