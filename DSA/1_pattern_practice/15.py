# Number Pyramid Pattern

# Problem Description:

# You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces


def number_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n - i) + " ".join(str(j) for j in range(1, i+1)))

number_pyramid(5)