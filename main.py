from _vizualize import *

# try:
# 	arquivo = input('Digite o nome do arquivo (acompanhado do formato): ')
# except:
# 	print('nome do arquivo incorreto, tente novamente')



# count = 0

# with open(arquivo) as f:
#     contents = f.read()

# #print(contents)
# grafo = GraphVisualization()
# removn = contents.split('\n')
# splited = removn.split()

# for i in splited:
# 	a = i
# 	print(a)


# for i in splited:
# 	a,b = splited.split(',')
# 	grafo.addEdge(a,b)

# grafo.visualize()

#f.close()
G = GraphVisualization()
G.addEdge(0, 2)
for i in range(3):
	G.addEdge(1,i)
G.visualize()
