#!/usr/bin/env python

# read the fasta file 
from util import read_input
DNA_string = read_input("rosalind_orf.txt")


code = {
    "TTT": "F",      "CTT": "L",      "ATT": "I",      "GTT": "V",
    "TTC": "F",      "CTC": "L",      "ATC": "I",      "GTC": "V",
    "TTA": "L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
    "TTG": "L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
    "TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT": "A",
    "TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "TAT": "Y",      "CAT": "H",      "AAT": "N",      "GAT": "D",
    "TAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "TAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "TAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
    "TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "TGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

# Start Codon RNA = AUG = Methionine || DNA = ATG
# Stop Codons RNA = UAG , UGA, UAA || DNA = TAG, TGA, TAA

# within string s (DNA) loop through string and traslate DNA from code dictionary with conditions 
# every time we encounter start codon = start translation when we encounter stop codon = stop translation and change row
# print result 
