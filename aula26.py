# Formataçao básica de strings
# s - string
# d - int
# f - float
# .<numero de casas decimais>f
# x e X - hexadecimal(ABCDEF0123456789)
# (Caractere) (<>^)(quantidade)
# > - esquerda
# < - direita
# ^ - Centro
# = Força o numero a aparecer depois do 0
# Sinal - + ou -
# Ex.: 0>-100, .1f
# Conversion Flags - !r !s !a


variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.23423523:+,.2f}')
print(f'O hexadecimal de 1500 é: {1500:04x}')