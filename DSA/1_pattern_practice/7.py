# Inverted Pyramid Pattern

# Problem Description

# You are given an integer n. Your task is to return an inverted pyramid pattern of '*'. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))  

inverted_pyramid(5)