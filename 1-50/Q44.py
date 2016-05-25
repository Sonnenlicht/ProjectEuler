#Pentagon numbers
#Problem 44
#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

#P = n(3n - 1)/2

pent_list = []
for i in range(1, 3000):
    pent = int(i * (3*i - 1) / 2)
    pent_list.append(pent)

for j in range(len(pent_list) - 1):
    for k in range(j, len(pent_list)):
        add_val = pent_list[j] + pent_list[k]
        sub_val = pent_list[k] - pent_list[j]
        if add_val in pent_list:
            if sub_val in pent_list:
                print(pent_list[k] - pent_list[j])


    
