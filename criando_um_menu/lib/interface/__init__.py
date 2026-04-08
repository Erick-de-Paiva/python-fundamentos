def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
