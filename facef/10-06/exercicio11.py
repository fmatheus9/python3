import random
num = random.randint(1,10)

print("Tente adivinha o valor sorteado!")

tentativas = 0
x = int(input("Chute um valor: "))
if x == num:
    print("Parabens! Acertou na primeira tentativa.")
else:
    print("Quase!")
    tentativas += 1
    while(x != num):
        x = int(input("Chute um outro valor: "))
        tentativas += 1
        if (num - x == 1 or 2 or -1 or -2) and x != num: 
            print("Esta quente!")
        elif (num - x > 3 or num -x < -3) and x != num:
            print("Esta frio!")
    print(f"Parabens! Acertou em {tentativas} tentativas.")