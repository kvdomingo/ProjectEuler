from timeit import timeit
from typing import Callable, AnyStr, Union


def time_it(obj: Union[AnyStr, Callable], reps: int = 10):
    if isinstance(obj, str):
        print(eval(obj))
    else:
        print(obj())
    time = timeit(obj, number=reps) / reps * 1e6
    unit = "µs"
    if time < 0.01:
        time *= 1e3
        unit = "ns"
    elif time >= 1e3:
        time /= 1e3
        unit = "ms"
    print(f"{round(time, 2)} {unit} per loop")
