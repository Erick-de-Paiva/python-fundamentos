# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}
nome = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
ctps = int(input('Carteira de trabalho (0 não tem): '))
if ctps != 0:
    anoContratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    aposentadoria = idade + (anoContratacao + 35) - date.today().year
    dados = {'nome':nome,
             'idade':idade,
             'ctps':ctps,
             'contratação':anoContratacao,
             'salário':salario,
             'aposentadoria':aposentadoria}
else:
    dados = {'nome': nome,
             'idade': idade,
             'ctps': ctps}
print()
for i, j in dados.items():
    print(f'  - {i} : {j}.')
