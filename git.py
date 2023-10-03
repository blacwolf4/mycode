#!/usr/env/python3

#This script will sync files to github with user input for project name




name=input("What is the name of this project?\n>")

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

git add *
git commit -m "(name)"
sleep(3)
git push origin HEAD


#print("Hi, ", name.capitalize() , "! Welcome to Day ", mylist[0] , " of " , mylist[5] ," Training!")

#print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")




