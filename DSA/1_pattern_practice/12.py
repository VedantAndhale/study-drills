# Sandglass Pattern

# Problem Description:

# You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.


def sandglass(n):
    for i in range(n):
        print(" " * i + "*" * (2*n - 1 - 2*i))
    for i in range(n-2, -1, -1):
        print(" " * i + "*" * (2*n - 1 - 2*i))

sandglass(5)

