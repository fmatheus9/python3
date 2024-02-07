# isinstace() - para saber se objeto é de determinado tipo
lista = ['a', 1, 1.2, True, [1,2,3], (2,3), {0,2}, {'nome': 'Matheus'}]
print(lista)
for item in lista:
    if isinstance(item, set):
        item.add(4)
        print(item, isinstance(item, set))
    if isinstance(item, str):
        item.upper()
        print(item.upper(), isinstance(item, str))
    if isinstance(item, (int, float)):
        print(item * 2)