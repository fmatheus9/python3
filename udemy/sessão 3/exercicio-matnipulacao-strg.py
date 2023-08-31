nome = input('Digite seu nome: ')
idade = int(input('Informe sua idade: '))

if(nome == ' ' or idade == ' '):
    print('Desculpe, voçê deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1::-1]}')
    if (' 'in nome): 
        print('Seu nome contrem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letra/caracteres')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')