from igraph import *
import random
import operator
import copy

# Estilo del ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 1

# Funcion para hacer la estadisticas de la eliminacion de nodos con diferentes tipos de ataques
def eliminacion_de_nodos(grafo,ataque):

	grafo = copy.copy(grafo)

	num_eliminaciones = 0
	giant_component = grafo.components().giant()

	n = grafo.vcount()
	n_aux = n

	if(ataque == "random"):

		while( float(giant_component.vcount())/float(n) > 0.5 ):
			random_num = random.randint(0,n_aux-1)
			grafo.delete_vertices(random_num)
			giant_component = grafo.components().giant()
			num_eliminaciones += 1
			n_aux -=1


	elif(ataque == "grado_decreciente"):

		grados = grafo.degree()
		grados_aux = {}
		labels = grafo.vs["label"]

		for i in range(len(labels)):
			vertice = labels[i]
			grados_aux[vertice] = grados[i]

		sorted_degree = sorted(grados_aux.items(), key=operator.itemgetter(1),reverse=True)
		labels_aux = labels

		while( float(giant_component.vcount())/float(n) > 0.5 ):
			label = sorted_degree[0][0]
			indice = labels_aux.index(label)
			grafo.delete_vertices(indice)
			giant_component = grafo.components().giant()
			del(sorted_degree[0])
			labels_aux = grafo.vs["label"]
			num_eliminaciones += 1
			n_aux -=1


	elif(ataque == "betweenness_decreciente"):

		betweenness = grafo.edge_betweenness()
		betweenness_aux = {}
		labels = grafo.vs["label"]

		for i in range(len(labels)):
			vertice = labels[i]
			betweenness_aux[vertice] = betweenness[i]

		sorted_betweenness = sorted(betweenness_aux.items(), key=operator.itemgetter(1),reverse=True)
		labels_aux = labels

		while( float(giant_component.vcount())/float(n) > 0.5 ):
			label = sorted_betweenness[0][0]
			indice = labels_aux.index(label)
			grafo.delete_vertices(indice)
			giant_component = grafo.components().giant()
			del(sorted_betweenness[0])
			labels_aux = grafo.vs["label"]
			num_eliminaciones += 1
			n_aux -=1

	#plot(grafo, **visual_style) # Descomentar para ver grafo con eliminaciones
	print "Ataque: "+ ataque.upper()
	print "Numero de Eliminaciones: ", num_eliminaciones
	print "Porcentaje de nodos eliminados: ", int((1-(float(n_aux)/float(n)))*100),"%"

# ----------------------------------------------------------------------------------

# Carga del archivo de nutella
gnutella = Graph.Read_GML("datosT3/gnutella.gml")
n1 = gnutella.vcount()
m1 = gnutella.ecount()

# Erdos Rengy de nutella
erdos_gnutella = Graph.Erdos_Renyi(n=n1,m=m1)
erdos_gnutella.vs["label"] = range(n1)

# Carga del archivo Dolphins
dolphins = Graph.Read_GML("datosT3/dolphins.gml")
n2 = dolphins.vcount()
m2 = dolphins.ecount()

# Erdos Rengy de Dolphins
erdos_dolphins = Graph.Erdos_Renyi(n=n2,m=m2)
erdos_dolphins.vs["label"] = range(n2)


tipos_de_ataques = ["random","grado_decreciente","betweenness_decreciente"]
grafos = [dolphins,erdos_dolphins, gnutella,erdos_gnutella]
nombres = ["Dolphins", "Endos Rengy Dolphins", "Nutella", "Endos Rengy Nutella"]

con = 0

# A cada grafo se le aplican los distintos tipos de eliminacion
for grafo in grafos:

	print "--------- Grafo "+nombres[con]+" --------------------------------"

	for ataque in tipos_de_ataques:
		#plot(grafo, **visual_style) # Se plotea el grafo original cada vez para comparar visualmente
		eliminacion_de_nodos(grafo,ataque)

	con+=1