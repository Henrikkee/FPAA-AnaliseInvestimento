def greedy(listaAtivos, opt):
    """
    Retorna uma lista de ativos ordenados a base de um criterio escolhido pelo usuario
    """

    if opt == 1:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.riscoRetorno) 
    elif opt == 2:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.retorno, reverse=True) 
    elif opt == 3:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.somaDividendos, reverse=True) 
    
    return lstGuloso