vetor = []
for i in range(10):
    vetor.append(int(input(f"Informe o valor {i}: ")))

maior_valor = vetor[0]
menor_valor = vetor[0]

for i in range(10):
    if menor_valor > vetor[i]:
        menor_valor = vetor[i]
    if maior_valor < vetor[i]:
        maior_valor = vetor[i]

print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")