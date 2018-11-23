import scipy.special as sp
from bayesnet.function import Function
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor


class Gamma(Function):

    def forward(self, x):
        x = self._convert2tensor(x)
        self.x = x
        self.output = sp.gamma(x.value)
        if isinstance(x, Constant):
            return Constant(self.output)
        return Tensor(self.output, parent=self)

    def backward(self, delta):
        dx = delta * self.output * sp.digamma(self.x.value)
        self.x.backward(dx)


def gamma(x):
    """
    element-wise gamma function
    """
    return Gamma().forward(x)
