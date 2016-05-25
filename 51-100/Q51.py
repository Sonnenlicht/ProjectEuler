#Prime digit replacements
#Problem 51
#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
#Starting number and last prime can help in deducing first prime

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_list = []

for num in range(100000, 200000):
    if isPrime(num) == True:
        prime_list.append(num)

#print(prime_list)
#print(len(prime_list))

for num in prime_list:
    numstr = str(num)
    length = len(numstr)

    #1 digits
    #1st digit
    numprimes = 0
    newstr = ''
    for i in range(1, 10):
        newstr = str(i) + numstr[1:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    #2nd digit
    numprimes = 0
    newstr = ''
    for i in range(10):
        newstr = numstr[0] + str(i) + numstr[2:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    #From 3rd digit
    for k in range(2, length):
        numprimes = 0
        newstr = ''
        for i in range(10):
            newstr = numstr[0:k] + str(i) + numstr[k+1:]
            newnum = int(newstr)
            #print(num, newnum)
            if isPrime(newnum) == True:
                numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    #2 digits
    #6C2
    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,2
        newstr = str(i) + str(i) + numstr[2:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,3
        newstr = str(i) + numstr[1] + str(i) + numstr[3:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    for j in range(3, length):
        numprimes = 0
        newstr = ''
        for i in range(1, 10): #1,4..
            newstr = str(i) + numstr[1:j] +  str(i) + numstr[j+1:]
            newnum = int(newstr)
            #print(num, newnum)
            if isPrime(newnum) == True:
                numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
            
    numprimes = 0
    newstr = ''
    for i in range(10): #2,3
        newstr = numstr[0] + str(i) + str(i) + numstr[3:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    for j in range(3, length):
        numprimes = 0
        newstr = ''
        for i in range(10): #2,4..
            newstr = numstr[0] + str(i) + numstr[2:j] +  str(i) + numstr[j+1:]
            newnum = int(newstr)
            #print(num, newnum)
            if isPrime(newnum) == True:
                numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #3,4
        newstr = numstr[0:2] + str(i) + str(i) + numstr[4:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    for j in range(4, length):
        numprimes = 0
        newstr = ''
        for i in range(10): #3,5..
            newstr = numstr[0:2] + str(i) + numstr[3:j] +  str(i) + numstr[j+1:]
            newnum = int(newstr)
            #print(num, newnum)
            if isPrime(newnum) == True:
                numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #4,5
        newstr = numstr[0:3] + str(i) + str(i) + numstr[5:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(10): #4,6
        newstr = numstr[0:3] + str(i) + numstr[4] + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(10): #5,6
        newstr = numstr[0:4] + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break


    #3 digits
    #5C3
    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,2,3
        newstr = str(i) + str(i) + str(i) + numstr[3:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    for j in range(3, length):
        numprimes = 0
        newstr = ''
        for i in range(1, 10): #1,2,4..
            newstr = str(i) + str(i) + numstr[2:j] +  str(i) + numstr[j+1:]
            newnum = int(newstr)
            #print(num, newnum)
            if isPrime(newnum) == True:
                numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
    
    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,3,4
        newstr = str(i) + numstr[1] + str(i) + str(i) + numstr[4:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,3,5
        newstr = str(i) + numstr[1] + str(i) + numstr[3] + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,3,6
        newstr = str(i) + numstr[1] + str(i) + numstr[3:5] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break


    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,4,5
        newstr = str(i) + numstr[1:3] + str(i) + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,4,6
        newstr = str(i) + numstr[1:3] + str(i) + numstr[4] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

    numprimes = 0
    newstr = ''
    for i in range(1, 10): #1,5,6
        newstr = str(i) + numstr[1:4] + str(i) +  str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

    if numprimes >= 8:
        print(num, newnum)
        break

 
    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,4
        newstr = numstr[0] + str(i) + str(i) + str(i) + numstr[4:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
        
    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,5
        newstr = numstr[0] + str(i) + str(i) + numstr[3] + str(i) + numstr[5:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,6
        newstr = numstr[0] + str(i) + str(i) + numstr[3:5] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break


    numprimes = 0
    newstr = ''
    for i in range(10): #2,4,5
        newstr = numstr[0] + str(i) + numstr[2] + str(i) + str(i) + numstr[5:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,4,6
        newstr = numstr[0] + str(i) + numstr[2] + str(i) + numstr[4] + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,5,6
        newstr = numstr[0] + str(i) + numstr[2:4] + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
            
        
    numprimes = 0
    newstr = ''
    for i in range(10): #3,4,5
        newstr = numstr[0:2] + str(i) + str(i) + str(i) + numstr[5:]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #3,4,6
        newstr = numstr[0:2] + str(i) + str(i) + numstr[4] + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #3,5,6
        newstr = numstr[0:2] + str(i) + numstr[3] + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #4,5,6
        newstr = numstr[0:3] + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
    
    #4 digits
    #6C4
    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,3,4
        newstr = str(i) + str(i) + str(i) + str(i) + numstr[4:] 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,3,5
        newstr = str(i) + str(i) + str(i) + numstr[3] + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,3,6
        newstr = str(i) + str(i) + str(i) + numstr[3:5] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    
    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,4,5
        newstr = str(i) + str(i) + numstr[2] + str(i) +  str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,4,6
        newstr = str(i) + str(i) + numstr[2] + str(i) + numstr[4] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,2,5,6
        newstr = str(i) + str(i) + numstr[2:4] + str(i) +  str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    
    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,3,4,5
        newstr = str(i) + numstr[1] + str(i) + str(i) + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,3,4,6
        newstr = str(i) + numstr[1] + str(i) + str(i) + numstr[4] + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,3,5,6
        newstr = str(i) + numstr[1] + str(i) + numstr[3] + str(i) +  str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(1,10): #1,4,5,6
        newstr = str(i) + numstr[1:3] + str(i) + str(i) +  str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break


    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,4,5
        newstr = numstr[0] + str(i) + str(i) + str(i) + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,4,6
        newstr = numstr[0] + str(i) + str(i) + str(i) + numstr[4] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,5,6
        newstr = numstr[0] + str(i) + str(i) + numstr[3] + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,4,5,6
        newstr = numstr[0] + str(i) + numstr[2] + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #3,4,5,6
        newstr = numstr[0:2] + str(i) + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    #5 digits
    #6C5
    numprimes = 0
    newstr = ''
    for i in range(10): #1,2,3,4,5
        newstr = str(i) + str(i) + str(i) + str(i) + str(i) + numstr[5]
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #1,2,3,4,6
        newstr = str(i) + str(i) + str(i) + str(i) + numstr[4] + str(i) 
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #1,2,3,5,6
        newstr = str(i) + str(i) + str(i) + numstr[3] + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #1,2,4,5,6
        newstr = str(i) + str(i) + numstr[2] + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #1,3,4,5,6
        newstr = str(i) + numstr[1] + str(i) + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break

    numprimes = 0
    newstr = ''
    for i in range(10): #2,3,4,5,6
        newstr = numstr[0] + str(i) + str(i) + str(i) + str(i) + str(i)
        newnum = int(newstr)
        #print(num, newnum)
        if isPrime(newnum) == True:
            numprimes += 1

        if numprimes >= 8:
            print(num, newnum)
            break
