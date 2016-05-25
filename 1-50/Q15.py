#Lattice paths
#Problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

#m ways to traverse on left, n ways to traverse up, m+n ways to traverse the last node
#     n
#m   m+n

#Hence 6 X 6 grid - ways matrix

#1  1  1  1   1   1
#1  2  3  4   5   6
#1  3  6 10  15  21
#1  4 10 20  35  56
#1  5 15 35  70 126	
#1  6 21 56 126 252


def latticeMatrix(num):
    myMatrix = []
    zerolist = []

    for i in range(num):
        zerolist.append(0)

    for j in range(num):
        myMatrix.append(zerolist)
        
    for a in range(num):
        myMatrix[a][0] = 1
        myMatrix[0][a] = 1
        
    for i in range(1, num):
        for j in range(1, num):
           myMatrix[i][j] = myMatrix[i-1][j] + myMatrix[i][j-1]

    print(myMatrix[0])

latticeMatrix(21)
