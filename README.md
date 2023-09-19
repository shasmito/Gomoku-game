# gomoku-AB-pruning
- A pet project after learning alpha beta pruning
- CAN EASILY BEAT AI AT https://gomokuonline.com/

## How do AI calculate moves?
- Random in the first two moves.
- Check if player has a CHECKMATE MOVE? if player does, AI will take the best move to prevent it.
- check if player has a HIGH IMPACT MOVE? if player does, AI will take the best move to prevent it.
  A high impact move is a move which could lead to a checkmate move or create a great advantage for the player.
  (Ex: a move can create a pair of unblocked threes)
- check if player has a COMBO MOVE? if player does, AI will take the best move to prevent it.
  A combo move is a combo which could create a one-end-blocked-four and a unblocked three or n blocked-four (n>=2).
- If none of the above moves are available, the AI will use the ALPHA-BETA PRUNING algorithm to calculate its next move.

## Screenshots:
![Screenshot_gomoku_01.png](/Screenshot_gomoku_01.png)
# Gomoku-game
