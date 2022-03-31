from _vizualize import *

while True:
	try:
		arquivo = input('Digite o nome do arquivo (acompanhado do formato): ')		
		with open(arquivo) as f:
			contents = f.read()

	except FileNotFoundError:
		print("nome incorreto do arquivo ou arquivo nao encontrado")
		continue
	break


count = 0


#print(contents)
grafo = GraphVisualization()
removn = contents.split('\n')

for i in removn:
	a = i.split()
	b= a[0].split(',')
	grafo.addEdge(b[0],b[1])



grafo.visualize()

f.close()

# G = GraphVisualization()
# G.addEdge(0, 2)
# for i in range(3):
# 	G.addEdge(1,i)
# G.visualize()
