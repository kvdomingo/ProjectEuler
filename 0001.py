"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from timeit import timeit


def get_lcm(a: int, b: int):
    greater = max(a, b)
    while True:
        if greater%a == 0 and greater%b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def main(upper_bound: int = 1000):
    suma: int = 0
    for multiple in [3, 5]:
        for i in range(multiple, upper_bound, multiple):
            suma += i
    lcm = get_lcm(3, 5)
    for i in range(lcm, upper_bound, lcm):
        suma -= i
    return suma


if __name__ == "__main__":
    reps = 1000
    print(main())
    print(f"{round(timeit(main, number=reps) / reps * 1e6, 2)} µsec per loop")
