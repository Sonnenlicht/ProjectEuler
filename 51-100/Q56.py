#Powerful digit sum
#Problem 56
#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def digitsum(largenum):
    string = str(largenum)
    total = 0
    for char in string:
        total += int(char)
    return total

max_val = 0
for a in range(1, 100):
    for b in range(1, 100):
        power_val = a ** b
        sum_val = digitsum(power_val)
        if sum_val > max_val:
            max_val = sum_val

print(max_val)
