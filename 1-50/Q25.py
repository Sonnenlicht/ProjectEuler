#1000-digit Fibonacci number
#Problem 25
#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

maxlimit = 10 ** 1000
#print(len(str(maxlimit)))

fibonacci_list = [1, 1]

num = 1
i = 1
j = 1
while num < maxlimit:
    num = i + j
    fibonacci_list.append(num)
    i = j
    j = num

index = 0
length = len(str(fibonacci_list[index]))
while length != 1000:
    length = len(str(fibonacci_list[index]))
    index += 1

print(index)
