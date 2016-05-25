#Number letter counts
#Problem 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numletter_dict = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}

def numstr(number):
    wordstr = ''
    numstr = ''
    if number < 21:
        wordstr += numletter_dict[number]
        return wordstr
    if number < 100:
        numstr = str(number)
        unit = numstr[1]
        tenstr = numstr[0] + '0'
        #print(unit)
        wordstr += numletter_dict[int(tenstr)]
        wordstr += numletter_dict[int(unit)]
        return wordstr
    elif number == 1000:
        wordstr += 'onethousand'
        return wordstr
    else:
        numstr = str(number)
        unit = numstr[2]
        tenstr = numstr[1] + '0'
        hunstr = numstr[0]
        wordstr += numletter_dict[int(hunstr)]
        wordstr += numletter_dict[100]
        if tenstr[0] == '1':
            wordstr += 'and'
            wordstr += numletter_dict[int(tenstr[0] + unit)] 
        elif tenstr != '00':
            wordstr += 'and'
            wordstr += numletter_dict[int(tenstr)]
            wordstr += numletter_dict[int(unit)]
        if tenstr == '00' and unit != '0':
            wordstr += 'and'
            wordstr += numletter_dict[int(unit)]
        return wordstr
    

total = 0
for i in range(1,1001):
    total += len(numstr(i))
    
print(total)
for i in range(900,1001):
    print(numstr(i), len(numstr(i)))

        
        
        
    
