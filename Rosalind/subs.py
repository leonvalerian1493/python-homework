
#!/usr/bin/env python

# s = string = "GATATATGCATATACTT"
# t = substring of s = "ATAT"

# representation of substring --> s[j:k] where j & k are start and ending positions of of the substring t within s
# if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
# note that t will have multiple locations in s if it occurs more than once as a substring of s

# OUTPUT: Positions of occruences of substring within string | Example from Rosalind --> output: 2 4 10 (ATAT is at position 2,4 and 10)

# ============================================================================================================================================
 

s= "GATATATGCATATACTT"
t= "ATAT" 

def find_substring_locations(s, t):
    locations = []
    for i in range(len(s) - len(t) + 1): # the lenght of s minus the lenght of t = the lenght in which t can surely fit into s
        if s[i:i + len(t)] == t: # slice string s from position i to i + lent(t)
            locations.append(i + 1)
    return locations

result = find_substring_locations(s, t)
print(" ".join(map(str, result)))