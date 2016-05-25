#Cubic permutations
#Problem 62
#The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

def digits_dict(number):
    digits = {}
    for i in range(10):
        digits[i] = 0
    string = str(number)
    for char in string:
        unit = int(char)
        digits[unit] += 1
    return digits

#cube_list = []
dict_list = []

for num in range(1, 10000):
    #cube_list.append(num ** 3)
    cube = num ** 3
    dict_list.append(digits_dict(cube))

#print(len(dict_list))

#for a in range(1000):
#    for b in range(a, 1000):
cubes_list = []

length = len(dict_list)        
for a in range(length - 1):
    cubes_list = [a+1]
    for b in range(a+1, length):
        if dict_list[a] == dict_list[b]:
            cubes_list.append(b+1)
    if len(cubes_list) >= 5:
        #print(cubes_list)
        print(cubes_list[0] ** 3)
        break    
        
    
    
