#Iterables e Iterators
#iteraval - um item sequencial, que pode acessar coisas sequencialmente, tem a responsabilidade de deter os valores sequencialmente.
#o iterator - entrega um valor por vez. É uma classe que tem o método iter e o next. Trabalha com iteraveis

iterable = ['eu', 'tenho', '__iter__']
iterator = iterable.__iter__()
print(next(iterator)) #nao tem indice, nem tamanho, so mostra o proximo valor
print(next(iterator))
print(next(iterator))

#Generator expression, Iterables e Iterators em Python
#geretaror são funções que sabem pausar 
import sys 
generator = (n for n in range(10000)) #criado um generator expression 
lista = [n for n in range(10000)]
print('Memória utilizada para o generator ',sys.getsizeof(generator))
print('Memória utilizada para a lista ',sys.getsizeof(lista))
#o generator não salva todos os valore na memória. So mostra um valor por vez 
#porem não tem indice, tamanho ja que não esta na memória
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#generator function
#geretaror são funções que sabem pausar