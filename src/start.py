import csv
import statistics
import itertools
from HistoricoAtivo import HistoricoAtivo
from Ativo import Ativo
from time import gmtime, strftime

print("Inicio")

listaAtivos = []
listaRiscoRetorno = []

# Ler arquivo .csv e adicionar os ativos na variavel listaAtivos
with open('../datamenor.csv', newline='') as csvfile:
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

    retorno = (precoFinal + somaDividendos - precoInicial) / precoInicial
    desvioPadrao = statistics.stdev(lstDividendo)
    mediaPreco = somaPreco/len(at.lstHistorico)
    riscoNormalizado = desvioPadrao/mediaPreco
    riscoRetorno = riscoNormalizado/retorno
    listaRiscoRetorno.append(riscoRetorno)

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


t = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Força Bruta
lstMenorValor = [{"pativos": None, "val": 100}] * 5 # Salvar os items com menos valor de Risco Portifolio

for porcentagemDivida in itertools.product(range(0,101), repeat=len(listaAtivos)): 
    if sum(porcentagemDivida) == 100:
        value = 0
        somaValue = 0
        cnt = 0
        for idx, pd in enumerate(porcentagemDivida):
            value = listaRiscoRetorno[idx] *  (pd/100) # Risco Retorno * Peso
            cnt += 1 if value > 0 else 0
            somaValue += value
        riscoPortifolio = somaValue/cnt
        if lstMenorValor[-1]['val'] > riscoPortifolio:
            lstMenorValor.pop()
            lstMenorValor.append({"pativos": porcentagemDivida, "val": riscoPortifolio})
            lstMenorValor = sorted(lstMenorValor, key=lambda d: d['val']) 

print("Lista de Sugestoes: ")
for idx, lmv in enumerate(lstMenorValor):
    print(f'{idx+1} - ', end='')
    for idx2, porcentagem in enumerate(lmv['pativos']):
        print(f'{porcentagem}% em {listaAtivos[idx2].nome.upper()} ', end='')
    print('')


print(t)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

print("Fim")