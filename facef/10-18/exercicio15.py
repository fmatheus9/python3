list = []
for i in range(10):
    list.append(int(input("Informe um valor: ")))

soma = 0
contador = 0
media = 0
for i in range(10):
    if list[i] % 2 == 0:
        soma = soma + list[i]
        contador = contador + 1

if soma == 0:
    print("Nenhum valor par dentro do vetor. ")
else:
    media = soma / contador
    print(f"Media dos números pares = {media}")