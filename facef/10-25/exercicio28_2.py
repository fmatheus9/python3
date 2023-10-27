'''
Fazer uma função que calcule a média dos valores pares de um vetor.

'''
import random
def media(vetor):
    x = 0
    m = 0
    for i in range(10):
        if vetor[i] % 2 == 0:
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
print(f"Média dos valores pares do vetor: {m}")