import numpy as np
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function


class Trace(Function):

    def forward(self, x):
        x = self._convert2tensor(x)
        self._is_equal_to_ndim(x, 2)
        self.x = x
        output = np.trace(x.value)
        if isinstance(self.x, Constant):
            return Constant(output)
        return Tensor(output, function=self)

    def backward(self, delta):
        dx = np.eye(self.x.shape[0], self.x.shape[1]) * delta
        self.x.backward(dx)


def trace(x):
    return Trace().forward(x)
