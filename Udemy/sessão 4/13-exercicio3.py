perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': [1,2,3,4],
        'Resposta': 4,
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': [25,10,20,15],
        'Resposta': 25,
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': [4,5,6,3],
        'Resposta': 5,
    }
]

cont = 0
resultado = 0
for i in range(len(perguntas)): #A lista tem 3 dicionarios, ou seja 3 indices. 
    print(perguntas[i]['Pergunta']) #O print mostra a 'Pergunta' do dicionário de cada índice da lista.
    print("Opções:")
    j=0
    for alternativas in perguntas[i]['Opções']: #for para mostrar as opçoes
        print(f'{j}) {alternativas}')
        j = j + 1
        if alternativas == perguntas[i]['Resposta']:
            resultado = j-1
    resp = int(input("Resposta (Informe a Alternativa Correta): "))
    if resp == resultado:
        print("ACERTOU!!")
        print()    
        cont = cont + 1
    else:
        print("Errou :(") 
        print()   
print(f'Total de acertos: {cont}')
        

    