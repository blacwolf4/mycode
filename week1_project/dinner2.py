#!/usr/bin/env python3
"""script to help you choose a place for dinner"""

#import modules
import random
import crayons

#main function
def main():
    rrs=input("What style of food do you want tonight? (American, Mexican, Chinese, Italian, Indian, European, BBQ):\n")

    rrs_dict = {
    "American":["Stonewood Tavern", "Five Guys", "Chicago's Best", "New York Diner"],
    "Mexican":["Chiptole", "Sabor a Mexico", "Chicken and Taco Loco"],
    "Chinese":["Panda Express", "China Star", "Asian Kitchen", "Robongi Sushi & Wok"],
    "Italian":["Pomodoro Pizza & More", "Allegria Italiana", "Olive Garden"],
    "Indian":["India's Grill", "Tandoor", "Bawarchi Indian Grill & Bar", "Naan Indian Grill"],
    "European":["Taste of Berlin", "Fox & Hound British Pub", "O'Toole's Irish Pub"],
    "BBQ":["Mission BBQ", "Dickey's BBQ Pit", "BubbaQue's", "Buffalo Wild Wings"]
    }

    option=random.choice(rrs_dict[rrs])
    print(f"I would suggest going to {crayons.green(option)}")

if __name__ == "__main__":

   main()
