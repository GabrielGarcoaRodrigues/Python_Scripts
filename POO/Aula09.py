# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo


class Caneta:
    def __init__(self,cor):
        #private protected
        self._cor = cor

    @property
    def cor(self):
        print('property')
        return self._cor

    @cor.setter
    def cor(self,cor):
        print('setter')
        self._cor = cor


caneta = Caneta('Vermelha')
caneta.cor = 'Rosa'

# -> getter
print(caneta.cor)
