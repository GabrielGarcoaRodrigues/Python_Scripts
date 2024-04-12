#Random tem geradores de numeros pseudoaleatorios


import random
random.seed(10)
#random.randrange(inicio, fim, passo)
# gera um numero inteiro aleatorio dentro de um intervalo especifico
r_range = random.randrange(10, 20, 2)
print(r_range)

#random.randint(inicio, fim)
# gera um numero inteiro aleatorio dentro de um intervalo especifico, sem passo
r_int = random.randint(10, 20)
print(r_int)

#random.uniform(inicio, fim)
# gera um numero flutuante aleatorio dentro de um intervalo especifico
r_uni = random.uniform(10,20)
print(r_uni)

#random.shuffle -> Embaralha uma lista
lista = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista)
print(lista)

#random.choice -> Escolhe um elemento aleatorio de uma lista
escolha = random.choice(lista)
print(escolha)

#ramdom.choices -> Escolhe varios elementos aleatorios de uma lista
escolha = random.choices(lista, k=3)
print(escolha)

#random.sample -> Escolhe varios elementos aleatorios de uma lista, sem repeticao
escolha = random.sample(lista, 3)
print(escolha)