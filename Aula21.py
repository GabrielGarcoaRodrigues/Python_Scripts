# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar ou [S]air: ')
senha = input('Digite sua senha: ')

senha_permeitida = '1234'

if entrada == 'E' and senha == senha_permeitida:
    print('Entrar')
else:
    print('Sair')


print(True and True and False)
print(True and 0 and True)