#Crie um programa que leia um vetor de 30 números inteiros e gere um segundo vetor cujas posições 
#pares são o dobro do vetor original e as ímpares são o triplo.


vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(int(input(f"Informe o valor {i}: ")))

for i in range(10):
    if vetor1[i] % 2 == 0: 
        vetor2.append(vetor1[i]*2)
    else:
        vetor2.append(vetor1[i]*3)

print(vetor2)