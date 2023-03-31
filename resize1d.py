import numpy as np
from scipy.interpolate import interp1d

def resize1d(array : np.array, target_len : int, kind : str = 'linear'):
    array = array.squeeze()
    shape = array.shape
    assert len(shape) == 1, 'wrong shape {array.shape} | shape should be 1d-array like if 2d or more recommend : torch.nn.functional.interpolate'
    length = shape[0]

    x = np.linspace(0, 100, num = shape[0])
    new_x = np.linspace(0, 100, num = target_len)
    f = interp1d(x, array, kind = kind)
    '''
    f means the mapping function f(R) -> R
    so, f(x) = array[i] where x in range(0, 100, original length) 
    thus, if we set where xx in range(0, 100, target_length) 
    them, f(xx)  means resize array for target_length
    '''
    new_y = f(new_x)
    return new_y
