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
#betweenness = g.edge_betweenness()
page_rank = g.pagerank()

L = g.laplacian()
print "Matriz laplaciana: ", L
EV = g.eigenvector_centrality()
print "Vector propio: ", EV

#g.vs["grados"] = grados
#g.vs["betweenness"] = betweenness
#g.vs["page_rank"] = page_rank

print(g)

new_labels = []
for i in range(6):
	new_label = "\n\n\n\n\n G:"+str(grados[i]/2)+"\nVal prop:"+str(round(EV[i],3))
	new_labels.append(new_label)

g.vs["label"] = new_labels


# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 100
visual_style["edge_width"] = 1

plot(g, **visual_style)

plot(g, "red_pregunta2.png")