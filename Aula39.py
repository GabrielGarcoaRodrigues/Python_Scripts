# Iterando strings com while

nome = 'Gabriel Garçoa'
tamanho_nome = len(nome)
contador = 0 
nova_string = ''

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'    
    contador += 1

print(nova_string)