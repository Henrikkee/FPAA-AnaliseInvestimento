import random

def randomAlg(listaRandom):
    """
    Retorna uma lista de ativos ordenados de forma aleatória
    """

    novaLista = listaRandom.copy()
    for i in range(len(listaRandom)-1, 0, -1):
        j = random.randint(0, i + 1)
        try:
            novaLista[i], novaLista[j] = listaRandom[j], listaRandom[i]
        except Exception:
            print()
    return novaLista