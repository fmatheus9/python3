import random
numeros_cpf = []
soma_primeiro = 0
soma_segundo = 0
j = 10

print("GERADOR DE CPF")
cpf = ''
for i in range(9):
    cpf = cpf + str(random.randint(0,9))

for digito in cpf:
    numeros_cpf.append(int(digito))

for i in range(9):
    soma_primeiro = soma_primeiro + numeros_cpf[i] * j 
    j = j - 1

resto_soma_cpf = (soma_primeiro * 10) % 11
primeiro_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf 
numeros_cpf.append(primeiro_digito)

j = 11
for i in range(10):
    soma_segundo = soma_segundo + numeros_cpf[i] * j 
    j = j - 1

resto_soma_cpf = (soma_segundo * 10) % 11
segundo_digito = 0 if resto_soma_cpf > 9 else resto_soma_cpf 

cpf_gerado = f'{cpf}{primeiro_digito}{segundo_digito}'
print(cpf_gerado)