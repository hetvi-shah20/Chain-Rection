class Board:
    '''This class will create a game board to play game'''
    board = list()
    row, column = 10, 8

    def __init__(self):
        for i in range(self.row):
            self.board.append(list())
        for i in range(self.row):
            for j in range(self.column):
                self.board[i].append(0)

    def __str__(self):
        pRows = list()
        for i in range(self.row):
            temp = '| '
            for j in range(self.column):
                temp = temp+ str(self.board[i][j])+' | '
            pRows.append(temp)
        pBoard = '\n'.join(pRows)
        return pBoard
