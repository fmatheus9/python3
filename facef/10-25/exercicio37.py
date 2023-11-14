def maior_valor(vetor):
    maior = vetor[0]
    for i in range(5):
        if maior < vetor[i]:
            maior = vetor[i]
    return maior

def segundo_maior(vetor):
    maior = maior_valor(vetor) #não passa como parametro, mas chama dentro da funcao.
    smaior = vetor[1] if(vetor[0] == maior) else vetor[0] 
    for i in range(5):
        if smaior < vetor[i] and vetor[i] != maior:
            smaior = vetor[i]
    return smaior

vetor = []
for i in range(5):
    vetor.append(int(input(f"N{i+1}: ")))

maior = maior_valor(vetor)
print(maior)
segundo = segundo_maior(vetor)
print(segundo)