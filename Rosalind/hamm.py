
s = "CGAGGTACGCTAGAACGTATATTGACGCATCGCCGGACTACGTACACAACCATCCTTGTTGGCAGCGTGTACCCCCAACCGTCGGAATTCGTGTGATTTCGGAATTCTCCCTTGAGGCGACCGCACTGGCAGCCACGTTGCCACTTTTGTCTGCCCGCAGGATTAATACTCCTTACCAAACGGTGTCATTCTTTCCACGCGATGACTTAGTTCTTGAGTCCGCATGGGCTGGCAAACGCCTTGCAACGTAGGTCGCCGAAGGAAAATAGTATGGCGTTCACCCTCGGTTGCGGGATCTGTACTTGTTTGTGTCTAGATCACGTTATGCGTCGAACACATAATCAGAAATGATACAACCACTCGCGTTATGGTGTGTGGTAAGGACTAAATTTTCTTTGTATATCGTCTTACAACTGAGATAGCGTTTCCGAGACCTCACCTGCGGGAACCTAAAATACTAGTCTAGAAGGATCGTTCCCCCCAGACGAGGCGCCCTCGGCCATAGCATTGTCTCTGTCGGTAGCCGCAGGCGAGGATCGAACAACGCTGAGGGTCCGGTGCGAGGTGACTTTGGACACGACTTTGACCGGATAGTCACGCATCAATATATGCTTCCAAATGATCCATGTACACCGACCCGATACTGGATCCTCCATAGTGACACACTCTTTTGAGTTGCTCCCATGGAATTCTAGGAGAAACGGCATCCCCTGCGCCTCCCGTTTCTTTTGGTGCGCGCGACGACACATCACTTTATGTGTCGGCAGTACTTATATAGTGCATGCGCGCACCTGCAAAATAACCAGCTTGATAATATGGGGAAAGTTTGACGCCTCAACGATCACAGCAACCGTTCTATTCAACACGCCGCAATACTATGCGTACCGACAAAAGTGAATGACGCAAATCACATCTCGCGCAGCCTAGAGACTCAGAGAACCGCGCG"
t = "ATCGATAGATTCATTAGGCTGACACGGTTGCTCGAGACTCCGTATATCCCAGCCCTTATTGGCTATCTGCGCCCTGTCCGCGCCGAATCCATGTCACCTAAGAACCCCGACCGATGGCGACAGCCATGCTACCCACGTATCCACTGTAGTCTGATAGCAGGGAGTTGCCAACGCGAGAAGAGATGTCCTTATAGCCATATATGGAGATGGTTCTGGAGTGCCTAGTGCCAGTCCTACGCACGGCAATGCATCTCACCGCCACACGTTGGTTTTACGATATCCGGCGACTACCCAATCGATGCCTCTATGTTGCTCCAGTCTGATTTACCATGGAGAGATCTATATTATCTTTACAACCTCTTGTCTCAAGAATAGGCTAAACAATCAAATGCGCCTGCTGCAACCCGGTACTAAATTTGTGGCGAATGTAAACCCTCAAGAGCCGCAACGTGTGAAAGATGCTGCGCACCATCGAACCCCGCTTTTCACACCCCCTCACTGTTAGGCTTACCCGATACGAGATCCGAGGTCGTTGTACGTATAGAGTTGAGAGTCAGGTTTTTGCCTTACCTGGACTCGTGTCGGAAGGTATAGCCGCTGCTCAATAACGGCAGCCAATAGTAGACTCTCGACAGTCTCACCTTTGAACGCGGTTTGGCCAAGCAGTCCTGGGCGTTGCTCCTAAGGGATGAGAGGGGGCACTGGGTCCTTAGGGTTTACCCTAACTCCTAGAGCGCGCCGGCGCCCAGCACTCCCATCGGCCCCAGGCGTTATGTATATCACGTAAGCATTTATCCTATACCAAACTAGGTCAGACCGGCAAGATCGATGGGCTACTTCATAATGGCACTCACTTTAGGCGACGCTCCTGAACGCTACTCGACCCGAGTCGTGTAGCGCATGTAAAGCTCATGTAACGCAGTTTTGAGACTTATCTACCTTCCCC"

count=0

for index, base in enumerate(s):
    if t[index] != base:
        count += 1

print(count)


