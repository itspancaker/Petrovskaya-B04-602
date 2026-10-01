import random
import numpy as np
def f(a, b, N, sigma=1.0):
    x = np.linspace(0, 10, N)
    y = np.array([a * xi + b + random.gauss(0, sigma) for xi in x])
    return x, y
x_data, y_data = f(a=2.5, b=4.0, N=100, sigma=1.0)
a_1, b_1 = np.polyfit(x_data, y_data, 1)
print(f"a = {a_1:.2f}, b = {b_1:.2f}")