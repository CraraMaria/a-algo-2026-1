"""
Implementar o algoritomo em Python que calcule o fatorial de um número utilizando recursão
Após isso, determine a complexidade assintótica O (n) do algoritmo,
incluindo a explicação do racioncínio. O objetivo é avalisar
como o tempo de execução cresce em função do tamanho da entrada n


Instruções: 
Leita um núemro inteiro n
Calcule o fatorial de n recursivamente
inclua comentários explicando cada parte do código
meça o tempo de execução do algoritmo para diferentes valoress de n: {10, 100, 500, 1000}
Submeta o código com os resultados do tempo de execução e 
uma breve explicação da análise de complexidade

Análise de Complexidade AssintóticaComplexidade de Tempo: $O(n)$O raciocínio para determinar que o algoritmo é linear baseia-se no número de chamadas de função:Para calcular o fatorial de $n$, a função é chamada exatamente $n$ vezes (uma para cada valor de $n$ até chegar ao caso base $1$).Cada chamada individual realiza uma operação aritmética de multiplicação e uma subtração, ambas consideradas operações de tempo constante $O(1)$ em termos de lógica algorítmica elementar.Portanto, o tempo total é a soma de $n$ chamadas de custo constante: $T(n) = n \times O(1) = O(n)$.Complexidade de Espaço: $O(n)$Diferente da versão iterativa (que seria $O(1)$ em espaço), a recursão consome memória na Pilha de Chamadas (Call Stack). Cada chamada calcular_fatorial(n) fica aberta na memória aguardando o retorno de calcular_fatorial(n-1). Como temos $n$ chamadas pendentes, o espaço cresce linearmente com $n$.Nota: Em Python, para valores muito grandes de $n$, a recursão pode causar um RecursionError. Por isso, ajustamos o sys.setrecursionlimit.Gostaria que eu implementasse a versão iterativa para compararmos a eficiência de memória entre as duas abordagens?

"""

import time
import sys

# Aumentando o limite de recursão para suportar n=1000
sys.setrecursionlimit(2000)

def calcular_fatorial(n):
    """
    Calcula o fatorial de n de forma recursiva.
    """
    # Caso base: o fatorial de 0 ou 1 é sempre 1
    if n <= 1:
        return 1
    
    # Passo recursivo: n! = n * (n-1)!
    return n * calcular_fatorial(n - 1)

def medir_execucao():
    valores_n = [10, 100, 500, 1000]
    
    print(f"{'n':<10} | {'Tempo de Execução (segundos)':<30}")
    print("-" * 45)
    
    for n in valores_n:
        inicio = time.perf_counter()
        resultado = calcular_fatorial(n)
        fim = time.perf_counter()
        
        tempo_total = fim - inicio
        print(f"{n:<10} | {tempo_total:<30.8f}")

if __name__ == "__main__":
    medir_execucao()
