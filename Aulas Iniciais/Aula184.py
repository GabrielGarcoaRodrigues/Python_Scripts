import locale
import string
from datetime import datetime
from pathlib import Path

caminho_arquivo = Path(__file__).parent / 'Aula184.txt'

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def converte_moeda(valor):
    brl = locale.currency(valor, grouping=True, symbol=True)
    return brl

data = datetime(2022, 12, 23)
dados = dict(
    nome = 'Gabriel',
    valor = converte_moeda(1230.50),
    data = data.strftime('%d/%m/%Y'),
    empresa = 'Google',
    telefone = '11999999999'
)


# texto = '''
# Prezado $nome,

# Informamos que sua mensalidade será cobrada no valor de $valor no dia $data.
# Tel: $telefone
# Atenciosamente,

# $empresa
# '''	
with open(caminho_arquivo, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    # print(template.safe_substitute(dados)) caso nao tenho um dos dados no dict
    print(template.substitute(dados))

