#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

from random import choice

# list of coordinates [north, south, east, west]
str_coordinates = [0,0]
cur_coordinates = [0,0]
prev_coordinates = [0,0]


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    #if "item" in rooms[currentRoom]:
    #  print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

# movement function
def movement(direction, cur_coordinates):
    if direction=="north":
        cur_coordinates=cur_coordinates[0]+1
        for room in rooms:
            if rooms[room] == cur_coordinates:
                exist=True
    elif direction=="south":
        cur_coordinates=cur_coordinates[0]-1
        for room in rooms:
            if rooms[room] == cur_coordinates:
                exist=True
    elif direction=="east":
        cur_coordinates=cur_coordinates[1]+1
        for room in rooms:
            if rooms[room] == cur_coordinates:
                exist=True
    elif direction=="west":
        cur_coordinates=cur_coordinates[1]-1
        for room in rooms:
            if rooms[room] == cur_coordinates:
                exist=True
    else:
        print("You died")
        return
    return cur_coordinates
# an inventory, which is initially empty
inventory = []

# types of rooms
room_names=["bedroom", "bathroom", "hallway", "kitchen", "sunroom", "basement", "dungeon"]

# direction dictionary
rooms= {

    "kitchen": [-1,0],

    "living room": [0,-1],

    "hall": [0,0],

    "bedroom": [1,0],

    "bathroom": [0,1],

    "garage": [0,2]

}

#list for movement check
move_check=["north", "south", "east", "west"]


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in move_check:
            pre_coordinates=cur_coordinates
            cur_coordinates=movement(move[1],cur_coordinates)
            for k,v in rooms.items():
                if v == cur_coordinates:
                    currentRoom=k
                    print("You are in the ", k)
            else:    
                print("You have died!")
                exit()

            #set the current room to the new room
        # if they aren't allowed to go that way:
        else:
            print("select from:\n", *move_check)

    #if they type 'get' first
#    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
 #       if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
  #          inventory.append(move[1])
            #display a helpful message
   #         print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
    #        del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
     #   else:
            #tell them they can't get it
      #      print('Can\'t get ' + move[1] + '!')


