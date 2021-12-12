import itertools

def bruteForce(listaAtivos, numAtivos):
    """
    Procura o melhor investimento baseado no risco retorno de cada ativo utilizando um algoritimo de forca bruta
    """
    lstMenorValor = [{"pativos": None, "val": 100}] * len(listaAtivos) # Salvar os items com menos valor de Risco Portifolio

    for porcentagemDivida in itertools.product(range(0,101), repeat=len(listaAtivos)) : 
        if sum(porcentagemDivida) == 100:
            value = 0
            somaValue = 0
            cnt = 0
            for idx, pd in enumerate(porcentagemDivida):
                value = listaAtivos[idx].riscoRetorno *  (pd/100) # Risco Retorno * Peso
                cnt += 1 if value > 0 else 0
                somaValue += value
            if(somaValue > 0):
                riscoPortifolio = somaValue/cnt
                if lstMenorValor[-1]['val'] > riscoPortifolio:
                    lstMenorValor.pop()
                    lstMenorValor.append({"pativos": porcentagemDivida, "val": riscoPortifolio})
                    lstMenorValor = sorted(lstMenorValor, key=lambda d: d['val']) 

    print("Lista de Sugestoes: ")
    for idx, lmv in enumerate(lstMenorValor):
        print(f'{idx+1} -  ', end='')
        for idx2, porcentagem in enumerate(lmv['pativos']):

            numAt = round((porcentagem/100) * numAtivos)

            print(f'{numAt} em {listaAtivos[idx2].nome.upper()} ', end='')
        print('')

    print("Obs: A quantidade de ativos recomendada é adaptada ao numero de ativos requisitados vezes o risco retorno de cada ativo")