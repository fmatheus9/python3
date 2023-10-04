#for e while
for numero in range(0,10,1): #inicio, final e incremento. Começa no 0, vai ate o 9 de um em um.
    print(numero)

print("================")
for numero in range(10,0,-2):
    print(numero)

print("================")
for numero in range(10): #usando o conceito default
    print(numero)

print("================")
nomes = ['pedro' , 'ana' , 'maria', 'aaa']
for n in nomes:
    print(nomes)

print("================")
list=[1,2,3,4,7,8]
for num in list:
    if num < 6:
        print(num)

print("================")
i=0
while(i<10):
    print(i)
    i=i+1


print("================")
j=0
x=2
while(j<=5):
    print(x)
    j += 1
else:
    print('O valor da variavel j é %d' %j)