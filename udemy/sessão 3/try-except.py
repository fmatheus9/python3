#try - tentou executar o código
#exept - ocorreu algum erro ao tentar executar

numero = input("vou dobrar o numero que voce digitar: ")

#tenta executar o código
try: 
    print(f"Sting {numero}")
    numero_float = float(numero)
    print(f"Float: {numero_float}")
    print(f"Dobro de {numero_float} é {numero_float*2:.1f}")
#caso ocorra um erro dentro do try pula pro exept
except:
    print("Isso não é um número")