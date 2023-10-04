soma = 0
cont = 0
for c in range (1,11,1):
    num = int(input(f"Informe valor {c}: "))
    if(num % 2 == 0):
        soma = soma + num
        cont = cont + 1
if cont != 0: 
    print(f"A média aritimética dos números pare informados é igual a {soma/cont}")
else:
    print("Nenhum valor par informado")