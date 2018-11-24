from bayesnet import xp
from bayesnet.optimizer.optimizer import Optimizer


class AdaDelta(Optimizer):
    """
    AdaDelta optimizer
    """

    def __init__(self, parameter, rho=0.95, epsilon=1e-8):
        super().__init__(parameter, None)
        self.rho = rho
        self.epsilon = epsilon
        self.mean_squared_deriv = []
        self.mean_squared_update = []
        for p in self.parameter:
            self.mean_squared_deriv.append(xp.zeros(p.shape))
            self.mean_squared_update.append(xp.zeros(p.shape))

    def update(self):
        self.increment_iteration()
        for p, msd, msu in zip(self.parameter, self.mean_squared_deriv, self.mean_squared_update):
            if p.grad is None:
                continue
            grad = p.grad
            msd *= self.rho
            msd += (1 - self.rho) * grad ** 2
            delta = xp.sqrt((msu + self.epsilon) / (msd + self.epsilon)) * grad
            msu *= self.rho
            msu *= (1 - self.rho) * delta ** 2
            p.value -= delta
