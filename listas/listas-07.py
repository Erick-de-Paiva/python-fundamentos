# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
totalPessoas = maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if totalPessoas == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    totalPessoas += 1
    cont = str(input('Deseja continuar? [S/N] '))
    while cont not in 'SsNn':
        cont = str(input('Opção inválida! Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print(f'Ao todo você cadastrou {totalPessoas} pessoas')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ',end='')
for i in pessoas:
    if i[1] == maiorPeso:
        print(f'{i[0]}',end=' ')
print()
print(f'O menor peso foi de {menorPeso:.1f}Kg. Peso de ',end='')
for i in pessoas:
    if i[1] == menorPeso:
        print(f'{i[0]}',end=' ')
