# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula a fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    res = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        res *= i
    return res


numero = int(input('Digite um número para calcular seu fatorial: '))
opcao = str(input('Deseja ver o processo do cálculo [S/N]? ')).upper().strip()
while opcao != 'S' and opcao != 'N':
    print('ERRO! Opção inválida!')
    f = str(input('Deseja ver o processo do cálculo [S/N]? ')).upper().strip()
if opcao == 'S':
    show = True
else:
    show = False
print(fatorial(numero, show))
