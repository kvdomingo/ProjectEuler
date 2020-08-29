"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
from src import time_it


def is_prime(n: int):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, max_div + 1):
        if n%i == 0:
            return False
        return True


def main(n: int = 600851475143):
    max_prime_factor = -1
    while n % 2 == 0:
        max_prime_factor = 2
        n >>= 1
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime_factor = i
            n /= i
    if n > 2:
        max_prime_factor = n
    return int(max_prime_factor)


if __name__ == "__main__":
    time_it(main)
