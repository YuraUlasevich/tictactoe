from __future__ import print_function


class Player():
    def __init__(self, name):
        self.playerName = name
        self.winFlag = False
        Player.a= [["/", "/", "/"], 
                   ["/", "/", "/"], 
                   ["/", "/", "/"]]
        
    def turn(self, pozitionX, pozitionY, symbol):
        self.positionX = pozitionX
        self.positionY = pozitionY
        if symbol == "O":
            Player.a[self.positionX-1][self.positionY-1] = "O"
        else:
            Player.a[self.positionX-1][self.positionY-1] = "X"
        self.displayDeck()
        self.winCheck()

    def turnCheck(self, turnX, turnY):
        if turnX>0 and turnX<4:
            if Player.a[turnX-1][turnY-1] == "/":
                return True
            else:
                return False
        else:
            return False

    def displayDeck(self):
        for i in range(len(Player.a)):
            for j in range(len(Player.a[i])):
                print(Player.a[i][j], end=' ')
            print()
        print()

    def winCheck(self):
        # Diagonal
        if Player.a[0][0] == Player.a[1][1] and Player.a[1][1] == Player.a[2][2] and Player.a[2][2] != "/":
            self.winFlag = True
        elif Player.a[0][2] == Player.a[1][1] and Player.a[1][1] == Player.a[2][0] and Player.a[2][0] != "/":
            self.winFlag = True
        # Gorizontal
        elif Player.a[0][0] == Player.a[0][1] and Player.a[0][1] == Player.a[0][2] and Player.a[0][2] != "/":
            self.winFlag = True
        elif Player.a[1][0] == Player.a[1][1] and Player.a[1][1] == Player.a[1][2] and Player.a[1][2] != "/":
            self.winFlag = True
        elif Player.a[2][0] == Player.a[2][1] and Player.a[2][1] == Player.a[2][2] and Player.a[2][2] != "/":
            self.winFlag = True
        # Vertical
        elif Player.a[0][0] == Player.a[1][0] and Player.a[1][0] == Player.a[2][0] and Player.a[2][0] != "/":
            self.winFlag = True
        elif Player.a[0][1] == Player.a[1][1] and Player.a[1][1] == Player.a[2][1] and Player.a[2][1] != "/":
            self.winFlag = True
        elif Player.a[0][2] == Player.a[1][2] and Player.a[1][2] == Player.a[2][2] and Player.a[2][2] != "/":
            self.winFlag = True