# Iteraçao -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o proximo valor
# iter -> me entregue seu iterador

# texto = iter('Gabriel')
# print(next(texto))

texto = 'Gabriel'
iterador = iter(texto) 

while True:
    try:
        print(next(iterador))   
    except StopIteration:
        print('Fim da string')
        break