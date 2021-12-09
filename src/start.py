import csv
import statistics
from bruteForce import bruteForce
from greedy import greedy
from HistoricoAtivo import HistoricoAtivo
from Ativo import Ativo
from time import gmtime, strftime

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

    # print(f'Ativo: {at.nome}')
    # print(f'P_i: {precoInicial}')
    # print(f'P_t: {precoFinal}')
    # print(f'Dividendos: {somaDividendos}')
    # print(f'Retorno: {at.retorno}')
    # print(f'Desvio Padrao: {desvioPadrao}')
    # print(f'Media de Preco: {mediaPreco}')
    # print(f'Risco Normalizado: {riscoNormalizado}')
    # print(f'Risco Retorno: {at.riscoRetorno}\n')

print("Menu de Investimentos:\n1- Analisar via Força Bruta\n2- Analisar via Guloso")
option = int(input())

t = strftime("%Y-%m-%d %H:%M:%S", gmtime())


if option == 1:
    bruteForce(listaAtivos)
elif option == 2:
    greedy(listaAtivos)



    




print(t)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

print("Fim")