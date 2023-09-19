
# BOARD SIZE
BOARD_ROW_COUNT, BOARD_COL_COUNT = 15, 15 

MAX_MOVE_COUNT = BOARD_ROW_COUNT * BOARD_COL_COUNT

EMPTY_BOARD = [[0 for c in range(BOARD_COL_COUNT)] for r in range(BOARD_ROW_COUNT)]

# PLAYERS
NO_ONE = 0
HUMAN = 1
COM = 2

def get_opponent(player):
    if player == 1:
        return 2
    if player == 2:
        return 1

# TURN
# Human move 1st
FIRST_TURN = HUMAN
SECOND_TURN = COM

# # COM move 1st
# FIRST_TURN = COM
# SECOND_TURN = HUMAN

# SYMBOL
EMPTY = NO_ONE
O = HUMAN
X = COM