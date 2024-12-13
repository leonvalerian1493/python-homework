

def calculate_offspring(k,m,n): 
    S = (k+m+n)
    Pr = (k/S)+((m/S)*((4*k+3*m-3+2*n)/(4*(S-1))))+((n/S)*((2*k+m)/(2*(S-1))))
    return Pr

print(calculate_offspring(30,23,18))