from igraph import *
import numpy as np

# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 50
visual_style["edge_width"] = 2

def crear_particiones(p1,p2):
	particion = range(len(p1+p2))
	for i in p1:
		particion[i]=0
	for i in p2:
		particion[i]=1
	return particion

def modularidad(grafo,particion):
	m = float(grafo.ecount())
	A = grafo.get_adjacency()
	total = 0.0
	for v1 in grafo.vs:
		for v2 in grafo.vs:
			if v1.index != v2.index:
				d1_in = float(v1.degree(mode=IN))
				d2_out = float(v2.degree(mode=OUT))
				misma_particion = particion[v1.index] == particion[v2.index]
				total+= (A[v1.index][v2.index] - d1_in*d2_out/m )*misma_particion
	return total/m


#crear grafo
grafo_ER = Graph().Erdos_Renyi(n=80,p= 0.2)
plot(grafo_ER, **visual_style)

#particiones
B1=range(40)
B2=range(40,80)
C1 =range(20) + range(40,60)
C2 = range(20,40) + range(60,80)

particion1 = crear_particiones(B1,B2)
particion2 = crear_particiones(C1,C2)

#eliminar entre b1 y b2
eliminados = []
for nodo1 in B1:
	for nodo2 in B2:
		try:
			grafo_ER.delete_edges([(nodo1,nodo2)])
			eliminados.append([nodo1,nodo2])
		except Exception as e:
			pass

grafo_ER.to_directed(mutual=False)

#agregar con probabilidad p
probabilidad = 0.8
for eliminar in eliminados:
	orientar1 = np.random.binomial(n=1,p=probabilidad)
	orientar2 = np.random.binomial(n=1,p=1.0-probabilidad)
	if orientar1: #pase probabilidad
		grafo_ER.add_edge(eliminar[0],eliminar[1])
	elif orientar2:
		grafo_ER.add_edge(eliminar[1],eliminar[0])
plot(grafo_ER, **visual_style)

print "Particion B1 y B2 ",grafo_ER.modularity(particion1)
print "Particion B1 y B2 con mia ",modularidad(grafo_ER,particion1)

print "Particion C1 y C2 ",grafo_ER.modularity(particion2)
print "Particion C1 y C2 con mia ",modularidad(grafo_ER,particion2)