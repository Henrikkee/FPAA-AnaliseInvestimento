import csv
import statistics
from classes.Ativo import Ativo
from classes.HistoricoAtivo import HistoricoAtivo

def readFile(fileLocation) -> list:
    """
    Funcao para ler os dados no CSV e realizar calculos de retorno, desvio padrão, media de preco, risco normalizado, risco retorno
    Retorna uma lista com os ativos
    """

    listaAtivos = []

    # Ler arquivo .csv e adicionar os ativos na variavel listaAtivos
    try:
        with open(fileLocation, newline='') as csvfile:
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

                at.retorno = (precoFinal + somaDividendos - precoInicial) / precoInicial
                desvioPadrao = statistics.stdev(lstDividendo)
                mediaPreco = somaPreco/len(at.lstHistorico)
                riscoNormalizado = desvioPadrao/mediaPreco
                riscoRetorno = riscoNormalizado/at.retorno
                at.riscoRetorno = riscoRetorno if riscoRetorno > 0 else abs(riscoRetorno) * 100 # Caso possua um ativo com risco negativo adicionar um peso extra para que nao seja recomendado
                at.somaDividendos = somaDividendos

        return listaAtivos
    except FileNotFoundError:
        print("Arquivo nao encontrado. Fechando a aplicacao")
        exit()
    except Exception:
        print("Nao foi possivel ler o arquivo (Extensao invalida ou conteudo do CSV nao corresponde ao padrao). Fechando a aplicacao")
        exit()
