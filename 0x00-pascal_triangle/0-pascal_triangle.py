#!/usr/bin/python3
"""
    generates the pascal triangle of n
    """


def pascal_triangle(n):
    '''generates the nth term of the pascal triangle'''
    triangle = [[1], [1, 1]]
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return triangle
    else:
        for i in range(2, n):
            last = triangle[-1]
            new = []
            new.insert(0, 1)
            for j in range(1, len(last)):
                sum = last[j - 1] + last[j]
                new.insert(len(new), sum)
            new.insert(len(new), 1)
            triangle.insert(i, new)

        return triangle
