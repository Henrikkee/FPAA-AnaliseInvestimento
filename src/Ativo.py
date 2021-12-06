from HistoricoAtivo import HistoricoAtivo

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