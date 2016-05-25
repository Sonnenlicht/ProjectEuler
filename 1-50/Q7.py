#10001st prime
#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def nthPrime(n):
    prime = 0
    num = 2
    while prime < n:
        if isPrime(num) == True:
            prime += 1
        num += 1
    return num - 1

print(nthPrime(10001))
        
        
        
