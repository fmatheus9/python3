'''
Fazer uma função que calcule o
quociente inteiro da divisão entre dois
números, sem utilizar funções prontas.

'''

def divisao(n1,n2):
    quociente = n1/n2
    print(f"Quociente inteiro da divisão entre {n1} e {n2} = {quociente:.0f}")

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
divisao(n1,n2)