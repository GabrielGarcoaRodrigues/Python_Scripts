import json

pessoa = {
    'nome': 'Prof. Albérto',
    'idade': 43,
    'cursos': ['React', 'Python']
}

with open ('Aulas_Iniciais/pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)


with open('Aulas_Iniciais/pessoa.json', 'r', encoding='utf-8') as arquivo:
    nova_pessoa = json.load(arquivo)

print(nova_pessoa)