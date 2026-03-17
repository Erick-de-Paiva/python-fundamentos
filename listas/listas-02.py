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
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while cont != 'N' and cont != 'S':
        print('Opção inválida, digite novamente.')
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
valores.sort()
print(f'Você digitou os valores: ',end='')
for i in range(0,len(valores)):
    print(f'{valores[i]}',end=' ')
