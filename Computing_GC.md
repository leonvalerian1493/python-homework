#INPUT: DNA.fas
#OUTPUT: ID of String with highest GC Content & GC content of string

* the file does not display like a text so we need to put it into a format of a readable text. 

```python
filepath = "./rosalind_gc.txt"
with open(filepath, 'r') as file:
    for line in file:
```
* turn the file into a dictionary ? to have each rosalind species being 1 entry in the dictionary        

* Now we need to cut the ">" and make it a string so we can isolate the name and the DNA sequence


* From the string we would need to calculate the percentage of GC groups in the string | (%)for that we need to count how often G and C are in the string and compare it to the total number of letters in the string
```python
x %= y
```

```python
def count_all(DNA):
    cnt_a = cnt_c = cnt_g = cnt_t = 0
    for base in DNA:
        if base == 'A':
            cnt_a += 1
        elif base == 'C':
            cnt_c += 1
        elif base == 'G':
            cnt_g += 1
        elif base == 'T':
            cnt_t += 1
    cnt_all=[cnt_a, cnt_c, cnt_g, cnt_t]
    return cnt_all


s = ''
# this print-function accords to the first version
print(count_occurrences(s,'A'), count_occurrences(s,'C'), count_occurrences(s,'G'), count_occurrences(s,'T'))
# this print-function accords to the second version
for val in count_all(s):
    print(val)
```

*take string with highest GC content and print its name and percentage


* honestly I have no idea how to even tackle this so above are my logically constructed ideas how to solve this problem. I am looking forward to the group effort in class tomorrow
