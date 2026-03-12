# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:
    novoValor = int(input('Digite um valor: '))
    if novoValor not in valores:
        valores.append(novoValor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        print('Opção inválida, digite novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
valores.sort()
print(f'Você digitou os valores: ',end='')
for i in range(0,len(valores)):
    print(f'{valores[i]}',end=' ')
