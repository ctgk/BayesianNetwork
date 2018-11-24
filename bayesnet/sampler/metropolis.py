import random
from bayesnet import xp
from bayesnet.network import Network
from bayesnet.random.random import RandomVariable


def metropolis(model, call_args, sample_size=100, downsample=1, **kwargs):

    if not isinstance(model, Network):
        raise TypeError("model must be Network object")

    def run_model():
        if isinstance(call_args, tuple):
            model(*call_args)
        elif isinstance(call_args, dict):
            model(**call_args)
        else:
            raise TypeError("call_args must be tuple or dict")

    sample = dict()
    previous = dict()
    proposal = kwargs
    variable = model.parameter

    for key in variable:
        sample[key] = []
        if key not in proposal:
            raise TypeError(f"metropolis expected {key} argument")
        elif not isinstance(proposal[key], RandomVariable):
            raise TypeError(f"{key} argument must be RandomVariable")

    run_model()
    log_posterior = model.log_pdf().value

    for _ in range(sample_size // 10):
        for key, v in variable.items():
            previous[key] = v.value
            v.value = v.value + proposal[key].draw().value
        run_model()
        log_posterior_new = model.log_pdf().value

        accept_proba = xp.exp(log_posterior_new - log_posterior)
        if random.random() < accept_proba:
            log_posterior = log_posterior_new
        else:
            for key, v in variable.items():
                v.value = previous[key]

    for i in range(1, sample_size * downsample + 1):
        for key, v in variable.items():
            previous[key] = v.value
            v.value = v.value + proposal[key].draw().value
        run_model()
        log_posterior_new = model.log_pdf().value

        accept_proba = xp.exp(log_posterior_new - log_posterior)
        if random.random() < accept_proba:
            log_posterior = log_posterior_new
            if i % downsample == 0:
                for key, v in variable.items():
                    sample[key].append(v.value)
        else:
            for key, v in variable.items():
                v.value = previous[key]
                if i % downsample == 0:
                    sample[key].append(v.value)

    return sample
