# Hollow Inverted Right Triangle

# Problem Description:

# You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned

def hollow_inverted_right_triangle(n):
    for i in range(n):
        if i == 0:
            print("*" * (n - i))
        elif i == n - 1:
            print("*")
        else:
            print("*" + " " * (n - i - 2) + "*")

hollow_inverted_right_triangle(5)