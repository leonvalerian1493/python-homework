##!/usr/bin/env python

from revc import reverse_complement

def is_palindrome(seq):
    if seq == reverse_complement(seq):
        return True 
    return False 

def main(): 
    data = 'TATAGCTGCTCCAGTTGAGACAGCTTATCAGTAGCCTGCTATGTGCAATGCGTCCCAGCGTAGGCTATTTGATAGATGCGCCCAATCTATAGGACAGCTCAGTCGGGCACCTCTCCATAACGGCAGAAGACCTAGTTAAAGCAATACGAAGGCCTCAGCAAATGATTGGCCGTCAGCAGGAGCAAGCCCTGGCGAAAAGCTTCTAGGGACCTTACATCTATTTCACATCTGGGTTCTCTCCCTAGCTACCATTAATAGACGACGTTCGCACAACGGGTTGAGGATTTTGGTGCTCAATATCACGCAAACGATTGGTACCACGAGGTCTAAACCATCGTCCGTCTGTTCCAATAGTTCTCTACCACAGTACACGAAGTCCGGGAAATCTAAGCTACGCTAGGTGATTAAATCGGGACGTCCCGTAGCCGTCGACGAATCCCGTCATAAGCGCTAAAAACTCTCATATTAAATGAGGGCTGGTTTCGTGCTCCCGTCAGTATAGCAGAAATCGAGAGATAGACTCAACTCGCAGTGAATCCTCCACTGATTGACAAGACTACGAAATAAACCGCGCCTGGTACGAGAGCTGCGCTGGCCCTAGACGTATCGCGATCGATGTCCTACTTATAACCAGATCTATTGCGACCACGAGTCTCCTCTTACCGACCCCCGATGCACCGCCCAAAAATCCCACCTAAAAGGGGACGTACCACCTAGGCGAACGAAGCAGAATTGCGCCGTTAATCTTGCACTCGAGAGGAGAATATAAGGTAGCGACCCGCTACATTCCCCCTTCACAGATACTTGCCCGAATCTCATCGACTGGGACGCG'
    # print(data)
    for window_size in range(4,13):
        for i in range(len(data)-window_size+1):
            seq = (data[i:i+window_size])
                # print(seq)
            if is_palindrome(seq):
                print(i+1,len(seq))

if __name__ == "__main__":
    main()