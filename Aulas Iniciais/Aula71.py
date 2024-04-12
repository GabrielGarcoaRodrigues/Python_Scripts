'''
Closure e funcoes que retornam outras funcoes
'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

saudacao_1 = criar_saudacao('Bom dia', 'Gabriel')
saudacao_2 = criar_saudacao('Boa noite', 'Gabriel')

print(saudacao_1())
print(saudacao_2())