# Execicio
# Peça ao usuario para digitar seu nome 
# Peça ao usuario para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contem (ou näo) espaços
#         Seu nome tem {n} letras
#         A primenria letra do seu nome é {letra}
#         A ultima letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     Exiba: 'Desculpe, voce nao digitou nada.'

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print('Seu nome nao tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')