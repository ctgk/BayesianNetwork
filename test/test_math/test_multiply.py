import unittest
import numpy as np
import bayesnet as bn


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        x = bn.Parameter(2)
        y = x * 5
        self.assertEqual(y.value, 10)
        y.backward()
        self.assertEqual(x.grad, 5)

        x = np.random.rand(5, 4)
        y = np.random.rand(4)
        yp = bn.Parameter(y)
        z = x * yp
        self.assertTrue((z.value == x * y).all())
        z.backward(np.ones((5, 4)))
        self.assertTrue((yp.grad == x.sum(axis=0)).all())


if __name__ == '__main__':
    unittest.main()
