#!/usr/bin/env python3

import paramiko
import os
import getpass

def main():
    # where to connect
    t = paramiko.Transport("10.10.2.3", 22)

    # how to connect
    t.connect(username="bender", password=getpass.getpass())
    
    # make an sftp connection
    sftp = paramiko.SFTPClient.from_transport(t)

    #copy firstpasswd.py script to bender
    sftp.put("file_to_move.txt", "file_to_move.txt")

    # close the connection
    sftp.close()

if __name__ == "__main__":
    main()


