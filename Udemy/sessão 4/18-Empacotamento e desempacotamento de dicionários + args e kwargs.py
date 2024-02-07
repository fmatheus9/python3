#Empacotamento e Desempacotamento de Dicionários

a, b = 1, 2
a, b = b, a
print(a,b)

pessoa = {
    'nome': 'Anile',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.70,
}

print(pessoa, dados_pessoa)
#como juntar os dados dos 2 dicionários?
pessoa_completa = { #primeira opção é criar um outro dicionário vazio e colocar a extração dos valores (**)
    **pessoa,
    **dados_pessoa,
    'sexo': 'F' #pode adicionar mais chaves ao dicionário
}
print(pessoa_completa)

a, b = pessoa
print(a,b) #por padrão mostra so as chaves
a, b = pessoa.values() #mostra os valores
print(a,b) 
a, b = pessoa.items() #mostra as chaves e valores 
print(a,b)
for chave, valor in pessoa.items():
    print(chave,valor)

#args e kwargs
#args = argumentos não nomeados 
#key words arguments (argumentos nomeados)
def mostra_argumentos_nomeados(*args,**kwargs):
    #não nomeados
    print(args)
    #nomeados
    for chave, valor in kwargs.items():
        print(chave,valor)

mostra_argumentos_nomeados(1,2,3,nome='JOANA', qlq = 123)
mostra_argumentos_nomeados(**pessoa_completa)

config = { 
    'chave1': 'x1',
    'chave2': 'x2',
    'chave3': 'x3',
    'chave4': 'x4',
    'chave5': 'x5',
    'chave6': 'x6',
    'chave7': 'x7',
    'chave8': 'x8',
    'chave9': 'x9',
}
mostra_argumentos_nomeados(**config)