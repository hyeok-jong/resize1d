import numpy as np
from scipy.interpolate import interp1d

def resize1d(array : np.array, target_len, kind = 'linear'):
    array = array.squeeze()
    shape = array.shape
    assert len(shape) == 1, 'wrong shape {array.shape}'
    length = shape[0]

    x = np.linspace(0, 100, num = shape[0])
    new_x = np.linspace(0, 100, num = target_len)
    f = interp1d(x, array, kind = kind)

    new_y = f(new_x)
    return new_y
