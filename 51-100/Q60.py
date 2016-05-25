#Prime pair sets
#Problem 60
#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_list = []

for num in range(3, 10000):
    if isPrime(num) == True:
        prime_list.append(num)

#print(prime_list)
length = len(prime_list)
#print(length)

#concat_primes = {0}
list_of_tuples = []
for i in range(length):
    for j in range(i+1, length):
        string1 = str(prime_list[i]) + str(prime_list[j])
        string2 = str(prime_list[j]) + str(prime_list[i])
        if isPrime(int(string1)) == True and isPrime(int(string2)) == True:
            #concat_primes.add(prime_list[i])
            #concat_primes.add(prime_list[j])
            num_tuple = (prime_list[i],prime_list[j])
            list_of_tuples.append(num_tuple)
            continue

#concat_primes = concat_primes.union(concat_primes)
#print(list_of_tuples)
#print(concat_primes)

total = 0
min_total = 0
for a,b in list_of_tuples:
    for c,d in list_of_tuples:
        if a == c and b == d:
            continue
        
        if (a,c) in list_of_tuples and (a,d) in list_of_tuples and (b,c) in list_of_tuples and (b,d) in list_of_tuples:
            for e,f in list_of_tuples:
                if (a == e and b == f) or (c == e and d == f):
                    continue
                
                if (a,e) in list_of_tuples and (b,e) in list_of_tuples and (c,e) in list_of_tuples and (d,e) in list_of_tuples:
                    total = a + b + c + d + e
                    if total < min_total:
                        min_total = total
                        print(min_total)
                    #print(a,b,c,d,e)

                if (a,f) in list_of_tuples and (b,f) in list_of_tuples and (c,f) in list_of_tuples and (d,f) in list_of_tuples:
                    total = a + b + c + d + f
                    if total < min_total:
                        min_total = total
                        print(min_total)
                    #print(a,b,c,d,f)    
        else:
            continue

print('END')
            
    
    
    
