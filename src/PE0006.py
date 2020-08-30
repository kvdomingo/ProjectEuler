"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from src import time_it


def main(upper_bound: int = 100):
    num = list(range(1, upper_bound + 1))
    sum_squares = sum(list(map(lambda x: x**2, num)))
    square_sum = sum(num)**2
    diff = square_sum - sum_squares
    return diff


if __name__ == "__main__":
    time_it(main)
