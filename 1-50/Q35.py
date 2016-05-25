#Circular primes
#Problem 35
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def circPrime():
    circset = {2, 3, 5, 7}
    for num in range(10, 1000000): #0000):
        numstr = str(num)
        length = len(numstr)

        while length > 0:
            if isPrime(num) == False:
                break
            length -= 1
            numstr = numstr[1:] + numstr[0]
            num = int(numstr)
            #print(num)
            if length == 0:
                circset.add(num)
    #print(circlist)
    circset = circset.union(circset)
    #print(circset)
    print(len(circset))
    
circPrime()
