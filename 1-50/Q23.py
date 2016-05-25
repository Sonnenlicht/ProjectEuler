#Non-abundant sums
#Problem 23
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def get_factors(number):
    numlist = [n for n in range(1, number) if number % n == 0]
    total = 0
    for num in numlist:
        total += num
    return total

new_dict = {}

#def total(numlist):
#    total = 0
#    for num in numlist:
#        total += num
#    return total


def get_all_factors(numbers_set):
    #for i in numbers_set:
    #    new_dict[i] = get_factors(i)
    #print(new_dict)
    new_dict = {i:get_factors(i) for i in numbers_set if i < get_factors(i)}
    return new_dict

numset = {0}
for i in range(1, 28124):
    numset.add(i)
numset.remove(0)
#print(numset)

my_dict = {}
my_dict = get_all_factors(numset)
#print(my_dict)

set_abundant = {0}
for k in my_dict.keys():
    set_abundant.add(k)
set_abundant.remove(0)
#list_abundant.sort()

#print(list_abundant)
#print(len(set_abundant))

#print(set_abundant)

sumset = {0}
sumlist = []
list_abundant = list(set_abundant)
#print(list_abundant)

for m in range(len(list_abundant)):
    for n in range(len(list_abundant)):
        sumlist.append(list_abundant[m] + list_abundant[n])

sumset = set(sumlist)
sumset = sumset.union(sumset)
#print(sumset)

finalset = numset - sumset
finalset = list(finalset)
#print(finalset)

total = 0

for num in finalset:
    total += num

print(total)

