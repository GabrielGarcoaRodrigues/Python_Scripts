import os

path = os.path.abspath('Aulas_Iniciais')
# o 'w' apaga tudo que tiver no arquivo e escreve o que foi passado
# o 'a' adiciona o que foi passado ao final do arquivo

caminho_arquivo = path  + "/" + 'aula116.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # passando o caminho absoluto
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é o meu arquivo de texto.\n')
    arquivo.writelines(['Linha 1\n', 'Linha 2\n', 'Linha 3\n'])


with open('Aulas_Iniciais/aula116.txt', 'r', encoding='utf-8') as arquivo: # passando o caminho relativo
    print(arquivo.read())


# os.remove(caminho_arquivo) apaga o arquivo
# os.rename(caminho_arquivo, path + "/" + 'aula116_renomeado.txt')  renomeia o arquivo