"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
"""

print("Crie um programa que leia dois valores e mostre um menu na tela:")
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
condicao = True
while condicao:
    opcao = int(input("Informe a função a se realizar:\n[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n--> "))
    if opcao == 1:
        resultado1 = lambda n1,n2: n1+n2
        print(resultado1(n1,n2))
        
    elif opcao == 2:
        resultado2 = lambda n1,n2:n1*n2
        print(resultado2(n1,n2))

    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é o maior valor')
        elif n1 < n2:
            print(f'{n2} é o maior valor')
        else:
            print('São iguais')

    elif opcao == 4:
        n1 = int(input("Informe o primeiro número: "))
        n2 = int(input("Informe o segundo número: "))

    elif opcao == 5:
        condicao = False

    
