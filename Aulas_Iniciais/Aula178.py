# Arquivo CSV
import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'aula178.csv'

with open (caminho_csv, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)

# with open (caminho_csv, 'r') as arquivo:
#     leitor = csv.DictReader(arquivo)

#     for linha in leitor:
#         print(linha['Ativo Codigo'])