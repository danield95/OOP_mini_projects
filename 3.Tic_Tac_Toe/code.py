

class TicTacToe():

    def __init__(self, board = ["", "", "", "", "", "", "", "", ""]):
        self.board = board

    def draw(self):
        print(self.board[0] + '|' + self.board[1], "|" + self.board[2])
        print("-"*6)
        print(self.board[3] + '|' + self.board[4], "|" + self.board[5])
        print("-"*6)
        print(self.board[6] + '|' + self.board[7], "|" + self.board[8])

    def playerX(self, position):
        if self.board[position] == "":
            self.board[position] = "X"
            if ((self.board[0]=="X" and self.board[1]=="X" and self.board[2]=="X")
                or (self.board[3]=="X" and self.board[4]=="X" and self.board[5]=="X")
                or (self.board[6]=="X" and self.board[7]=="X" and self.board[8]=="X")):
                TicTacToe.draw(self)
                print("PlayerX WON!")
                self.board = ["", "", "", "", "", "", "", "", ""]
            else:
                TicTacToe.draw(self)
        else:
            print("Error: This position has already been taken! Try something else")
            TicTacToe.draw(self)

    def playerY(self, position):
        if self.board[position] == "":
            self.board[position] = "Y"
            if ((self.board[0]=="Y" and self.board[1]=="Y" and self.board[2]=="Y")
                or (self.board[3]=="Y" and self.board[4]=="Y" and self.board[5]=="Y")
                or (self.board[6]=="Y" and self.board[7]=="Y" and self.board[8]=="Y")):
                TicTacToe.draw(self)
                print("PlayerY WON!")
                self.board = ["", "", "", "", "", "", "", "", ""]
            else:
                TicTacToe.draw(self)

        else:
            print("Error: This position has already been taken! Try something else")
            TicTacToe.draw(self)

g = TicTacToe();
g.playerX(0); g.playerY(1); g.playerX(3); g.playerY(4);g.playerX(6)
