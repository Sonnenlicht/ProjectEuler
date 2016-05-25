#Coin sums
#Problem 31
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:

#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

#currency = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
ways = 0 # for 1x2, 2x1

target = 200

for a in range(200, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            ways += 1

print(ways)

