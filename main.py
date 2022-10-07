from cVetor import vetor


if __name__ == '__main__':

# === abrindo o arquivo de placas PIV desordenadas e adicionando o conteúdo a um vetor ===

    with open("PIVs-10000.piv", "r") as arquivo:
        placas = arquivo.read()

    tamanho = 0

    for i in placas.split():
        tamanho+=1


    listaPIV = vetor(tamanho)

    for placa in placas.split():
        listaPIV.inserir(placa)

# ========================================================================================


# ====== ordenando as placas PIV utilizando LSD Radix Sort ===================================

    listaPIV.ordenar()

# ========================================================================================


# === criando e escrevendo no arquivo de placas PIV ordenadas lexicograficamente =========

    with open("PIVs-10000-ORDENADOS.piv", "a") as arquivo:
        for i in range(tamanho):
            arquivo.write(f"{listaPIV.acessar(i)}\n")

# ========================================================================================