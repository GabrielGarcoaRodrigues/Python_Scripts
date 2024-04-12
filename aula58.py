# split e join com list e str
# split - divide uma string
# join - une uma string

frase = "O rato, roeu a roupa"
lista_palavras = frase.split(',')

for i, frase in enumerate(lista_palavras):
    print(i, '-', frase.strip())


frase_unida = '-'.join(frase)
print(frase_unida)