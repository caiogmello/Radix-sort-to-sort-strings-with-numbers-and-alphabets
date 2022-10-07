# Problema 1 - Procura-se Veículos
Aluno: Caio Gomes de Mello
## Pensamento para a solução do problema

O problema se trata de uma forma de ordenar lexicograficamente uma lista de **placas PIV**, do tipo abaixo:

![Exemplo de Placa do Mercosul](imgs/PlacaMercosul.jpg)

E meu pensamento para a solução desse problema partiu da seguinte proposição dada na aba de *motivação* do trabalho:


> "A base de dados poderá chegar a 456.976.000 combinações/placas possíveis. Portanto, para que a base de dados possa ser mantida ordenada algoritmos cuja complexidade seja `O(n²)` estão descartados. Algoritmos `O(n.log(n))` são a escolha mais direta, mas dado que sabemos que as placas tem tamanho fixo, talvez seja possível conceber um algoritmo mais eficiente nesse contexto [2][3]."

### Com esse texto, fui capaz de pensar em algumas coisas:

- Algoritmos `O(n²)` e `O(n.log(n))` são os tipos de ordenação mais rápidos para **ordenações por comparação**, portanto, algoritmos como *quick sort*, *merge sort* e ordenação por *heap* estão descartados. [2]

- Para conseguir um algoritmo mais eficiente que os citados acima, precisamos optar por algoritmos de **ordenação em tempo linear** (`O(n)`), em que não utilizam nenhum tipo de comparação entre os elementos. Nos meus estudos, descobri 3 delas: [2]
    1. Ordenação por **contagem** (*counting sort*);
    2. Ordenação **digital** (*radix sort*);
    3. Ordenação por **balde** (*bucket sort*). 
---
 Dentre esses algoritmos de ordenação, tive que buscar o que mais se adequava a situação dada: os elementos possuem mais de um dígito e um número fixo de digitos (**7**). 

 ---
 Logo, o algoritmo que encaixa perfeitamente, nesse caso, é o ***Radix sort***.

 ## *Radix sort*

> O *Radix sort* é um algoritmo de ordenação rápido e estável que pode ser usado para ordenar itens que estão identificados por chaves únicas. Cada chave é uma cadeia de caracteres ou número, e o *radix sort* ordena estas chaves em qualquer ordem relacionada com a lexicografia. [6]

### Existem duas classificações do radix sort, que são:

- *Least significant digit* (LSD - dígito menos significativo) radix sort;
- *Most significant digit* (MSD - dígito menos significativo) radix sort.
---
- o *LSD radix sort* é o ideal para sequenciar inteiros e palavras e ordenar lexicograficamente chaves do mesmo tamanho;
- o *MSD radix sort* é o ideal para sequenciar palavras usando ordem lexicográfica.

Portanto, o escolhido para uso foi o ***LSD radix sort***, visto que teremos um número constante de dígitos e trabalharemos com uma *string* de números inteiros e letras.

## Implementação

Uma variação na implementação do *radix sort* que evita o uso de **listas encadeadas** é a repetição de **algoritmos estáveis** como o *counting sort*, que foi antes citado. [1]

> A ordenação por contagem determina, para cada elemento de entrada x, o número de elementos menores que x e
usa essa informação para inserir o elemento x diretamente em sua posição no arranjo de saída. [2]

Logo, se fizermos uma função do algoritmo *counting sort* se repetir *d* vezes, cada vez com um dígito diferente, em que *d* é a quantidade de dígitos,  teremos um algoritmo *radix sort* implementado. [1]

## Complexidade

> Dados *n* números de *d* dígitos nos quais cada dígito pode adotar até *k* valores possíveis, *radix sort* ordena
corretamente esses números no tempo `O(d(n + k))` se a ordenação estável levar o tempo `O(n + k)`.

>Então, cada passagem sobre n números de d dígitos leva
o tempo `O(n + k)`. Há d passagens e, assim, o tempo total para ordenação digital é `O(d(n + k))`.

>Quando *d* é constante e *k* = `O(n)`, podemos executar ordenação digital em tempo linear. [2]

### Aplicando essa teoria no nosso exemplo, temos que:

