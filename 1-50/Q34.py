#Digit factorials
#Problem 34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.


def fact(num):
    product = 1
    if num == 0:
        return 1
    for i in range(1, num+1):
        product *= i
    return product

for num in range(10, 10000000):
    numstr = str(num)
    total = 0
    for char in numstr:
        total += fact(int(char))

    if total == num:
        print(num)
