'''
Métodos úteis dos dicionários em python.
    len - quantidade (de chaves nesse caso)
    keys - iteraveis com as chaves
    values - iteraveis com os valores
    items - iteraveis com as chaves e valores
    setdefault - adiciona valor se a chave não existe
    copy - retorna uma cópia rasa
    get - obtem uma chave
    pop - apaga um item com a chave especificada
    popitem - apaga o uktimo item adicionado
    update - atualiza um dicionário com outro

'''

pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Ferrarezi',
    'l1': [0,2,3,4,15]
}

print(len(pessoa)) # mostra a quantidade de chaves 
print()

print(list(pessoa.keys())) #retorna as chaves do dicionário em forma de list
for i in pessoa.keys():
    print(i)
print()

print(list(pessoa.values())) #retorna os valores das chaves
for i in pessoa.values():
    print(i)
print()

print(list(pessoa.items())) #mostra as chaves e os valores
for i in pessoa.items():
    print(i)
print()

pessoa.setdefault('idade', 10) #adiciona uma chave e um valor à biblioteca
print(pessoa['idade'])
print()

pessoa2 = pessoa.copy() #faz uma copia do 'pessoa' para o 'pessoa2' sem alterar a biblioteca do 'pessoa'. Porem não copia valores mutaveis como uma lista por exemplo.
pessoa2['nome'] = 'luiz'
print(list(pessoa.values()))
print(list(pessoa2.values()))
pessoa2['l1'][0] = 100 #nesse caso muda as duas bibliotecas.
print(list(pessoa.values()))
print(list(pessoa2.values()))
print()

import copy
pessoa2 = copy.deepcopy(pessoa) # desse jeito os valores mutaveis não sao alterados nas duas bibliotecas
pessoa2['l1'][0] = 10000 
print(list(pessoa.values()))
print(list(pessoa2.values()))
print()

print(pessoa.get('nome'))
print(pessoa['nome'])
print()

nome = pessoa.pop('nome') #a variável 'nome' recebe o valor da chave 'nome' e a função pop o apaga da biblioteca
print(nome)
print(pessoa)
pessoa.setdefault('nome',nome)
print(pessoa)
print()

pessoa.update({ #atualiza a biblioteca
    'nome': 'Novonome',
    'idade': 'AAAA',
    'l2': [3,4,62,61,245,3]
})
print(pessoa)