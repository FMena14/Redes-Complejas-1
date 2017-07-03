from igraph import *
import pandas as pd

#g = Graph.Full(3)
matriz_adyacencia = [  
	[0,1,1,0,0,0],
	[1,0,1,0,0,0],
	[1,1,0,1,0,0],
	[0,0,1,0,1,1],
	[0,0,0,1,0,1],
	[0,0,0,1,1,0]
]
a = pd.DataFrame(matriz_adyacencia)

A= a.values
g = Graph.Adjacency(A.astype(bool).tolist())

print g.density()

grados = g.degree()

L = g.laplacian()
print "Matriz laplaciana: ", L

import numpy as np
lambdas,w = np.linalg.eig(L)
print "valor propio asociado ",lambdas
print "vectores propios ",w

val2 = sorted(lambdas)[1]
print "valor de Fiedler ", val2 #segundo mas grande
w2 = w[:, np.where(lambdas ==val2)]
print "vector propio asociado ", w2


new_labels = []
for i in range(6):
	new_label = "\n\n\n\n G:"+str(grados[i]/2)+"\nVal prop:"+str(round(w2[i],3))
	new_labels.append(new_label)

g.vs["label"] = new_labels


# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 100
visual_style["edge_width"] = 1

plot(g, **visual_style)