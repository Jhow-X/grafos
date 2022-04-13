# Arquivos
Breve explicação sobre os arquivos presentes no projeto
## Makefile
Contém os atalhos para ajudar a rodar o projeto com mais facilidade
```Makefile
all: run

run:
	python3 main.py

save:
	pip freeze > requirements.txt

import:
	pip install -r requirements.txt

venv:
	python3 -m venv graf

```
## _vizualize.py
Contém as principais funções do programa e imports

## main.py
Contém o código por trás das escolhas do usuário

## requirements.txt
Contém os requisitos para executar o programa

## peso,voos,arquivo.txt
Contém valores para teste do projeto e podem ser modificados seguindo as regras

* `arquivo.txt`: para grafos não valorados
* `peso,voos.txt`: para grafos valorados