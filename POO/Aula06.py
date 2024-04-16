# Métodos de classe
# Sao metodos onde o "self" será "cls", ou seja,
#ao onves de receber a instancia no primeiro
#parametro, ele receberá a classe.	

class Pessoa:
    populacao = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.populacao += 1

    def falar(self):
        print(f'A pessoa {self.nome} está falando')

    @classmethod
    def populacaoa(cls):
        return cls.populacao


p1 = Pessoa("Gabriel", 20)
print(Pessoa.populacaoa())