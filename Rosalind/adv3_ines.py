
from util import read_input
import re
estring = ' '
data = read_input("Rosalind/aocd3.txt")

for ln in data:
    estring += ln

muls = re.findall("mul\(\d{1,3},\d{1,3}\)",estring)

cnt = 0 
for mul in muls:
    cnt += int(mul.split(",")[0].strip("mul("))*int(mul.split(",")[1].strip(")")))

print(cnt)

