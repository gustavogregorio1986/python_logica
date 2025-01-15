dados = {
    'nome':'Mariana',
    'idade':27,
    'estado':'Minas Gerais',
    'Cidade':'Belo Horizonte'
}

print(dados)

dados_numericos = {
    1:'numero um',
    2:'numero dois',
    3:'numero três'
}

print(type(dados))

print(dados.keys())

print(type(dados.keys()))

print(dados.values())

print(dados.items())

print(dados)

print(dados['nome'])

print(dados['estado'])

print(dados['idade'])

dados['nacionalidade'] = 'brasileira'

print(dados)

print(dados_numericos[3])

dados_numericos[4] = 'numero 4'

print(dados_numericos)

dados['idade'] = 33

print(dados)

dados['cidade'] = 'Juiz de Fora'

print(dados)

dados.pop('nacionalidade')

print(dados)

dados.popitem()

print(dados)

del dados['idade'] 

print(dados)

dados.clear()

print(dados)

dados = {
    'nome':'Vinicius',
    'status': True,
    'notas': [10, 9.8, 7.7, 4.9] 
}

print(dados)

print(dados['nome'])

print(dados['notas'])

print(dados['notas'][0])

print(dados['notas'][-1])

print(dados['notas'][1])

