filepath = "./rosalind/INI5.txt"
with open(filepath, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())

for l in lines[1::2]:
    print(l.strip())