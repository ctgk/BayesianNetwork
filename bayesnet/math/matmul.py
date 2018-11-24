from bayesnet import xp
from bayesnet.array.broadcast import broadcast_to
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function


class MatMul(Function):
    """
    Matrix multiplication function
    """
    enable_auto_broadcast = True

    def _autobroadcast(self, args):
        x, y = args[0], args[1]
        self._assert_ndim_atleast(x, 2)
        self._assert_ndim_atleast(y, 2)
        if x.shape[-1] != y.shape[-2]:
            raise ValueError(
                "shapes {} and {} not aligned: {} (dim -1) != {} (dim -2)"
                .format(x.shape, y.shape, x.shape[-1], y.shape[-2])
            )
        if x.shape[:-2] != y.shape[:-2]:
            shape = xp.broadcast(x[..., 0, 0], y.value[..., 0, 0]).shape
            if x.shape[:-2] != shape:
                x = broadcast_to(x, shape + x.shape[-2:])
            if y.shape[:-2] != shape:
                y = broadcast_to(y, shape + y.shape[-2:])
        return [x, y]

    @staticmethod
    def _forward(x, y):
        return x @ y

    @staticmethod
    def _backward(delta, x, y):
        dx = delta @ xp.swapaxes(y, -1, -2)
        dy = xp.swapaxes(x, -1, -2) @ delta
        return dx, dy


def matmul(x, y):
    return MatMul().forward(x, y)


def rmatmul(x, y):
    return MatMul().forward(y, x)
