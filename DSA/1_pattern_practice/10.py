# Diamond Pattern

# Problem Description:

# You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.


# Input:

#     A single integer n, where 1 <= n <= 100.



def diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2*i + 1))
    for i in range(n-2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2*i + 1))

diamond(5)