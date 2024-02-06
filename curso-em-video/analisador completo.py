#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
idade_mais_velho = 0
nome_mais_velho = ''
qnt = 0

for c in range(4):
    print(f'============{c+1}ª Pessoa============')
    nome = input(f'Informe o nome {c+1}: ')
    idade = int(input(f'Informe a idade {c+1}: '))
    sexo = input(f'Informe o sexo (M/F): ').upper()

    media = media + idade
    if idade > idade_mais_velho and sexo == 'M':
        idade_mais_velho = idade
        nome_mais_velho = nome

    if sexo == 'F' and idade < 20:
        qnt =+ 1


print(f'Média de idade do grupo: {media/4}')
print(f'Homem mais velho: {nome_mais_velho}')
print(f'Quantidade de mulheres com menos de 20 anos: {qnt}')
