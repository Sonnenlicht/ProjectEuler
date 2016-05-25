#Consecutive prime sum
#Problem 50
#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?
#Answer: 997651

def isPrime(n):#
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

total = 0
prime_list = []
for num in range(1, 1000000):
    if isPrime(num) == True:
        prime_list.append(num)
        
prime_total = []
total = 0

for num in prime_list:
    total += num
    prime_total.append(total)
    
#print(prime_list)
#print(len(prime_total))

maxima  = 0
numPrimes = 0

for i in range(1, len(prime_total)):
    for j in range(i-(numPrimes+1), 0, -1):
        diff = prime_total[i] - prime_total[j]
        if diff >= 1000000:
            break
        if diff in prime_list:
            numPrimes = i - j
            if diff > maxima:
                maxima = diff

print(maxima)
