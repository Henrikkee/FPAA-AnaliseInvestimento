import csv

class HistoricoAtivo:
    def __init__(self, data, preco, valor, dividendo):
        self.data = data
        self.preco = preco
        self.valor = valor
        self.dividendo = dividendo
        pass

class Ativo:
    def __init__(self, nome):
        self.nome = nome
        self.lstHistorico = []
        pass

    def __str__(self) -> str:
        return f'{self.nome} Historico armazenado: {len(self)}'

    def __len__(self):
        return len(self.lstHistorico)

    def adicionaHistorico(self, historico: HistoricoAtivo):
        self.lstHistorico.append(historico)


print("Start")

listaAtivos = []

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    ativo = None
    for row in reader:
        if(ativo is None or (ativo is not None and ativo.nome != row['ativo'])):
            ativo = Ativo(row['ativo'])
            listaAtivos.append(ativo)
        ht = HistoricoAtivo(row['data'],row['preco'], row['valor'], row['dividendo'])
        ativo.adicionaHistorico(ht)

for at in listaAtivos:
    print(at)

print("Fim")