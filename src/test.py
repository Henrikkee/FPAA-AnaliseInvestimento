from functions.readFile import readFile
from functions.bruteForce import bruteForce
from functions.greedy import greedy
from functions.random import randomAlg

listaAtivos = readFile('datamenor.csv')

def test_greddy():
    assert listaAtivos != greedy(listaAtivos, 1), "Greddy should be different 1"
    assert listaAtivos != greedy(listaAtivos, 2), "Greddy should be different 2"
    assert listaAtivos != greedy(listaAtivos, 3), "Greddy should be different 3"

def test_random():
    assert listaAtivos != randomAlg(listaAtivos), "Random should be different"

if __name__ == "__main__":
    test_greddy()
    test_random()
    print("Everything passed")