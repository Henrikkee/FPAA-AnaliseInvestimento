from .HistoricoAtivo import HistoricoAtivo

class Ativo:
    def __init__(self, nome):
        self.nome = nome
        self.lstHistorico = []
        self.riscoRetorno = None
        self.retorno = None
        self.somaDividendos = None
        pass

    def __str__(self) -> str:
        return f'{self.nome}\nRisco Retorno:{self.riscoRetorno} \nHistorico armazenado: {len(self)}'

    def __len__(self):
        return len(self.lstHistorico)


    def adicionaHistorico(self, historico: HistoricoAtivo):
        self.lstHistorico.append(historico)