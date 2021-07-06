rowOne = [" ", " ", " "]
rowTwo = [" ", " ", " "]
rowThree = [" ", " ", " "]


def placingInBoardP1(desiredSpot):

    if (desiredSpot == "a1" or desiredSpot == "A1") and rowOne[0] == " ":
        rowOne[0] = "X"
    elif (desiredSpot == "a2" or desiredSpot == "A2") and rowOne[1] == " ":
        rowOne[1] = "X"
    elif (desiredSpot == "a3" or desiredSpot == "A3") and rowOne[2] == " ":
        rowOne[2] = "X"

    elif (desiredSpot == "b1" or desiredSpot == "B1") and rowTwo[0] == " ":
        rowTwo[0] = "X"
    elif (desiredSpot == "b2" or desiredSpot == "B2") and rowTwo[1] == " ":
        rowTwo[1] = "X"
    elif (desiredSpot == "b3" or desiredSpot == "B3") and rowTwo[2] == " ":
        rowTwo[2] = "X"

    elif (desiredSpot == "c1" or desiredSpot == "C1") and rowThree[0] == " ":
        rowThree[0] = "X"
    elif (desiredSpot == "c2" or desiredSpot == "C2") and rowThree[1] == " ":
        rowThree[1] = "X"
    elif (desiredSpot == "c3" or desiredSpot == "C3") and rowThree[2] == " ":
        rowThree[2] = "X"
    else:
        return False

    return True


def placingInBoardP2(desiredSpot):
    if (desiredSpot == "a1" or desiredSpot == "A1") and rowOne[0] == " ":
        rowOne[0] = "O"
    elif (desiredSpot == "a2" or desiredSpot == "A2") and rowOne[1] == " ":
        rowOne[1] = "O"
    elif (desiredSpot == "a3" or desiredSpot == "A3") and rowOne[2] == " ":
        rowOne[2] = "O"

    elif (desiredSpot == "b1" or desiredSpot == "B1") and rowTwo[0] == " ":
        rowTwo[0] = "O"
    elif (desiredSpot == "b2" or desiredSpot == "B2") and rowTwo[1] == " ":
        rowTwo[1] = "O"
    elif (desiredSpot == "b3" or desiredSpot == "B3") and rowTwo[2] == " ":
        rowTwo[2] = "O"

    elif (desiredSpot == "c1" or desiredSpot == "C1") and rowThree[0] == " ":
        rowThree[0] = "O"
    elif (desiredSpot == "c2" or desiredSpot == "C2") and rowThree[1] == " ":
        rowThree[1] = "O"
    elif (desiredSpot == "c3" or desiredSpot == "C3") and rowThree[2] == " ":
        rowThree[2] = "O"

    else:
        return False

    return True


def gameBoard():
    print("   1   2   3")
    print(" A "+ rowOne[0] + " | " + rowOne[1] + " | " + rowOne[2])
    print("   ---------")
    print(" B "+rowTwo[0] + " | " + rowTwo[1] + " | " + rowTwo[2])
    print("   ---------")
    print(" C "+rowThree[0] + " | " + rowThree[1] + " | " + rowThree[2])


def winConP1():
    # If  all horizontals are win conditions
    if rowOne[0] == "X" and rowOne[0] == rowOne[1] and rowOne[1] == rowOne[2]:
        return True
    elif rowTwo[0] == "X" and rowTwo[0] == rowTwo[1] and rowTwo[1] == rowTwo[2]:
        return True
    elif rowThree[0] == "X" and rowThree[0] == rowThree[1] and rowThree[1] == rowThree[2]:
        return True
    # If all verticals are win conditions
    elif rowOne[0] == "X" and rowOne[0] == rowTwo[0] and rowTwo[0] == rowThree[0]:
        return True
    elif rowOne[1] == "X" and rowOne[1] == rowTwo[1] and rowTwo[1] == rowThree[1]:
        return True
    elif rowOne[2] == "X" and rowOne[2] == rowTwo[2] and rowTwo[2] == rowThree[2]:
        return True
    # If all diagonals are win conditions
    elif rowOne[0] == "X" and rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
        return True
    elif rowOne[2] == "X" and rowOne[2] == rowTwo[1] and rowTwo[1] == rowThree[0]:
        return True
    else:
        return False

