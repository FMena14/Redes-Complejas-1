from igraph import *

# Estilo del ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 3
# -----------------------------------------

# Carga del archivo de epinion
epinion = Graph.Read_Pajek("datosT3/epinion_signed.net")

n = epinion.vcount()
m = epinion.ecount()
print "Numero de vertices: ",n
print "Numero de arcos: ",m

m_pos = 0
for edge in epinion.es:
	if edge['weight'] == 1:
		m_pos+=1
print "Numero de arcos positivos: ",m_pos
print "Probabilidad p: ", float(m_pos)/m


def triangles(g):
    triangulos = g.cliques(min=3, max=3)
    #print triangulos
    t0,t1,t2,t3 = [0,0,0,0]

    for i, j, k in triangulos: #por cada triangulo
    	arcos = g.es.select(_between = ([i,j,k] ,[i,j,k]) )
    	total_positivos = 0
    	for arco in arcos:
    		if arco['weight'] == 1 and not arco.is_loop() :
    			total_positivos+=1
    	#print "triangulo ", (i,j,k) ,
    	#print "es de tipo ", total_positivos
    	t0 += total_positivos==0
    	t1 += total_positivos==1
    	t2 += total_positivos==2 
    	t3 += total_positivos==3
    return t0,t1,t2,t3

t0,t1,t2,t3 = triangles(epinion)
print "triangulos tipo t0", t0
print "triangulos tipo t1", t1
print "triangulos tipo t2", t2
print "triangulos tipo t3", t3


# Etiquetas customizadas -------------------
#labels = epinion.es["label"]
new_labels = []
colors = []

new_labels2 = []
for v in epinion.vs:
	new_labels2.append(v.index)

for e in epinion.es:
    new_label = int(e['weight'])
    if new_label == 1:
        colors.append("green")
    elif new_label == -1:
        colors.append("red")
    new_labels.append(new_label)

epinion.es["label"] = new_labels
epinion.es["color"] = colors
epinion.vs["color"] = "white"
epinion.vs["label"] = [ v.index for v in epinion.vs]

plot(epinion, **visual_style)