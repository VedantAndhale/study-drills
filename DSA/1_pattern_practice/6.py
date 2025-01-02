# Pyramid Pattern

# Problem Description:

# You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

def generate_pyramid(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))
generate_pyramid(5)