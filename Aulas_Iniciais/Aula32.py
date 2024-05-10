# Faça um programa que peça ao usuario para digitar um numero inteiro,
# informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro,
# informe que não é um numero inteiro.
numero = input("Digite um numero inteiro: ")
numero_inteiro = None

if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
else:
    print("Isso não é um numero inteiro")

# Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudaçao apropriada. EX.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
hora = input('Digite a hora: ')
hora_int = None

if hora.isdigit():
    hora_int = int(hora)

    if hora_int <= 11:
        print('Bom dia')
    elif hora_int <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
else:
    print('Digite um horario entre 0 e 23')


# Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos
# escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 escreva "Seu nome é grande".
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4: 
    print('Seu nome é curto!')

elif tamanho_nome <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')