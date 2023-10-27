'''
Fazer uma função que receba o valor de
N como parâmetro, calcular e retorne o
valor do somatório S:

'''
def somatorio(N):
    s = 0.0
    for i in range(N):
        s = s + (i+1) / ((i+1)*(i+1))
    return s

N = int(input("Informe o valor de N: "))
s = somatorio(N)
print(f"Valor do somatório: {s}")