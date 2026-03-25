# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(n, sit=False):
    """
    -> Situação para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total de notas'] = len(n)
    r['maior nota'] = max(n)
    r['menor nota'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


n = []
qntNotas = int(input('Quantas notas serão digitada? '))
for i in range(0, qntNotas):
    teste = float(input(f'Nota {i+1}: '))
    while teste < 0 or teste > 10:
        print('Nota inválida!')
        teste = float(input(f'Nota {i + 1}: '))
    n.append(teste)
opcao = str(input('Deseja ver a situação final [S/N]? ')).upper().strip()
while opcao != 'S' and opcao != 'N':
    print('ERRO! Opção inválida!')
    opcao = str(input('Deseja ver a situação final [S/N]? ')).upper().strip()
if opcao == 'S':
    situacao = True
else:
    situacao = False
if len(n) == 0:
    print('Nenhuma nota informada.')
else:
    print(notas(n, situacao))
