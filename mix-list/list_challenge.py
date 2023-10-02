#!/usr/bin/env python3

#list 1
wordbank= ["indentation", "spaces"] 

#list 2
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

#add integer 4 to list 1
print(wordbank.append(4))

#ask user for number between 0 and 20 store as num
num=int(input("Give me a number between 0 and 20: \n"))

#slice num from list 2
student_name=tlgstudents[num]


#print to screen
print(student_name , "always uses" , wordbank[2] , wordbank[1] , "to indent.")

#print(wordbank)
#print(num)


