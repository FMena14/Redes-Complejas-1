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


#analizar
print grafo_tarea1.coreness()
print grafo_ER.coreness()
print grafo_tarea1_aleatorizada.coreness()
