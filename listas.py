lista = [ 'Vinicius','Gabriel','Lucas1' ]

print(type(lista))

lista = [10, True, 'Vinicius',123.45, 'Python']

print(lista)

print(type(lista))

lista2 = [ 10, 'B=Vinicius',[1,2,3] ]

print(lista2)

print(type(lista2))

print(lista)

print(lista[0])

print(lista[2])

print(lista[4])

print(lista[-1])

print(lista[-2])

print(lista2)

print(lista2[2][1])

print(lista2[2][2])

print(lista)

print(lista[0:3])

print(lista[1])

print(10 in lista)

print(20 in lista)

print('Vinicius' not in lista)

lista.append('Formação Expert Python')

print(lista)

lista.insert(1,'maça')

print(lista)

lista.pop()

print(lista)

lista.remove(True)

print(lista)

lista.remove('maça')

print(lista)

del lista[2] 

print(lista)

lista[0] = 'Computador'

print(lista)

lista[2] = 'Pandas'

print(lista)