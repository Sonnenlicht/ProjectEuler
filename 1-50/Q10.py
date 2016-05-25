#Summation of primes
#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def sumPrime(n):
    primesum = 0
    num = 2
    while num < n:
        if isPrime(num) == True:
            primesum += num
        num += 1
    return primesum

print(sumPrime(2000000))

