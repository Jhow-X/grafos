import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

	def __init__(self):
		self.visual = []
		self.Wvisual = []
	
	def addEdge(self, a, b):
		"""Recebe dois elementos e adiciona em um array vazio
		para criar um grafo não valorado

		Args:
			a (any): primeiro vertice
			b (any): segundo vertice
		"""
		temp = [a, b]
		self.visual.append(temp)
	
	def addWeigEdge(self, a, b, c):
		"""Recebe três elementos e adiciona em um array vazio
		para criar um grafo valorado

		Args:
			a (any): primeiro vertice
			b (any): segundo vertice
			c (number): peso da aresta
		"""
		temp = [a, b, c]
		self.Wvisual.append(temp)
	
	def Nodeconected(self,grafo):
		"""Recebe um grafo para uma verificação de conexão e diz se os dois vertices estão conectados

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		u = input('v1: ')
		v = input('v2: ')
		if u in grafo.neighbors(v):
			print(u,'e',v,'Sao vizinhos\n')
		else:
			print(u, 'e',v,'Nao sao vizinhos\n')

	def grauV(self,grafo):
		"""Recebe um grafo para uma checagem de grau e pendencia para um grafo não direcionado e no final diz o grau e se um vertice é pendente ou não


		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		variavel = input("Vertice: ")
		gr = grafo.degree[variavel]
		print('grau do vertice:',gr)
		if gr == 1:
			print("pendente\n")
		else:
			print('nao pendente\n')
		

	def grauVD(self,grafo):
		"""Recebe um grafo para uma checagem de grau e pendencia para um grafo direcionado e no final diz o grau de entrada e saída e se um vertice é pendente ou não


		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		variavel = input("Vertice: ")
		gr = grafo.degree[variavel]
		print('grau de entrada: ',grafo.in_degree(variavel))
		print('grau de saida: ',grafo.out_degree(variavel))
		if gr == 1:
			print("pendente\n")
		else:
			print('nao pendente\n')

	def isAdj(self,grafo):
		"""Checa os vertices adjacentes ao vertice passado de um grafo não direcionado e retorna a lista com todos

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		variavel = input("Digite o vertice que deseja verificar: ")
		print('vertices adjacentes: ',grafo.edges(variavel))

	def isAdjD(self,grafo):
		"""Checa os vertices adjacentes ao vertice passado de um grafo direcionado e retorna a lista com todos separados por entrada e saída

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		variavel = input("Digite o vertice que deseja verificar: ")
		print('vertices adjacentes de entrada: ',grafo.in_edges(variavel))
		print('vertices adjacentes de saida: ',grafo.out_edges(variavel),'\n')

	def shortP(self,grafo):
		"""Checa o menor caminho entre dois vertices de um grafo não valorado e retorna uma lista de v1 a v2

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		try:
			t1 = input('de: ')
			t2 = input('para: ')
			sp= nx.shortest_path(grafo,t1,t2)
			print('menor caminho de',t1,'para',t2,':',sp,"\n")
		except nx.NetworkXNoPath:
			print("não existem caminhos de",t1,"ate", t2,'\n')

	def shortPV(self,grafo):
		"""Checa o menor caminho entre dois vertices de um grafo valorado e retorna uma lista de v1 a v2 e o custo total do caminho

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		try:
			t1 = input('de: ')
			t2 = input('para: ')
			sp= nx.single_source_dijkstra(grafo,t1,t2)
			print('menor caminho de',t1,'para',t2,':',sp,"\n")
		except nx.NetworkXNoPath:
			print("não existem caminhos de",t1,"ate", t2,'\n')

	def getOrder(self,grafo):
		"""Recebe um grafo e retorna sua ordem

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		print('ordem do grafo:',grafo.order(),'\n')

	def getSize(self,grafo):
		"""Recebe um grafo e retorna seu tamanho

		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		print('tamanho do grafo: ',grafo.size(),'\n')

	def visualize(self,directed,weighted):
		"""Função principal do programa, responsável por montar, exibir e retornar o grafo passado pelo usuário dependendo do tipo de grafo

		Args:
			directed (int): Informa se um grafo é direcionado ou não
			weighted (int): Informa se um grafo é valorado ou não

		Returns:
			grafo: Retorna um grafo preenchido com os valores passados pelo usuário
		"""
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
