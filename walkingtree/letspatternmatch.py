#!/usr/bin/env python3

# script to search for a pattern
import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("what pattern am I looking for?")
lookwhere = input("Where am I looking?")

print(find(lookfor, lookwhere))

