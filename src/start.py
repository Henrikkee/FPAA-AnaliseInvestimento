import csv
import statistics
from HistoricoAtivo import HistoricoAtivo
from Ativo import Ativo


print("Inicio")


listaAtivos = []

# Ler arquivo .csv e adicionar os ativos na variavel listaAtivos
with open('../data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ativo = None
    for row in reader:
        if(ativo is None or (ativo is not None and ativo.nome != row['ativo'])):
            ativo = Ativo(row['ativo'])
            listaAtivos.append(ativo)
        ht = HistoricoAtivo(row['data'],float(row['preco']), float(row['valor']), float(row['dividendo']))
        ativo.adicionaHistorico(ht)

for at in listaAtivos:
    precoInicial = at.lstHistorico[0].preco
    precoFinal = at.lstHistorico[-1].preco
    
    somaPreco = 0
    somaDividendos = 0
    lstDividendo = []
    for idx,item in enumerate(at.lstHistorico):
        somaDividendos += item.dividendo
        somaPreco += item.preco
        if idx > 0:
            lstDividendo.append(round(item.preco - at.lstHistorico[idx-1].preco, 2))


    retorno = (precoFinal + somaDividendos - precoInicial) / precoInicial
    desvioPadrao = statistics.stdev(lstDividendo)
    mediaPreco = somaPreco/len(at.lstHistorico)
    riscoNormalizado = desvioPadrao/mediaPreco
    riscoRetorno = riscoNormalizado/retorno

    print(f'Acao: {at.nome}')
    print(f'P_i: {precoInicial}')
    print(f'P_t: {precoFinal}')
    print(f'Dividendos: {somaDividendos}')
    print(f'Retorno: {retorno}')
    print(f'Desvio Padrao: {desvioPadrao}')
    print(f'Media de Preco: {desvioPadrao}')
    print(f'Risco Normalizado: {riscoNormalizado}')
    print(f'Risco Retorno: {riscoRetorno}')
    print('\n\n')
    break




print("Fim")