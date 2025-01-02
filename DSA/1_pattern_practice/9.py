# Floyds Triangle

# Problem Description:

# You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.


# Input:

#     A single integer n, where 1 <= n <= 100

def floyds_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
floyds_triangle(5)