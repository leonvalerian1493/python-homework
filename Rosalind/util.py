#!/usr/bin/env python

#library of untility function for Roslaind 

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readline()
        stripped=[]
        for line in lines:
            stripped.append(line.strip())

    return stripped 




