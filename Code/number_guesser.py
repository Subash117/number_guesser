#by Subash

from random import randrange
import os
import sys



def returnRandInt(level):
    if(level==1):
        return(randrange(2,10))
    if(level==2):
        return(randrange(2,100))
    if(level==3):
        return(randrange(2,1000))
    if(level==4):
        return(randrange(2,3000))
    if(level==5):
        return(randrange(2,5000))

def nextLevel():
    number=returnRandInt(level)
    return number


print()
print("Welcome to Number Guesser\n")
print('''Level 1: Range 2-10\nLevel 2: Range 2-100\nLevel 3: Range 2-1000
Level 4: Range 2-3000\nLevel 5: Range 2-5000\n''')
i=input("Press Enter to Start (0 to exit) ")
print()

if(i=="0"):
    exit()

level=1
number=returnRandInt(level)
while(True):
    if(level==1):
        print("Level 1: Range 1-10")
    if(level==2):
        print("Level 2: Range 1-100")
    if(level==3):
        print("Level 3: Range 1-1000")
    if(level==4):
        print("Level 4: Range 1-3000")
    if(level==5):
        print("Level 5: Range 1-5000")

    while(True):
        
        check=int(input("Guess Number: (Enter 0 to exit the game or 1 to restart the level) "))
        if(check==1):
            print("\nLevel",level,"restarted\n")
            number=returnRandInt(level)
            continue
        if(check==0):
            exit()
        if(check==number and level!=5):
            print()
            print("Congratulations You win.....moving to next level")
            print()
            break;
        if(check==number and level==5):
            print()
            print("Congratulations You win....Thank You for playing the game")
            print()
            break;
    
        elif(check<number):
            print("Bigger")
    
        else:
            print("Smaller")
            
    level+=1
    if(level>5):
        break
    else:
        number=nextLevel()

n=input("Press Enter to exit....To Play again enter 1")

if(n=="1"):
    os.system("cls")
    os.execv(sys.argv[0], sys.argv)


    
