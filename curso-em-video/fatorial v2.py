
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
def funcao(f):
    result = 1
    i = 1
    while i <= f:
        result = result * i
        i = i + 1
    return result
f = int(input("Informe o valor: "))
result = funcao(f)
print(f'Resultado: {result}')