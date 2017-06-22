from igraph import *

# Estilo del ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 1


def calcular_p1(a,n):

	p1 = 0

	for i in range(n):
		for j in range(n):
			if i != j:
				p1 += a[i][j]*a[j][i]

	p1 = float(p1)/float(m)

	return p1

# -----------------------------------------


# Carga del archivo de pescado
pescado = Graph.Read_Pajek("datosT3/pescado.net")
n = pescado.vcount()
m = pescado.ecount()

print "Numero de vertices: ",n
print "Numero de arcos: ",m

#plot(pescado, **visual_style)

# Adjacency_matrix
a = pescado.get_adjacency()

p1 = calcular_p1(a,n)
a_prom = float(m)/(n*(n-1))

# Reciprocidad
p = (p1 - a_prom)/(1-a_prom)

print "Reciprocidad Correjida: ",p

