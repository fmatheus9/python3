nome = input("Informe o nome: ")
altura = float(input("Informe a altura em metros: "))
peso = int(input("Informe o peso: "))

imc = peso / (altura*altura)

print(f"Nome: {nome}\nAltura: {altura}\nPeso: {peso}\nIMC: {imc:.1f}")