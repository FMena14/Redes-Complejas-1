from igraph import *
import pandas as pd
import re

#--Lectura grafo tarea 1--
def cargar_tarea1():
	aux = pd.read_csv("datosT3/grafo_tarea1",delimiter="\s+")
	A= [ tuple( map(int, edge[:2]) ) for edge in aux.values ]
	tarea1 = Graph(edges=A,directed=False)
	return tarea1

grafo_tarea1 = cargar_tarea1()

n = grafo_tarea1.vcount()
density = grafo_tarea1.density()


#grados = grafo_tarea1.degree()


# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 20
visual_style["edge_width"] = 2

#plot(grafo_tarea1, **visual_style)

##---Erdos Renyi
grafo_ER = Graph().Erdos_Renyi(n=n,p= density) #puede ser Erdos_Renyi(n=nodostarea1,m=numero de edges)


#plot(grafo_ER, **visual_style)

#grafo_BA = Graph().Barabasi(n=n, m=density)

##--Aleatorizar red tarea1
grafo_tarea1_aleatorizada = grafo_tarea1.copy()
m=grafo_tarea1.ecount()
grafo_tarea1_aleatorizada.rewire(n=2*m)

#plot(grafo_tarea1_aleatorizada, **visual_style)



print "densidad grafo tarea 1: ",density
print "densidad grafo con E-R: ",grafo_ER.density()
#print "densidad grafo con B-A: ",grafo_BA.density()
print "densidad grafo tarea 1 aleatorizada: ",grafo_tarea1_aleatorizada.density()



##calcula la cantida de core
def cores(grafo):
	lista = grafo.coreness()
	return {i:lista.count(i) for i in set(lista)}
	#for i in lista:

#analizar
print "cores grafo tarea1: ",cores(grafo_tarea1)
print "cores grafo E-R: ",cores(grafo_ER)
print "cores grafo tarea1 aleatorizada: ",cores(grafo_tarea1_aleatorizada)


##calcula la modularidad
def modularidad(grafo):
	aux = grafo.community_fastgreedy()
	algoritmo_gloton = aux.as_clustering()
	return grafo.modularity(algoritmo_gloton)

print "modularidad grafo tarea1: ",modularidad(grafo_tarea1)
print "modularidad grafo E-R: ",modularidad(grafo_ER)
print "modularidad grafo tarea1 aleatorizada: ",modularidad(grafo_tarea1_aleatorizada)


##calcula la asortividad
print "asortividad grafo tarea1: ",grafo_tarea1.assortativity_degree(directed=False)
print "asortividad grafo E-R: ",grafo_ER.assortativity_degree(directed=False)
print "asortividad grafo tarea1 aleatorizada: ",grafo_tarea1_aleatorizada.assortativity_degree(directed=False)

import matplotlib.pyplot as plt
def graficar_knn(grafo):
	lista = grafo_tarea1.knn()[1]
	plt.plot( range(1,len(lista)+1), lista )
	plt.xticks(range(1,len(lista)+1))
	plt.xlabel('grado')
	plt.ylabel('grado promedio de vecinos')
	plt.title('grafico knn')
	plt.show()
#knn
graficar_knn(grafo_tarea1)
