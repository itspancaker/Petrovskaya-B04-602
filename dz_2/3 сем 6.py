import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.1, 8.0, 10.2])

k, b = np.polyfit(x, y, 1)

print(f"k = {k:.2f}, b = {b:.2f}")