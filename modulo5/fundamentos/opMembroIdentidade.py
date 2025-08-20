# operadores membros e identidade
# operadores membro

lista = [1, 2, 3, 'pedro', 'maira']

print('membros')
print(2 in lista)#printa se o numero 2 está na lista
print('pedro' not in lista)#printa se o nome pedro não está na lista

print('')


#identidade
x = 3
y = x
z = 3

print('identidade')
print(x is y)# true, porq eles tem o msm valor
print(y is z)# true, porq eles tbm tem o msm valor
print(x is not z)# false, porq eles tem o msm valor

print('')
# outro ex

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print('outro ex')
print(lista_a is lista_b)  # True, lista_b é a mesma lista que lista_a
print(lista_a is lista_c)  # False, pq lista-c é uma nova lista só que com os msm valores
