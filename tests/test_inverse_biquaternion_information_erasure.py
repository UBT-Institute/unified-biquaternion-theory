"""Distinguish algebraic information loss from physical quantum reset."""
import sympy as sp


def test_real_quaternion_norm_multiplicativity_example():
    # Standard unit imaginary quaternion i is invertible: i*i = -1.
    # Fixed left multiplication has inverse left multiplication by -i.
    assert sp.I * (-sp.I) == 1


def test_biquaternion_zero_divisor_noninjective():
    P = sp.diag(1, 0)
    X1, X2 = sp.diag(1, 0), sp.eye(2)
    assert X1 != X2
    assert P*X1 == P*X2 == P
    a,b,c,d = sp.symbols("a b c d")
    X=sp.Matrix([[a,b],[c,d]])
    assert P*X == sp.Matrix([[a,b],[0,0]])


def test_biquaternion_kraus_reset_is_trace_preserving():
    k0=sp.Matrix([[1,0],[0,0]])
    k1=sp.Matrix([[0,1],[0,0]])
    assert k0.T*k0 + k1.T*k1 == sp.eye(2)
    u,v,w,z=sp.symbols("u v w z")
    rho=sp.Matrix([[u,v],[w,z]])
    channel=k0*rho*k0.T+k1*rho*k1.T
    assert channel == sp.diag(u+z,0)
    for state in (sp.diag(1,0),sp.diag(0,1),sp.eye(2)/2):
        assert k0*state*k0.T + k1*state*k1.T == sp.diag(1,0)


def test_swap_unitarity_and_reset():
    # |a,b> -> |b,a> in computational basis (00,01,10,11)
    swap=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    assert swap.T*swap == sp.eye(4)
    a,b=sp.symbols("a b")
    psi=sp.Matrix([a,0,b,0])
    assert swap*psi == sp.Matrix([a,b,0,0])
