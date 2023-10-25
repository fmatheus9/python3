lista = []
x = True
while x == True:
    print("SELECIONE UMA OPÇÃO")
    y = str(input("[I]NSERIR - [A]PAGAR - [L]ISTAR - [S]AIR:\n --> ")).upper()
    if y == 'I':
        valor_inserir = input("Informe o valor a ser inserido na lista: ")
        lista.append(valor_inserir)
    elif y == 'A':
        if len(lista) == 0:
            print("NENHUM VALOR INFORMADO NA LISTA")
        else:
            valor_apagar = int(input("Escolha um indice para apagar: "))
            if valor_apagar > len(lista) or type(valor_apagar) != int:
                print("Valor inválido")
            else: 
                lista.pop(valor_apagar)
    elif y == 'L':
        print(lista)
    elif y == 'S':
        print("Fim do sistema")
        print(f"Valor final da lista: {lista}")
        x = False