def winConP2():
    # If  all horizontals are win conditions
    if rowOne[0] == "O" and rowOne[0] == rowOne[1] and rowOne[1] == rowOne[2]:
        return True
    elif rowTwo[0] == "O" and rowTwo[0] == rowTwo[1] and rowTwo[1] == rowTwo[2]:
        return True
    elif rowThree[0] == "O" and rowThree[0] == rowThree[1] and rowThree[1] == rowThree[2]:
        return True
    # If all verticals are win conditions
    elif rowOne[0] == "O" and rowOne[0] == rowTwo[0] and rowTwo[0] == rowThree[0]:
        return True
    elif rowOne[1] == "O" and rowOne[1] == rowTwo[1] and rowTwo[1] == rowThree[1]:
        return True
    elif rowOne[2] == "O" and rowOne[2] == rowTwo[2] and rowTwo[2] == rowThree[2]:
        return True
    # If all diagonals are win conditions
    elif rowOne[0] == "O" and rowOne[0] == rowTwo[1] and rowTwo[1] == rowThree[2]:
        return True
    elif rowOne[2] == "O" and rowOne[2] == rowTwo[1] and rowTwo[1] == rowThree[0]:
        return True
    else:
        return False

def checkHorizontals():
    #6 conditions
    pass
def checkVerticals():
    #6 conditions
    pass
def checkDiagonals():
    #4 conditions
    pass
def preventTrap():
    pass
def randomPlacement():
    pass


def botMove():

    if checkHorizontals() == False:
        if checkVerticals() == False:
            if checkDiagonals() == False:
                if preventTrap() == False:
                    randomPlacement()



def winMsgP1():
    print("Player 1 has won")
    print("")
    print("Here is the game board")
    gameBoard()
    exit()


def winMsgP2():
    print("Player 2 has won")
    print("")
    print("Here is the game board")
    gameBoard()
    exit()


def winMsgBot():
    print("The bot has won.  You are garbage.")
    print("")
    print("Here is the game board")
    gameBoard()
    exit()


def tieMsg():
    print("There is no winner, the game has ended in a tie")
    print("")
    print("Here is the game board")
    gameBoard()
    exit()


def personGame():
    turnCount = 0
    while True:

        gameBoard()
        while True:
            print("Player one, choose a spot.")
            desiredSpot = input()

            if (placingInBoardP1(desiredSpot)):
                turnCount = turnCount + 1
                break
            else:
                print("That is not a valid spot.  Please choose another spot")
                continue

        if winConP1():
            winMsgP1()
        if turnCount == 9:
            tieMsg()

        gameBoard()
        while True:
            print("Player 2, choose a spot.")
            desiredSpot = input()

            if (placingInBoardP2(desiredSpot)):
                turnCount = turnCount + 1
                break
            else:
                print("That is not a valid spot.  Please choose another spot")
                continue

        if winConP2():
            winMsgP2()
        if turnCount == 9:
            tieMsg()


def botGame():

    gameBoard()
    while True:
        print("Player one, choose a spot.")
        desiredSpot = input()
        if (placingInBoardP1(desiredSpot)):
            turnCount = turnCount + 1
            break
        else:
            print("That is not a valid spot.  Please choose another spot")
            continue

    if winConP1():
        winMsgP1()
    if turnCount == 10:
        tieMsg()

    gameBoard()
    botMove()

    if winConP2():
        winMsgBot()
    if turnCount == 10:
        tieMsg()



print("Do you want to face another person or a robot? Write P for person or B for bot.")
choice = input()
while True:
    if choice == "P":
        personGame()
    elif choice == "B":
        botGame()
    else:
        continue

# Made from 3:45 to 4:31  Done in 46 minutes

