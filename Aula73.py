pessoa = {}

pessoa['Nome'] = 'Gabriel'

print(pessoa)

pessoa['Nome'] = 'Paulo'

print(pessoa)

print(pessoa.get('Nome', 'Nao existe'))

print(pessoa.get('Idade', 'Nao existe'))