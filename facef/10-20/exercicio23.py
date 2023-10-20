'''
Crie um programa que leia uma série de 50 notas e calcule quantas são 10% acima da média e quantas são 10% abaixo da média.
'''

import random
notas = []
media = 0

for i in range(50):
    notas.append(float(random.randint(0,10)))
    media = media + notas[i]

media = media/50
acm_media = media + media*0.1
abx_media = media - media*0.1

qnt1 = 0 
qnt2 = 0

for i in range(50):
    if notas[i] > acm_media:
        qnt1 = qnt1+1
    elif notas[i] < abx_media:
        qnt2 = qnt2 + 1

print(f"Média: {media}")
print(f"Quantidade de pessoas com a nota 10% acima da média: {qnt1}")
print(f"Qunatidade de pessoas com a nota 10% abaixo da média: {qnt2}")