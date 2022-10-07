letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def countingSortLetras(array, index): # ORDENANDO POR LETRAS NO ÍNDICE (index):

    contador = [0] * len(letras) # 26 = letras do alfabeto
    saida = [0] * len(array) # tamanho do vetor

    for item in array: # adicionando valor ao vetor contador
        idx_letra = letras.index(item[index])
        contador[idx_letra] += 1 
    
    for i in range(1, len(contador)): # criando vetor acumulador
        contador[i] += contador[i-1]

    i = len(array) - 1
    while i >= 0: # colocando o vetor 'saida' em ordem com base no index
        idx_letra = letras.index(array[i][index])
        saida[contador[idx_letra] - 1] = array[i]
        contador[idx_letra] -= 1
        i -= 1

    for i in range(0, len(array)): # transformando o vetor de retorno
        array[i] = saida[i]  

    return array


def countingSortNumeros(array, index): # ORDENANDO POR NÚMEROS NO ÍNDICE (index):

    contador = [0]*10 # 10 = base decimal
    saida = [0]*len(array) # tamanho do vetor

    for i in range(len(saida)): # adicionando valor ao vetor contador
        idx_num = int(array[i][index])
        contador[idx_num] += 1

    for i in range(1,10): # criando vetor acumulador
        contador[i] += contador[i-1]

    i = len(array) - 1
    while i >= 0: # colocando o vetor 'saida' em ordem com base no index
        idx_num = int(array[i][index])
        saida[contador[idx_num] - 1] = array[i]
        contador[idx_num] -= 1
        i -= 1

    for i in range(0, len(array)): # transformando o vetor de retorno
        array[i] = saida[i] 

    return array


def radixSort(array, numDigitos=7): # LSD radix sort com valor fixo do número de digitos da placa PIV: (7)

    for i in range(numDigitos-1, -1, -1): # do dígito mais a direita para o dígito mais a esquerda: (LSD)
        if (i <= 2 or  i == 4): # posições em que estão as letras com base na placa PIV: (0, 1, 2 e 4)
            array = countingSortLetras(array, i)
        else: # posições em que estão os números com base na placa PIV: (3, 5 e 6)
            array = countingSortNumeros(array, i)

    return array # lista ordenada
