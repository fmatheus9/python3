#Manipulando chaves e valores em dicionários 

pessoa = {} #declaração

chave = 'nome_completo'
pessoa[chave] = 'Matheus Ferrarezi'
#pessoa['nome'] = 'Matheus Ferrarezi'
print(pessoa[chave])
print(pessoa)

pessoa['nome'] = 'Felipe'
pessoa['sobrenome'] = 'Almeida'
print(pessoa)

del pessoa['sobrenome'] #deletar uma chave
print(pessoa)

if pessoa.get('sobrenome') is None:
    print("Não Existe")
else:
    print(pessoa['sobrenome'])