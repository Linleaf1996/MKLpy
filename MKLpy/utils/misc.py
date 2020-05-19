

import torch
from . import exceptions


def uniform_vector(n):
    return torch.ones(n)/n


def onehot_vector(n,idx):
	w = torch.zeros(n)
	w[idx] = 1
	return w


def identity_kernel(n):
    return torch.diag(torch.ones(n))



def ideal_kernel(Y, T=None):
    """performs the ideal kernel between the labels vectors *Y* and *Z*.
    The ideal kernel kernel is defines as:
    .. math:: YT^\top

    Parameters
    ----------
    Y : (n) array_like,
        the train labels vector.
    T : (l) array_like,
        the test labels vector. If it is not defined, then the kernel is calculated
        between *Y* and *Y*.

    Returns
    -------
    K : (l,n) ndarray,
        the ideal kernel matrix.
    """
    if len(Y.unique()) > 2:
        raise exceptions.BinaryProblemError('Ideal kernel works only for binary problems')
    pos = Y[0]
    yy = (Y == pos) * 2 - 1
    tt = yy if (T is None) or (T is Y) else (T == pos) * 2 - 1
    return yy.view(len(yy), 1) @ tt.view(1, len(tt))







