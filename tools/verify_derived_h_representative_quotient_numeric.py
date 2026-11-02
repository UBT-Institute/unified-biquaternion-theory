#!/usr/bin/env python3
"""Independent source-field roundtrips and finite representative replacements.

NumPy and finite differences; no import of the symbolic test implementation.
These checks do not prove the continuum quotient or a canonical Dirac count.
"""
from __future__ import annotations
import json
import numpy as np

ETA = np.diag([-1., 1., 1., 1.])
SCALE = 1.4
SLOPES = {-1: np.diag([1., .2, .3, .4]), 1: np.diag([.2, .3, .4, 1.])}
OFFSETS = {-1: np.array([2., 0., 0., 0.]), 1: np.array([0., 0., 0., 2.])}


def generator(a, b):
    result = np.zeros((4, 4))
    result[a, b] = 1.
    result[b, a] = -ETA[a, a]/ETA[b, b]
    return result


GENERATORS = [generator(a, b) for a in range(4) for b in range(a+1, 4)]


def image_inverse(y, value):
    q = y@ETA@y
    lower_y, lower_value = ETA@y, ETA@value
    return ETA@(np.outer(lower_value, lower_y)-np.outer(lower_y, lower_value))/q


def frame(y):
    q = y@ETA@y
    n = y/np.sqrt(abs(q))
    if q < 0:
        assert n[0] > 0
        result = np.eye(4)
        result[0, 0] = n[0]
        result[0, 1:] = result[1:, 0] = n[1:]
        result[1:, 1:] += np.outer(n[1:], n[1:])/(1+n[0])
        return result
    spatial_length = np.linalg.norm(n[1:])
    unit = n[1:]/spatial_length
    cross = np.cross(np.array([0., 0., 1.]), unit)
    cross_matrix = np.array([[0., -cross[2], cross[1]],
                             [cross[2], 0., -cross[0]],
                             [-cross[1], cross[0], 0.]])
    rotation = np.eye(4)
    rotation[1:, 1:] += cross_matrix+cross_matrix@cross_matrix/(1+unit[2])
    boost = np.eye(4)
    boost[0, 0] = spatial_length
    boost[0, 1:] = boost[1:, 0] = n[0]*unit
    boost[1:, 1:] += (spatial_length-1)*np.outer(unit, unit)
    return boost@rotation


def original(point, sign, coefficients):
    y = OFFSETS[sign]+SLOPES[sign]@point
    h = np.exp(.17*point[0]+.11*point[1]*point[2])
    matrices = []
    for mu in range(4):
        matrices.append(sum((.004*coefficients[mu, j]*np.cos((j+1)*point[mu]+.2*j)*g
                             for j, g in enumerate(GENERATORS)), np.zeros((4, 4))))
    e = np.vstack([h/SCALE*(SLOPES[sign][:, mu]+matrices[mu]@y) for mu in range(4)])
    return h, y, matrices, e


def radial_data(point, sign, amplitude=0., direction=None):
    y = OFFSETS[sign]+SLOPES[sign]@point
    r = y@ETA@y
    dr = 2*SLOPES[sign].T@ETA@y
    if amplitude:
        angle = direction@point+.3
        r += amplitude*np.sin(angle)
        dr += amplitude*np.cos(angle)*direction
    return r, dr


def classified_fields(point, sign, coefficients, amplitude=0., direction=None):
    e = original(point, sign, coefficients)[3]
    r, dr = radial_data(point, sign, amplitude, direction)
    metric = e@ETA@e.T
    k = dr@np.linalg.solve(metric, dr)
    assert r*k > 0
    h = 2*SCALE*np.sqrt(r/k)
    y = h/(2*SCALE)*ETA@np.linalg.solve(e, dr)
    return h, y, e


