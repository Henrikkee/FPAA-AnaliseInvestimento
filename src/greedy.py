def greedy(listaAtivos):
    #Criterio Guloso - Selecionar o item que possui retorno
    print("Escolha o criterio:\n1-Menor Risco\n2-Maior Retorno\n3-Maior valor em dividendos")
    opt = int(input("Opcao: "))
    if opt == 1:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.riscoRetorno) 
    elif opt == 2:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.retorno, reverse=True) 
    elif opt == 3:
        lstGuloso = sorted(listaAtivos, key=lambda d: d.somaDividendos, reverse=True) 
    
    print("Recomendacoes: ")
    for idx,l in enumerate(lstGuloso):
        print(f'{idx+1} - {l.nome}')