"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from timeit import timeit


def main():
    pass


if __name__ == "__main__":
    reps = 1000
    print(main())
    print(f"{round(timeit(main, number=reps) / reps * 1e6, 2)} µsec per loop")
