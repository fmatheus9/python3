#raise - lançando exceções (erros)

#raise ValueError("Deu erro") #interompe o funcionamento do programa com um erro colocado itencionamelte

def verifica_y(y):
    tipoy = type(y)
    if not isinstance(y,(int, float)):
        raise TypeError(f'Valor de y inválido. Y é {tipoy}')
    if y == 0:
        raise ZeroDivisionError('Valor de "y" não pode ser 0')
    return True

def verifica_x(x):
    tipox = type(x)
    if not isinstance(x,(int, float)):
        raise TypeError(f'Valor de x inválido. X é {tipox}')
    return True

def divide(x,y):
    verifica_x(x)
    verifica_y(y)
    return x / y

print(divide(8,0))