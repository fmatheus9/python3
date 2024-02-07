#list comprehension é uma forma de criar lista a partir de iteraveis 
#Um objeto é chamado de iterável se formos capazes de obter um iterador dele, estruturas como lista, tupla e string são iteráveis.

print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

#list comprehension:
lista_nova = [
    numero 
    for numero in range(10)
] 
print(lista_nova)

lista_nova = [
    numero * 2 
    for numero in range(10)
] 
print(lista_nova)

#mapeamento de dados em list comprehension
#gerar uma nova lista transformando os dados, mas mantendo o mesmo tamanho
#é oq vem antes do 'for'
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
    {'nome': 'p4', 'preço': 40, }
]

novos_produto = [
    produto
    for produto in produtos
]
print(*novos_produto, sep='\n')

novos_produto = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    
]
print(*novos_produto, sep='\n')

#filtro:
#vai ser um 'if' depois do 'for'
lista1 = [
    n 
    for n in range(10)
    if n < 5 #inclui o valor se ele for menor do q 5 
]
print(lista1)