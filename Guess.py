import random
ournum = random.randint(1,10)
chances = 5
while(chances > 0):
    userchr = int(input("Write the number from 1-10"))
    if userchr == ournum:
        print("You guessed it correctly")
        break
    else:
        print("You are wrong")
        chances = chances-1
        if userchr > ournum:
            print("Your number is greater. Guess a lower one")
        else:
            print("Your Number is lesser. Guess a bigger number")
if chances == 0:
    print("You Lose. The number was",ournum)