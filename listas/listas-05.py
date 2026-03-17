# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaPares = []
listaImpares = []
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista.append(n)
        listaPares.append(n)
    else:
        lista.append(n)
        listaImpares.append(n)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont != 'S' and cont != 'N':
        cont = str(input('Opção inválida! Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('A lista completa é: ',end='')
for i in lista:
    print(i,end=' ')
print()
print('A lista de pares é: ',end='')
for i in listaPares:
    print(i,end=' ')
print()
print('A lista de ímpares é: ',end='')
for i in listaImpares:
    print(i,end=' ')
