# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont != 'S' and cont != 'N':
        cont = str(input('Opção inválida! Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: ',end='')
for i in range(0,len(lista)):
    print(f'{lista[i]}',end=' ')
print()
cincoLista = ''
for i, j in enumerate(lista):
    if j == 5:
        cincoLista = 'S'
    else:
        cincoLista = 'N'
if cincoLista == 'S':
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
