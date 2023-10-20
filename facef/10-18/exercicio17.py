list1 = []
list2 = []
soma1 = 0
soma2 = 0
for i in range(50):
    list1.append(int(input("Informe um valor: ")))
    soma1 = soma1 + list1[i]

for i in range(50):
    list2.append(int(input("Informe um valor: ")))
    soma2 = soma2 + list2[i]

print(f"Valor da soma do primeiro vetor: {soma1}.\nValor da soma do segundo vetor: {soma2}.\nValor da soma dos dois vetores: {soma2+soma1}")