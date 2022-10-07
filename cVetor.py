from radixSort import radixSort # importando o radix sort (função de ordenação)

class vetor: # (TAD - Tipo Abstrato de Dados)

# Criar vetor 
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vet = [0]*tamanho
        self.numObjs = 0

# Acessar elemento do vetor
    def acessar(self, posicao):
        if(self.numObjs>0 and posicao<self.numObjs):
            return self.vet[posicao]
        else:
            return False

# Tamanho do vetor
    def tamanho(self):
        return self.numObjs   
    

# Imprimir vetor
    def imprimir(self):
        if self.numObjs == 0:
            print("Vetor vazio")
        else:
            for i in range(self.numObjs):
                print(f'Elemento {i+1} = {self.vet[i]}')
        
# Inserir no vetor
    def inserir(self, valorInserido):
        if self.numObjs < self.tam:
            self.vet[self.numObjs] = valorInserido
            self.numObjs += 1
            return True
        else:
            return False


# Ordenação do vetor
    def ordenar(self):
        radixSort(self.vet)


