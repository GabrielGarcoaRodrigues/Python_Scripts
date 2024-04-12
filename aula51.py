# Cuidados com dados mutaveis
# = - copiado o valor (imutaveis)
# = - aposta para o mesmo valor na memoria (mutaveis)

# nome = 'Gabriel'
# nome_novo = nome
# nome = 'zé'

# print(nome)
# print(nome_novo)

lista_a = ['gabriel', 'luiz']
lista_b = lista_a
# lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_b)