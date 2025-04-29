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
    if((computer - you)== -1 or (computer - you)== 2):
        print("You lose!")

    else:
        print("You win") 