
'''
A MODA de um vetor de números é o número no vetor que é repetido com maior frequência.
Se mais de um número for repetido com frequência máxima igual, não existirá uma moda.
Escreva uma função que aceite um vetor de números e retorne a moda ou uma indicação de que
a moda não existe.
'''

import random

def funcao(vetor):
    moda = []
    vetor_comparacao1 = []
    vetor_comparacao2 = []

    # adiciona o valor 0 a todas as posiçoes do vetor 'moda' e compara todos os valores dentro do vetor passado como parametro para verificar repetiçoes
    for i in range(20):
        moda.append(0)
        for j in range(20):
            if vetor[i] == vetor[j]:
                moda[i] += 1
    
    frequencia = moda[0] # define a frequencia como sendo o primeiro valor do vetor moda
    valor = 0
    for i in range(20): # compara os valores dentro do vetor moda para achar a maior frequencia
        if frequencia < moda[i]:
            frequencia = moda[i]
            if frequencia == moda[i]: 
                valor = i # 'valor' recebe o indice da maior frequencia
    
    #para verificar se existe mais de um valor que possui a maior frequencia, cria-se um vetor 'vetor_comparacao1' que recebe os valores 
    #que possuem a maior frequencia
    for i in range(20):
        if moda[i] == frequencia:
            vetor_comparacao1.append(vetor[i])
        vetor_comparacao2 = vetor_comparacao1[::-1] # inverte o vetor 'vetor_comparacao1' e adiciona ao 'vetor_comparacao2'
    for i in range(len(vetor_comparacao1)): 
        if(vetor_comparacao1[i] != vetor_comparacao2[i]) or vetor_comparacao1[i] != vetor_comparacao1[i+1]: # compara os vetores para ver se existem numeros diferentes
            return -1 #caso existam numeros diferentes a funcao retorna -1
        else:
            return vetor[valor]
    
    
vetor = []
print("\nEXERCICIO 2: MODA DE UM VETOR")
for i in range(20):
    vetor.append(int(input(f'Vetor[{i+1}]: ')))

print(vetor,'\n')
resultado = funcao(vetor)
if resultado == -1:
    print("Não existe uma moda.\n")
    
else:
    print(f"MODA = {resultado}\n")
