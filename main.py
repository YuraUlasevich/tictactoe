from player import Player

firstPlayer = Player("Yura")
secondPlayer = Player("Demid")
turnCount = 0

for i in range(5):
    turnCount += 1
    print("First player turn")
    for j in range(10000):
        print("Enter X ")
        turnX = input()
        print("Enter Y ")
        turnY = input()
        print(firstPlayer.turnCheck(int(turnX), int(turnY)))
        if firstPlayer.turnCheck(int(turnX), int(turnY)) == True:
            break
    firstPlayer.turn(int(turnX), int(turnY), "X")
    if firstPlayer.winFlag == True:
        print("First player won")
        break
    print("Second player turn")
    turnCount += 1
    for j in range(10000):
        print("Enter X ")
        turnX = input()
        print("Enter Y ")
        turnY = input()
        print(secondPlayer.turnCheck(int(turnX), int(turnY)))
        if secondPlayer.turnCheck(int(turnX), int(turnY)) == True:
            break
    secondPlayer.turn(int(turnX), int(turnY), "O")
    if secondPlayer.winFlag == True:
        print("Second player won")
        break
    if turnCount == 9:
        break