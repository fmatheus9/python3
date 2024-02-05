'''
Sets - Conjuntos em Python 
São tipos de dados mutaveis mas so aceitam tipos imutaveis. Não aceitam listas ou objetos.
Criando um set --> set(iteravel) ou {1,2,3}

'''

set1 = set()
print(set1)
print()

set1 = set('Matheus')
print(set1)
print()

set1 = {'Matheus', 2,2,3,3,1,1,3,4,1}
print(set1)
print()

'''
São eficientes para remover valores duplicados de iteraveis, pois seus valores sempre serão únicos.
Não aceitam valores mútaveis.
Não tem index.
Não garentem ordem.
São iteraveis (for, in, not in)

'''

lista = [1,2,3,4,5,6,5,3,1,1,0]
set2 = set(lista)
print(set2)
print(4 in set2)
for numero in set2:
    print(numero)
lista2 = list(set2)
print(lista2)
print()

'''
Métodos úteis --> add, update, clear, discard

'''

set3 = set()
set3.add("Matheus")
set3.add(1)
set3.update("Felipe")
print(set3)
set3.clear()
print(set3)
set3.add(1)
print(set3)
set3.discard(1)
print(set3)
print()

'''
Operadores úteis --> união (|), intersecção (&), Diferença (-), diferença simétrica (^) 

'''

set4 = {1,2,3}
set5 = {2,3,4}
uniao = set4 | set5
print(uniao)
inter = set4 & set5
print(inter)
dif = set4 - set5
print(dif)
difs = set4 ^ set5
print(difs)
print()

'''
Exemplo de uso:

'''
letras = set()
while True:
    letra = input("DIGITE UMA LETRA: ")
    letras.add(letra.upper())
    if 'L' in letras:
        print("BOA")
        break

print(letras)