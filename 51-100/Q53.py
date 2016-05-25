#Combinatoric selections
#Problem 53
#There are exactly ten ways of selecting three from five, 12345:

#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

#In combinatorics, we use the notation, 5C3 = 10.

#In general,

#nCr =	
#n!
#r!(n−r)!
#,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

#How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

def factorial(num):
    if num == 0:
        return 1
    mult = 1
    for i in range(1, num+1):
        mult *= i
    return mult

def combinations(n, r):
    comb = factorial(n) / (factorial(r) * factorial(n-r))
    return int(comb)

total = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if combinations(n, r) > 1000000:
            total += 1

print(total)
        
    
