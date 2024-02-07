def executa_funcao(funcao, *args):
    return(funcao(*args))

def soma(x,y):
    return x + y
  

#print(executa_funcao(lambda x, y: x + y, 2,3))
print(
    executa_funcao(
        lambda x, y: x + y, 2,3 #funcao anonima lambda --> o lambda vai para o parâmetro 'funcao' 
    )
)
lista = [1,2,3,4,5,6,7,8,9,10]
print(
    executa_funcao(
        lambda lista: sum(lista),lista #lambda -> parametro 'lista': resultado = expressão soma(lista),  argumento?
    )
)