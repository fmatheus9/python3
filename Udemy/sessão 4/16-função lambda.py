# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lambda arguments : expression <-----------------------------------------------------------------
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

lista = [1,2,8,4,3,6,9,4,2,67,7654,32345,2]
lista.sort() #ordena a lista. Lista com números e letras por exemplo o python ordena sozinho.
print(lista)

#essa lista, que possiu dicionarios, o python não sabe como ordenar. Então precisamos ensinar como ordenar essa estrutura de dados 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#ORDENAR POR FUNÇÃO

def ordena(item):
    return item['nome'] #o item é as bibliotecas. Para cada item, ele ordena de acordo com a chave nome

lista.sort(key=ordena) #passa a função que sera utilizada para a ordenação.
for item in lista: #mostra cada item na lista, mas agora de forma ordenada.
    print(item)
print()
#ORDENAR POR FUNÇÃO LAMBDA

lista.sort(key=lambda item: item['sobrenome']) #key=lambda(como se fosse o def) item(parametros): item['sobrenome'](o item que deseja ordenar)
for item in lista: #mostra cada item na lista, mas agora de forma ordenada.
    print(item)