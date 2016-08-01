from numba import jit
import time
import numpy as np


@jit
def sum_auto_jitting(x, y):
    array = np.arange(x * y).reshape(x, y)
    sum = 0
    for i in range(x):
        for j in range(y):
            sum += array[i, j]
    return sum


# force compilation in nopython mode
@jit(nopython=True)
def jitted_loop(array, x, y):
    sum = 0
    for i in range(x):
        for j in range(y):
            sum += array[i, j]
    return sum

# compiled in object mode
@jit
def sum(x, y):
    array = np.arange(x * y).reshape(x, y)
    return jitted_loop(array, x, y)

sum_auto_jitting(29, 10)
sum(29, 10)

sum_auto_jitting.inspect_types()
sum.inspect_types()