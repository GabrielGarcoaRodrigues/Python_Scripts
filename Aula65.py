# Valores padrao para parametros
# Ao definir uma funcao, os parametros podem ter
# valores padrao, caso o valor nao seja enviado
# para o parametro, o valor padrao sera usado

def soma(x, y, z=0):
    print(f'{x=} {y=} {z=}')

soma(100, 200)
soma(100, 200, 300)