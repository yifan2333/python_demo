import numpy as np

import matplotlib as m

import pandas as pd

if __name__ == '__main__':

    a = np.array([[1, 2], [3, 4]])

    A = np.linalg.eigvals(a)

    print(A)

    b = pd.DataFrame(a)


