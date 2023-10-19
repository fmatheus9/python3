#CRUD - create read update delete

print("CRIANDO A LISTA")
lista = [1, 2, 3, 4, 5] #create

print("\nLENDO UM VALOR DA LISTA")
numero = lista[2]
print(numero) #read

print("\nATUALIZANDO A LISTA")
lista[2] = 300 #update 
print(lista)

print("\nDELETANDO UM ÍNDICE DA LISTA")
del lista[1] #delete an iten of the list 
print(lista)

#Métodos uteis: append, insert, pop, del, clear, extend

lista.append(50) #adiciona o valor dentro dos parênteses no final da lista. Tipo o push
print(lista)

lista.pop() #exclui o ultimo item da lista
print(lista)

lista.pop(2) #exclui o item do indice 2 da lista 
print(lista)

lista.insert(0, 10) #adiciona um elemento em determidao indice (prieiro o indice, dps o valor)
print(lista)

lista.clear() #limpa a lista
print(lista)