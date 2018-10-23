# This problem was asked by Salesforce.
# Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically 
# suspended grid. The game ends either when one player creates a line of four consecutive discs of 
# their color (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.
# Design and implement Connect 4.
####
class pieces:
    RED = 'R'
    YELLOW = 'Y'
    BLANK = ' '

class ConnectX:
    def verify_win(self, x, y):
        b = self.board
        m = self.m
        n = self.n
        X = self.X
        # traverse horizontal
        i = 1
        ctr = 1
        while y-i >= 0 and b[x][y-i] == b[x][y]:
            i += 1
            ctr += 1
        i = 1
        while y+i < m and b[x][y+i] == b[x][y]:
            i += 1
            ctr += 1
        if ctr >= X:
            return 1
        # traverse vertical
        i = 1
        ctr = 1
        while x-i >= 0 and b[x-i][y] == b[x][y]:
            i += 1
            ctr += 1
        if ctr == X:
            return 1
        # traverse diagonal 1
        i = 1
        ctr = 1
        while x-i >= 0 and y-i >= 0 and b[x-i][y-i] == b[x][y]:
            i += 1
            ctr += 1
        i = 1
        while x+i < m and y+i < n and b[x+i][y+i] == b[x][y]:
            i += 1
            ctr += 1
        if ctr >= X:
            return 1
        # traverse diagonal 2
        i = 1
        ctr = 1
        while x-i >= 0 and y+i < n and b[x-i][y+i] == b[x][y]:
            i += 1
            ctr += 1
        i = 1
        while x+i < m and y-i >= 0 and b[x+i][y-i] == b[x][y]:
            i += 1
            ctr += 1
        if ctr >= X:
            return 1
        # None were formed
        return 0

    def place_piece(self, col, piece = pieces.RED):
        if col < 0 or col >= self.m or self.won:
            return 0
        if self.lowest[col] == self.n:
            return 0
        self.board[self.lowest[col]][col] = piece

        if self.verify_win(self.lowest[col], col):
            self.won = True
            return -1

        self.lowest[col] += 1
        return 1
        
    def print_board(self):
        tmp = '|'
        for i in range(self.n):
            tmp += '{}|'.format(i)
        print(tmp)
        for i in range(self.m-1, -1, -1):
            print('|{}|'.format('|'.join(self.board[i])))

    def __init__(self, m = 6, n = 7, X = 4):
        self.won = False
        self.board = [[pieces.BLANK]*n for _ in range(m)]
        self.lowest = [0]*m
        self.m = m
        self.n = n
        self.X = X
####

c4 = ConnectX()
c4.place_piece(1, pieces.YELLOW)
c4.place_piece(2, pieces.RED)
c4.place_piece(2, pieces.YELLOW)
c4.place_piece(3, pieces.RED)
c4.place_piece(3, pieces.RED)
c4.place_piece(3, pieces.YELLOW)
c4.place_piece(4, pieces.RED)
c4.place_piece(4, pieces.RED)
c4.place_piece(4, pieces.RED)
c4.place_piece(4, pieces.YELLOW)
c4.print_board()
print(c4.won)