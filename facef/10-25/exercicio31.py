'''
Fazer uma função que calcule o fatorial
de um número.

'''
def fatorial(f):
    fa = 1
    for i in range(f):
        fa = fa * (i+1)
    return fa

f = int(input("\nInforme o valor: "))
fa = fatorial(f)
print(f"O fatorial de {f} = {fa}\n")