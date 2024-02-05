"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args): #passa como parametros uma quantidade ilimitada de argumentos não nomeados. Empacota dentro de uma tupla
    total = 0
    for numero in args:
        total += numero
    return total
def soma2(num):
    total = 0
    for numero in num:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) #desempacota uma tupla para enviar como parâmetros para a funçao
print(outra_soma)

print(sum(numeros)) # função pronta que realiza a soma dos numeros passados 

num = [1,2,3,4,5,6,7,8,9,10]
soma1 = soma2(num)
print(soma1)
print(sum(num))
