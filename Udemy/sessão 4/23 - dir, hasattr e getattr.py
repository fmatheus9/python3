string = 'String'
print(dir(string)) #quais métodos estão disponiveis dentro da string
print(string)

if hasattr(string, 'upper'): #verifica se o objeto tem esse método
    print('Existe o método upper')
    print(string.upper())

metodo = 'upper'
print(getattr(string,metodo))

if hasattr(string, metodo): #verifica se o objeto tem esse método
    print('Existe o método upper')
    print(string.upper())