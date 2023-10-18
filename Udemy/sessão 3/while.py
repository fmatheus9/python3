numero = int(input("Informe um valor: "))
i = 0 
while i<10:
    i = i+1
    if i == 5: #pula o valor que satisfaz a condição, tudo dentro do laco funciona normal ate chagar no continue, que faz voltar no inicio do laço. 
        print("Não quero mostrar esse valor :p")
        continue
    print(numero*i)

    

