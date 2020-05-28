import numpy as np
import random, time

class Connect4:
    def __init__(self, rows, cols, win_len):
        self.board = np.zeros((rows,cols), dtype=int)
        self.rows = rows
        self.cols = cols
        self.win_len = win_len
        self.p1_wins = 0
        self.p2_wins = 0
    
    def clear_board(self):
        self.board = np.zeros((self.rows,self.cols), dtype=int)
        print('Clearing the board')
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
            for i in range(self.cols-(self.win_len-1)):
                checks.append(self.board[row, i:i+self.win_len])

        for col in range(self.cols):
            for i in range(self.rows-(self.win_len-1)):
                checks.append(self.board[i:i+self.win_len, col])

        for i in range(self.rows-(self.win_len-1)):
            for j in range(self.cols-(self.win_len-1)):
                checks.append(self.board[i:i+self.win_len].diagonal(j)[:self.win_len])
                checks.append(np.fliplr(self.board[i:i+self.win_len]).diagonal(j))
                checks.append(np.flipud(self.board[i:i+self.win_len]).diagonal(j))
                checks.append(np.flipud(np.fliplr(self.board[i:i+self.win_len])).diagonal(j))


        p1_win = [1] * self.win_len
        p2_win = [2] * self.win_len
        for item in checks: 
            if np.array_equal(item, p1_win):
                self.winner = 'Player 1'
                self.p1_wins += 1
                return True
            elif np.array_equal(item, p2_win):
                self.winner = 'Player 2'
                self.p2_wins += 1
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
            inp = int(input(f'Which column would you like to play? (enter 0-{self.cols-1}) '))
            
            if self.valid_input(inp):
                self.board = self.add_chip(inp, player)
                print(self.board[::-1])
                print('\n')
                player1 = not player1
            else:
                print('Not a valid move. Try again')
            game_over = self.check_winner() 
        print(f"{self.winner} won the game!")
        self.clear_board()

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
            if self.p1_wins > num_game:
                return print('Player 1 won the tournament!')
            if self.p2_wins > num_game:
                return print('Player 2 won the tournament!')

            start = input('Would you like to start the game? (y/n) ').lower().strip()
            if start == 'y':
                print('\n')
                self.play_game()
            else:
                time.sleep(5)
                continue
            num_game -= 1

new = Connect4(6, 7, 4)
new.start_game()