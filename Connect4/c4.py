# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import random, time

class Connect4:
    def __init__(self, rows, cols):
        self.board = np.zeros((rows,cols), dtype=int)
        self.rows = rows
    
    def add_chip(self, col, player):
        for idx, row in enumerate(self.board[:, col]):
            if row == 0:
                self.board[idx][col] = player
                break
        return self.board
    
    def valid_input(self, col):
        if not isinstance(col, int) or col > self.rows or col < 0:
            return False
        elif not np.any(self.board[:, col]==0):
            return False
        else:
            return True

    '''def winner(self):
        p1_win = np.array([1, 1, 1, 1])
        p2_win = np.array([2, 2, 2, 2])
        sub_arrs = [board[i:i+4] for i in range(len(board)-3)]
        return np.isin(p1_win, board)'''

    def play_game(self):
        game_over = False
        player1 = random.choice((True, False))
        while not game_over:
            if player1:
                player = 1
            else:
                player = 2
            
            print(f"It is Player {player}'s turn to play")
            inp = int(input('Which column would you like to play? (enter 0-6) '))
            
            if self.valid_input(inp):
                self.board = self.add_chip(inp, player)
                print(self.board[::-1])
                player1 = not player1
            else:
                print('Not a valid move. Try again')  

    def start_game(self):
        #cpu = input('Would you like to play PvP or PvCPU? (enter p or cpu) ').lower().strip()
        tourn = input('Would you like to play a single game or tournament? (enter s or t) ').lower().strip()
        if tourn == 't':
            num_game = input('How many games would you like the tournament to be out of? ').lower().strip()
        else:
            num_game = 1
        while num_game > 0:
            start = input('Would you like to start the game? (y/n) ').lower().strip()
            if start == 'y':
                self.play_game()
            else:
                time.sleep(5)
                continue
            num_game -= 1

new = Connect4(6,7)
new.start_game()

# %%
