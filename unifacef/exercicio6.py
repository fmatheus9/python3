combustivel = input("A-álcool, G-gasolina: ").upper()
litros = int(input("Informe a quantidade de litros: "))

if combustivel == 'A':
    if litros <= 20:
        preco = (litros*2.10) 
        desconto = preco * 0.3
        print(f"Total a pagar: {preco-desconto}")
    else:
        preco = (litros*2.10) 
        print(f"Total a pagar: {preco-(preco*0.5)}")
else:
    if litros <=20:
        preco = (litros*3.30) 
        print(f"Total a pagar: {preco-(preco*0.4)}")
    else:
        preco = (litros*3.30) 
        print(f"Total a pagar: {preco-(preco*0.6)}")