'''
Argumentos nomeados e não nomeados em funçoes Python
Argumento nomeado tem nome com sinal de igual.
Argumento não nomeado recebe apenas o valor.

'''
def soma(x, y):
    print(f'{x=} {y=} | x + y = {x+y}')


soma(1, 2) # ---> Argumentos 1 e 2
soma(x = 2, y = 1)

