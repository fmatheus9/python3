def maior_numero(x,y):
    if x > y:
        print(f"O maior número é o {x}")
    elif x < y:
        print(f"O maior número é o {y}")
    elif x == y:
        print(f"Os valores são iguais")

x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))
maior_numero(x,y)
