# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import random, time

class Connect4:
    def __init__(self, rows, cols):
        self.board = np.zeros((rows,cols), dtype=int)
        self.rows = rows
        self.cols = cols
    
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

    def check_winner(self):
        checks = []
        for row in range(self.rows):
            for i in range(self.cols-3):
                checks.append(self.board[row, i:i+4])

        for col in range(self.cols):
            for i in range(self.rows-3):
                checks.append(self.board[i:i+4, col])

        for i in range(self.rows-3):
            for j in range(self.cols-3):
                checks.append(self.board[i:i+4].diagonal(j)[:4])
                checks.append(np.fliplr(self.board[i:i+4]).diagonal(j))
                checks.append(np.flipud(self.board[i:i+4]).diagonal(j))
                checks.append(np.flipud(np.fliplr(self.board[i:i+4])).diagonal(j))


        p1_win = [1, 1, 1, 1]
        p2_win = [2, 2, 2, 2]
        for item in checks: 
            if np.array_equal(item, p1_win):
                self.winner = 'Player 1'
                return True
            elif np.array_equal(item, p2_win):
                self.winner = 'Player 2'
                return True
        return False

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
                print('\n')
                player1 = not player1
            else:
                print('Not a valid move. Try again')
            game_over = self.check_winner() 
        print(f"{self.winner} won the game!") 

    def start_game(self):
        #cpu = input('Would you like to play PvP or PvCPU? (enter p or cpu) ').lower().strip()
        tourn = input('Would you like to play a single game or tournament? (enter s or t) ').lower().strip()
        if tourn == 't':
            while True:
                num_game = int(input('How many games would you like the tournament to be out of? ').strip())
                if num_game%2 == 0:
                    even = input('An even number was entered. Is this correct? (y/n) ').lower().strip()
                    if even == 'y':
                        break
                else:
                    break
        else:
            num_game = 1
        print('\n')
        
        while num_game > 0:
            start = input('Would you like to start the game? (y/n) ').lower().strip()
            if start == 'y':
                print('\n')
                self.play_game()
            else:
                time.sleep(5)
                continue
            num_game -= 1

new = Connect4(6,7)
new.start_game()

# %%
