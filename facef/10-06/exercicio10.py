soma = 0
contador = 0 

num = int(input("Informe um valor: "))
if num % 2 == 0 and num != 0:
    soma = soma + num 
    contador += 1
    while(num != 0):
        num = int(input(f"Informe valor: "))
        if(num % 2 == 0):
            soma = soma + num
            contador = contador + 1
    resultado = soma/(contador-1)
    print(f"A média aritimética dos números pare informados é igual a {resultado:.2f}")
else:
    print("Nenhum valor par informado.")