def greedy(listaAtivos, opt):
    if opt == 1:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.riscoRetorno) 
    elif opt == 2:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.retorno, reverse=True) 
    elif opt == 3:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.somaDividendos, reverse=True) 
    
    print("Recomendacoes: ")
    for idx,l in enumerate(lstGuloso):
        print(f'{idx+1} - {l.nome}')