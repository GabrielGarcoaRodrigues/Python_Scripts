# Faça uma lista de compras com listas
# O usuario deve ter a possibilidade de 
# inserir, apagar e listar valores da sua lista
# nao permita que o programa quebre com 
# erros de indices inexistentes

lista = []

while True:
    opcao = input('Selecione uma opçaõ: \n1 - Inserir item\n2 - Remover item\n3 - Listar itens\n4 - Sair\n')

    if opcao == '1':
        item = input('Digite um produto: ')
        if item in lista:
            print('\nItem já inserido\n')
        else:
            lista.append(item)
            print('\nItem inserido \n')

    elif opcao == '2':
        item = input('\nDigite o item que deseja remover: ') 
        if item in lista:
            lista.remove(item)
            print('\nItem removido \n')
        else:
            print('\nItem não encontrado \n')

    elif opcao == '3':
        if len(lista) == 0:
            print('\nLista vazia\n')
        else:
            print(f'\n{lista}\n')

    elif opcao == '4':
        print('\nFim da lista\n')
        break

    else:
        print('\nOpção inválida\n')


