import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

	def __init__(self):
		self.visual = []
		self.Wvisual = []
	
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
	
	def addWeigEdge(self, a, b, c):
		temp = [a, b, c]
		self.Wvisual.append(temp)

	def visualize(self,directed,weighted):
		if directed == 0:
			if weighted == 0:
				G = nx.Graph()
				G.add_edges_from(self.visual)
				nx.draw_networkx(G)
				plt.show()
			else:
				G = nx.Graph()
				G.add_weighted_edges_from(self.Wvisual)
				pos=nx.spring_layout(G)
				nx.draw_networkx(G,pos)
				labels = nx.get_edge_attributes(G,'weight')
				nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
				plt.show()
		else:
			if weighted == 0:
				DG = nx.DiGraph()
				DG.add_edges_from(self.visual)
				nx.draw_networkx(DG)
				plt.show()
			else:
				DG = nx.DiGraph()
				DG.add_weighted_edges_from(self.Wvisual)
				pos=nx.spring_layout(DG)
				nx.draw_networkx(DG,pos)
				labels = nx.get_edge_attributes(DG,'weight')
				nx.draw_networkx_edge_labels(DG,pos,edge_labels=labels)
				plt.show()

#https://networkx.org/documentation/stable/tutorial.html
