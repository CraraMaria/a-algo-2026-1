import time

def verificar_palindromo_recursivo(lista):
    """
    Verifica se uma lista é um palíndromo usando recursão.
    Um palíndromo é uma sequência que se lê da mesma forma de trás para frente.
    """
    # Caso base: uma lista vazia ou com um único elemento é sempre um palíndromo
    if len(lista) <= 1:
        return True

    # Verifica se o primeiro e o último elementos são iguais
    if lista[0] == lista[-1]:
        # Passo recursivo: chama a função novamente retirando as pontas (fatiamento)
        # lista[1:-1] cria uma nova sublista sem o primeiro e o último item
        return verificar_palindromo_recursivo(lista[1:-1])

    # Se os elementos das pontas forem diferentes, não é palíndromo
    return False

def medir_execucao():
    """Função principal para testar a lógica e medir o desempenho."""
    
    # Casos de teste variados
    test_cases = [
        [0, 1, 2, 3, 2, 1, 0],              # Ímpar, palíndromo
        ["a", "b", "b", "a"],               # Par, palíndromo
        ["a", "b", "c", "b", "a"],          # Ímpar, palíndromo
        ["a", "b", "c", "f", "b", "a"],      # Não é palíndromo
        [i for i in range(500)] + [i for i in range(498, -1, -1)] # Grande palíndromo para teste de n
    ]

    print(f"{'Caso':<10} | {'Resultado':<20} | {'Tempo (s)':<15}")
    print("-" * 55)

    for i, arr in enumerate(test_cases, 1):
        inicio = time.perf_counter()
        resultado = verificar_palindromo_recursivo(arr)
        fim = time.perf_counter()
        
        status = "É palíndromo" if resultado else "Não é palíndromo"
        tempo = fim - inicio
        
        # Exibindo apenas uma parte da lista se for muito grande
        resumo_lista = str(arr)[:20] + "..." if len(arr) > 10 else str(arr)
        
        print(f"Teste {i:<5} | {status:<20} | {tempo:<15.8f}")

if __name__ == "__main__":
    medir_execucao()


def main():
    """Main function to test the palindrome logic."""
    array1 = [0, 1, 2, 3, 2, 1, 0]
    array2 = ["a", "b", "b", "a"]
    array3 = ["a", "b", "c", "b", "a"]
    array4 = ["a", "b", "c", "f", "b", "a"]

    test_cases = [array1, array2, array3, array4]

    for i, arr in enumerate(test_cases, 1):
        result = is_palindrome(arr)
        status = "Is a palindrome" if result else "Is NOT a palindrome"
        print(f"array{i} = {arr} -> {status}")


if __name__ == "__main__":
    main()
