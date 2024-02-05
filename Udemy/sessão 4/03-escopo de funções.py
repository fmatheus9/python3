'''
Escopo da função em Python.
Escopo significa o local onde aquele código pode atingir.
Existe escopo local e global.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
O escopo global é o escopo onde todo código pode ser alcançavel.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavre global faz uma variável do escopo externo ser a mesma do interno.  

'''

x = 1 # -> 'x' esta definido no escopo global.

def escopo():
    #x = 1 # -> esta definida dentro do escopo da função. Se eu tentar fazer algo com o 'x' fora da função vai dar probrema.
    print(x)

def funcao():
    y=2

    def outra_funcao():
        print(y)

    outra_funcao()
    print(x)
    

escopo()
funcao()

