#Prime permutations
#Problem 49
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?
##################################################################
#Generate a list of primes below between 1000 and 10000.
#Take two primes i and j with i < j and calculate k = j + (j-i).
#Check if k < 10000 and check if k is a prime, if not go to 2.
#Check if i and j are permutations of each other and check if i and k are permutations of each other. If not go to 2.
#Found the triple, so exit.
###################################################################

import itertools
numstr = ''

def digits(num):
    numdigits = {}
    for a in range(10):
        numdigits[a] = 0

    numstr = str(num)
    for char in numstr:
        b = int(char)
        numdigits[b] += 1

    return numdigits

def isPrime(n):#
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_list = []
for num in range(1000, 10000):
    if isPrime(num) == True:
        prime_list.append(num)

#print(prime_list)
#print(len(prime_list))

for i in range(len(prime_list) - 1):
    for j in range(i+1, len(prime_list)):
        k = prime_list[j] + prime_list[j] - prime_list[i]
        if k not in prime_list:
            continue
        i_dict = digits(prime_list[i])
        j_dict = digits(prime_list[j])
        k_dict = digits(k)

        if i_dict == j_dict:
            if i_dict == k_dict:
                print(prime_list[i], prime_list[j], k)
        
        
    
    
    
