sair = 'Nao'
while sair != 's':

    primeiro_numero = float(input('Digite um numero: '))
    segundo_numero = float(input('Digite outro numero: '))
    operador = input('Digite um operador: ')

    if operador == '+':
        print(f'A soma é: {primeiro_numero + segundo_numero}')
    elif operador == '-':
        print(f'A subtraçao é: {primeiro_numero - segundo_numero}')
    elif operador == '*':
        print(f'A multiplicaçao é: {primeiro_numero * segundo_numero}')
    elif operador == '/':
        print(f'A divisao é: {primeiro_numero / segundo_numero}')
    else:
        print('Operador invalido!')

    print('')
    sair = input('Quer sair ? [s]im: ').lower()
    
