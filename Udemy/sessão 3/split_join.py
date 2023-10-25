# split - divide uma string
# join - une uma string

frase = 'Olha so! que coisa doida'
print(frase)
lista_palavras = frase.split()
print(lista_palavras)
lista_palavras = frase.split('! ')
print(lista_palavras)

frases_unidas = ' - '.join('abc')
print(frases_unidas)