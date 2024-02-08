#(Parte 1) try e except para tratar exceções:
#erros nao devem passar despercebidos a nao ser que sejam explicitamente silenciados 

try:
    a = 10
    b = 0
    print("Linha 1")
    c = a / b #silenciar o erro 
    print("Linha 2") #não mostra essa linha pois houve um erro na linha anterior
except ZeroDivisionError: #é importante colocar o nome do erro na exceção
    print("Dividiu por 0")
finally:
    #sempre é executado 
    print("Finalizado")
print('Continuar')