import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorna o estado inicial do tabuleiro.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna o jogador (X ou O) que deve fazer o próximo movimento.
    """
    # Conta quantos espaços foram preenchidos
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    
    # Se X tem mais jogadas, é a vez de O. X começa o jogo.
    return O if count_x > count_o else X


def actions(board):
    """
    Retorna um conjunto de todas as ações (i, j) possíveis no tabuleiro.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Retorna o tabuleiro resultante de uma jogada (i, j) sem alterar o original.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Ação inválida: posição já ocupada.")
    
    # Deep copy para não modificar o estado original
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Retorna o vencedor (X ou O), se houver.
    """
    # Checar linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
            
    # Checar diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
        
    return None


def terminal(board):
    """
    Retorna True se o jogo acabou, False caso contrário.
    """
    if winner(board) is not None:
        return True
    
    # Se não há vencedor, checa se ainda existem espaços vazios
    for row in board:
        if EMPTY in row:
            return False
            
    return True


def utility(board):
    """
    Retorna 1 se X venceu, -1 se O venceu, 0 caso contrário.
    """
    res = winner(board)
    if res == X:
        return 1
    elif res == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Retorna a jogada ideal para o jogador atual.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # X quer maximizar o valor
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
        return best_move
    else:
        # O quer minimizar o valor
        best_val = math.inf
        best_move = None
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action
        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
