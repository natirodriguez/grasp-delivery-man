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
Parametro usado para no seguir buscando scores en caso de no encontrar mejoraias. Como se pueden observar en los graficos posteriores, se puede observar para una misma linea como hay más de dos score para una misma solución. Pero al dejarselo para que encuentre uno solo, eso no sucede, y se ve como la linea va decreciendo con distintas soluciones, y no hay más de un score para una misma solución.

Score: 20; 1 grafo: 10x10; bus local: 10 
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/be734e10-6f6a-4681-964f-0c52d2cf6be5)

Score: 100; 2 grafo: 30x30; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/2a890a49-bbb4-452f-96ca-92bc0a08b4e0)

Score: 10; 2 grafo: 30x30; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/aaf88b89-7f62-4e04-bdad-5047d1a0fe8b)

Score: 50; 2 grafo: 30x30; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/13c94508-2fec-4eec-ab50-44119829af27)

Score: 1; 2 grafo: 30x30; bus local: 10
![image](https://github.com/natirodriguez/grasp-delivery-man/assets/1548366/c2c535a3-20c6-44ef-af40-b58573d4d4a3)


