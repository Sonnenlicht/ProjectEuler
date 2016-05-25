#Spiral primes
#Problem 58
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def spiralPrime(num):
    diag = 1
    rval = 1
    lval = 1
    prime = 0
    for i in range(num):
        rval += 2 * (i)
                        
        if i%2 == 0:
            lval += 4 * (i/2)
        else:
            lval += 4 * (i+1)/2

        lval = int(lval)
        #total += (int(lval) + rval)
        #print(int(lval), rval)
        if isPrime(lval) == True:
            prime += 1
        if isPrime(rval) == True:
            prime += 1

        if i > 0:
            diag += 2
    #print(prime * 100/diag)
    return (prime * 100/diag)

for i in range(26201, 26300, 2): #Set by trials
    if spiralPrime(i) < 10:
        print(i)
        break
    
