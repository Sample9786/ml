import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('student.csv', data, delimiter=',', fmt='%d')