- *d* é constante e igual a 7 (número de dígitos da placa PIV);
- *n* é igual ao números de placas no vetor;
- *k* é igual ao número de valores possíveis, que podem ser dois:
    - 10, se for um número (0-9);
    - 26, se for uma letra (A-Z).
---
Na placa PIV temos 4 dígitos destinados a letras e 3 dígitos destinados a números, logo: 

>O(4(n + 26) + 3(n + 10)) = **O(7(n + 134/7))**

        Portanto, se trata de uma complexidade linear: O(n)

Como o *radix sort* não é um algoritmo de comparação, ele terá a mesma complexidade para **todos** os casos (pior, médio e melhor).


# Código

 Meu código:
 - 100% em python:
    - nenhuma biblioteca exterior importada.
 - Modularizado;
 - Tipo Abstrato de Dados `cVetor.py` criado:
    - Cria o vetor;
    - Insere;
    - Retorna tamanho;
    - Imprime;
    - Acessa qualquer elemento;
    - Ordena por meio do `radixSort()`;
 - `main.py`:
    - Abre o arquivo de texto;
    - Através das funções do `cVetor.py`:
        - Adiciona todo conteúdo a um vetor;
        - Ordena o vetor;
        - Escreve um arquivo de texto ordenado;

##  `radixSort.py`:

Na implementação, utilizei do recurso que já citei, de utilizar o *counting sort* como **algoritmo estável**. 

Para isso, criei duas funções do tipo *counting sort*:

- `countingSortNumeros(a, i)`:
    - Duas listas são criadas:
        - `contador`
        : lista de tamanho 10, com todos os elementos começando em 0, para a **contagem** dos valores dos dígitos.
        - `saida`
        : lista de tamanho `len(a)`, sendo `a` o vetor recebido.
    - Quatro loops são feitos:
        1. Adiciona valor ao vetor `contador`;
        2. No vetor `contador` soma o item com seu item anterior, criando um **"contador acumulador"**, onde o último elemento do vetor é o total de índices contados.
        3. Ordena vetor `saida` com base no `i`;
        4. Transforma o vetor de retorno no vetor `saida`.
    - Retorna vetor `a` ordenado com base no número do índice `i`.

- `countingSortLetras(a, i)`:
    - Segue a mesma lógica do `countingSortNumeros(a, i)`, com algumas mudanças mínimas:
        - O tamanho do vetor contador é 26;
        - Uma lista `letras` de todas as letras possíveis em uma placa PIV, em ordem alfabética, é criada;
        - A função `index()` do python é usada para retornar o índice de cada letra na lista `letras`.
    - Retorna vetor `a` ordenado com base na letra do índice `i`.

Por fim, a função:

- `radixSort(a, d)`:

    - `d` é o número máximo de dígitos, que no caso atual, é fixo em 7;
    - Realiza um loop inverso por ser um LSD *radix sort*;
    - Chama uma das funções *counting sort* com base em uma condicional:
        - Se o dígito `i` analisado for o dígito 0, 1, 2 ou 4: `countingSortLetras()`;
        - Se o dígito `i` analisado for o dígito 3, 5 ou 6: `countingSortNumeros()`.

Para apoio com a abstração do código do algoritmo, utilizei essas fontes: [1], [3], [7]








 












## Fontes utilizadas:

### Para a ordenação:

[1] Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

[2] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012.

[3] **Radix sort Algorithm:** https://www.programiz.com/dsa/radix-sort

[4] **Ordenação: Radixsort** https://homepages.dcc.ufmg.br/~cunha/teaching/20121/aeds2/radixsort.pdf

[5] **Radix sort in integer alphabets:** https://www.cs.helsinki.fi/u/tpkarkka/opetus/13s/spa/lecture03.pdf

[6] **Radix sort - Wikipedia:** https://pt.wikipedia.org/wiki/Radix_sort

[7] RADIX Sort in Python | **tutorial and how to implement in code:** https://www.youtube.com/watch?v=BVGRgTALQ44

### Para a organização do código e do relatório:

[8] Erica Vartanian, **"6 coding best practices for beginner programmers"**. Disponível em:  https://www.educative.io/blog/coding-best-practices

[9] Matt Cone, **Markdown Cheat Sheet - A quick reference to the Markdown syntax**. Disponível em: https://www.markdownguide.org/cheat-sheet/
