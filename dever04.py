import sys
import time

def funcao_recursiva(n):
    """
    Calcula F(n) usando recursão.
    Relação: F(n) = 2 * F(n-1) + n^2
    """
    # Caso base: definido no problema como F(1) = 1
    if n == 1:
        return 1
    
    # Passo recursivo
    return 2 * funcao_recursiva(n - 1) + n**2

def funcao_fechada(n):
    """
    Calcula F(n) usando a fórmula fechada (matemática direta).
    F(n) = 13 * 2^(n-1) - n^2 - 4n - 6
    """
    return 13 * (2 ** (n - 1)) - n**2 - 4 * n - 6

def medir_execucao():
    """Função para testar os valores e medir o desempenho de ambos os métodos."""
    # Aumentando o limite para suportar valores maiores de n
    sys.setrecursionlimit(3000)
    
    valores_n = [10, 100, 500, 1000]
    
    print(f"{'n':<10} | {'Método':<15} | {'Resultado (parcial)':<25} | {'Tempo (s)':<15}")
    print("-" * 75)
    
    for n in valores_n:
        # Medição da Recursão
        inicio_r = time.perf_counter()
        res_r = funcao_recursiva(n)
        fim_r = time.perf_counter()
        tempo_r = fim_r - inicio_r
        
        # Medição da Fórmula Fechada
        inicio_f = time.perf_counter()
        res_f = funcao_fechada(n)
        fim_f = time.perf_counter()
        tempo_f = fim_f - inicio_f
        
        # Exibindo resultados (abreviados para não quebrar a tabela)
        print(f"{n:<10} | {'Recursivo':<15} | {str(res_r)[:20]:<25} | {tempo_r:<15.8f}")
        print(f"{'':<10} | {'Fechada':<15} | {str(res_f)[:20]:<25} | {tempo_f:<15.8f}")
        print("-" * 75)

if __name__ == "__main__":
    medir_execucao()