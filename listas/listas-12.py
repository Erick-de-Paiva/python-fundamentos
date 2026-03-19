# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

alunos = []
totalAlunos = []
while True:
    nome = (input('Nome: '))
    nota1 = float(input('Nota 1: '))
    while nota1 > 10 or nota1 < 0:
        print('Nota inválida!')
        nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    while nota2 > 10 or nota2 < 0:
        print('Nota inválida!')
        nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont = input('Quer continuar? [S/N] ').strip().upper()
    if cont == 'N':
        break
print(f'{"No.":<4}{"ALUNO":<10}{"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(alunos) -1:
        print(f'Notas de {alunos[opc][0]} são: ',end='')
        for i in alunos[opc][1]:
            print(i,end=' ')
        print()
