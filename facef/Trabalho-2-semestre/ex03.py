'''
3.Fazer um programa que desenvolva um jogo para adivinhar uma palavra oculta. Será um jogo
semelhante ao da forca, mas com algumas diferenças. Neste jogo, o jogador tenta adivinhar uma
palavra oculta, mediante uma quantidade de tentativas limitada. Para isso, o programa escolhe,
aleatoriamente, uma palavra de uma lista de palavras contidas em um arquivo e o jogador deve
adivinhar a palavra. Essa lista deve conter, no mínimo, 10 palavras. A quantidade de tentativas
também deve ser aleatória, em um intervalo de 6 a 11. Quando o jogador adivinha alguma letra,
as letras correspondentes na palavra são reveladas. Além disso, deve ser informado também a
quantidade de tentativas que ainda resta quando a letra for incorreta, mensagem caso já tenha
tentado a letra, e outras situações para tornar o jogo mais interessante. O jogo finaliza quando o
jogador adivinhar a palavra ou acabar as suas tentativas.

'''
import random 

def funcao(palavra_secreta, tentativas):
    letras_acertadas = ''
    letras_tentadas = ''
    numero_tentativas = 0
    condicao = True
    while condicao:
        letra_digitada = input('Digite uma letra: ').upper() #INFROMA UMA LETRA 
        numero_tentativas += 1 
        while letra_digitada in letras_tentadas or len(letra_digitada) > 1: #SE A LETRA ESTIVER NAS LETRAS ACERTADAS PEDE PRA INFORMAR DENOVO
            print("Letra repetida ou mais de uma letra digitada.")
            letra_digitada = input('Digite uma nova letra: ').upper()
        letras_tentadas += letra_digitada

        if letra_digitada in palavra_secreta: #SE A LETRA DIGITADA ESTIVER NA PALAVRA SECRETA ADICIONA A LETRA NAS "LETRAS ACERTADAS"
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta: #PERCORRE A PALAVRA SECRETA E ADICIONA A PALAVRA_FORMADA SE A LETRA FOR CORRETA
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '_'
        print(f"Tentativas restantes: {tentativas-numero_tentativas}")
        print(f'Palavra secreta: {palavra_formada}\n================================================')

        if palavra_formada == palavra_secreta and tentativas-numero_tentativas >= 0:
            return 'ACETROU!'
            condicao = False
        elif palavra_formada != palavra_secreta and numero_tentativas == tentativas:
            return 'Não acertou.'
            condicao = False
            

palavras = []
with open("Trabalho-2-semestre\palavras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

palavra_secreta = random.choice(palavras)
print("ACERTE A PALAVRA")
print("________")
print("|      |")        
print("|      O")        
print("|    / | \ ")    
print("|     / \ ")        
print("|\n")        
tentativas = random.randint(6,11)
print(f"Você possui {tentativas} tentativas para acertar a palavra.\n================================================")
resultado = funcao(palavra_secreta, tentativas)
print(resultado)
print(f"A palavra era: {palavra_secreta}")