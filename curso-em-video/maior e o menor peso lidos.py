#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 200
for i in range(5):
    peso = float(input(f'Informe o peso {i+1}: '))
    if peso < menor_peso:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
print(f'O maior peso foi: {maior_peso}Kg')
print(f'O menor peso foi: {menor_peso}Kg')