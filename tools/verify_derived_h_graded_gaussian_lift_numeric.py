#!/usr/bin/env python3
"""Independent finite-difference/NumPy check of the derived-H Gaussian lift.

Uses randomly sampled smooth boosted coframes, not the exact test's rational
matrices or its symbolic derivatives. Does not prove local Gaussian existence,
full constraint reduction, physical stability, or a microscopic action.
"""
from __future__ import annotations
import json
import numpy as np

ETA = np.diag([-1., 1., 1., 1.])
PAULI = (np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.diag([1., -1.]).astype(complex))
BASIS = (1j*np.eye(2),) + tuple(-1j*p for p in PAULI)


def boost(velocity):
    v = np.asarray(velocity)
    norm2 = v@v
    gamma = 1/np.sqrt(1-norm2)
    result = np.eye(4)
    result[0, 0] = gamma
    result[0, 1:] = result[1:, 0] = gamma*v
    result[1:, 1:] += (gamma-1)/norm2*np.outer(v, v)
    return result


def coframe(position, epsilon):
    t, x, y, z = position
    rates = np.array([.13, -.17, .23])
    if epsilon == -1:
        raw = np.diag(np.r_[1., np.exp(rates*t)])
        raw[0, 1:] = .08*np.sin([x+y, y+z, z+x])
    else:
        raw = np.diag(np.r_[np.exp(rates*z), 1.])
    velocity = .12*np.sin([t+x+.3, x+y+.7, y+z+1.1])
    return raw@boost(velocity).T


def carrier(position, epsilon, s, length):
    du = np.eye(4)[:, 0 if epsilon == -1 else 3]
    return s*length*ETA@np.linalg.solve(coframe(position, epsilon), du)


def check():
    random = np.random.default_rng(20261102)
    error = dict(normal=0., orthogonality=0., recovered=0., lorentz=0.,
                 sharp_metric=0., hermitian=0.)
    samples = 128
    s, length, h0, step = 1.7, .8, 1.3, 1e-5
    for epsilon in (-1, 1):
        normal_index = 0 if epsilon == -1 else 3
        du = np.eye(4)[:, normal_index]
        for _ in range(samples):
            point = random.uniform(-.7, .7, 4)
            e = coframe(point, epsilon)
            x = carrier(point, epsilon, s, length)
            q = x@ETA@x
            error['normal'] = max(error['normal'], abs(q-epsilon*s*s*length*length))
            recovered = []
            for mu in range(4):
                displacement = np.eye(4)[mu]*step
                derivative = (carrier(point+displacement, epsilon, s, length)
                              - carrier(point-displacement, epsilon, s, length))/(2*step)
                w = epsilon*du[mu]/length
                residual = s*e[mu]-derivative-w*x
                r_lower, x_lower = ETA@residual, ETA@x
                k_lower = (np.outer(r_lower, x_lower)-np.outer(x_lower, r_lower))/q
                k = ETA@k_lower
                reconstructed = (derivative+k@x+w*x)/s
                recovered.append(reconstructed)
                error['orthogonality'] = max(error['orthogonality'], abs(x@ETA@residual))
                error['lorentz'] = max(error['lorentz'], np.max(abs(k.T@ETA+ETA@k)))
                error['recovered'] = max(error['recovered'], np.max(abs(reconstructed-e[mu])))
            tetrad = [sum((row[a]*BASIS[a] for a in range(4)), np.zeros((2, 2), complex))
                      for row in recovered]
            metric = e@ETA@e.T
            for mu in range(4):
                for nu in range(4):
                    sharp = lambda m: np.trace(m)*np.eye(2)-m
                    central = (sharp(tetrad[mu])@tetrad[nu]+sharp(tetrad[nu])@tetrad[mu])/2
                    error['sharp_metric'] = max(error['sharp_metric'],
                                               np.max(abs(central-metric[mu, nu]*np.eye(2))))
            h = h0*np.exp(-epsilon*point[normal_index]/length)
            theta = h*np.eye(2)+sum((x[a]*BASIS[a] for a in range(4)),
                                   np.zeros((2, 2), complex))
            error['hermitian'] = max(error['hermitian'],
                                     np.max(abs(theta+theta.conj().T-2*h*np.eye(2))))
            assert np.linalg.svd(theta, compute_uv=False).min() >= h-1e-12
    assert max(error.values()) < 2e-8, error
    return {'samples_per_sign': samples, 'normal_signs': [-1, 1],
            'finite_difference_step': step, 'absolute_tolerance': 2e-8,
            'numpy': np.__version__, 'max_errors': error,
            'result': 'PASS', 'scope': 'finite numerical controls only'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
