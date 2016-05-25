#Amicable numbers
#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def get_factors(number):
    return [n for n in range(1, number) if number % n == 0]

new_dict = {}

def total(numlist):
    total = 0
    for num in numlist:
        total += num
    return total

def get_all_factors(numbers_set):
    #for i in numbers_set:
    #    new_dict[i] = get_factors(i)
    #print(new_dict)
    new_dict = {i:total(get_factors(i)) for i in numbers_set}
    return new_dict
    
#get_all_factors({1, 2, 3, 4})
#get_all_factors({62, 293, 314})
numset = {0}
for i in range(1, 10000):
    numset.add(i)

my_dict = {}
my_dict = get_all_factors(numset)
#print(my_dict)

list_of_tuples = []
list_of_unique_tuples = []
for k, v in my_dict.items():
    if my_dict[k] < 10000:
        if my_dict[v] == k:
            if k != v:
                list_of_tuples.append((k, v))

for i in range(1, len(list_of_tuples), 2):
    list_of_unique_tuples.append(list_of_tuples[i])
            
print(list_of_unique_tuples)           

total = 0
for i in range(len(list_of_unique_tuples)):
    for j in range(2):
        total += list_of_unique_tuples[i][j]
    
print(total)
