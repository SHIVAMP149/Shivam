
# Importing random module......
import random


# 
def user():
    a = input("ENTER THE NUMBER YOU WANT TO START FROM : ")
    a = int(a)
    if a == str(a):
        print(" PLEASE ENTER A DIGIT ")
        quit()
    b = input("ENTER THE NUMBER YOU WANT TO END FROM : ")
    b = int(b)
    if b == str(b):
        print(" PLEASE ENTER THE DIGIT ")
        quit()
    number = random.randrange(a,b)
    print("RANGE IS [",a,"",b,"]")
    print("RANDOMLY GENERATED NUMBER IS :",number)
    print("-----PROPERTIES FOLLOWED BY THIS NUMBER-----")

    if number%2==0:
        print("RANDOMLY GENERATED NUMBER IS AN EVEN NUMBER :",number)
    else:
        print("RANDOMLY GENERATED NUMBER IS A ODD NUMBER :",number)


    if number >= 0:
        print("RANDOMLY GENERATED NUMBER IS A POSITIVE NUMBER :",number)
    else:
        print("RANDOMLY GENERATED NUMBER IS A NEGATIVE NUMBER :",number)

    if number == 1 or number == 0:
        print("RANDOMLY GENERATED NUMBER IS NEITHER A COMPOSITE NUMBER NOR A PRIME NUMBER :",number)
    elif number == 2 :
        print("RANDOMLY GENERATED NUMBER IS PRIME NUMBER :",number)
    else:
        for factor in range(2,(number//2)+1):
            if (number % factor) == 0:
                print("RANDOMLY GENERATED NUMBER IS COMPOSITE NUMBER :",number)
                break
        else:
            print("RANDOMLY GENERATED NUMBER IS A PRIME NUMBER :",number)
        

user()