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
	
	def Nodeconected(self,grafo):
		u = input('v1: ')
		v = input('v2: ')
		if u in grafo.neighbors(v):
			print(u,'e',v,'Sao vizinhos\n')
		else:
			print(u, 'e',v,'Nao sao vizinhos\n')

	def grauV(self,grafo):
		variavel = input("Vertice: ")
		print('grau do vertice:',grafo.degree[variavel],'\n')

	def grauVD(self,grafo):
		variavel = input("Vertice: ")
		print('grau de entrada: ',grafo.in_degree(variavel))
		print('grau de saida: ',grafo.out_degree(variavel),'\n')

	def isAdj(self,grafo):
		variavel = input("Digite o vertice que deseja verificar: ")
		print('vertices adjacentes: ',grafo.edges(variavel))

	def isAdjD(self,grafo):
		variavel = input("Digite o vertice que deseja verificar: ")
		print('vertices adjacentes de entrada: ',grafo.in_edges(variavel))
		print('vertices adjacentes de saida: ',grafo.out_edges(variavel),'\n')

	def shortP(self,grafo):
		try:
			t1 = input('de: ')
			t2 = input('para: ')
			sp= nx.shortest_path(grafo,t1,t2)
			print('menor caminho de',t1,'para',t2,':',sp,"\n")
		except nx.NetworkXNoPath:
			print("não existem caminhos de",t1,"ate", t2,'\n')

	def shortPV(self,grafo):
		try:
			t1 = input('de: ')
			t2 = input('para: ')
			sp= nx.single_source_dijkstra(grafo,t1,t2)
			print('menor caminho de',t1,'para',t2,':',sp,"\n")
		except nx.NetworkXNoPath:
			print("não existem caminhos de",t1,"ate", t2,'\n')

	def getOrder(self,grafo):
		print('ordem do grafo:',grafo.order())
		
	def visualize(self,directed,weighted):
		if directed == 0:
			if weighted == 0:
				G = nx.Graph()
				G.add_edges_from(self.visual)
				nx.draw_networkx(G)
				plt.show()
				return G
			else:
				G = nx.Graph()
				G.add_weighted_edges_from(self.Wvisual)
				pos=nx.spring_layout(G)
				nx.draw_networkx(G,pos)
				labels = nx.get_edge_attributes(G,'weight')
				nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
				plt.show()
				return G
		else:
			if weighted == 0:
				DG = nx.DiGraph()
				DG.add_edges_from(self.visual)
				nx.draw_networkx(DG)
				plt.show()
				return DG
			else:
				DG = nx.DiGraph()
				DG.add_weighted_edges_from(self.Wvisual)
				pos=nx.spring_layout(DG)
				nx.draw_networkx(DG,pos)
				labels = nx.get_edge_attributes(DG,'weight')
				nx.draw_networkx_edge_labels(DG,pos,edge_labels=labels)
				plt.show()
				return DG

#https://networkx.org/documentation/stable/tutorial.html
