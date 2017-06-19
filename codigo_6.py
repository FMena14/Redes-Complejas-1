from igraph import *
import operator
from tabulate import tabulate

def separar_en_listas(lista):
	l1 = []
	l2 = []

	for tupla in lista:
		x,y = tupla
		l1.append(x)
		l2.append(y)

	return l1,l2
# -----------------------------------------------

# Carga de archivo
red_chica = Graph.Read_GML("datosT3/redchica.gml")

# A) Graficar con atributos -----------------------------------------------

# Atributos por vertice -------------------
grados = red_chica.degree()
betweenness = red_chica.edge_betweenness()
page_rank = red_chica.pagerank()

red_chica.vs["grados"] = grados
red_chica.vs["betweenness"] = betweenness
red_chica.vs["page_rank"] = page_rank

# Etiquetas customizadas -------------------
labels = red_chica.vs["label"]
new_labels = []

for i in range(len(labels)):
	new_label = "\n\n\n\n\n"+labels[i]+": G:"+str(grados[i])+"\nB:"+str(betweenness[i])+"\nP:"+str(page_rank[i])
	new_labels.append(new_label)

red_chica.vs["label"] = new_labels

# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 1

plot(red_chica, **visual_style)

# B) Ranking segun atributos de cada vertice ------------------------------

grados_aux = {}
betweenness_aux = {}
page_rank_aux = {}

for i in range(len(labels)):
	vertice = labels[i]

	grados_aux[vertice] = grados[i]
	betweenness_aux[vertice] = betweenness[i]
	page_rank_aux[vertice] = page_rank[i]

grados_aux = sorted(grados_aux.items(), key=operator.itemgetter(1),reverse=True)
betweenness_aux = sorted(betweenness_aux.items(), key=operator.itemgetter(1),reverse=True)
page_rank_aux = sorted(page_rank_aux.items(), key=operator.itemgetter(1),reverse=True)

grados_l1, grados_l2 = separar_en_listas(grados_aux)
betweenness_l1, betweenness_l2 = separar_en_listas(betweenness_aux)
page_rank_l1, page_rank_l2 = separar_en_listas(page_rank_aux)

separacion = ["#","#","#","#","#","#","#","#","#","#"]

a = [grados_l1,grados_l2,separacion,betweenness_l1,betweenness_l2,separacion,page_rank_l1,page_rank_l2]
table =  zip(*a)

print tabulate(table, headers=["Etiqueta","Grado","#","Etiqueta","Betweenness","#","Etiqueta","PageRank"],  tablefmt="rst")





'''
visual_style = {}
visual_style["vertex_size"] = 20
visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
visual_style["vertex_label"] = g.vs["name"]
visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
visual_style["layout"] = layout
visual_style["bbox"] = (300, 300)
visual_style["margin"] = 20
plot(g, **visual_style)
'''

#layout = red_chica.layout("kk")
#plot(red_chica, layout = layout)




'''
red_gnutella = Graph.Read_GML("datosT3/gnutella.gml")

layout = red_gnutella.layout("kk")
plot(red_gnutella, layout = layout)


red_correos = Graph.Read_GML("datosT3/correos.gml")

layout = red_correos.layout("kk")
plot(red_correos, layout = layout)

'''


''' Documentacion READS -----------------------------------------------
Read_DIMACS(f, directed=False)
Reads a graph from a file conforming to the DIMACS minimum-cost flow file format.	source code
 	
Read_DL(f, directed=True)
Reads an UCINET DL file and creates a graph based on it.	source code
 	
Read_Edgelist(f, directed=True)
Reads an edge list from a file and creates a graph based on it.	source code
 	
Read_GML(f)
Reads a GML file and creates a graph based on it.	source code
 	
Read_GraphDB(f, directed=False)
Reads a GraphDB format file and creates a graph based on it.	source code
 	
Read_GraphML(f, directed=True, index=0)
Reads a GraphML format file and creates a graph based on it.	source code
 	
Read_Lgl(f, names=True, weights="if_present", directed=True)
Reads an .lgl file used by LGL.	source code
 	
Read_Ncol(f, names=True, weights="if_present", directed=True)
Reads an .ncol file used by LGL.	source code
 	
Read_Pajek(f)

'''


