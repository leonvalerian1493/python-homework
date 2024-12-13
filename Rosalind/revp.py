##!/usr/bin/env python


# 1) parse Fasta File 

# ATGCAT
# TGCA
# GCATGC
# CATG
# TATA
# ATAT
# ATGCAT
# TGCA

# looping over Sequence 
# making a dictionry with all the possible choices 

# [4-6-8-10-12 palindrom sequences]
# maybe use enumerate?

# for our example use 4-6 palindromes 


# ================================

from revc import reverse_complement

def is_palindrome(seq):
    if seq == reverse_complement(seq):
        return True 
    return False 

def main(): 
    data = 'TCAATGCATGCGGGTCTATATGCAT'
    window_size = 4
    for window_size in range(4,13):
        for i in range(len(data)-window_size+1):
            seq = (data[1:1:+window_size])
            if is_palindrome(seq):
                print(i+1,len(seq))


