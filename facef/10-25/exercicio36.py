'''
Fazer um algoritmo que leia a idade e o nome de 30 pessoas (o algoritmo não deve permitir valores inválidos).
Os valores lidos devem ser armazenados em um vetor. Após a leitura de todos os valores, encontre: 

a) a média das idades; 
b) a quantidade de pessoas que possuem idade acima da média; 
c) o nome das pessoas que possuem idade abaixo da média; 
d) o nome da pessoa mais velha e da mais nova; 
e) para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.

'''
def funcao1(idade):
    media = 0
    for i in range(5):
        media = media + idade[i]
    media = media/5
    return media

def funcao2(idade, a):
    qnt = 0
    for i in range(5):
        if idade[i] > a:
            qnt +=1
    return qnt

def funcao3(idade,nomes, a): 
    for i in range(5):
        if idade[i] < a:
            print(nomes[i])

def funcao4(nomes, idade):
    idadeMais = idade[0]
    idadeMenos = idade[0]
    nomeMais = nomes[0]
    nomeMenos = nomes[0]
    for i in range(5):
        if(idadeMais < idade[i]):
            idadeMais = idade[i]
            nomeMais = nomes[i]
        if(idadeMenos > idade[i]):
            idadeMenos = idade[i]
            nomeMenos = nomes[i]
    print(nomeMais)
    print(nomeMenos)

def funcao5(idade):
    for i in range(5):
        f = 1
        for j in range(idade[i]+1):
            if j == 0:
                f = 1
            else:
                f = f * j
        print(f)

nomes = []
idade = []
for i in range(5):
    nomes.append(input(f"NOME[{i+1}]: "))
    idade.append(int(input(f"IDADE[{i+1}]: ")))
    while idade[i] < 0:
        idade.append(int(input(f"IDADE[{i+1}]: ")))

a = funcao1(idade)
print(a)
b = funcao2(idade, a)
print(b)
c = funcao3(idade,nomes, a)
d = funcao4(nomes, idade)
e = funcao5(idade)
