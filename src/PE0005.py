"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from src import time_it


def gcd(a: int, b: int):
    return b and gcd(b, a%b) or a


def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def main(upper_bound: int = 20):
    n = 1
    for i in range(1, upper_bound + 1):
        n = lcm(n, i)
    return n


if __name__ == "__main__":
    time_it(main)
