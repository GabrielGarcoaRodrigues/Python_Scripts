# args - argumentos nao nomeados
# * - *args (empacotamento e desempacotamento)

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

soma_4_5_6 = soma(4, 5, 6)

print(soma_4_5_6)