'''
10. Fazer uma função que verifica se uma
palavra, frase ou número é um
palíndromo.
Um palíndromo é qualquer sequência de
caracteres que seja a mesma se lida da
esquerda para a direita ou da direita
para a esquerda. Por exemplo, a palavra
“osso” é um palíndromo, pois é idêntica
não importa o sentido da leitura.

'''

def palindromo(palavra): 
    palavra_invertida = palavra[-1::-1]
    if palavra_invertida == palavra:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
palavra = str(input("Digite uma palavra: "))
palindromo(palavra)