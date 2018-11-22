from bayesnet.math.add import add
from bayesnet.math.divide import divide, rdivide
from bayesnet.math.exp import exp
from bayesnet.math.log import log
from bayesnet.math.matmul import matmul, rmatmul
from bayesnet.math.mean import mean
from bayesnet.math.multiply import multiply
from bayesnet.math.nansum import nansum
from bayesnet.math.negative import negative
from bayesnet.math.power import power, rpower
from bayesnet.math.product import prod
from bayesnet.math.sqrt import sqrt
from bayesnet.math.square import square
from bayesnet.math.subtract import subtract, rsubtract
from bayesnet.math.sum import sum


from bayesnet.tensor.tensor import Tensor
Tensor.__add__ = add
Tensor.__radd__ = add
Tensor.__truediv__ = divide
Tensor.__rtruediv__ = rdivide
Tensor.mean = mean
Tensor.__matmul__ = matmul
Tensor.__rmatmul__ = rmatmul
Tensor.__mul__ = multiply
Tensor.__rmul__ = multiply
Tensor.__neg__ = negative
Tensor.__pow__ = power
Tensor.__rpow__ = rpower
Tensor.prod = prod
Tensor.__sub__ = subtract
Tensor.__rsub__ = rsubtract
Tensor.sum = sum


__all__ = [
    "add",
    "divide",
    "exp",
    "log",
    "matmul",
    "mean",
    "multiply",
    "nansum",
    "power",
    "prod",
    "sqrt",
    "square",
    "subtract",
    "sum"
]
