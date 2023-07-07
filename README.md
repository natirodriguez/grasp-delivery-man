# GRASP
Implementación de un repartidor de items, se necesita calcular la mejor distancia para entregar todos los items sin tener que pasar dos veces por el mismo camino. 
Se empieza de un item, y se debe de terminar en el mismo item. 
Se tomo como condición que el grafo es completo.
Para generar las soluciones iniciales se calcula el score de muchos circuitos (las mismas creadas a partir de la busqueda local). 

Búsqueda local
Se van probando swaps entre los circuitos, desde el comienzo y desde el final de la lista. Luego de esos swasp te da un score actualizado

Plotter
Se grafican los resultados (mejorados) de la búsqueda local para un solo greedy 

Grasp
Se ejecuta varias veces la primera repartición y su consecuente busqueda local.

Ejecución
El archivo "Main.py" va a tener la ejecución tanto del grasp como la de greedy/busqueda local. 

A continuación se va a estar mostrando la ejecución del GRASP, variando los parametros modificables tanto de LocalSearch como del GRASP; además de variar la cantidad de nodos de la matriz inicial.

## Variación veces permitidas por un score/mejora
Score es un parametro usado en el LocalSearch para no seguir buscando mejoras en caso de no encontrarlas, es decir le estoy poniendo un corte a la cantidad de veces que puede estar revisando una secuencia sin cambio alguno de la anterior. Como se pueden observar en los graficos posteriores, se puede observar para una misma linea(Grasp) como hay más de dos mejoras para una misma secuencia. Pero al dejarselo para que encuentre uno solo, eso no sucede, y se ve como la linea va decreciendo con distintas soluciones, y no hay más de un score para una misma solución.

Score: 20; 1 grafo de 30 nodos; bus local: 10 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/e1d615e6-92de-408a-b81d-d27759e5b5ed)

Score: 100; 2 ejecuciones del grasp con un grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/b1dd9e88-3953-4cf5-9422-066fcbceea88)

Score: 10; 2 ejecuciones del grasp con un grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/7de2c157-eb2f-4ae2-9d82-e93909082c1c)

Score: 50; 1 ejecución del grasp con un grafo de 100 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/c3dee6d7-ddac-42f6-bb76-d44293ddb5eb)

Score: 1; 1 ejecución del grasp con un grafo de 100 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/ca2c99a2-c09a-4364-9e73-8f04e3698743)


## Variación limite del bus local
Parametro usado en LocalSearch para poner un corte en caso de que se encuentre siempre una mejor solución. Esto quiere decir que si por ejemplo para cada secuencia siempre se encuentra un costo minimo de cambio, en algun momento le diré al sistema que corte.

Score: 1, Bus Local: 50; ejecución 2 veces del grasp de un grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/ca31e8bb-cdb8-41fc-8f11-5958ffddb4eb)

Score: 1, Bus Local: 10; ejecución 2 veces del grasp de un grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/523951fd-7c9d-4c2c-b8a3-a81f2f939290)

Score: 1, Bus Local: 50; ejecución 2 veces del grasp de un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/69767926-733d-4c76-8c2e-c7510b4f0c53)

En el siguiente ejemplo, del lado izquierdo de la pantalla, se puede observar como para una vecindad se encuentran valores muy cercanos, que al largo plazo termina siendo una mejora minima. Por lo que el sistema gracias a este parametro corta, se queda con la minima mejora encontrada, la cual se va a estar mostrando en el grafico.
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/3516e2c4-6b11-4747-a0a5-f8f6dc6e8b07)


## Variación repetición de vecindad
Parametro usado en LocalSearch agregado para saber, a partir del circuito generado por el greedy randomizado, cuantas veces se va a ir repitiendo y buscando por cada vecino o posible solucion swapeada. Este cambio hace que se tarde más o menos tiempo en procesar toda la información, ya que cuanto más alto sea este parametro más tiempo tardará en compilar. Se puede ver que a partir de una secuencia relativamente baja, llega un momento que la solución se aplana totalmente, y no hay variación.

Grafo de 30 nodos; vecindad:50 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/57fbd006-e627-4055-ab6c-7a4ce45f1c32)

Grafo de 30 nodos; vecindad:15 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/331ff3c3-9cf9-4e33-ada0-55e0eaebe71a)


## Aplanamiento GRASP - Variación corteGrasp
Para esta parte de la prueba la variación de los parametros anteriores no cambio, lo unico que fue cambiando fue el parametro corteGrasp, y la cantidad de nodos. 
Después de ejecutar varias veces, e ir jugando con la cantidad de veces que puede repetirse un grasp, pude observar que a partir de la 5ta o 6ta secuencia, la grafica se va aplanando.

Se repite 3 veces un grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/257ce349-5a6a-4805-8586-644ceccc2ad2)
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/40b7f4f5-af09-4f55-9c66-c87187f4a905)

Se repite 5 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/7d6652e2-84af-4429-8769-a7f2d2c30637)
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/4fc218ef-e85a-4a0a-a29d-0d05e1d2bdfe)

Se repite 10 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/2363e29b-0d60-4ac7-90a3-2753aa791cb3)

Se repitio 20 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/155d4c78-2579-4b45-8ba6-197eaeb2e9b5)

## Orden de complejidad
### GreedyRandom.py
En el peor de los casos es O(n^2). Siendo __n__ la cantidad de nodos.
Hacer un sorted en el metodo ElementosOrdenadosPorIndice tiene un O(n log n); pero anteriormente yo estoy recorriendo todo el grafo segun la cantidad de nodos. Por lo que en el peor de los casos la complejidad es n.

### LocalSearch.py
r = O(max(i,j)). Siendo __i__ es el número de corte en el que el sistema siempre encuentra una mejora para una vecindad y __j__ es el parametro de la cantidad de veces de un mejor score. Por ejemplo, en los últimos casos que estuve mostrando en graficos (al ser j=1), el parametro variable era i. Por lo que ese sería el peor orden. Pero al ser j variable, nada me asegura que sea menor que j.
O(v*r*n) Siendo __v__ la cantidad de veces que repito la vecindad, y __n__ siendo la cantidad de nodos.

### Grasp.py
Considero que la complejidad en el peor caso es O(c)*O(max(g, l)). Siendo __c__ la cantidad de veces que repito el grasp, __g__ la complejidad del greedy randomizado y __l__ la complejidad del localsearch. Como yo no puedo suponer si el greedy tiene mayor orden de complejidad que el local search, necesito saber el maximo de los dos.

