#Distinct primes factors
#Problem 47
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
#Ans: 134043

def isPrime(n):#
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def get_factors(number):
    return [n for n in range(2, number) if number % n == 0 and isPrime(n) == True]

new_dict = {}
def get_all_factors(numbers_set):
    #for i in numbers_set:
    #    new_dict[i] = get_factors(i)
    #print(new_dict)
    new_dict = {i:get_factors(i) for i in numbers_set}
    return new_dict

#print(get_all_factors({14, 15}))
#print(get_all_factors({644, 645, 646}))

for i in range(130000, 140000):
    a = i
    b = i + 1
    c = i + 2
    d = i + 3
    my_dict = get_all_factors({a,b,c,d})

    total = 0
    for k, v in my_dict.items():
        if len(v) >= 4:
            total += 1

    if total == 4:
        print(a)
            




        
   
    
