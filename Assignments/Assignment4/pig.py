#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 4 - Pig

#The game of Pig is a simple two-player dice game in which the first player to reach 100 or more points wins.  Players take turns.  On each turn a player rolls a six-sided die.  After each roll:
#a) If the player rolls a 1 then the player gets no new points and it becomes the other player’s turn.
#b) If the player rolls 2-6 then they can either roll again or hold.  If the player holds the sum of all rolls is added to his/her score and the turn passes to the other player.
#Write a program that plays the game of Pig where one player is human and the other is the computer.  When it is the human’s turn the program should show the score of both players and the previous roll.
#Allow the human to input “r” for roll again and “h” for hold.  (Hint: use the input function).
#When it is the computer’s turn you need not do any prompting.  Simply keep rolling until the computer has earned 20 or more points and then hold.
#If the computer rolls a 1 at any time, then the turn is lost and no points are added to the score.  If at any point the computer has enough points to win the game, then the computer holds and the game ends.
#Allow the human player to roll first.  A random roll can be simulated with a call to random.randint(1,6) which generates a uniform random number in [1,6].  Make sure to import the random module (ie. import random).

#Import Random Library for Dice Roll
import random

#Declare Variables
playerSum = 0       #Keep Track of Player Sum
computerSum = 0     #Keep Track of Computer Sum for a given round
compTotalSum = 0    #Keep Track of Total Computer Sum

playerTurn = True   #Keep Track of Player Turn or Computer Turn
dice = 0            #Keep Track of Dice Value

playerChoice = ""   #Keep Track of Player Input

#If the Player Wins, call playerWin()
def playerWin():
    print("*********************\nDr. Phil: Congratulations on winning, I knew you could do it")
#If the Computer Wins, call computerWin()
def computerWin():
    print("*********************\nDr. Phil: Congratulations on win- wait... the computer won??\nI knew you couldn't win... :(")

#Opening Message
print("**** WELCOME TO THE GAME OF PIG *****\n\nDr. Phil: I'm your host, Dr. Phil!\nDr. Phil: You ready for a good game? Well let's roll!")
#Set loop to go between Player and Computer until Game is Won
while True:
    if playerTurn == True:
        #Prompt Player for Input
        playerChoice = input("*********************\nWill you Roll (r) or Hold (h)? ")
        #If Input is Roll
        if playerChoice == "r":
            #Roll the Dice Using Random
            dice = random.randint(1, 6)
            print("You Rolled a ", dice)

            #If Dice == 1, End Player Turn
            if dice == 1:
                print("Dr. Phil: Darn, you Rolled a 1. Send him to THE RANCH")
                playerTurn = False
            #If Dice is between 2 & 6, Add Dice Roll to Player Sum
            else:
                playerSum = playerSum + dice
                print("Your Score is now ", playerSum)

                #If Player Sum is Greater Than or Equal to 100, Call playerWin() and Break the While Loop to End the Game
                if playerSum >= 100:
                    playerWin()
                    break
                continue
        #If Input is Hold
        elif playerChoice == "h":
            playerTurn = False
            #If Player Sum is Greater Than or Equal to 100, Call playerWin() and Break the While Loop to End the Game
            if playerSum >= 100:
                playerWin()
            #Else, Print Total Score for Player
            else:
                print("Dr. Phil: Holding with a ", playerSum, " smart move kid")
        #If Input is not Roll or Hold
        else:
            print("Dr. Phil: Come on... Please Enter a Valid Option")
            continue
    #If playerTurn is False, it is the Computers Turn
    elif playerTurn == False:
        #If Computer Sum for this given round is less than 20, Roll Dice
        if computerSum <= 20:
            dice = random.randint(1, 6)
            #If Dice == 1, End Computer Turn
            if dice == 1:
                playerTurn = True
                computerSum = 0
                print("*********************\nDr. Phil: Looks like the Computer rolled a 1")
            #Else, if Dice is between 2 & 6 add Dice to Computer Sum
            else:
                computerSum = computerSum + dice
                continue
        #If Computer Sum is Greater than or Equal To 20
        else:
            #Add Computer Sum to Total Computer Sum
            compTotalSum = compTotalSum + computerSum
            #Reset Computer Sum
            computerSum = 0
            #f Total Computer Sum is Greater Than or Equal to 100, Call computerWin() and Break the While Loop to End the Game
            if compTotalSum >= 100:
                computerWin()
                break

            #Print Total Score for Computer
            print("*********************\nDr. Phil: The Computer has ", compTotalSum)
            #Set playerTurn to True for the Player to go
            playerTurn = True
