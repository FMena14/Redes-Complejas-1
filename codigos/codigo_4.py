from igraph import *

g = Graph()

g.add_vertices(12)

g.add_edges([
	(0,1), (0,2), (2,1),
	(3,4), (3,5), (4,5),
	(6,7), (6,8), (7,8),
	(9,10), (9,11), (10,11)
	])
print g

new_labels = []
for i in range(12):
	new_label = str(i)
	new_labels.append(new_label)

g.vs["label"] = new_labels

# Estilo y ploteo --------------------------
visual_style = {}
visual_style["bbox"] = (900, 600)
visual_style["margin"] = 100
visual_style["edge_width"] = 1

plot(g, **visual_style)
