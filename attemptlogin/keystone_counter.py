#!/usr/bin/python3

#parse keystone.common.wsgi

loginfail = 0 #counter for fails

#open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

keystone_file_lines=keystone_file.readlines()

for line in keystone_file_lines:
    if "- - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)

keystone_file.close()

