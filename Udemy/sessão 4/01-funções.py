'''
Introdução a funções (def) em Python.
Funções são trechos de código usados para replicar determinada ação ao longo do sistema.
Eles podem receber valores para parâmetros (argumentos) e reportnar um valor específico.
Por padrão as funcoes python retornam None (nada).

'''

def Print():
    print('AAAAA')

def soma(x1,x2):
    soma = x1 + x2
    return soma

def saudacao(nome = 'Sem nome'):
    print(f'Ola {nome}')

Print()
x1 = int(input("Informe o valor de X1: "))
x2 = int(input("Informe o valor de X2: "))
resultado = soma(x1, x2)
print(resultado)

for i in range(5):
    nome = input('Informe o nome: ')
    saudacao(nome)