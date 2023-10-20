'''
Crie um programa que permita a leitura de um vetor de 30 números inteiros e gere um segundo vetor com os mesmos dados, 
só que de maneira invertida, ou seja, o primeiro elemento do vetor original ficará na última posição do novo vetor, 
o segundo na penúltima posição e assim por diante.

'''

vetor1 = []
vetor2 = []

for i in range(30):
    vetor1.append(int(input(f"Informe o valor {i+1}: ")))

for i in range(30):
    vetor2.append(vetor1[29-i])

print(vetor2)