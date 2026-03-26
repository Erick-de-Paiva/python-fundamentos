from modularizacao.utilidades import moeda
from modularizacao.utilidades import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
taxaAumento = dado.leiaInt('Digite uma taxa de aumento [%]: ')
taxaReducao = dado.leiaInt('Digite uma taxa de redução [%]: ')
moeda.resumo(preco, taxaAumento, taxaReducao)
