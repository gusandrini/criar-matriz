#usa I para linhas e J para colunas

def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input('Número: '))
            linha.append(n) #adiciona o 'n' para a lista de linhas
        matriz.append(linha) #adiciona a lista de linhas na matriz
    return matriz


def imprimir_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(f'matriz[{linha}][{coluna}]: {matriz[linha] [coluna]}')


def soma_numeros_matriz(matriz):
    soma = 0 #variável acumuladora
    for linhas in range (len(matriz)): #qtde de linhas
        for colunas in range (len(matriz[linhas])): #qtde de colunas
            soma += matriz [linhas] [colunas]
    return soma
            



#principal
matriz = criar_matriz (3,3) #tamanho da lista (qunatidade de numeros, quantidade de colunas)
print(matriz)
imprimir_matriz(matriz)
print(f'Soma: {soma_numeros_matriz(matriz)}')

#crie uma função que receba uma matriz por parametro e retorne o somatorio de todos elementos da matriz


