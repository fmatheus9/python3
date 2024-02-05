'''
Crie funções que que duplicam, triplicam e quadruplicam o numero recebido como parâmetro.

'''

def criar_multiplicador(i): #função que cria outra função (multiplicar). Recebe o valor de 'i'.
    def multiplicar(numero):#função que multiplica o valor de i pelo número informado e retorna o resultado.
        return numero * i
    return multiplicar #retorna o resutado do retorno da função 'multiplicar', por assim dizer

numero = int(input('Numero: '))
for i in range(2,5,1): #estrutura de repetição de começa do 2 e vai ae o 5.
    x = criar_multiplicador(i) 
    print(x(numero))