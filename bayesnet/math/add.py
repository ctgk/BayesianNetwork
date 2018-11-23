import numpy as np
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function
from bayesnet.array.broadcast import broadcast_to


class Add(Function):
    """
    add arguments element-wise
    """

    def _check_input(self, x, y):
        x = self._convert2tensor(x)
        y = self._convert2tensor(y)
        if x.shape != y.shape:
            shape = np.broadcast(x.value, y.value).shape
            if x.shape != shape:
                x = broadcast_to(x, shape)
            if y.shape != shape:
                y = broadcast_to(y, shape)
        return x, y

    def forward(self, x, y):
        x, y = self._check_input(x, y)
        self.x = x
        self.y = y
        if isinstance(self.x, Constant) and isinstance(self.y, Constant):
            return Constant(x.value + y.value)
        return Tensor(x.value + y.value, parent=self)

    def backward(self, delta):
        dx = delta
        dy = delta
        self.x.backward(dx)
        self.y.backward(dy)


def add(x, y):
    return Add().forward(x, y)
