'''
INTRODUÇÃO AO DESEMPACOTAMENTO + TUPLAS
'''

nomes = ['Maria', 'Joao', 'Pedro']
nome1, nome2, nome3 = nomes
print(nome1)

#ou

nome1, nome2, nome3 = ['Maria', 'Joao', 'Pedro']
print(nome1)

nome1, *_ = ['Maria', 'Joao', 'Pedro']
print(nome1, _)

_, nome2, _ = ['Maria', 'Joao', 'Pedro']
print(nome2)

#tuplas uma lista imutavel

lista_tuple = (1, 'lucas', 423, True, 5.4)
print(lista_tuple)
print(lista_tuple[-1])



