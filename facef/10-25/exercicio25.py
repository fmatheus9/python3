'''
Fazer uma função que calcule a média
dos elementos de um vetor.

'''
import random

def media(vetor):
    resultado = 0
    for i in range(15):
        resultado = resultado + vetor[i]
    resultado = resultado / 15
    return resultado

vetor = []
for i in range(15):
    vetor.append(random.randint(1,10))

print(vetor)
m = media(vetor)
print(f"A média dos valores do vetor é {m:.2f}")