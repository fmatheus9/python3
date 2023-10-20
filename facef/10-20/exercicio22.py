'''
Crie um programa que leia um vetor de 20 números inteiros e 
em seguida divida estes números em outros 2 novos vetores, separando os números pares dos números ímpares.
'''

vetor = []
vetor_pares = []
vetor_impares = []

for i in range(20):
    vetor.append(int(input(f"Informe o valor {i+1}: ")))

for i in range(20):
    if vetor[i] % 2 == 0: 
        vetor_pares.append(vetor[i])
    else:
        vetor_impares.append(vetor[i])
    
print(f"Vetor original: {vetor}\n")
print(f"Vetor dos números pares: {vetor_pares}\n")
print(f"Vetor dos números ímpares: {vetor_impares}")