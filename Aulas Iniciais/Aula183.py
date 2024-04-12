import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def converte_moeda(valor):
    brl = locale.currency(valor, grouping=True, symbol=True)
    return brl


saldo = 1256
print(converte_moeda(saldo))