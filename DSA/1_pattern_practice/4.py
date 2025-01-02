# Right Angled Triangle

# Problem Description:

# You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

def generate_right_angle_triangle(n):
    for i in range(1, n+1):
        print('*'*i)
generate_right_angle_triangle(5)
