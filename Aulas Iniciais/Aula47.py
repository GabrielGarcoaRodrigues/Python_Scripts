# Desafio jogo da palavra secreta

# Faça um jogo para o usuario adivinhar qual a palavra secreta.
# Voce vai propr uma palavra secreta
# qualquer e vai dar a possibilidade do usuario tentar adivinha-la.
# Quando o usuario digitar uma letra, voce vai conferir se a letra digitada  esta na palavra secreta.

# se a letra digitada estiver na palavra, exiba a letra;
# se a letra digitada nao estiver na palavra, exiba *

# Faça a contagem de tentativas do seu usuario.


palavra_secreta = 'banana'
tamanho_palavra = len(palavra_secreta)
palavra = '_' * tamanho_palavra
tentativas = 0   

print('******** BEM VINDO AO JOGO DA PALAVRA SECRETA ******** ')
print('Vamos começar...')
print(palavra)

while '_' in palavra:
    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1 or letra.isnumeric() or letra == ' ' or letra == '':
        letra = input('Digite apenas uma letra: ').lower()
        tentativas += 1
        continue

    elif letra in palavra:
        print('A letra já foi digitada')
        tentativas += 1
        continue

    else:
        if letra in palavra_secreta:
            for i in range(tamanho_palavra):
                if letra == palavra_secreta[i]:
                    palavra = palavra[:i] + letra + palavra[i+1:]
        tentativas += 1
        print(palavra)

print('   ')
print(f'Parabéns, você acertou a palavra secreta: {palavra_secreta.capitalize()} em {tentativas} tentativas')