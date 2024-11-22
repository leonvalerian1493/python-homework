```python
DNA="AAAACCCGGT"
reversed= DNA[::-1]

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
```
