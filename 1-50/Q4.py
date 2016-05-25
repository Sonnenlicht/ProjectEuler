#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(myString):
    length = len(myString)
    revString = ''
    for i in range(length):
        revString += myString[length - i - 1]
    #print(revString)
    if revString == myString:
        return True
    else:
        return False
    
def Palindrome():
    palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            numstr = str(product)
            if isPalindrome(numstr) == True:
                if palindrome < product:
                    palindrome = product
    return palindrome                    
            
print(Palindrome())
