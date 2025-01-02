# Hollow Right Triangle

# Problem Description:

# You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.



def hollow_right_triangle(n):
    for i in range(n):
        if i == 0:
            print("*" * n)
        elif i == n - 1:
            print(" " * (n-1) + "*")
        else:
            print(" " * i + "*" + " " * (n - i - 2) + "*")

hollow_right_triangle(5)