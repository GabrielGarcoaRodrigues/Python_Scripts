# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o 
# -6 -5 -4 -3 -2 -1

nome = 'Otávio'

# print(nome[2])
# print(nome[-4])

print('t' in nome)
print('z' in nome)

print('t' not in nome)

encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'Encontrei "{encontrar}" em {nome}')
else:
    print(f'"{encontrar}" não está em {nome}')