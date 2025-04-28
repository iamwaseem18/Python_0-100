# The game() function in a program lets a user play a game returns the score as an integer . You need to read a file 'Hi- Score.txt' which is either blank or contains 
# the previous hi score. You need to write a program to update the hi score whenevr the game() functions breaks the hi score.

import random

def game():
    print("You are playing the game...")
    score = random.randint(1,100)

    #Fetch the hi score

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)

        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
    #Now update the high score in the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))


    return score


game()