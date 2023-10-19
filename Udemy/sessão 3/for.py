texto = 'Matheus'
novo_texto = ''
for letra in texto:
    novo_texto += f'{letra} - '
print('- '+novo_texto)

numero = int(input("Informe um valor: "))
for i in range(1, 11, 1):
    print(numero*i)
print("==========")
for i in range(10, 0, -1):
    print(numero*i)