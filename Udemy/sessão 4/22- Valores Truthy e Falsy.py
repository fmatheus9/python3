'''
Valores Truthy e Falsy
Tipos mutáveis - [], {}, set()
Tipos imutáveis - '', 0, 0.0, None, False, range(), tuple()
'''

lista = []
dic = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
real = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(falsy(lista))
print(falsy(dic))
print(falsy(conjunto))
print(falsy(tupla))
print(falsy(string))
print(falsy(inteiro))
print(falsy(real))
print(falsy(nada))
print(falsy(falso))
print(falsy(intervalo))
print()

lista = [1]
dic = {1}
conjunto = set('1')
tupla = (1)
string = '1'
inteiro = 1
real = 0.01
nada = None
falso = True
intervalo = range(10)

print(falsy(lista))
print(falsy(dic))
print(falsy(conjunto))
print(falsy(tupla))
print(falsy(string))
print(falsy(inteiro))
print(falsy(real))
print(falsy(nada))
print(falsy(falso))
print(falsy(intervalo))
print()