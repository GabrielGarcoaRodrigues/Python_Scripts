# Dicionarios em python (dict)
# chave e valor
# indice
# usamos as chaves - {}

pessoa = {
    'Nome' : 'Gabriel',
    'Idade' : 20, 
    'Sexo' : 'Masculino'
}


# print(pessoa)
print(pessoa['Nome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])