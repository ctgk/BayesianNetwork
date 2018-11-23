from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function


class ReLU(Function):
    """
    Rectified Linear Unit
    y = max(x, 0)
    """

    def forward(self, x):
        x = self._convert2tensor(x)
        self.x = x
        output = x.value.clip(min=0)
        if isinstance(x, Constant):
            return Constant(output)
        return Tensor(output, parent=self)

    def backward(self, delta):
        dx = (self.x.value > 0) * delta
        self.x.backward(dx)


def relu(x):
    """
    Rectified Linear Unit
    y = max(x, 0)
    """
    return ReLU().forward(x)
