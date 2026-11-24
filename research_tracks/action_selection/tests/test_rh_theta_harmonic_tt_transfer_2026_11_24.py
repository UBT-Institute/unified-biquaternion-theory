"""Exact toy tests: harmonic Gaussian TT obstruction and oscillator spin-two.

These are NOT tests of the arithmetic automorphic theta lift or full UBT gravity.
"""
import itertools
import sympy as s


def test_isotropic_gaussian_traceless_hessian_and_tt_projection():
    a, k = s.symbols("a k", positive=True, real=True)
    x, y, z = s.symbols("x y z", real=True)
    vec = s.Matrix([x, y, z])
    f = s.exp(-a * vec.dot(vec))
    h = s.hessian(f, vec)
    K = s.simplify(h - s.eye(3) * s.trace(h) / 3)
    expected = 4 * a*a * f * (vec*vec.T - s.eye(3)*vec.dot(vec)/3)
    assert s.simplify(K-expected) == s.zeros(3)
    at_kz = s.simplify(K.subs({x: 0, y: 0, z: k}))
    P = s.diag(1, 1, 0)
    tt = s.simplify(P*at_kz*P-P*s.trace(P*at_kz)/2)
    assert tt == s.zeros(3)
    assert s.simplify(at_kz[0, 0]-at_kz[1, 1]) == 0
    assert at_kz[0, 1] == 0


def test_weight_two_oscillator_pair_and_gap():
    x, y, z = s.symbols("x y z", real=True)
    qp = (x*x-y*y)/2
    qx = x*y
    Lz = lambda obj: s.expand(x*s.diff(obj, y)-y*s.diff(obj, x))
    assert Lz(qp) == -2*qx
    assert Lz(qx) == 2*qp
    r2=x*x+y*y+z*z
    vacuum=s.exp(-r2/2)
    H=lambda obj:s.simplify(-sum(s.diff(obj,t,2) for t in (x,y,z))/2+r2*obj/2)
    assert s.simplify(H(vacuum)-s.Rational(3,2)*vacuum)==0
    for q in (qp,qx):
        assert s.simplify(H(q*vacuum)-s.Rational(7,2)*q*vacuum)==0


def test_finite_cubic_theta_harmonic_tensor_cancels():
    for radius in (1, 2):
        T=s.zeros(3)
        for v in itertools.product(range(-radius, radius+1), repeat=3):
            n=s.Matrix(v)
            norm=int(n.dot(n))
            T+=(n*n.T-s.eye(3)*s.Rational(norm,3))*s.Rational(1,2**norm)
        assert T == s.zeros(3)


def test_transverse_vector_bilinear_can_have_nonzero_tt():
    # An independent transverse vector supplies extra directional information;
    # its bilinear has a TT component, but is quadratic at the isotropic origin.
    v=s.Matrix([1, 0, 0])
    Q=v*v.T-s.eye(3)*v.dot(v)/3
    P=s.diag(1, 1, 0)
    TT=s.simplify(P*Q*P-P*s.trace(P*Q)/2)
    assert TT==s.diag(s.Rational(1,2),-s.Rational(1,2),0)
    eps=s.symbols("eps", real=True)
    Qeps=(eps*v)*(eps*v).T-s.eye(3)*(eps*v).dot(eps*v)/3
    assert s.simplify(Qeps.diff(eps).subs(eps,0))==s.zeros(3)
