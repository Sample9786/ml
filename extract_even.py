import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = arr[arr % 2 == 0]
print("Even numbers:\n", even_numbers)
