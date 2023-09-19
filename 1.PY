import random
import time
import pygame
from pygame.locals import *
from copy import deepcopy
from math import inf as infinity
import Settings.aisettings as ai_settings 
import Settings.gamesettings as game_settings
from state import State
from minimaxnode import MinimaxNode
from gamerender import GameRender

class ABPruningAI:
    def __init__(self, state: State) -> None:
        self.state = state

    def next_move(self):
        if len(self.state.moves) <= 1:
            return self.random_move(self.state, 1)
        
        checkmate_move = State.checkmate(self.state.board, self.state.current_turn)
        if checkmate_move:
            return checkmate_move
        
        opponent_checkmate = State.checkmate(self.state.board, game_settings.get_opponent(self.state.current_turn))
        if opponent_checkmate: 
            return opponent_checkmate

        if ai_settings.ENABLE_HIGH_IMPACT_MOVE:
            opponent_high, opponent_score = State.high_impact_move(self.state.board, game_settings.get_opponent(self.state.current_turn))
            com_high, com_score = State.high_impact_move(self.state.board, self.state.current_turn)
            if opponent_high and opponent_score > com_score:
                return opponent_high
            if com_high and com_score >= opponent_score:
                return com_high

        opponent_combo = State.combo_move(self.state.board, game_settings.get_opponent(self.state.current_turn))
        com_combo = State.combo_move(self.state.board, self.state.current_turn)
        if com_combo:
            return com_combo
        if opponent_combo:
            return opponent_combo

        root_node = MinimaxNode(self.state.board, self.state.moves[-1], self.state.current_turn, None)
        score = self.alpha_beta(root_node, ai_settings.MAX_TREE_DEPTH_LEVEL, -infinity, infinity, True)
        return root_node.planing_next_move

    def random_move(self, state, expansion_range):
        if state.board == game_settings.EMPTY_BOARD:
            return (game_settings.BOARD_ROW_COUNT//2, game_settings.BOARD_COL_COUNT//2) 
        moves = State.generate_possible_moves(state.board, expansion_range)
        return random.choice(moves)

    def alpha_beta(self, node, depth, alpha, beta, maximizing):
        if depth == 0 or State.game_over(node.board):
            o, x = State.evaluate(node.board)
            return x - o
        
        if maximizing:
            value = -infinity  
            for child in node.generate_child_nodes():
                value = max(value, self.alpha_beta(child, depth-1, alpha, beta, False))
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            value = infinity
            for child in node.generate_child_nodes():
                value = min(value, self.alpha_beta(child, depth-1, alpha, beta, True))
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value

class MinimaxNode:
    def __init__(self, board, last_move, current_turn, planing_next_move) -> None:
        self.board = deepcopy(board)
        self.last_move = last_move
        self.planing_next_move = planing_next_move
        self.current_turn = current_turn

    def generate_child_nodes(self):
        moves = State.generate_possible_moves(self.board, ai_settings.EXPANSION_RANGE)
        nodes = []
        for move in moves:
            node = MinimaxNode(self.board, move, game_settings.get_opponent(self.current_turn), None)
            node.board[move[0]][move[1]] = self.current_turn
            nodes.append(node)
        return nodes

if __name__ == "__main__":
    game_state = State()
    renderer = GameRender(game_state)
    ai = ABPruningAI(game_state)

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        
        if len(game_state.moves) == game_settings.MAX_MOVE_COUNT:
            renderer.render_state(game_state.board, game_settings.NO_ONE, game_settings.NO_ONE, game_state.moves[-1])
            continue

        if game_settings.FIRST_TURN == game_settings.COM and len(game_state.moves) == 0:
            ai_move = ai.next_move()
            renderer.handle_com_move(ai_move, game_state)
            renderer.render_state(game_state.board, game_state.current_turn, State.game_over(game_state.board), game_state.moves[-1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if renderer.is_new_game_button_pressed():
                    game_state = State()
                    ai = ABPruningAI(game_state)
                    renderer.render_state(game_state.board, game_settings.FIRST_TURN, False, (-1,-1))
                
                if State.game_over(game_state.board):
                    continue
                
                if game_state.current_turn == game_settings.HUMAN:
                    renderer.handle_human_move(game_state)
                    renderer.render_state(game_state.board, game_state.current_turn, State.game_over(game_state.board), game_state.moves[-1])
                    ai.state.board = game_state.board

                if State.game_over(game_state.board):
                    continue
                
                if game_state.current_turn == game_settings.COM:
                    ai_move = ai.next_move()
                    renderer.handle_com_move(ai_move, game_state)  
                    renderer.render_state(game_state.board, game_state.current_turn, State.game_over(game_state.board), game_state.moves[-1])

                if State.game_over(game_state.board):
                    continue
