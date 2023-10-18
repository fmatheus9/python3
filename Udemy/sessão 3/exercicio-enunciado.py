"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero = input("Informe um número inteiro: ")
try:
    numero_inteiro = int(numero)
    if(numero_inteiro%2==0):
        print("Numero par")
    else:
        print("Numero impar")
except:
    print("Voce não digitou um número inteiro")



hora = input("Informe a hora: ")
min = input("Informe os minutos: ")

hora_inteiro = int(hora)
if(hora_inteiro<11):
    print("Bom dia!")
elif(hora_inteiro>11 and hora_inteiro<17):
    print("Boa Tarde!")
elif(hora_inteiro>17 and hora_inteiro<24):
    print("Boa noite!")
else:
    print("O horario informado não é valido")

nome = input("Informe seu nome: ")
tamanho_nome = len(nome)
if(tamanho_nome<=4):
    print("Nome curto")
elif(tamanho_nome>4 and tamanho_nome<6):
    print("Nome normal")
else:
    print("Nome longo")