# CPF: 74682489070
# Colete a soma dos 9 primeiros digitos do CPF
# Multiplicando cada um dos valores por uma contagem regressiva comecando de 10

# ex: 74682489070 (746824890)
#     10 9  8  7  6  5  4  3  2
# *   7  4  6  8  2  4  8  9  0
# =   70 36 48 56 12 20 32 27 0

# Somar = 70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
# Multiplicar o resultado anterior por 10
# 221 * 10 = 2210
# obter o resto da divisao da conta anterior por 11
# 2210 % 11 = 0
# se o resultado anterior for maior que 9:
#     resultado é 0
# contrario disso:
#     resultado é o valor da conta

# o primeiro digito do cpf é 0


cpf = input('Digite o CPF:')
novo_cpf = cpf[:9]
contador = 10
soma = 0

for numero in novo_cpf:
    soma += (int(numero) * contador)
    contador -= 1  

digito = (soma * 10) % 11

digito = digito if digito <=9 else 0

print(f'O primeiro digito do CPF é: {digito}')   