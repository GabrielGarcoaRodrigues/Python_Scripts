# Introdução ao try/except
# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

numero = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero)
    print(f'STR: {numero}')
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero} é {numero_float * 2}')

except:
    print('Isso não é um número')