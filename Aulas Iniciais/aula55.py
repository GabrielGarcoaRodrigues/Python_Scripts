# enumerate - enumera iteraveis (indices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')    

# lista_enumerada = list(enumerate(lista))

for indice, nome in enumerate(lista):
    # indice, nome = item
    print(indice, nome)

    
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)