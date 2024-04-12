# Argumentos nomeados e nao nomeados em funcoes python
# argumento nomeado tem nome com sinal de igual
# argumento nao nomeado recebe apenas o argumento(valor)

def soma(x, y):
    print(f'{x} + {y} = {x+y}')    


soma(2, 3)
soma(y=2, x=3)
soma(3, y=2)    