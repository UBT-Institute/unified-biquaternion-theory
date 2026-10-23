#!/usr/bin/env python3
"""Conditional auxiliary-action test: exact SymPy plus Python Fraction checks.

This does not select a UBT action, prove a physical spectrum, or establish
stability. The generic proof and independent-variable assumptions are in
auxiliary_action.en.md / auxiliary_action.cs.md. Lean is pending.
"""
import json
import platform
from fractions import Fraction as Q
from pathlib import Path
import sympy as s


def fraction_det(matrix):
    """Independent determinant by exact Gaussian elimination; no CAS."""
    m = [[Q(v) for v in row] for row in matrix]
    n = len(m)
    determinant = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if m[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            m[pivot], m[j] = m[j], m[pivot]
            determinant = -determinant
        value = m[j][j]
        determinant *= value
        for i in range(j+1, n):
            ratio = m[i][j]/value
            for k in range(j+1, n):
                m[i][k] -= ratio*m[j][k]
    return determinant


def fraction_coefficient(values, degree):
    """Coefficient from exact Lagrange interpolation at integer nodes."""
    answer = Q(0)
    for i, val in enumerate(values):
        poly = [Q(1)]
        denom = Q(1)
        for j in range(len(values)):
            if i == j:
                continue
            prod = [Q(0)]*(len(poly)+1)
            for k, c in enumerate(poly):
                prod[k] -= j*c
                prod[k+1] += c
            poly = prod
            denom *= i-j
        answer += val*poly[degree]/denom
    return answer


def verify():
    checks = []

    def exact(name, expression, channel='SymPy'):
        vals = list(expression) if isinstance(expression, (list, tuple, s.MatrixBase)) else [expression]
        passed = all(s.simplify(v) == 0 for v in vals) if channel == 'SymPy' else all(v == 0 for v in vals)
        checks.append({'name':name, 'channel':channel, 'passed':passed})
        if not passed:
            raise AssertionError(name)

    eta = s.diag(-1, 1, 1, 1)
    X = s.Matrix(s.symbols('X0:4'))
    Y = s.Matrix(s.symbols('Y0:4'))
    q = (X.T*eta*X)[0]
    dw = (X.T*eta*Y)[0]/q
    perp = Y-dw*X
    lowX, lowP = eta*X, eta*perp
    dK = (lowP*lowX.T-lowX*lowP.T)/q
    exact('generic_Lorentz_antisymmetry', dK+dK.T)
    exact('generic_nonnull_right_inverse', eta*dK*X+dw*X-Y)

    # A full coframe: four columns E plus a fixed nonzero one-form u.
    v = s.symbols('v0:4')
    E = s.eye(4).col_join(s.Matrix([v]))
    u = s.Matrix([0, 0, 0, 0, 1])
    coframe = E.row_join(u)
    eta5 = s.diag(-1, 1, 1, 1, 1)
    metric = coframe*eta5*coframe.T
    exact('self_contracted_kinetic_trace', s.trace(metric.inv()*(E*eta*E.T))-4)
    eps, F = s.symbols('eps F')
    scaling_density = F*((1+eps)*E).row_join(u).det()
    exact('four_column_scale_variation', s.diff(scaling_density, eps).subs(eps, 0)-4*F*coframe.det())

    # Stationary critical potential: neither delta E nor its derivatives
    # enter the quadratic coefficient. H is only a test Hessian.
    H = s.Matrix([[2, 1, 0, 0], [1, 3, 0, 0], [0, 0, 5, 0], [0, 0, 0, 7]])
    dx = s.Matrix([1, -2, 3, -1])
    delta = s.Matrix([[2,1,0,-1], [0,1,2,0], [1,0,-1,1], [0,2,0,1], [3,0,1,-2]])
    base = s.Matrix([[2,1,0,0], [0,1,1,0], [0,0,3,1], [1,0,0,2], [1,2,3,4]])
    f2 = -(dx.T*H*dx)[0]/2
    density = s.expand(eps**2*f2*(base+eps*delta).row_join(u).det())
    expected = f2*base.row_join(u).det()
    exact('critical_background_quadratic_density', density.coeff(eps, 2)-expected)

    signs = [-1, 1, 1, 1]
    witness_count = 0
    for x in [[2,1,0,0], [1,2,3,4], [3,-1,1,0]]:
        norm = sum(signs[i]*x[i]*x[i] for i in range(4))
        for y in [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1], [2,-3,1,5]]:
            w = Q(sum(signs[i]*x[i]*y[i] for i in range(4)), norm)
            p = [Q(y[i])-w*x[i] for i in range(4)]
            klow = [[Q(signs[i]*p[i]*signs[j]*x[j]-signs[i]*x[i]*signs[j]*p[j], norm)
                     for j in range(4)] for i in range(4)]
            obtained = [sum(signs[i]*klow[i][j]*x[j] for j in range(4))+w*x[i] for i in range(4)]
            exact('fraction_right_inverse_'+str(witness_count), [obtained[i]-y[i] for i in range(4)], 'Python Fraction')
            witness_count += 1

    b = [[int(base[i,j]) for j in range(4)]+[int(u[i])] for i in range(5)]
    de = [[int(delta[i,j]) for j in range(4)]+[0] for i in range(5)]
    values = []
    for n in range(7):
        mat = [[b[i][j]+n*de[i][j] for j in range(5)] for i in range(5)]
        values.append(Q(int(f2))*n*n*fraction_det(mat))
    exact('fraction_interpolated_quadratic_density', fraction_coefficient(values, 2)-Q(int(f2))*fraction_det(b), 'Python Fraction')
    scale_values = [fraction_det([[b[i][j]*(1+n) if j<4 else b[i][j] for j in range(5)] for i in range(5)]) for n in range(5)]
    exact('fraction_interpolated_scale_variation', fraction_coefficient(scale_values, 1)-4*fraction_det(b), 'Python Fraction')
    return {'passed':all(c['passed'] for c in checks), 'checks_count':len(checks), 'checks':checks,
            'python':platform.python_version(), 'sympy':s.__version__,
            'scope':'Nonnull split-jet auxiliary candidate with equal kinetic/metric pairing, full composite volume variation, fixed u, smooth algebraic V.',
            'not_tested':'UBT action origin, all complex field modes, constrained or derivative-dependent jet functionals, physical mode quotient, stability, data.',
            'lean_status':'LEAN-PENDING: lean and lake executables were unavailable in this runtime; generic differential-geometric claims have not been formalized.'}


if __name__ == '__main__':
    result = verify()
    Path(__file__).with_name('auxiliary_action_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['passed','checks_count','python','sympy']}))
