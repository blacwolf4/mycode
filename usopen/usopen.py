#!/usr/bin/env python3

## US Open Tournament Swith Checker

import os
import csv

# python3 -m pip install netmiko
from netmiko import ConnectHandler

# retreive data from excel
def get_csv(fileloc):
    d= {} 
    with open(fileloc, "r") as foo:
        for row in csv.DictReader(foo):
            # first value of row
            keypair= {row['hostname']: row['driver']}
            # first value of keypair
            d.update(keypair)

    return d

# ping the router - true or false
def ping_router(hostname):
    response = os.system("ping -c 1 " + hostname)
    # if no errors with ping response = 0
    # if errors with ping response > 0
    if response == 0:
        return True

    else:
        return False

# Check interfaces - Issue "show ip int brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        #attempt to open a connection
        open_connection = ConnectHandler(device_type=dev_type,
                                        ip=dev_ip,
                                        username=dev_un,
                                        password=dev_pw)

        # send a command to the switch
        my_command = open_connection.send_command("show ip int brief")

    except:
        # if an error occurs
        my_command = "** Issuing Command Failed **"

    finally:
        # no matter what, this function will return "my_command"
        return my_command

# login to router
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        # attempt to connect to switch
        open_connection = ConnectHandler(device_type=dev_type,
                                        ip=dev_ip,
                                        username=dev_un,
                                        password=dev_pw)
        # if no errors
        return True

    except:
        # if errors
        return False

def main():
    #determine where *.xls input is
    file_location = input("Host file location [Press ENTER for default: 'host_list.csv']\n>") or "host_list.csv"

    # entry is now a dictionary returned from get_csv()
    entry = get_csv(file_location)

    # user a loop to check each device
    print("\n***** BEGIN ICMP CHECKING *****")
    for switchip in entry:
        if ping_router(switchip):
            # if function returns TRUE:
            print("\n\t**HOST: - " + switchip + " - responding to ICMP\n")

        else:
            # if function is FALSE:
            print("\n\t**HOST: - " + switchip + " - NOT responding to ICMP\n")

    # Use a loop to check each device for SSH
    print("\n***** BEGIN SSH CHECK ****")
    for switchip in entry:
        if login_router(f"{entry[switchip]}",
                        switchip,
                        "admin",
                        "alta3"):
            
            # if function returns true
            print("\n\t**HOST: - " + switchip + " - SSH connectivity UP\n")

        else:
            # if function is false
            print("\n\t**HOST: - " + switchip + " - SSH connectivity DOWN\n")

    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for switchip in entry:
        result= interface_check(f"{entry[switchip]}",
                                switchip,
                                "admin",
                                "alta3")
        print("\n" + result)

if __name__ == "__main__":
    main()





