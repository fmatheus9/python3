'''
Fazer uma função que retorne o menor
elemento de um vetor.

'''
import random

def menor_elemento(vetor, tamanho_vetor):
    menor = vetor[0]
    for i in range(tamanho_vetor):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor

vetor = []
tamanho_vetor = int(input("Informe a quantidade de indices do vetor: "))
for i in range(tamanho_vetor):
    vetor.append(random.randint(1,100))

print(f"VETOR:\n\n{vetor}\n")
x = menor_elemento(vetor, tamanho_vetor)
print(f"Menor elemento do vetor {x}")