# Aprimore o desafio anterior para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []
partidas = []
totalGols = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador['nome']} jogou? '))
    partidas.clear()
    for i in range(0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    cont = str(input('Quer continuar [S/N]? ')).strip()
    while cont not in 'SsNn':
        print('ERRO! Digite novamente.')
        cont = str(input('Quer continuar [S/N]? ')).strip()
    if cont in 'Nn':
        break
print()
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for i, j in enumerate(time):
    print(f'{i:>3} ',end='')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('Volte sempre!')
