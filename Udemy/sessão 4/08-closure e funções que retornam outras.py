
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_ola = criar_saudacao('Olá',)
falar_boanoite = criar_saudacao('Boa noite')

nomes = ['Matheus', 'Felipe', 'Lucas', 'Pedro']
for nome in nomes:
    print(falar_ola(nome))