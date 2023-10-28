'''
11. A jornada de trabalho semanal de um
funcionário é de 40 horas. O funcionário
que trabalhar mais de 40 horas receberá
hora extra, cujo cálculo é o valor da
hora regular com um acréscimo de 50%.
Escreva uma função que receba o
número de horas trabalhadas em uma
semana e o salário por hora, e retorne o
salário do funcionário.
'''
def funcao(horas_semana, salário_hora): 
    if horas_semana <= 40:
        resultado = salário_hora * horas_semana
        return resultado
    elif horas_semana > 40:
        resultado = (salário_hora+salário_hora*0.5) * (horas_semana - 40)
        resultado = resultado + salário_hora * 40
        return resultado

horas_semana = int(input("Informe a quantidade de horas trabalhadas: "))
salário_hora = float(input("Informe o valor do salário/hora: "))
valor = funcao(horas_semana, salário_hora)
print(f"Salário: R${valor}")