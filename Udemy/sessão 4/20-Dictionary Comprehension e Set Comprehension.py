produto = { 
    'nome': 'Caneta',
    'preço': 2.50,
    'categoria': 'Escritório'
}

dc = {
    chave: valor
    for chave,valor in produto.items()
}

print(dc)