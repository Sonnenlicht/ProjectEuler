#Digit fifth powers
#Problem 30
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

result_list = []
total = 0

for num in range(2, 1000000):
    digit_sum = 0
    numstr = str(num)
    for char in numstr:
        digit_sum += (int(char) ** 5)
    if num == digit_sum:
        total += num
        #result_list.append(num)

#print(result_list)
print(total)        
        
    
