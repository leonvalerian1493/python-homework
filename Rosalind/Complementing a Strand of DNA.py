

# go over sequence
# do stuff
# build up solution

# reverse complement || Reverse =  s becomes TGGCCCAAAA || complemnt = A becomes T & G becomes G

DNA="AAAACCCGGT"
reversed= DNA[::-1]
#Result(Reversed complement)=


def complement(base): 
    if base == "T":
        return("A")
    elif base == "G":
        return("C")
    elif base == "A":
        return("T")
    elif base == "C":
        return("G")


revc = ''
for letter in reversed:
    revc = revc + complement(letter)

print(revc)