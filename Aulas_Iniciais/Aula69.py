

def multiplicar(*args):
    return args[0] * args[1] * args[2]


total = multiplicar(3,5, 2)

print(f'Multiplicaçao: {total}')


def par_impar(x):
    if x % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

numero = input('Digite um numero: ')

print(par_impar(int(numero)))