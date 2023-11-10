'''
9. Fazer uma função que verifique se o
número de um CPF é válido.

'''

def validar_cpf(cpf):
    numeros_cpf = []
    soma_primeiro = 0
    soma_segundo = 0
    j = 10

    for digito in cpf:
        numeros_cpf.append(int(digito))

    for i in range(9):
        soma_primeiro = soma_primeiro + numeros_cpf[i] * j 
        j = j - 1

    resto_soma_cpf = (soma_primeiro * 10) % 11
    primeiro_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf 

    j = 11
    for i in range(10):
        soma_segundo = soma_segundo + numeros_cpf[i] * j 
        j = j - 1

    resto_soma_cpf = (soma_segundo * 10) % 11
    segundo_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf 

    if primeiro_digito == numeros_cpf[9] and segundo_digito == numeros_cpf[10]:
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")

cpf = input("Informe o CPF: ") \
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')
validar_cpf(cpf)






import random
numeros_cpf = []
soma_primeiro = 0
soma_segundo = 0
j = 10

print("GERADOR DE CPF")
cpf = ''
for i in range(9):
    cpf = cpf + str(random.randint(0,9)) #coloca valores aleatórios str na variável cpf

for digito in cpf:
    numeros_cpf.append(int(digito)) #transforma os valores da variavel cpf em inteiros e adiciona no vetor

for i in range(9):
    soma_primeiro = soma_primeiro + numeros_cpf[i] * j 
    j = j - 1

resto_soma_cpf = (soma_primeiro * 10) % 11
primeiro_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf 
numeros_cpf.append(primeiro_digito) # Faz a conta do primeiro digito verificador e adiciona no vetor 

j = 11
for i in range(10):
    soma_segundo = soma_segundo + numeros_cpf[i] * j 
    j = j - 1

resto_soma_cpf = (soma_segundo * 10) % 11
segundo_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf # Faz a conta do segundo digito verificador e adiciona no vetor 

cpf_gerado = f'{cpf}-{primeiro_digito}{segundo_digito}'
print(cpf_gerado)