#!/usr/bin/env python

# from util import read_input
# line_list = read_input("rosalind_orf.txt")
DNA="CCATAAAGTACAAACTCGTTCAATCAACGTAGGACGAGGATCGCGTTAATGTAGCAATATTAAGATGTAGCGTCCCTAGGCCCTCGTAGCGCATAAAAATCCCATCAACCGCTGTAACCTGTTAGACAATGTGGTCCATCTAGAGACCTTTGTGTTGGAGCACAATACTTGGTGGGGAACATACGACATACATACCTGCTTACGACTGATGCAGTTCGCACAAGCCGAGCTGGTGCTACACATGAATGTTGTATAAGCGCTTTTACGTTAGCGGGGAGTCTGATCGTTGTGCTTACTTTAAGCTTCTGTTTAGAGCCCGCCATATAACCTGACACAGATCTATCATGAAAAGTATGCCCACCTGCCTGTCTATTGGGGGCCGCCCTTCCACAGGTTTCAATTATACATACACAATAGATAGAACGGGGGTGGTTGATGCGTCTTGAGACTATCTCGATGAGCTTTGGGGTGAGCTGGTAGCTACCAGCTCACCCCAAAGCTCATATGGACGGGCCGCAACCTTTGCCGACAAAACAGCGTCGTGCGTCCGAAATTCCATTAGAGCGACGATGGACCTTTGGCGCAGTAATAAGATTACTTTGGGCACATCTCCTCATCGCACCTGATGATCCAACAAGTGGAAAATTTCAGTATTCATCAAGATGTCAGAAGCTATAACTAATCTTTACAAGTGAAGCACTCCTAGGACCAGGTCCCCCATTTAGCCTAACACCGTTCTCCCGAACCTTCACCGAACTGCCGTCGAAACAAAAAATGTTTATGCTCCCAGATCTCACACGTTTTGGCCAAGACCGCAACGGAATACATCGATGGGCGGGATGTCGCTTTTACATCGCATATATTTCTGGAACCGTAGCTGGACTCCCCGAATTTTCATAAACAGACAACCAAGTAAGATGACAGTCCCTGGGCTAGTGCTCCCCGCCATCTCATAGTACG"

code = {
   "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

RNA=''

for letter in DNA: 
    if letter == "T":
            RNA+="U"
    else:
            RNA+=letter



# find ORF's in RNA | Start Codon = "AUG" | Stop Codon = "UAA", "UAG", "UGA"

# RNA  || reverse_RNA = RNA[::-1]


# read the rna in triplets:

def find_orfs(RNA,start_codon):
    peptide = "" # mayeb also as list []
    for start in range(0, len(RNA), 3):       
        codon = RNA[start:start+3]
        aminoacid = code[codon]
        if aminoacid == "M" and aminoacid == "Stop":
            print(aminoacid)

Result=find_orfs(RNA,"AUG")
print(Result)


# 
# def find_orfs(RNA, start):
    # locations = []
    # for i in range(len(RNA) - len(start) + 1): 
        # if RNA[i:i + len(start)] == start:
            # locations.append(i + 1)
    # return locations
# 
# result = find_orfs(RNA,start)
# print(*result)
#print(" ".join(map(str, result)))