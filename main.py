from _vizualize import *

MENU_STRING = "1) Criar grafo\n2) Obter ordem do grafo\n3) Obter tamanho do grafo\n4) Obter lista de vertices adjacentes\n5) Obter grau do vértice\n6) Verificar se dois vértices são adjacentes\n7) Obter o menor caminho entre dois vértices\n8) Sair\n"

def menu():

	

	print("Bem-vindo ao nosso Sistema de Grafos!\n")

	option = 0

	while(option != 8):

		print(MENU_STRING)
		option = int(input("Digite a opção desejada: "))

		if (option == 1):

			while True:
				try:
					arquivo = input('Digite o nome do arquivo (acompanhado do formato): ')		
					with open(arquivo) as f:
						contents = f.read()

				except FileNotFoundError:
					print("nome incorreto do arquivo ou arquivo nao encontrado")
					continue
				break
			
			grafo = GraphVisualization()
			removn = contents.split('\n')

			for i in removn:
				a = i.split()
				b= a[0].split(',')
				grafo.addEdge(b[0],b[1])

			
			grafo.visualize()
			f.close()

		elif (option == 2):
			
			arquivo = "arquivo.txt"
			with open(arquivo) as f:
				g = f.read()

			real_g = g.replace(",", "\n")
			
			order_g = list(set(real_g.split("\n")))
			
			print("Ordem do grafo:",len(order_g),"\n")
			
			

		elif (option == 3):

			arquivo = "arquivo.txt"
			with open(arquivo) as f:
				g = f.read()
			real_g = g.split("\n")
			print("Tamanho do grafo:",len(real_g),"\n")
			





menu()
# menu:
# Digite a opção desejada: 1) Criar grafo 2) Obter ordem do grafo 3) Obter tamanho do grafo 4) Obter lista de vertices adjacentes

#while True:
#	try:
#		arquivo = input('Digite o nome do arquivo (acompanhado do formato): ')		
#		with open(arquivo) as f:
#			contents = f.read()
#
#	except FileNotFoundError:
#		print("nome incorreto do arquivo ou arquivo nao encontrado")
#		continue
#	break
#

#count = 0


#print(contents)




# G = GraphVisualization()
# G.addEdge(0, 2)
# for i in range(3):
# 	G.addEdge(1,i)
# G.visualize()
