import time
import random

def insertion_sort(lista_dados):
    """
    Implementação do algoritmo Insertion Sort com complexidade O(n²).
    """
    n = len(lista_dados)
    for i in range(1, n):
        chave = lista_dados[i]
        j = i - 1
        while j >= 0 and chave < lista_dados[j]:
            lista_dados[j + 1] = lista_dados[j]
            j -= 1
        lista_dados[j + 1] = chave

def comparar_algoritmos():
    """
    Gera listas aleatórias e compara o tempo de execução entre 
    Insertion Sort e o Timsort nativo do Python.
    """
    TAMANHOS_N = [1000, 5000, 10000, 20000, 50000]
    
    # Cabeçalho formatado (corrigido sem espaços após os dois pontos)
    print(f"{'n':<10} | {'Insertion SORT (s)':<20} | {'Timsort (s)':<15}")
    print("-" * 55)

    for n in TAMANHOS_N:
        # Cria uma lista de tamanho n cheia de números aleatórios
        lista_base = [random.randint(0, n * 2) for _ in range(n)]

        # Teste Insertion Sort
        copia_insertion = lista_base.copy()
        inicio_ins = time.time()
        insertion_sort(copia_insertion)
        fim_ins = time.time()
        tempo_ins = fim_ins - inicio_ins

        # Teste Timsort (sorted)
        copia_tim = lista_base.copy()
        inicio_tim = time.time()
        _ = sorted(copia_tim)
        fim_tim = time.time()
        tempo_tim = fim_tim - inicio_tim

        # Imprime os resultados para o 'n' atual
        print(f"{n:<10} | {tempo_ins:<20.5f} | {tempo_tim:<15.5f}")

if __name__ == "__main__":
    comparar_algoritmos()