from functions.readFile import readFile
from functions.bruteForce import bruteForce
from functions.greedy import greedy
from functions.random import randomAlg
def printRecomendacoes(listaAtivos):
    print("Lista de Recomendacoes: ")
    for idx,l in enumerate(listaAtivos):
        print(f'{idx+1} - {l.nome}')

def main():

    print("Inicio")
    # Funcao para ler os dados no CSV e realizar calculos de retorno, desvio padrão, media de preco, risco normalizado, risco retorno
    path = input("Digite o caminho do arquivo de dados de entrada: ")
    listaAtivos = readFile(path)

    option = -1

    while option != 4:
        print("\nMenu de Investimentos:\n1- Analisar via Força Bruta\n2- Analisar via Guloso\n3- Analise Aleatoria\n4- Sair")
        option = int(input("Opcao: "))

        if option == 1: #Algoritmo de força bruta
            numSugestoes = int(input('Digite o numero de ativos que deseja obter: '))
            bruteForce(listaAtivos,numSugestoes)
        elif option == 2: #Solução gulosa
            print("Escolha o criterio:\n1-Risco/Retorno\n2-Maior Retorno\n3-Maior valor em dividendos")
            opt = int(input("Opcao: "))
            printRecomendacoes(greedy(listaAtivos, opt))
        elif option == 3: #Estratégia aleatória
            printRecomendacoes(randomAlg(listaAtivos))
    

    print("Fim")

if __name__ == "__main__":
    main()