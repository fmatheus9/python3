'''
Calcular a média dos valores das
posições ímpares de um vetor. Passar o
vetor como parâmetro e retornar a
média.

'''

import random

def media(vetor): 
    m = 0
    x = 0
    for i in range(10):
        if i % 2 != 0:
            m = m + vetor[i]
            x += 1
    if x == 0:
        return 0
    else:
        m = m/x
        return m

vetor = []
for i in range(10):
    vetor.append(random.randint(1,100))
m = media(vetor)
print(vetor)
print(f"Média dos valores das posições ímpares do vetor: {m}")
