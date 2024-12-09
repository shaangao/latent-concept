import numpy as np


def normalize(v, ord=1):
    v = np.array(v, dtype=float)  # change dtype to floats
    norm = np.linalg.norm(v, ord)
    if norm == 0: 
       return v
    v[v != 0] /= norm
    return v