import numpy as np
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function


class Inverse(Function):

    def forward(self, x):
        x = self._convert2tensor(x)
        self.x = x
        self._is_equal_to_ndim(x, 2)
        self.output = np.linalg.inv(x.value)
        if isinstance(self.x, Constant):
            return Constant(self.output)
        return Tensor(self.output, parent=self)

    def backward(self, delta):
        dx = -self.output.T @ delta @ self.output.T
        self.x.backward(dx)


def inv(x):
    """
    inverse of a matrix

    Parameters
    ----------
    x : (d, d) tensor_like
        a matrix to be inverted

    Returns
    -------
    output : (d, d) tensor_like
        inverse of the input
    """
    return Inverse().forward(x)
