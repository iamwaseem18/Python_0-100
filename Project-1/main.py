'''
We are going to create a rock paper scissor game and play with computer

rock = 1
paper = 0
scissor = -1

'''

import random #Asked chatgpt to generate a random number from -1, 0 and 1

computer = random.choice([-1, 0, 1 ])

youstr = input("Enter your choice: ")
youDict = {"r": 1, "p":0, "s":-1}
reverseDict = {1:"Rock", 0:"Paper", -1:"Snake"}


you = youDict[youstr]

#By now we have two numbers, You and Computer

print(f"You chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:

    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lost")

    elif(computer == 1 and you == -1):
        print("You lost")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You lost")

    elif(computer == 0 and you == -1):
        print("You win")

    else:
        print("Something Went wrong")    