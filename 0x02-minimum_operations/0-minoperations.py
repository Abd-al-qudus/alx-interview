#!/usr/bin/env python3
"""Compute the minimum possible operation to copy
    and paste to reach a number of character"""


def minOperations(n):
    """compute the minimum operation"""
    sumfactors = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            sumfactors += i
        else:
            i += 1
    return sumfactors + n if n > 1 else sumfactors
