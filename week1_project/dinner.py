#!/usr/bin/env python3
"""script to help you choose a place for dinner"""

#import choice from random module
import random

#function to pick from restaurant options
def dine(pick):
    rrs_dict = {
        "american":["stonewood tavern", "five guys", "chicago's best", "new york diner"],
        "mexican":["chiptole", "sabor a mexico", "chicken and taco loco"],
        "chinese":["panda express", "china star", "asian kitchen", "robongi sushi & wok"],
        "italian":["pomodoro pizza & more", "allegria italiana", "olive garden"],
        "indian":["india's grill", "tandoor", "bawarchi indian grill & bar", "naan indian grill"],
        "european":["taste of berlin", "fox & hound british pub", "o'toole's irish pub"],
        "bbq":["mission bbq", "dickey's bbq pit", "bubbaque's", "buffalo wild wings"]
        }
    while True:
        pick=input("What style of food would you like tonight?\n")
        if pick == rrs_dict.key
            print("Good choice.")
            r BBQ:")
            if pick.isalpha():
                break


while True:
    round=round + 1
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer=input("Your guess-->")
    if answer=="Brian":
        print("Correct")
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

#main function
def main():
    
    pick = input("What style of food would you like tonight?\n")

    #run function
    dine(pick)

if __name__ == "__main__":
    main()

