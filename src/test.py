import csv
import statistics
from functions.greedy import greedy
from classes.Ativo import Ativo
from classes.HistoricoAtivo import HistoricoAtivo

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

# Realizar calculos de retorno, desvio padrão, media de preco, risco normalizado, risco retorno
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

    at.retorno = (precoFinal + somaDividendos - precoInicial) / precoInicial
    desvioPadrao = statistics.stdev(lstDividendo)
    mediaPreco = somaPreco/len(at.lstHistorico)
    riscoNormalizado = desvioPadrao/mediaPreco
    riscoRetorno = riscoNormalizado/at.retorno
    at.riscoRetorno = riscoRetorno if riscoRetorno > 0 else abs(riscoRetorno) * 100 # Caso possua um ativo com risco negativo adicionar um peso extra para que nao seja recomendado
    at.somaDividendos = somaDividendos

greedy(listaAtivos, 1)