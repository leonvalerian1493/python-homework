

seqs=["A T C C A G C T",
"G G G C A A C T",
"A T G G A T C T",
"A A G C A A C C",
"T T G G A A C T",
"A T G C C A T T",
"A T G G C A C T",]

counter={"A":0,"C":0,"G":0,"T":0}

for s in seqs: 
    #print(s[0])
    counter[s] +=1

print(counter)

