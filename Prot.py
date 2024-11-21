
# make a dictionary with the codons

codons = { "AUG":"M","etc..." } 

# translate the RNA into the AA by using the dictonry we created: 

rna="UAGUGCAAUGCAGAUGCA"

for something in range(0,len(rna),3) # divides the rna in triplets which we can then associate with the Codons from the dictionary
# I know we have to let it loop over the rna sequence in triplets but I have other clue how to associate it with the dictionary
