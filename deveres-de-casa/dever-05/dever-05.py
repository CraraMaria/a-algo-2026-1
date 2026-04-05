import sys
import time
import math

def funcao_recursiva_exponencial(n):
    """
    Calcula F(n) de forma exponencial O(2^n).
    Para gerar essa complexidade, a função chama a si mesma duas vezes.
    """
    # Caso base conforme a dica
    if n == 1:
        return 2
    
    # Chamando a si mesma duas vezes para gerar a complexidade exponencial O(2^n)
    # Isso é equivalente a 2 * funcao_recursiva_exponencial(n - 1), 
    # mas computacionalmente força o computador a refazer o cálculo.
    return funcao_recursiva_exponencial(n - 1) + funcao_recursiva_exponencial(n - 1) + n**2

def funcao_fechada_otimizada(n):
    """
    Calcula a fórmula fechada utilizando a biblioteca math.
    Baseado na estrutura F(n) = 2^n + ... (ajustada para o caso base)
    """
    # Exemplo de uso da biblioteca math como solicitado na dica
    # F(n) = 13 * 2^(n-1) - n^2 - 4n - 6 (usando a mesma do exercício anterior)
    return 13 * math.pow(2, n - 1) - math.pow(n, 2) - 4 * n - 6

def main():
    sys.setrecursionlimit(2000)
    
    try:
        print("DICA: Como a complexidade é O(2^n), evite valores de n > 25.")
        n = int(input("Digite o valor de n (n >= 1): "))
        
        if n < 1:
            print("O caso base começa em 1.")
            return

        # Medindo a Recursão Exponencial
        inicio_r = time.perf_counter()
        res_r = funcao_recursiva_exponencial(n)
        fim_r = time.perf_counter()
        
        # Medindo a Fórmula Fechada (O(1))
        inicio_f = time.perf_counter()
        res_f = funcao_fechada_otimizada(n)
        fim_f = time.perf_counter()

        print("\n--- Resultados ---")
        print(f"Recursivo O(2^n): {res_r}")
        print(f"Fórmula Fechada:  {res_f}")
        print(f"\nTempo Recursivo: {fim_r - inicio_r:.8f} s")
        print(f"Tempo Fechada:   {fim_f - inicio_f:.8f} s")

    except ValueError:
        print("Entrada inválida.")
    except RecursionError:
        print("Erro: O valor de n é muito grande para a pilha de recursão.")

if __name__ == "__main__":
    main()
