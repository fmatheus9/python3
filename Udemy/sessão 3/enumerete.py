lista = [1,2,3,4,5,6,7]
lista.append('AAAA')
for i in enumerate(lista):
    print(i)

for i, valor in enumerate(lista, start=10):
     print(i, valor)

cpf = '47094420889'
for i, valor in enumerate(cpf):
     print(valor)