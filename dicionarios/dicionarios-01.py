# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: ')).capitalize()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
while aluno['media'] > 10 or aluno['media'] < 0:
    print('Média inválida!')
    aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
for i, j in aluno.items():
    print(f'  - {i} : {j}')
