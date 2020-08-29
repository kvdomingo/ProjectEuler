"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from src import time_it


def main():
    pal = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            prod = i*j
            if prod > pal and str(prod) == str(prod)[::-1]:
                pal = prod
    return pal


if __name__ == "__main__":
    time_it(main)
