print("Exercício calculadora ")
while True:
    operacao = str(input("Informe uma operação (+,-,x,/ ou (s)sair): "))
    if(operacao == '+'):
        n1 = float(input("Informe o n1: "))
        n2 = float(input("Informe o n2: "))
        resultado = n1+n2
        print(f"Resultado = {resultado}")
    elif(operacao == '-'):
        n1 = float(input("Informe o n1: "))
        n2 = float(input("Informe o n2: "))
        resultado = n1-n2
        print(f"Resultado = {resultado}")
    elif(operacao == 'x'):
        n1 = float(input("Informe o n1: "))
        n2 = float(input("Informe o n2: "))
        resultado = n1*n2
        print(f"Resultado = {resultado}")
    elif(operacao == '/'):
        n1 = float(input("Informe o n1: "))
        n2 = float(input("Informe o n2: "))
        resultado = n1/n2
        print(f"Resultado = {resultado}")
    elif(operacao == 's'):
        print("Programa encerrado")
        break