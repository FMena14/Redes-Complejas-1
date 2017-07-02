from igraph import *
from numpy import std
import matplotlib.pyplot as plt
import scipy.stats as stats


# Estilo del ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 1


def separar_en_listas(lista):
	l1 = []
	l2 = []

	for tupla in lista:
		x,y = tupla
		l1.append(x)
		l2.append(y)

	return l1,l2

# Funcion que calcula la probabilidad de un atributo del grafo con respecto al total
def calcular_P(grafo, atributo, tipo_calculo, mode="ALL"):

	nodos = grafo.vs
	arcos = grafo.es
	con = 0

	if tipo_calculo == "fuerza":

		for nodo in nodos:
			a = grafo.strength(nodo, mode= mode)
			if(a == atributo):
				con +=1

	elif tipo_calculo == "grado":

		for nodo in nodos:
			a = grafo.degree(nodo)
			if(a == atributo):
				con +=1

	elif tipo_calculo == "peso":

		for arco in arcos:
			a = arco["weight"]
			if(a == atributo):
				con +=1

		return float(con)/float(m)

	return float(con)/float(n)

# -----------------------------------------


# Carga del archivo pescado
pescado = Graph.Read_Pajek("datosT3/pescado.net")
n = pescado.vcount()
m = pescado.ecount()

print "Numero de vertices: ",n
print "Numero de arcos: ",m

plot(pescado, **visual_style)

# A)

# Adjacency_matrix
a = pescado.get_adjacency()

p1 = pescado.reciprocity()
a_prom = float(m)/(n*(n-1))

# Reciprocidad
p = (p1 - a_prom)/(1-a_prom)
print "Reciprocidad: ",p1
print "Reciprocidad Correjida: ",p

# B)

# Lista de las sumas de los pesos de arcos IN y OUT
lista_S_in = pescado.strength(pescado.vs, mode="IN")
lista_S_out = pescado.strength(pescado.vs, mode="OUT")

conj_S_in = set(lista_S_in)
conj_S_out = set(lista_S_out)


print "Distribuciones P(S_in) y P(S_out) ---------------------------------------"


lista_fuerzas_in = []
lista_fuerzas_out = []
lista_P_fuerzas_in = []
lista_P_fuerzas_out = []


for fuerza in conj_S_in:
	P_fuerza = calcular_P(pescado, fuerza, "fuerza", "IN")
	lista_fuerzas_in.append(fuerza)
	lista_P_fuerzas_in.append(P_fuerza)

mu_1 = 2.0
sigma_1 = std(lista_fuerzas_in)

print "Mu_in: ", mu_1
print "Sigma_in: ", sigma_1


for fuerza in conj_S_out:
	P_fuerza = calcular_P(pescado, fuerza, "fuerza", "OUT")
	lista_fuerzas_out.append(fuerza)
	lista_P_fuerzas_out.append(P_fuerza)

mu_2 = 0.0
sigma_2 = std(lista_fuerzas_out)

print "Mu_out: ", mu_2
print "Sigma_out: ", sigma_2


# Comparacion graficos de P(S_in) y P(S_out)

f, axarr = plt.subplots(1,2, figsize=(14,5) )

fit = stats.norm.pdf(lista_fuerzas_in, mu_1, 3.3)
axarr[0].plot(lista_fuerzas_in,fit,'-o')
axarr[0].plot( lista_fuerzas_in, lista_P_fuerzas_in)
axarr[0].set_title('Distribucion P(S_in)')
axarr[0].set_xlabel('S_in')
axarr[0].set_ylabel('P(S_in)')

fit = stats.norm.pdf(lista_fuerzas_out, mu_2, 3.9)
axarr[1].plot(lista_fuerzas_out,fit,'-o')
axarr[1].plot( lista_fuerzas_out, lista_P_fuerzas_out)
axarr[1].set_title('Distribucion P(S_out)')
axarr[1].set_xlabel('S_out')
axarr[1].set_ylabel('P(S_out)')

f.tight_layout()
plt.show()


# C)

plt.plot( range(n), lista_S_in, color = 'b', label = "S_in")
plt.plot( range(n), lista_S_out, color = 'g', label = "S_out")

plt.legend(loc=1)
plt.axis([0.0,max(lista_S_out),0.0,100.0])
plt.xlabel('Nodos')
plt.ylabel('Strength')
plt.title('Comparacion S_in y S_out')
plt.show()

