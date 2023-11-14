'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma
prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número
de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a
ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o
valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste
momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a
quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação, e quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
def valorPagamento(valor_prestacao, atraso):
    if atraso == 0:
        resultado = valor_prestacao
        return resultado
    elif atraso > 0:
        resultado = valor_prestacao + (valor_prestacao*0.03)
        for i in range(atraso):
            resultado = resultado + (resultado * 0.001)
        return resultado

condicao = True
quantidade = 0
valor_total = 0

print("\nEXERCICIO 1: CÁLCULO DE PRESTAÇÕES")
while(condicao):
    valor_prestacao = float(input("Informe o valor da prestação: "))
    if valor_prestacao == 0:
        print("=======================================\nRELATÓRIO DO DIA")
        print(f"Quantidade de prestações: {quantidade}\nValor total das prestações: R${valor_total:.2f}")
        condicao = False
    else:
        atraso = int(input("Informe a quantidade de dias de atraso: "))
        resultado = valorPagamento(valor_prestacao, atraso)
        quantidade += 1
        valor_total += resultado
        print(f"O valor a ser pago é de R${resultado:.2f}\n=======================================")
    
