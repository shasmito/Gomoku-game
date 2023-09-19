import pygame
from time import sleep

from state import State
import Settings.rendersettings as render_settings
import Settings.gamesettings as game_settings

class GameRender:
    def __init__(self, state: State):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((render_settings.WINDOW_WIDTH, render_settings.WINDOW_HEIGHT))
        pygame.display.set_caption(render_settings.WINDOW_TITLE)
        self.screen.fill(render_settings.BOARD_COLOR)
        if (len(state.moves) > 0):
            self.render_state(state.board, game_settings.FIRST_TURN, False, state.moves[-1])
        else:
            self.render_state(state.board, game_settings.FIRST_TURN, False, (-1,-1))
        pygame.display.update()

    
    def render_state(self, board, current_turn, player_win, last_move):
        """
        It renders board state and displays that board state
        
        :param board: the current state of the board
        :param current_turn: The current turn of the game
        :param player_win: The player who won the game
        :return: The return value of the function is the value of the last expression evaluated.
        """
        self.clear()

        # COM WIN
        if(player_win == game_settings.COM):
            self.draw_board(board, render_settings.COM_WIN_INFO_TEXT, render_settings.COLOR_DARK_GREEN, last_move, render_settings.get_last_move_color(player_win))
            return
        # HUMAN WIN
        if(player_win == game_settings.HUMAN):
            self.draw_board(board, render_settings.HUMAN_WIN_INFO_TEXT, render_settings.COLOR_DARK_GREEN, last_move, render_settings.get_last_move_color(player_win))
            return
        if(player_win == game_settings.NO_ONE):
            last_turn = game_settings.get_opponent(current_turn)
            # DRAW
            if(current_turn == game_settings.NO_ONE):
                self.draw_board(board, render_settings.DRAW_INFO_TEXT, render_settings.COLOR_DARK_GREEN, last_move, render_settings.get_last_move_color(last_turn))
                return
            # GAME IS NOT OVER YET. HUMAN TURN
            if(current_turn == game_settings.HUMAN):
                self.draw_board(board, render_settings.HUMAN_TURN_INFO_TEXT, render_settings.COLOR_RED, last_move, render_settings.get_last_move_color(last_turn))
                return
            # GAME IS NOT OVER YET. COM TURN
            if(current_turn == game_settings.COM):
                self.draw_board(board, render_settings.COM_TURN_INFO_TEXT, render_settings.COLOR_BLUE, last_move, render_settings.get_last_move_color(last_turn))
                return

    def draw_X(self, x, y, color):
        """
        Draw an X on the screen at the given coordinates
        
        :param x: the x coordinate of the cell
        :param y: 0-2
        """
        #    x
        # y ╔═════════════════════════════════▶
        #   ║ (X1, Y1) ╔═══╗ (X2, Y1)
        #   ║          ║   ║
        #   ▼ (X1, Y2) ╚═══╝ (X2, Y2)
        #
        # line 1: (X1, Y1) -> (X2, Y2)
        # line 2: (X1, Y2) -> (X2, Y1)

        

        posX = render_settings.BOARD_POS_X_MIN + render_settings.SQUARE_SIZE/2 + y * render_settings.SQUARE_SIZE + render_settings.O_LINE_THICKNESS/2
        posY = render_settings.BOARD_POS_Y_MIN + render_settings.SQUARE_SIZE/2 + x * render_settings.SQUARE_SIZE + render_settings.O_LINE_THICKNESS/2
        # subtract cell border
        radius = render_settings.O_RADIUS - render_settings.O_CELL_BORDER
        # draw circle
        pygame.draw.circle(self.screen, color, [posX, posY], radius , render_settings.O_LINE_THICKNESS)
        
    def draw_O(self, x, y, color):
        """
        Draw a circle with a radius of O_RADIUS - O_CELL_BORDER at the center of the square at position
        (x,y) on the board.
        
        :param x: the x coordinate of the board
        :param y: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29,
        """
        posX = render_settings.BOARD_POS_X_MIN + render_settings.SQUARE_SIZE/2 + y * render_settings.SQUARE_SIZE + render_settings.O_LINE_THICKNESS/2
        posY = render_settings.BOARD_POS_Y_MIN + render_settings.SQUARE_SIZE/2 + x * render_settings.SQUARE_SIZE + render_settings.O_LINE_THICKNESS/2
        # subtract cell border
        radius = render_settings.O_RADIUS - render_settings.O_CELL_BORDER
        # draw circle
        pygame.draw.circle(self.screen, color, [posX, posY], radius , render_settings.O_LINE_THICKNESS)
    
    def draw_button(self, pos, width, height, text):
        """
        It draws a button on the screen with the given text, width, height, and position.
        
        :param pos: (x, y)
        :param width: width of the button
        :param height: the height of the button
        :param text: The text that will be displayed on the button
        """
        rectButton = pygame.Rect(pos, (width, height))
        font_text = pygame.font.Font(pygame.font.get_default_font(), render_settings.BUTTON_TEXT_FONT_SIZE)
        text_surf = font_text.render(text, True, render_settings.BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center = rectButton.center)
        pygame.draw.rect(self.screen, render_settings.BUTTON_COLOR, rectButton)
        self.screen.blit(text_surf, text_rect)

    def draw_info_text(self, text, textColor):
        """
        It draws text to the screen
        
        :param text: the text to be displayed
        :param textColor: (255, 255, 255)
        """
        text_pos = (render_settings.WINDOW_WIDTH/2, render_settings.BORDER_SIZE + render_settings.INFO_TEXT_FONT_SIZE/2)

        font_text = pygame.font.Font(pygame.font.get_default_font(), render_settings.INFO_TEXT_FONT_SIZE)
        text_surf = font_text.render(text, False, textColor)
        text_rect = text_surf.get_rect(center = text_pos)
        self.screen.blit(text_surf, text_rect)
        pygame.display.update()

    
    def draw_board(self, board_state, info_text, info_text_color, last_move, last_move_color):
        """
        It draws the board, the info text, the new game button, and the moves on the board.
        
        :param board_state: the current state of the board
        :param infoText: The text to be displayed on the screen
        :param infoTextColor: The color of the text
        """
        # draw board
        # draw vertical line
        for r in range (0, game_settings.BOARD_COL_COUNT + 1):
            
            pygame.draw.line(self.screen, render_settings.COLOR_BLACK, 
            [render_settings.BOARD_POS_X_MIN + render_settings.SQUARE_SIZE * r, render_settings.BOARD_POS_Y_MIN], [render_settings.BOARD_POS_X_MIN + render_settings.SQUARE_SIZE * r, render_settings.BOARD_POS_Y_MIN + render_settings.BOARD_HEIGHT], render_settings.BOARD_LINE_WIDTH)
        # draw horizontal line
        for r in range (0, game_settings.BOARD_ROW_COUNT + 1):
            pygame.draw.line(self.screen, render_settings.COLOR_BLACK,
            [render_settings.BOARD_POS_X_MIN, render_settings.BOARD_POS_Y_MIN + render_settings.SQUARE_SIZE * r], [render_settings.BOARD_POS_X_MIN + render_settings.BOARD_WIDTH, render_settings.BOARD_POS_Y_MIN + render_settings.SQUARE_SIZE * r], render_settings.BOARD_LINE_WIDTH)
        
        # draw INFO TEXT
        self.draw_info_text(info_text, info_text_color)

        # draw NEW GAME button
        self.draw_button(render_settings.NEW_GAME_BUTTON_POS, render_settings.BUTTON_WIDTH, render_settings.BUTTON_HEIGHT, "NEW GAME")

        # render board moves
        last_move_r, last_move_c = last_move
        for r in range (0, game_settings.BOARD_ROW_COUNT):
            for c in range (0, game_settings.BOARD_COL_COUNT):
                # set color
                color = None
                if (r == last_move_r and c == last_move_c):
                    color = last_move_color
                else:
                    if board_state[r][c] == game_settings.O: 
                        color = render_settings.O_COLOR
                    elif board_state[r][c] == game_settings.X: 
                        color = render_settings.X_COLOR
                # Empty cell
                if board_state[r][c] == game_settings.EMPTY: 
                    continue
                # Human move
                if board_state[r][c] == game_settings.O: 
                    self.draw_O(r, c, color)
                # COM move
                if board_state[r][c] == game_settings.X: 
                    self.draw_X(r, c, color)
        pygame.display.update()

        # Announcement
        print("Drawing board is completed.")
        print("==================================================================")
    
    #COM moves
    def handle_com_move(self, com_move, state: State):
        """
        The function takes in a move from the AI and updates the state of the game
        
        :param com_move: the move the AI made
        :param state: the current state of the game
        :type state: State
        :return: the move of the computer.
        """

        # Announcement
        print("AI move: (row:", com_move[0], ", column:", com_move[1], ").")

        state.update_move(game_settings.COM, com_move)
        return

    #HUMAN moves
    def is_new_game_button_pressed(self):
        """
        If the mouse button is pressed, and the mouse is in the button area, return True. Otherwise,
        return False
        :return: The return value is a boolean.
        """
        mouse_button_pressed = pygame.mouse.get_pressed()
        if mouse_button_pressed[0]:
            mouse_position = pygame.mouse.get_pos()
            mouse_x_position, mouse_y_position = mouse_position
            is_in_x_button_area = render_settings.NEW_GAME_BUTTON_POS_X_MIN < mouse_x_position < render_settings.NEW_GAME_BUTTON_POS_X_MAX
            is_in_y_button_area = render_settings.NEW_GAME_BUTTON_POS_Y_MIN < mouse_y_position < render_settings.NEW_GAME_BUTTON_POS_Y_MAX
            return is_in_x_button_area and is_in_y_button_area
        return False
        
    def is_new_move_valid(self, mouse_position, state: State):
        """
        If the mouse position is in the board area, and the selected square is empty, then the move is
        valid
        
        :param mouse_position: The position of the mouse on the screen
        :param state: State
        :type state: State
        :return: The function is_new_move_valid() returns a boolean value.
        """
        if (self.is_mouse_position_in_board_area(mouse_position)):
            square_x_position, square_y_position =  self.get_board_square_position(mouse_position)
            is_selected_square_empty = state.board[square_x_position][square_y_position] == game_settings.EMPTY
            return is_selected_square_empty
        else:
            return False

    def is_mouse_position_in_board_area(self, mouse_position):
        """
        It checks if the mouse position is within the board area
        
        :param mouse_position: (x, y)
        :return: The return value is a boolean.
        """
        mouse_x_position, mouse_y_position = mouse_position
        is_mouse_x_position_valid = render_settings.BOARD_POS_X_MIN < mouse_x_position < render_settings.BOARD_POS_X_MAX
        is_mouse_y_position_valid = render_settings.BOARD_POS_Y_MIN < mouse_y_position < render_settings.BOARD_POS_Y_MAX
        return is_mouse_x_position_valid and is_mouse_y_position_valid

    def get_board_square_position(self, mouse_position):
        """
        The boardsquare's x, y position is inverse to the mouse positions'.
        
        :param mouse_position: (x, y)
        :return: The board_square_x_position and board_square_y_position are being returned.
        """
        mouse_x_position, mouse_y_position = mouse_position
        #The boardsquare's x, y position is inverse to the mouse positions'. 
        board_square_y_position = int((mouse_x_position - render_settings.BOARD_POS_X_MIN) / render_settings.SQUARE_SIZE)
        board_square_x_position = int((mouse_y_position - render_settings.BOARD_POS_Y_MIN) / render_settings.SQUARE_SIZE)
        return (board_square_x_position, board_square_y_position)
    
    def clear(self):
        """
        It clears the screen and updates the display
        """
        self.screen.fill(render_settings.BOARD_COLOR)
        pygame.display.update()

    def handle_human_move(self, state: State):
        """
        It takes human's mouse left click position and checks if it's a valid move. If it is, it updates the state with
        the move
        
        :param state: State
        :type state: State
        :return: the position of the square that the human player clicked on.
        """
        mouse_button_pressed = pygame.mouse.get_pressed()
        # mouse left click
        if mouse_button_pressed[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.is_new_move_valid(mouse_position, state):
                human_move = self.get_board_square_position(mouse_position)

                # Announcement
                print("HUMAN move: (row:", human_move[0], ", column:", human_move[1], ").")
                
                state.update_move(game_settings.HUMAN, human_move)
                return
        return