#!/usr/bin/env python3
"""Exact scoped RH-to-UBT spectral-gap and critical-composite-pole diagnostics.

Finite-dimensional intertwiners and a massive scalar-bubble response ansatz
only. Neither arithmetic theta-lift validation nor a UBT spin-two action.
"""
import sympy as s


def intertwining_gap_gate():
    source = s.diag(0, 2, 3, 6)
    target = s.diag(0, 1, 2, 3, 6)
    variables = s.symbols("x0:20")
    T = s.Matrix(5, 4, variables)
    solutions = s.linsolve(list(target*T-T*source), variables)
    assert isinstance(solutions, s.FiniteSet)
    general = T.subs(dict(zip(variables, next(iter(solutions)))))
    assert general.row(1) == s.zeros(1, 4)
    assert general[0, 0] == variables[0]
    assert general[2, 1] == variables[9]
    assert general[3, 2] == variables[14]
    assert general[4, 3] == variables[19]
    tau = s.symbols("tau", positive=True)
    heat = s.diag(*(s.exp(-tau*source[j, j]) for j in range(4)))
    vector = s.Matrix([0, 1, 1, 1])
    assert (heat*vector)[0] == 0
    assert target*general-general*source == s.zeros(5, 4)
    print("PASS exact intertwiner: target energy-1 gap state receives no image")


def massive_bubble_criticality_gate():
    x, z, mass, momentum2, delta = s.symbols(
        "x z mass momentum2 delta", positive=True, real=True
    )
    moments = [s.integrate((x*(1-x))**j, (x, 0, 1))
               for j in (1, 2, 3)]
    assert moments == [s.Rational(1, 6), s.Rational(1, 30),
                       s.Rational(1, 140)]
    series = sum((-1)**(j+1)*moments[j-1]*z**j/j for j in (1, 2, 3))
    assert s.expand(series) == (
        z/6-z*z/60+z**3/420
    )
    # Finite subtracted massive scalar bubble, Euclidean momentum squared.
    D = s.expand(series.subs(z, momentum2/mass**2)/(16*s.pi**2))
    assert s.simplify(s.diff(D, momentum2).subs(momentum2, 0)) == (
        1/(96*s.pi**2*mass**2)
    )
    critical = 1/D
    residue = s.limit(momentum2*critical, momentum2, 0, dir="+")
    assert s.simplify(residue) == 96*s.pi**2*mass**2
    detuned = 1/(delta+D)
    assert s.limit(detuned, momentum2, 0, dir="+") == 1/delta
    assert s.limit(momentum2*detuned, momentum2, 0, dir="+") == 0
    # x(1-x) has maximum 1/4: the two-mass threshold is 4*m^2.
    assert s.maximum(x*(1-x), x, s.Interval(0, 1)) == s.Rational(1, 4)
    assert s.simplify(1/(moments[0]/(16*s.pi**2*mass**2))) == residue
    print("PASS massive-bubble critical residue 96*pi^2*m^2, threshold 4*m^2")
    print("PASS generic positive detuning removes the massless pole")


def massless_free_bubble_negative_control():
    momentum2, mu2 = s.symbols("momentum2 mu2", positive=True, real=True)
    subtracted = -s.log(momentum2/mu2)/(16*s.pi**2)
    assert s.limit(momentum2*subtracted, momentum2, 0, dir="+") == 0
    print("PASS free massless bubble has no isolated 1/p^2 residue")



def rotational_symmetry_does_not_protect_criticality_gate():
    x, y, z, detune = s.symbols("x y z detune", real=True)
    plus = (x*x-y*y)/2
    cross = x*y
    Lz = lambda expr: x*s.diff(expr, y)-y*s.diff(expr, x)
    assert s.simplify(Lz(plus*plus+cross*cross)) == 0
    assert s.simplify(plus*plus+cross*cross-(x*x+y*y)**2/4) == 0
    vector = s.Matrix([x,y,z])
    norm2 = vector.dot(vector)
    traceless = vector*vector.T-s.eye(3)*norm2/3
    assert s.simplify(s.trace(traceless*traceless)
                      -s.Rational(2,3)*norm2*norm2) == 0
    assert s.simplify(Lz(detune*(plus*plus+cross*cross))) == 0
    print("PASS rotational spin-two channel allows arbitrary scalar detuning")

if __name__ == "__main__":
    intertwining_gap_gate()
    massive_bubble_criticality_gate()
    massless_free_bubble_negative_control()
    rotational_symmetry_does_not_protect_criticality_gate()
    print("SCOPE: scalar RPA-response benchmark, NOT derived physical UBT graviton")
