# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.


# string = 'Gabriel'  # str
# print(string.upper())

# print(isinstance(string, int))
# print(isinstance(string, str))

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def dirigir(self):
        return f'O {self.modelo} está dirigindo'

    def buzinar(self):
        print(f'O {self.modelo} está buzinando')

    def __str__(self):
        return f'{self.modelo} {self.ano} {self.cor}'

    def acelerar(self):
        return f'O {self.modelo} está acelerando'
   

golf = Carro("Golf GTI", 2019, "Branco")

golf.buzinar()
print(golf.acelerar())
print(golf.modelo)
print(golf.__str__())
Carro.buzinar(golf)