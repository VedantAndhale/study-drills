# Right Angled Triangle II

# Problem Description:

# You are given an integer n. Your task is to return a right-angled triangle pattern of '*', where each row contains stars aligned to the right. The first row has one star, the second row has two stars, and so on, until the nth row has n stars.


# Input:

#     A single integer n, where 1 <= n <= 100.

def right_angle_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))

right_angle_triangle(5)