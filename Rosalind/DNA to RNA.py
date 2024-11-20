

# change DNA string t into RNA 

# go over all letters 
# if its' a "T" change it to "U"
# if it's not a "T" write the letter 

# correct solution
t="GATGGAACTTGACTACGTAAATT"
rna=""

for letter in t: 
    if letter == "T":
        rna+=("U")
    else:
        rna+=(letter)

print(rna)




# first try out
for letter in t: 
    if letter == "T":
        print("U")
    else:
        print(letter)

