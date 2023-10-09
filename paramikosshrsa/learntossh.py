#!/usr/bin/python3

"""issuing commands across ssh"""


import os
import paramiko

def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_sterr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

    # if you want to connect with username and password, uncomment this:
    #sshsession.connect(server, username=username, password=password)

    #using private keys
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    #if we never went to this SSH host, add the fingerprint to the know hosts file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #creds to connect
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    # simple list of commands to issue
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
    
    # cycle through our commands and issue them
    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))

main()


