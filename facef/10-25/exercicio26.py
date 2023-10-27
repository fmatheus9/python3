'''
Fazer uma função que retorne o maior
elemento de um vetor.

'''
import random

def maior_elemento(vetor, tamanho_vetor):
    maior = vetor[0]
    for i in range(tamanho_vetor):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior

vetor = []
tamanho_vetor = int(input("Informe a quantidade de indices do vetor: "))
for i in range(tamanho_vetor):
    vetor.append(random.randint(1,100))

print(f"VETOR:\n\n{vetor}\n")
x = maior_elemento(vetor, tamanho_vetor)
print(f"Maior elemento do vetor {x}")