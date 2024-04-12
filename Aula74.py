# Metodos uteis para dicionarios
# len - quantas chaves
# keys - iteravel com as chaves
# values - iter
# items - iter com chave e valor
# setdefault - se a chave nao existir, cria
# copy - copia o dicionario
# get - obtem a chave
# pop - remove a chave
# popitem - remove o ultimo item
# update - atualiza o dicionario
# clear - limpa o dicionario


pessoa = {
    'Nome' : 'Gabriel',
    'Idade' : 20, 
    'Sexo' : 'Masculino'
}

print(len(pessoa))

print(pessoa.keys())

print(pessoa.values())

print(pessoa.items())

print(pessoa.setdefault('Cidade', 'São Paulo'))

opa = pessoa.copy()
print(opa)

print(pessoa.get('Nome'))

print(pessoa.pop('Sexo'))

print(pessoa.popitem())

pessoa.update({'Nome' : 'Gabriel', 'Idade' : 20, 'Sexo' : 'Masculino'})
