#!/usr/bin/env python3

# import paramiko
import paramiko

# standard library
import os

def main():
    # "where to connect to" - IP and port
    t = paramiko.Transport("10.10.2.3", 22)

    # "how to connect
    t.connect(username="bender", password="alta3")

    # make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    # iterate across the files within the directory
    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy/"+x):
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

    # close the sftp connection
    sftp.close()
    t.close()

if __name__ == "__main__":
    main()