# Version no dirigida del grafo
pescado_no_dirigido = pescado.as_undirected(mode="collapse", combine_edges= "sum")

# Evaluacion P()

# P(k)

lista_grados = []
lista_P_grados = []

lista_G = pescado_no_dirigido.degree()
conj_G = set(lista_G)

for grado in conj_G:
	P_grado = calcular_P(pescado_no_dirigido, grado, "grado")
	lista_grados.append(grado)
	lista_P_grados.append(P_grado)

# P(s)

lista_fuerzas = []
lista_P_fuerzas = []

lista_S = pescado_no_dirigido.strength(pescado_no_dirigido.vs)
conj_S = set(lista_S)

for fuerza in conj_S:
	P_fuerza = calcular_P(pescado_no_dirigido, fuerza, "fuerza")
	lista_fuerzas.append(fuerza)
	lista_P_fuerzas.append(P_fuerza)


# P(w)

lista_pesos = []
lista_P_pesos = []

lista_W = pescado_no_dirigido.es["weight"]
conj_W = set(lista_W)

for peso in conj_W:
	P_peso = calcular_P(pescado_no_dirigido, peso, "peso")
	lista_pesos.append(peso)
	lista_P_pesos.append(P_peso)


# Comparacion graficos de P(k), P(s) y P(w)

print "Distribuciones P(K), P(s) y P(w) ---------------------------------------"

mu_k = 15.0
sigma_k = 5.0

print "Mu_k: ",mu_k
print "Sigma_k",sigma_k


fit = stats.norm.pdf(lista_grados, mu_k, sigma_k)
plt.plot(lista_grados,fit,'-o')
plt.plot( lista_grados, lista_P_grados)
plt.title('Distribucion P(k)')
plt.xlabel('k')
plt.ylabel('P(k)')

plt.show()

mu_s = 15.0
sigma_s = 7.5

print "Mu_s: ",mu_s
print "Sigma_s",sigma_s

fit = stats.norm.pdf(lista_fuerzas, mu_s, sigma_s)
plt.plot(lista_fuerzas,fit,'-o')
plt.plot( lista_fuerzas, lista_P_fuerzas)
plt.title('Distribucion P(s)')
plt.xlabel('s')
plt.ylabel('P(s)')

plt.show()

mu_w = 0.0
sigma_w = 1.3

print "Mu_w: ",mu_w
print "Sigma_w",sigma_w

fit = stats.norm.pdf(lista_pesos,mu_w, sigma_w)
plt.plot(lista_pesos,fit,'-o')
plt.plot( lista_pesos, lista_P_pesos)
plt.axis([0.0,30.0,0.0,0.4])
plt.title('Distribucion P(w)')
plt.xlabel('w')
plt.ylabel('P(w)')

plt.show()



# F)

grado = pescado_no_dirigido.degree()
fuerza = pescado_no_dirigido.strength()

plt.plot( grado, fuerza)
plt.title('Grado vs Fuerza')
plt.xlabel('K')
plt.ylabel('S')

plt.show()

# G)

pesos = pescado_no_dirigido.es["weight"]
sorted_degree = sorted(list(set(grado)))

list_coef_clust1 = []
list_coef_clust2 = []


for grado in sorted_degree:

	list_vertex = pescado_no_dirigido.vs.select(_degree=grado)

	if len(list_vertex) != 0:
		vertex = list_vertex[0]

		# Sin pesos
		coef_clust = pescado_no_dirigido.transitivity_local_undirected(vertex)
		list_coef_clust1.append(coef_clust)

		# Con pesos
		coef_clust = pescado_no_dirigido.transitivity_local_undirected(vertex, weights=pesos)
		list_coef_clust2.append(coef_clust)


# Comparacion graficos de C(k) y C_w(k)

f, axarr = plt.subplots(1,2, figsize=(14,5) )

axarr[0].plot( sorted_degree, list_coef_clust1)
axarr[0].set_title('Coef. clustering vs grado')
axarr[0].set_xlabel('k')
axarr[0].set_ylabel('C(k)')

axarr[1].plot( sorted_degree, list_coef_clust2)
axarr[1].set_title('Coef. clustering (con pesos) vs grado')
axarr[1].set_xlabel('k')
axarr[1].set_ylabel('C_w(k)')

f.tight_layout()
plt.show()