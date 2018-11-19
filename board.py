class Board:
    '''This class will create a game board to play game'''
    board = list()
    row, column = 10, 10

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


    def positive_move(self,row,column):
        if self.board[row][column] >= 0:
            self.board[row][column] += 1
            return self.board[row][column]
        else:
              return 9# for wrong move it will ask for new position


    def negative_move(self,row,column):
        if self.board[row][column] <= 0:  # player 2
            self.board[row][column] -= 1
            return self.board[row][column]
        else:
            return 9


    def find_neighbour(self,row,column):
        neighbours = list()
        if row-1>=0:
            neighbours.append((row-1,column))
        if column-1>=0:
            neighbours.append((row, column-1))
        if row+1<self.row:
            neighbours.append((row+1, column))
        if column+1<self.column:
            neighbours.append((row, column+1))
        return neighbours


    def positive_expand(self, x, y):
        points = list()
        points.append((x,y))
        while len(points) > 0:
            row, column = points[0]
            neighbours = self.find_neighbour(row, column)
            if self.board[row][column] == len(neighbours):
                self.board[row][column] = 0
                for i in neighbours:
                    self.board[i[0]][i[1]] = abs(self.board[i[0]][i[1]])+1

                points.extend(neighbours)
            points.remove((row, column))
        return

    def negative_expand(self, x, y):
        points = list()
        points.append((x, y))
        while len(points) > 0:
            row, column = points[0]
            neighbours = self.find_neighbour(row, column)
            if abs(self.board[row][column]) == len(neighbours):
                self.board[row][column] = 0
                for i in neighbours:
                    self.board[i[0]][i[1]] = (abs(self.board[i[0]][i[1]]) + 1) * -1

                points.extend(neighbours)
            points.remove((row, column))
        return
