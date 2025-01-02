# Hollow Square of side 'N'

# Problem Description:

# You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*'.

def generate_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*'*n)
        else:
            print('*' + ' '*(n-2) + '*')

generate_hollow_square(5)