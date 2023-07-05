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
El archivo "Main.py" va a tener la ejecución tanto del grasp como la de greedy/busqueda local/plotter. Se pide comentar alguno de los dos, para no perderse en los logs de ambos.

## Variación veces permitidas por un score 
Parametro usado para no seguir buscando scores en caso de no encontrar mejorias, es decir que le pongo un corte a la cantidad de veces que puede estar revisando una secuencia sin cambio alguno con la anterior. Como se pueden observar en los graficos posteriores, se puede observar para una misma linea como hay más de dos score para una misma solución. Pero al dejarselo para que encuentre uno solo, eso no sucede, y se ve como la linea va decreciendo con distintas soluciones, y no hay más de un score para una misma solución.
Como quise hacer una variación del parametro sin concentrarme en cuando se aplana, deje de graficar las sencuencias en las que el grafico se aplana con respecto a la secuencia anterior. 

Score: 20; 1 grafo de 30 nodos; bus local: 10 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/be734e10-6f6a-4681-964f-0c52d2cf6be5)

Score: 100; 2 grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/2a890a49-bbb4-452f-96ca-92bc0a08b4e0)

Score: 10; 2 grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/aaf88b89-7f62-4e04-bdad-5047d1a0fe8b)

Score: 50; 2 grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/13c94508-2fec-4eec-ab50-44119829af27)

Score: 1; 2 grafo de 30 nodos; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/c2c535a3-20c6-44ef-af40-b58573d4d4a3)

## Variación limite del bus local
Parametro usado para poner un corte en caso de que se encuentre siempre una mejor solución. Esto quiere decir que si por ejemplo para cada secuencia siempre se encuentra un costo minimo de cambio, en algun momento le diré al sistema que corte. Con la variación de este parametro pude observar como se incrementaban las cantidad de secuencias (solución ID), al variar se puede encontrar varias veces un nodo minimo y se estaría agregando al grafico, aunque puede observarse que también se estaría agregando varias secuencias, aunque la diferencia entre una y otra sea infima. 
Como quise hacer una variación del parametro sin concentrarme en cuando se aplana, deje de graficar las sencuencias en las que el grafico se aplana con respecto a la secuencia anterior. 

Score: 1, Bus Local: 15; 1 grafo de 10 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/85172369-5295-476d-8997-bb5f9ae6203d)

Score: 1, Bus Local: 50; 2 grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/d9dffbf5-d6e0-411c-a4c1-ec6052d87147)

Score: 1, Bus Local: 10; 2 grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/695ddd36-3a05-49ff-b8b5-a5f8fe6edcf7)


## Variación repetición de vecindad
Para estos ejemplo se ejecuto 2 veces el grasp. Este parametro fue agregado para saber a partir del arbol greedy randomizado, cuantas veces se va a ir repitiendo y buscando por cada vecino o posible solucion swapeada. Este cambio hace que se tarde más o menos tiempo en procesar toda la información, ya que cuanto más alto sea este parametro más tiempo tardará en compilar. 
Como quise hacer una variación del parametro sin concentrarme en cuando se aplana, deje de graficar las sencuencias en las que el grafico se aplana con respecto a la secuencia anterior. 

Grafo de 30 nodos; vecindad:100 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/2e6934f7-cec8-4a6d-bac7-3010f52a19dc)

Grafo de 30 nodos; vecindad:30 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/7f20d01b-2278-4827-aa48-14ee00f123ad)

## Aplanamiento GRASP - Variación corteGrasp
Para esta parte la variación de los parametros anteriores no cambio, lo unico que fue cambiando fue el parametro corteGrasp, y la cantidad de nodos. 
Después de ejecutar varias veces, e ir jugando con la cantidad de veces que puede repetirse un grasp, pude observar que a partir de la secuencia 5 o 6, la grafica se va aplanando.

Se repite 3 veces un grafo de 30 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/257ce349-5a6a-4805-8586-644ceccc2ad2)
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/40b7f4f5-af09-4f55-9c66-c87187f4a905)

Se repite 5 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/bac5921f-2606-44f6-bb5f-aeb06a79e686)
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/8dde8754-4208-4e7e-aa43-4936cfebddc5)

Se repite 10 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/f6b466d1-dcfe-41d5-a832-362da3f99a04)

Se repitio 100 veces un grafo de 100 nodos
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/e41dfbfe-9ea6-4d43-af6a-befe9b44f4b8)

## Orden de complejidad
### GreedyRandom.py
En el peor de los casos es O(n^2). Siendo n la cantidad de nodos.
Hacer un sorted en el metodo ElementosOrdenadosPorIndice tiene un O(n log n); pero anteriormente yo estoy recorriendo todo el grafo segun la cantidad de nodos. Por lo que en el peor de los casos la complejidad es n.

### LocalSearch.py
O(v*i*j*n) Siendo v la cantidad de veces que repito la vecindad, i el tamaño del bus local, j el parametro de la cantidad de veces de un mejor score y n siendo la cantidad de nodso.

### Grasp.py
Considero que la complejidad en el peor caso es O(c)*O(n^2). Siendo c la cantidad de veces que repito el grasp, y (n^2) como el resultado de greedy. 
Pienso que la complejidad de greedy es peor que la del local search, ya que estuve haciendo pruebas para variables muchisimo menores a n, por lo que el resultado de v*i*j*n < n^2.

