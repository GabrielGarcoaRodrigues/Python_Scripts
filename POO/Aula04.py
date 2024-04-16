#Atributo de classe

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Gabriel', 22)
p2 = Pessoa('Larissa', 35)

print(p1.__dict__)
print(p2.__dict__)

print()

print(vars(p1))
print(vars(p2))