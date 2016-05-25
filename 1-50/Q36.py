#Double-base palindromes
#Problem 36
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(string):
    length = len(string)
    newstr = ''
    for i in range(length - 1, -1, -1):
        newstr += string[i]
    if newstr == string:
        return True
    else:
        return False

total = 0

for num in range(1, 1000000):
    decstr = str(num)
    binstr = str(bin(num))
    binstr = binstr[2:]
    if isPalindrome(decstr) == True:
        if isPalindrome(binstr) == True:
            total += num

print(total)          

