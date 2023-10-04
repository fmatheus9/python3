a = int(input("Informe o lado A: "))
b = int(input("Informe o lado B: "))
c = int(input("Informe o lado C: "))
if a<b+c or b<a+c or c<a+b:
    if a == b and a == c:
        print("Triângulo Equilátero.")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Os valores informados não conseguem formar um triângulo.")