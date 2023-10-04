sexo = input("Informe o sexo (masculino ou feminino): ")
h = float(input("Informe a altura: "))

if sexo == 'masculino':
    ideal = (72.7 * h) - 58
else:
    ideal =  (62.1 * h) - 44.7

print(f"Peso ideal: {ideal:.1f}")
