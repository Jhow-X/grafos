# Todas as funções do código
Breve descrição contendo todos os arquivos de código do projeto e suas funções 

código fonte e demais arquivos usados para teste [aqui](https://github.com/Jhow-X/grafos)
## main.py
Menu da aplicação, responsável por toda lógica do programa
```python
def menu():
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

``` 
## _vizualize.py
### init
lista de arrays vazios que serão populados pelos valores passados pelo usuário
```python
def __init__(self):
        self.visual = [] // array para grafos não valorados
        self.Wvisual = [] // array para grafos valorados

```
### addEdge
Recebe dois elementos e adiciona em um array vazio para criar um grafo não valorado
```python
def addEdge(self, a, b):
        """
		Args:
			a (any): primeiro vertice
			b (any): segundo vertice
		"""
		temp = [a, b]
		self.visual.append(temp)
	

```
### addWeigEdge
Recebe três elementos e adiciona em um array vazio para criar um grafo valorado
```python
def addWeigEdge(self, a, b, c):
		"""
		Args:
			a (any): primeiro vertice
			b (any): segundo vertice
			c (number): peso da aresta
		"""
		temp = [a, b, c]
		self.Wvisual.append(temp)

```
### Nodeconected
Recebe um grafo para uma verificação de conexão e diz se os dois vertices estão conectados
```python
def Nodeconected(self,grafo):
		"""
		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		u = input('v1: ')
		v = input('v2: ')
		if u in grafo.neighbors(v):
			print(u,'e',v,'Sao vizinhos\n')
		else:
			print(u, 'e',v,'Nao sao vizinhos\n')


```
### grauV
Recebe um grafo para uma checagem de grau e pendencia para um grafo não direcionado e no final diz o grau e se um vertice é pendente ou não
```python
def grauV(self,grafo):
		"""
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

```
### grauVD
Recebe um grafo para uma checagem de grau e pendencia para um grafo direcionado e no final diz o grau de entrada e saída e se um vertice é pendente ou não
```python
def grauVD(self,grafo):
		"""
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

```
### isAdj
Checa os vertices adjacentes ao vertice passado de um grafo não direcionado e retorna a lista com todos
```python
def isAdj(self,grafo):
		"""
		Args:
			grafo (graph): Grafo preenchido com os valores
		"""
		variavel = input("Digite o vertice que deseja verificar: ")
		print('vertices adjacentes: ',grafo.edges(variavel))

```
### isAdjD
Checa os vertices adjacentes ao vertice passado de um grafo direcionado e retorna a lista com todos separados por entrada e saída
```python
def isAdjD(self,grafo):
    """
    Args:
        grafo (graph): Grafo preenchido com os valores
    """
    variavel = input("Digite o vertice que deseja verificar: ")
    print('vertices adjacentes de entrada: ',grafo.in_edges(variavel))
    print('vertices adjacentes de saida: ',grafo.out_edges(variavel),'\n')

```
### shortP
Checa o menor caminho entre dois vertices de um grafo não valorado e retorna uma lista de v1 a v2
```python
def shortP(self,grafo):
    """
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


```
### shortPV
Checa o menor caminho entre dois vertices de um grafo valorado e retorna uma lista de v1 a v2 e o custo total do caminho
```python
def shortPV(self,grafo):
    """
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

```
### getOrder e getSize
Recebe um grafo, retorna sua ordem e tamanho

```python
def getOrder(self,grafo):
    """
    Args:
        grafo (graph): Grafo preenchido com os valores
    """
    print('ordem do grafo:',grafo.order(),'\n')

def getSize(self,grafo):
    """
    Args:
        grafo (graph): Grafo preenchido com os valores
    """
    print('tamanho do grafo: ',grafo.size(),'\n')

```
### visualize
Função principal do programa, responsável por montar, exibir e retornar o grafo passado pelo usuário dependendo do tipo de grafo
```python
def visualize(self,directed,weighted):
    """
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

```