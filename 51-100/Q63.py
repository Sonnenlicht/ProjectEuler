#Powerful digit counts
#Problem 63
#The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

def numDigits(number):
    return len(str(number))

count = 0
for num in range(1, 10):
    for power in range(1, 100):
        power_num = num ** power
        if power == numDigits(power_num):
            count += 1

print(count)
