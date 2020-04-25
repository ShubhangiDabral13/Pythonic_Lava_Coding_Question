"""
Pascal’s triangle is a triangular array of the binomial coefficients. Write a function that takes an integer
value n as input and prints first n lines of the Pascal’s triangle. Following are the first 6 rows of
Pascal’s Triangle.

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
Time complexity is 0(N^2).
Space complexity is 0(1).
"""

def pascal(n):

    for line in range(1,n+1):
        c = 1

        for j in range(1,line+1):

            print(c,end = " ")
            c= int(c* (line -j)/ j )

        print()

n = int(input("Enter the number whose pascal triangle you want to find"))
pascal(n)
