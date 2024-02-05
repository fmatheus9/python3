'''
1-Crie uma função que multiplica todos os argumentos não nomeados recebidos.
2-Crie uma função que fala se o número é par ou ímpar.

'''
def multip(*args):
    acm = 1
    for i in args:
        acm = acm * i
    return acm

def func(num):
    if num % 2 == 0:
        return 'Par'
    return 'Impar'

numeros = 1,2,3,4,5
result = multip(*numeros)
print(result)

num = int(input("Informe um número: "))
print(func(num))

