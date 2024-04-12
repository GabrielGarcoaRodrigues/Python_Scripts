# Repetiçoes
# while (enquanto)
# Executa uma açao enquanto uma condiçao for verdadeira 
# loop infinito -> Quando um codigo nao tem fim

contador = 0

while contador < 100:
    contador += 1

    if contador >= 10 and contador <= 19:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('acabou')