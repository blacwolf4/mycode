#!/usr/bin/env python3



def main():
    configfile = open("vlanconfig.cfg", "r")
    print(configfile.read())
    configfile.seek(0,0)
    configlist=configfile.readlines()
    print(configlist)

    for x in configlist:
        print(x)

    configfile.close

if __name__ == "__main__":
    main()





