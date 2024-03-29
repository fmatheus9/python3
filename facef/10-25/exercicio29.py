'''
Fazer um programa que possui um menu com as
seguintes opções para executar diferentes funções, até
que o usuário digite -1 e termine o programa:

(OK) Escrever a tabuada de um número ou uma mensagem
de erro caso o número não esteja entre 1 e 9. O
número deve ser passado como parâmetro e a
validação feita na função.

(OK) Calcular o Índice de Massa Corporal (IMC): a fórmula
é IMC = peso / altura2 Passar o peso e altura como
parâmetros e retornar o IMC.
◦ Calcular o fatorial de um número. O número deve ser
passado como parâmetro e retornar o resultado.

'''
def tabuada(x):
    resultado = []
    if x > 9 or x < 1:
        print('Valor inválido')
        print("=======================================")
    else:
        for i in range(10):
            print(f"{i+1} x {x} = {x*(i+1)}")
        print("=======================================")
        

def imc(peso, altura):
    if altura > 2.2:
        altura = altura / 100
    resultado = peso / (altura*altura)
    return resultado
        
def fatorial(f):
    fa = 1
    for i in range(f):
        fa = fa * (i+1)
    return fa


condicao = True 
print("MENU DE OPÇÕES:")
while condicao: 
    n = int(input("[1] Escrever a tabuada de um número.\n[2] Calcular o Índice de Massa Corporal (IMC).\n[3] Calcular o fatorial de um número.\n[-1] Encerra o programa.\n= "))
    if n == 1: 
        x = int(input("Informe um valor (1 a 9): "))
        tabuada(x)
    elif n == 2:
        peso = float(input("Informe o peso: "))
        altura = float(input("Informe a altura: "))
        resultado = imc(peso, altura)
        print(f"IMC: {resultado:.2f}kg/m2")
        print("=======================================")
    elif n == 3:
        f = int(input("Informe o valor: "))
        fa = fatorial(f)
        print(f"O fatorial de {f} = {fa}")
        print("=======================================")
    elif n == -1:
        print("Fim do sistema.")
        condicao = False