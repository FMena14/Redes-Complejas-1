from igraph import *

# Estilo del ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 70
visual_style["edge_width"] = 1
# -----------------------------------------

# Carga del archivo de epinion
epinion = Graph.Read_Pajek("datosT3/epinion_signed.net")
n = epinion.vcount()
m = epinion.ecount()

print "Numero de vertices: ",n
print "Numero de arcos: ",m

#plot(epinion, **visual_style)