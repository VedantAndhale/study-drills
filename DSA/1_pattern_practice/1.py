# Square of side 'N'

# Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*'.


def generate_square(n):
    for i in range(n):
        print('*'*n)

generate_square(5)