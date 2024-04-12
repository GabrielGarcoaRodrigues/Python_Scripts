# Exercicio - sistema de perguntas e respostas

temas = ['História', 'Matemática', 'Geografia']

perguntas = [
    {
        'Pergunta' : 'Quem descobriu o Brasil?',
        'Opções' : ['Papa Francisco', 'Pedro Alvares Cabral', 'Toguro', 'Neymar'],
        'Resposta' : 'Pedro Alvares Cabral'
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['10', '15', '20', '25'],
        'Resposta' : '25'
    },
    {
        'Pergunta' : 'Qual é a capital do Brasil?',
        'Opções' : ['Curitiba', 'Laranjeiras do Sul', 'Brasília', 'RJ 40 graus'],
        'Resposta' : 'Brasília'
    },
]

print('Bem vindo ao sistema de perguntas e respostas!\n')
count = 0

print('Escolha o tema da pergunta: ')
for tema in temas:
    print(f'{count}) {tema}')
    count += 1


tema = int(input('\nTema: '))

count = 0

print(f'\nPergunta: {perguntas[tema]["Pergunta"]}')
print('')

print('Opções: ')
for opcoes in perguntas[tema]['Opções']:
    print(f'{count}) {opcoes}')
    count += 1

resposta = input('Sua resposta: ')

if perguntas[tema]['Opções'][int(resposta)] == perguntas[tema]['Resposta']:
    print('\nVOCÊ ACERTOU!')
else:
    print('\nVOCÊ ERROU!')
    
