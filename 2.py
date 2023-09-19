import pygame
from copy import deepcopy
from math import inf

# Game settings
BOARD_SIZE = 15
WIN_LENGTH = 5

X = "X"
O = "O"
EMPTY = "."

# PyGame initialization 
SQUARE_SIZE = 30
LINE_WIDTH = 2
RADIUS = SQUARE_SIZE // 2 - 3
OFFSET = SQUARE_SIZE // 2 + LINE_WIDTH

pygame.init()
screen = pygame.display.set_mode((SQUARE_SIZE * BOARD_SIZE, SQUARE_SIZE * BOARD_SIZE))
pygame.display.set_caption("Gomoku")

def minimax(board, depth, maximizingPlayer, alpha, beta):

    if depth == 0 or  is_game_over(board):
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -inf
        for move in get_valid_moves(board):
            boardAfterMove = make_move(board, move, X)
            eval = minimax(boardAfterMove, depth-1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = +inf
        for move in get_valid_moves(board):
            boardAfterMove = make_move(board, move, O)
            eval = minimax(boardAfterMove, depth-1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def get_valid_moves(board):
    validMoves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY:
                validMoves.append((r,c))
    return validMoves
                
def make_move(board, move, player):
    boardCopy = deepcopy(board)
    r, c = move
    boardCopy[r][c] = player
    return boardCopy

def evaluate(board):

    x_score = 0
    o_score = 0
    
    # Check rows
    for row in board:
        x_score += count_seq(row, X, WIN_LENGTH)
        o_score += count_seq(row, O, WIN_LENGTH)
    
    # Check columns
    for col in range(BOARD_SIZE):
        column = [board[i][col] for i in range(BOARD_SIZE)]
        x_score += count_seq(column, X, WIN_LENGTH)
        o_score += count_seq(column, O, WIN_LENGTH)
        
    # Check diagonals
    for offset in range(-BOARD_SIZE+1, BOARD_SIZE):
        diagonal1 = [board[i][i+offset] for i in range(BOARD_SIZE) if 0 <= i+offset < BOARD_SIZE]
        diagonal2 = [board[i][BOARD_SIZE-i-1+offset] for i in range(BOARD_SIZE) if 0 <= BOARD_SIZE-i-1+offset < BOARD_SIZE]
        x_score += count_seq(diagonal1, X, WIN_LENGTH) 
        o_score += count_seq(diagonal1, O, WIN_LENGTH)
        x_score += count_seq(diagonal2, X, WIN_LENGTH)
        o_score += count_seq(diagonal2, O, WIN_LENGTH)
        
    return (x_score, o_score)

def count_seq(array, player, seq_len):
    count = 0
    for i in range(len(array)-seq_len+1):
        window = array[i:i+seq_len]
        if window.count(player) == seq_len:
            count += 1
    return count
        
def game_over(board):
    return has_won(board, X) or has_won(board, O)

def has_won(board, player):

    # Check rows
    for row in board:
        if row.count(player) == BOARD_SIZE:
            return True
            
    # Check columns
    for col in range(BOARD_SIZE):
        column = [board[i][col] for i in range(BOARD_SIZE)]
        if column.count(player) == BOARD_SIZE:
            return True
    
    # Check diagonals
    for offset in range(-BOARD_SIZE+1, BOARD_SIZE):
        diagonal1 = [board[i][i+offset] for i in range(BOARD_SIZE) if 0 <= i+offset < BOARD_SIZE]
        if diagonal1.count(player) == BOARD_SIZE:
            return True

        diagonal2 = [board[i][BOARD_SIZE-i-1+offset] for i in range(BOARD_SIZE) if 0 <= BOARD_SIZE-i-1+offset < BOARD_SIZE]
        if diagonal2.count(player) == BOARD_SIZE:
            return True
        
    return False

def draw_board():

    # Draw grid
    for x in range(0, BOARD_SIZE):
        pygame.draw.line(screen, (0,0,0), (0, SQUARE_SIZE * x), (BOARD_SIZE * SQUARE_SIZE, SQUARE_SIZE * x), LINE_WIDTH)
        pygame.draw.line(screen, (0,0,0), (SQUARE_SIZE * x, 0), (SQUARE_SIZE * x, BOARD_SIZE * SQUARE_SIZE), LINE_WIDTH)
        
    # Draw pieces  
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == O:
                pygame.draw.circle(screen, (0,0,255), (OFFSET + SQUARE_SIZE * y, OFFSET + SQUARE_SIZE * x), RADIUS)
            elif board[x][y] == X: 
                pygame.draw.line(screen, (255, 0, 0), (OFFSET + SQUARE_SIZE * y - RADIUS, OFFSET + SQUARE_SIZE * x - RADIUS), (OFFSET + SQUARE_SIZE * y + RADIUS, OFFSET + SQUARE_SIZE * x + RADIUS))
                pygame.draw.line(screen, (255, 0, 0), (OFFSET + SQUARE_SIZE * y + RADIUS, OFFSET + SQUARE_SIZE * x - RADIUS), (OFFSET + SQUARE_SIZE * y - RADIUS, OFFSET + SQUARE_SIZE * x + RADIUS))
                
    pygame.display.update()

# Main driver
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
is_game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP and not game_over:
            x,y = pygame.mouse.get_pos()
            col = int(x//SQUARE_SIZE)
            row = int(y//SQUARE_SIZE)
            make_move(board, (row,col), O)
            draw_board()

            if  is_game_over:
                break

            move = minimax(board, 4, True, -inf, inf)
            make_move(board, move, X)
            draw_board()

            if  is_game_over:
                break

    if has_won(board, X):
        print("X won!")
        game_over = True

    elif has_won(board, O):
        print("O won!")
        game_over = True

    elif get_valid_moves(board) == []:
        print("Draw!")
        game_over = True