#DADOS MUTAVEIS 
listaA = ['matheus', 'lucas']
listaB = listaA

listaA[0] = 'Pepino'
print(listaB) 

listaA = ['matheus', 'lucas']
listaB = listaA.copy()

listaA[0] = 'Pepino'
print(listaB) 

listaC = [1,2,3,4,5,6,7,'matheus']
for i in range(len(listaC)):
    print(listaC[i])