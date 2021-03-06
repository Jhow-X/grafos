from _vizualize import *
import networkx as nx
import matplotlib.pyplot as plt
MENU_STRING = "1) Criar grafo 1 por 1 \n2) Criar grafo em lote\n3) Obter ordem do grafo\n4) Obter tamanho do grafo\n5) Obter lista de vertices adjacentes\n6) Obter grau e pendencia do vértice\n7) Verificar se dois vértices são adjacentes\n8) Obter o menor caminho entre dois vértices\n9) Sair\n"
grafo = GraphVisualization()
def menu():
	"""Menu da aplicação, responsável por toda lógica do programa
	"""

	print("Bem-vindo ao nosso Sistema de Grafos!\n")

	option = 0

	while(option != 9):

		print(MENU_STRING)
		option = int(input("Digite a opção desejada: "))
		
		if (option == 1):
			G = nx.Graph()
			flag = 0
			while(flag != '$'):
				flag = input("Digite '$' para parar de digitar as arestas ")
				if(flag != '$'):
					G.add_node(flag)
			flag1 = 0
			flag2 = 0
			while(flag1 != '$' or flag2 != '$'):
				flag1 = input("Digite '$' para parar de digitar os vertices ou digite a primeira aresta ")
				flag2 = input("Digite '$' para parar de digitar os vertices ou digite a segunda aresta ")
	
				if(flag != '$' or flag2 != '$'):
					G.add_edge(flag1, flag2)
			nx.draw_networkx(G)
			plt.show()
			sp = G
			direcionado = 0
			valorado = 0
			
		elif (option == 2):

			direcionado = int(input("digite 1 para direcionado 0 para não direcionado: "))
			valorado = int(input("digite 1 para valorado 0 para não valorado: "))

			while True:
				try:
					arquivo = input('Digite o nome do arquivo (acompanhado do formato): ')		
					with open(arquivo) as f:
						contents = f.read()

				except FileNotFoundError:
					print("nome incorreto do arquivo ou arquivo nao encontrado")
					continue
				break

			removn = contents.split('\n')
			if valorado == 0:
				for i in removn:
					a = i.split()
					b= a[0].split(',')
					grafo.addEdge(b[0],b[1])
			else:
				for i in removn:
					a = i.split()
					b= a[0].split(',')
					grafo.addWeigEdge(b[0],b[1],float(b[2]))

			sp = grafo.visualize(direcionado,valorado)

		elif (option == 3):
			grafo.getOrder(sp)
			
		elif (option == 4):
			grafo.getSize(sp)
			
		elif (option == 5):
			if direcionado == 0:
				grafo.isAdj(sp)
			else:
				grafo.isAdjD(sp)
			
		elif (option == 6):
			if direcionado == 0:
				grafo.grauV(sp)
			else:
				grafo.grauVD(sp)

		elif(option == 7):
			grafo.Nodeconected(sp)

		elif (option == 8):
			if valorado == 0:
				grafo.shortP(sp)
			else:
				grafo.shortPV(sp)
		


menu()
