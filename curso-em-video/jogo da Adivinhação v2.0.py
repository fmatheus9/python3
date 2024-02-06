#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
numero = random.randint(1,10)
condicao = True
tentativas = 0

while condicao == True:
    t = int(input("Tente acertar o valor: "))
    tentativas = tentativas + 1
    print(f'Tentativa número {tentativas}')
    if t == numero:
        print("Acertou!")
        condicao = False
    else:
        print('Tente novamente')

print(f"Acertou em {tentativas} tentativas!")