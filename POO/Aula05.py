# Exercicio - Salve a classe em JSON
import json
caminho = 'POO/Aula05.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f'A pessoa {self.nome} está falando')


p1 = Pessoa('Gabriel', 22)
p2 = Pessoa('Larissa', 35)

bd = [vars(p1), vars(p2)]

with open(caminho, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)