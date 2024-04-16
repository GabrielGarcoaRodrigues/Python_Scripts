#Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return

        print(f'{self.nome} parou de filmar')
        self.filmando = False



camera1 = Camera("Sony Xperia")

print(camera1.nome)

print(camera1.filmando)

camera1.filmar()
camera1.filmar()

# print(camera1.filmando)

camera1.parar_filmar()
camera1.parar_filmar()

# print(camera1.filmando)