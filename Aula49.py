# Listas em python 
# Tipo list - Mútavel
# Suporta varios valores de qualquer tipo
# conhecimentos reutilizáveis - indices e fatiamento
# # metodos uteis: append, insert, pop, remove, clear, extend e +
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)

lista = [10, 20, 30, 40]
lista[2] = 300
print(lista)

del lista[2]      # remove o elemento

print(lista) 
print(lista[2])

lista.append(50)  # adiciona
lista.pop()       # remove o ultimo elemento
lista.append(60)
lista.append(70)
lista.pop(4)
lista.insert(2, 555) # insere na posição 2 o valor 555
# lista.clear()     # limpa a lista   
print(lista)