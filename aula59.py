# Lista de lista e seus indices

salas = [
    ['Maria', 'Joao', 'Gabriel'],     #0
    ['Pedro', 'Jose', 'Ana'],         #1
    ['Carlos', 'Lucas', 'Mariana',]    #2
]

# print(salas[0])

# print(salas[0][0])  

# print(salas[2][2])


for sala in salas:
    print(f'Sala: {salas.index(sala)}')
    for aluno in sala:
        print('-', aluno)