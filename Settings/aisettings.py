from math import inf as infinity
from Settings.gamesettings import X, O, EMPTY

# ALPHA BETA PRUNING SETTINGS
MAX_TREE_DEPTH_LEVEL = 2
EXPANSION_RANGE = 2 # FOR GENERATING POSSIBLE MOVES


# EVALUATION SCORES

SCORE_4_UNBLOCKED_PIECES = 50_007
SCORE_3_UNBLOCKED_PIECES = 5_005
SCORE_2_UNBLOCKED_PIECES = 103
SCORE_1_UNBLOCKED_PIECES = 11

SCORE_5_BLOCKED_PIECES = 1_000_009 # WIN
SCORE_4_BLOCKED_PIECES = 6_007
SCORE_3_BLOCKED_PIECES = 185

# CHECK BEFORE ALPHA BETA PRUNING
ENABLE_HIGH_IMPACT_MOVE = True 
# lower this setting value could reduce time AI thinking but also reduce move quality
HIGH_IMPACT_MOVE_THRESHOLD = 15440 #15440
# a high impact move is a move which could lead to a win or great advantage


# EVALUATION PATTERNS
X_6_PATTERNS = [[EMPTY, X, X, X, X, EMPTY],
                [EMPTY, X, X, X, EMPTY, EMPTY],
                [EMPTY, EMPTY, X, X, X, EMPTY],
                [EMPTY, X, X, EMPTY, X, EMPTY],
                [EMPTY, X, EMPTY, X, X, EMPTY],
                [EMPTY, EMPTY, X, X, EMPTY, EMPTY],
                [EMPTY, EMPTY, X, EMPTY, X, EMPTY],
                [EMPTY, X, EMPTY, X, EMPTY, EMPTY],
                [EMPTY, X, EMPTY, EMPTY, X, EMPTY],
                [EMPTY, EMPTY, X, EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY, X, EMPTY, EMPTY]]

X_6_PATTERNS_SCORES = [
    SCORE_4_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES]

X_5_PATTERNS = [[X, X, X, X, X],
                [X, X, X, X, EMPTY],
                [EMPTY, X, X, X, X],
                [X, X, EMPTY, X, X],
                [X, EMPTY, X, X, X],
                [X, X, X, EMPTY, X],
                [X, EMPTY, X, EMPTY, X],
                [X, X, EMPTY, EMPTY, X],
                [X, EMPTY, EMPTY, X, X],
                [EMPTY, X, X, EMPTY, X],
                [X, EMPTY, X, X, EMPTY],
                [EMPTY, X, X, X, EMPTY],
                [X, X, X, EMPTY, EMPTY],
                [EMPTY, EMPTY, X, X, X]]

X_5_PATTERNS_SCORES = [
    SCORE_5_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES,
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES]

X_END_GAME_PATTERN = [X, X, X, X, X]

O_6_PATTERNS = [[EMPTY, O, O, O, O, EMPTY],
                [EMPTY, O, O, O, EMPTY, EMPTY],
                [EMPTY, EMPTY, O, O, O, EMPTY],
                [EMPTY, O, O, EMPTY, O, EMPTY],
                [EMPTY, O, EMPTY, O, O, EMPTY],
                [EMPTY, EMPTY, O, O, EMPTY, EMPTY],
                [EMPTY, EMPTY, O, EMPTY, O, EMPTY],
                [EMPTY, O, EMPTY, O, EMPTY, EMPTY],
                [EMPTY, O, EMPTY, EMPTY, O, EMPTY],
                [EMPTY, EMPTY, O, EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY, O, EMPTY, EMPTY]]

O_6_PATTERNS_SCORES = [
    SCORE_4_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES]

O_5_PATTERNS = [[O, O, O, O, O],
                [O, O, O, O, EMPTY],
                [EMPTY, O, O, O, O],
                [O, O, EMPTY, O, O],
                [O, EMPTY, O, O, O],
                [O, O, O, EMPTY, O],
                [O, EMPTY, O, EMPTY, O],
                [O, O, EMPTY, EMPTY, O],
                [O, EMPTY, EMPTY, O, O],
                [EMPTY, O, O, EMPTY, O],
                [O, EMPTY, O, O, EMPTY],
                [EMPTY, O, O, O, EMPTY],
                [O, O, O, EMPTY, EMPTY],
                [EMPTY, EMPTY, O, O, O]]

O_5_PATTERNS_SCORES = [
    SCORE_5_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES,
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES]

O_END_GAME_PATTERN = [O, O, O, O, O]