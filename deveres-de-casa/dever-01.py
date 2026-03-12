"""
Implementar o algoritomo InsertionSort O(n²)
utilizar a função nativa do Python sorted () que usa o Timsort,
(n log n) para fins de comparação
gere listas de tamanhos n= [1000, 5000, 10000, 20000, 50000]
Medir o tempo de execução de ambos os algoritmos para cada n,
gerando a saída no terminal de cada um deles, utilizando a bibliotec TIME

snake_case para variáveis, funções e métodos
Pascal_Case para classes
SCREAMING_SNAKE_CASE para constantes
Blocos de comentários com as convenções de Docstrings
"""

import time
import random

# Implementar o algoritomo InsertionSort O(n²)
def insertion_sort (lista_dados):

    n = len(lista_dados) # Len = length; comprimento


    for i in range(1, n): #percorrer a lista a partir do segundo elemento
        chave = lista_dados[i] #chave = valor que está posicionando agora
        j = i - 1  #indice do elemento imediatamente à esquerda da chave
        # ENQUANTO o valor a esquerda (lista_dados[j]) for maior que a CHAVE
        while j >= 0 and chave < lista_dados[j]:
            # Move o elemento maior para a direita
            lista_dados[j + 1] = lista_dados[j]
            # diminui o j para comparar a chave com o próximo elemento a esquerda
            j -= 1
        # quando o espaço correto é encontrado, "espetamos" a chave ali, +1 porque o loop while subtraiu uma unidade a mais antes de encerrar
        lista_dados[j + 1] = chave

# é a parte que vai fazer o teste desse loop acima
def comparar_algoritmos():
    TAMANHOS_N = [1000, 5000, 10000, 20000, 50000 ]
    # cabeçalho da tela funcionalidade f-strings
    print(f"{'n':<10} | {'Insertion SORT (s)':<20}| {'Timesort (s)': 15}")

    #cria uma lista de tamanho n cheia de números aleatórios
    lista_base = [ random.randint(0, n* 2) for _ in range (n)]

    # Teste Insertion Sort
    copia_insertion = lista_base.copy() # Cria uma cópia para não estragar a original
    inicio_ins = time.time()            # Bate o cronômetro e marca o segundo atual
    insertion_sort(copia_insertion)     # Executa o algoritmo
    fim_ins = time.time()               # bate o cronômetro de novo
    tempo_ins = fim_ins - inicio_ins    # Calcula a diferença do tempo final - inicial

            # Teste Timsort (sorted)
    copia_tim = lista_base.copy()
    inicio_tim = time.time()
    _ = sorted(copia_tim)
    fim_tim = time.time()
    tempo_tim = fim_tim - inicio_tim

    print(f"{n:<10} | {tempo_ins:<20.5f} | {tempo_tim:<15.5f}")

if __name__ == "__main__":
    comparar_algoritmos()
