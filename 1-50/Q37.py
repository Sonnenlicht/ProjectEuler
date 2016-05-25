#Truncatable primes
#Problem 37
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def truncPrime(num):
    numstr = str(num)
    length = len(numstr)

    while length > 0:
        if isPrime(int(numstr)) == False:
            return False
        numstr = numstr[1:]
        length -= 1
        
    numstr = str(num)
    length = len(numstr)

    while length > 0:
        if isPrime(int(numstr)) == False:
            return False
        length -= 1
        numstr = numstr[:length]

    return True

total = 0
for i in range(10, 1000000):
    if truncPrime(i) == True:
        #print(i)
        total += i

print(total)
        
