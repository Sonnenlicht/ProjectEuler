#Goldbach's other conjecture
#Problem 46
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for num in range(3, 10000, 2):
    if isPrime(num) == True:
        continue

    sqr_list = []
    i = 1
    inj = 0
    while inj < num:
        inj = int(2 * (i ** 2))
        if inj < num:
            sqr_list.append(inj)
        i += 1
        
    #print('Sqr List')
    #print(sqr_list)

    prime_list = []
    for k in range(3, num, 2):
        if isPrime(k) == True:
            prime_list.append(k)
    #print('Prime List')
    #print(prime_list)

    times = 0
    for j in prime_list:
        diff = int(num - j)
        #print('Diff is')
        #print(diff)
        if diff in sqr_list:
            times += 1

    if times == 0:
        print(num)
            
    
