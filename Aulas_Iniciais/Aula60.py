# Desempacotamento em chamadas
# de metodos e funçoes

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Joao', 'Gabriel'],     #0
    ['Pedro', 'Jose', 'Ana'],         #1
    ['Carlos', 'Lucas', 'Mariana',]    #2
]
# a, b, c = lista
# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

print(*lista)
print(*tupla)
print(*string)

print(*salas, sep='\n')