def derivative_of_classified_y(point, sign, coefficients, amplitude, direction, step):
    values = []
    for mu in range(4):
        shift = np.eye(4)[mu]*step
        plus = classified_fields(point+shift, sign, coefficients, amplitude, direction)[1]
        minus = classified_fields(point-shift, sign, coefficients, amplitude, direction)[1]
        values.append((plus-minus)/(2*step))
    return values


def check():
    rng = np.random.default_rng(20261103)
    samples, step = 96, 1e-5
    error = dict(h=0., y=0., original_A=0., finite_tetrad=0.,
                 stabilizer=0., frame=0., finite_composition=0.)
    for sign in (-1, 1):
        for _ in range(samples):
            point = rng.uniform(-.25, .25, 4)
            coefficients = rng.uniform(-1., 1., (4, 6))
            old_h, old_y, old_a, e = original(point, sign, coefficients)
            h, y, _ = classified_fields(point, sign, coefficients)
            error['h'] = max(error['h'], abs(h-old_h))
            error['y'] = max(error['y'], np.max(abs(y-old_y)))
            b = frame(y)
            inverse_b = np.linalg.inv(b)
            error['frame'] = max(error['frame'], np.max(abs(b.T@ETA@b-ETA)))
            fixed_z = []
            for mu in range(4):
                z = old_a[mu]-image_inverse(y, old_a[mu]@y)
                fixed_z.append(inverse_b@z@b)
                error['stabilizer'] = max(error['stabilizer'], np.max(abs(z@y)))
            # Source-to-target-to-source, using independently differentiated Y.
            derivatives = derivative_of_classified_y(point, sign, coefficients, 0., None, step)
            for mu in range(4):
                t = SCALE/h*e[mu]-derivatives[mu]
                recovered = image_inverse(y, t)+b@fixed_z[mu]@inverse_b
                error['original_A'] = max(error['original_A'], np.max(abs(recovered-old_a[mu])))
            # A finite change of the radial label at identical entire tetrad.
            direction = rng.uniform(-1., 1., 4)
            amplitude = .003
            new_h, new_y, new_e = classified_fields(point, sign, coefficients, amplitude, direction)
            new_derivatives = derivative_of_classified_y(point, sign, coefficients, amplitude, direction, step)
            new_b, new_inverse_b = frame(new_y), np.linalg.inv(frame(new_y))
            recovered_labels = []
            for mu in range(4):
                t = SCALE/new_h*new_e[mu]-new_derivatives[mu]
                a = image_inverse(new_y, t)+new_b@fixed_z[mu]@new_inverse_b
                rebuilt = new_h/SCALE*(new_derivatives[mu]+a@new_y)
                error['finite_tetrad'] = max(error['finite_tetrad'], np.max(abs(rebuilt-e[mu])))
                z = a-image_inverse(new_y, a@new_y)
                recovered_labels.append(new_inverse_b@z@new_b)
                error['stabilizer'] = max(error['stabilizer'], np.max(abs(z@new_y)))
            # Composition depends on final labels, not the intermediate field.
            final_h, final_y, _ = classified_fields(point, sign, coefficients, 2*amplitude, direction)
            final_derivatives = derivative_of_classified_y(point, sign, coefficients, 2*amplitude, direction, step)
            final_b = frame(final_y)
            for mu in range(4):
                t = SCALE/final_h*e[mu]-final_derivatives[mu]
                direct = image_inverse(final_y, t)+final_b@fixed_z[mu]@np.linalg.inv(final_b)
                composed = image_inverse(final_y, t)+final_b@recovered_labels[mu]@np.linalg.inv(final_b)
                error['finite_composition'] = max(error['finite_composition'], np.max(abs(direct-composed)))
    assert max(error.values()) < 2e-7, error
    return {'samples_per_sign': samples, 'normal_signs': [-1, 1],
            'finite_difference_step': step, 'absolute_tolerance': 2e-7,
            'numpy': np.__version__, 'max_errors': error, 'result': 'PASS',
            'scope': 'Finite source-field roundtrips and finite representative changes; no continuum or Dirac-count verification.'}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
