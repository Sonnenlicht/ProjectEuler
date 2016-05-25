#Pandigital prime
#Problem 41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def isPanDigital(mystr):
    length = len(mystr)

    for char in mystr:
        if int(char) > length:
            return False
    
    strdict = {}
    for i in range(0, length+1):
        strdict[str(i)] = 0
    #print(strdict)
    
    for char in mystr:
        strdict[char] = strdict[char] + 1
    #print(strdict)
    for k, v in strdict.items():
        if k != '0':
            if v != 1:
                return False
    if strdict['0'] != 0:
        return False
    return True

max_num = 0
for num in range(10000, 10000000): #, 100000):
    if isPanDigital(str(num)) == True:
        if isPrime(num) == True:
            if num > max_num:
                max_num = num
            #print(num)

print(max_num)
