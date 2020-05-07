import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def surfaceArea(A):
    rows_nb = len(A)
    cols_nb = len(A[0])
    bellow_surface = rows_nb * cols_nb

    def compute_absolute_differences(vec):
        ext_vec = [0] + vec + [0]
        return sum([abs(ext_vec[i] - ext_vec[i - 1]) for i in range(1, len(ext_vec))])

    rows_surface = sum([compute_absolute_differences(raw) for raw in A])

    all_columns = [[a[i] for a in A] for i in range(0, cols_nb)]

    cols_surface = sum([compute_absolute_differences(col) for col in all_columns])

    return 2 * bellow_surface + rows_surface + cols_surface