from igraph import *
import pandas as pd
import re

#--Lectura grafo tarea 1--
def cargar_tarea1():
	aux = pd.read_csv("datosT3/grafo_tarea1",delimiter="\s+")
	tarea1 = Graph()
	n=1467+1
	tarea1.add_vertices(n)
	A= [ tuple( map(int, edge[:2]) ) for edge in aux.values ]
	tarea1.add_edges(A)
	return tarea1


grafo_tarea1 = cargar_tarea1()
#gafo_tarea1 = Graph.Adjacency(A.astype(bool).tolist())


# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 20
visual_style["edge_width"] = 2

plot(grafo_tarea1, **visual_style)
#grafo_ER = Erdos_Renyi(n=nodostarea1,p) #puede ser Erdos_Renyi(n=nodostarea1,m=numero de edges)
#grafo_BA = Barabasi(n=nodostarea1, m)