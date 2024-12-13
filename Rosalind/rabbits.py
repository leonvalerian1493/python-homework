#!/usr/bin/env python

# Rn = Rn-1 + k*Rn-2

def rabbits(n,k):
    if n<1:
        return 0
    if n==1 or n==2:
        return 1
    return rabbits(n-1,k) + k*rabbits(n-2,k)

result=rabbits(35,2)
print(result)