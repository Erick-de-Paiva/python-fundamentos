# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
pessoas = []
totalPessoas = totalIdade = 0
mulheres = []
acimaMedia = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while dados['sexo'] not in 'MF':
        print('ERRO! Digite M ou F')
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    totalPessoas += 1
    totalIdade += dados['idade']
    pessoas.append(dados.copy())
    cont = str(input('Deseja continuar [S/N]? ')).strip()
    while cont not in 'SsNn':
        print('ERRO! Digite S ou N')
        cont = str(input('Deseja continuar [S/N]? ')).strip()
    if cont in 'Nn':
        break
mediaIdade = totalIdade / totalPessoas
for p in pessoas:
    if p['idade'] > mediaIdade:
        acimaMedia.append(p)
print(f'A) Ao todo temos {totalPessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {mediaIdade:.2f} anos.')
print('C) As mulheres cadastradas foram: ',end='')
for i in range(0,len(mulheres)):
    print(mulheres[i],end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for i in acimaMedia:
    print(f'   nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};')
print('<< ENCERRADO >>')
