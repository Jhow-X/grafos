# Sistema de visualização e analise de grafos

Sistema básico para criação de grafos manualmente ou através de arquivos

## Baixando o projeto

Para baixar todo projeto:
```shell
$ git clone https://github.com/Jhow-X/grafos.git
```

## Setup inicial
no mesmo diretório do makefile rode:
```shell
$ make venv
```
caso não possua o python3-venv ler a [documentação](https://docs.python.org/3/library/venv.html)

Após isso rode:
```shell
$ source graf/bin/activate
```
Para inicializar o ambiente virtual.

Para importar as coisas necessárias pra executar o código, rode:
```shell
$ make import
```

com isso tudo estará setado e pronto para o funcionamento do projeto então por fim rode:
```shell
$ make run
```
para iniciar o projeto

# Passando os dados

## Manualmente

O sistema começará a pedir os vértices um a um para parar de inserir valores é só digitar '$'(sem as aspas), depois começará a pedir a informação das arestas e para parar faça igual anteriormente.

## Usando arquivos
os valores são passados em um arquivo (preferencialmente txt ou csv) com os valores separados por vírgulas como no exemplo a baixo:
```text
1,2
```
O sistema cria grafos direcionados e não direcionados com base na opção escolhida considerando o valor da esquerda como o vertice de saída e o da direita como vértice de entrada.
### Grafos valorados
Para criar grafos valorados apenas adicione uma coluna a mais com o valor do peso, como no exemplo a baixo:
```text
1,2,40
```
