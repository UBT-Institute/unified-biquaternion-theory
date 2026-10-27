"""First-order finite Fock-state action gives Schrodinger equation."""
import sympy as s

def test_two_complex_amplitudes_euler_lagrange():
    z=s.Matrix(s.symbols('z0:2'))
    zb=s.Matrix(s.symbols('zb0:2'))
    dz=s.Matrix(s.symbols('dz0:2'))
    dzb=s.Matrix(s.symbols('dzb0:2'))
    h=s.Matrix(2,2,s.symbols('h0:4'))
    lam=s.symbols('lam',real=True)
    L=s.I*(zb.dot(dz)-dzb.dot(z))/2-(zb.T*h*z)[0]+lam*(zb.dot(z)-1)
    # E-L for independent adjoints zb: dL/dzb - d/dt (dL/ddzb)
    # L is linear in zb and its first derivative, so total derivative is direct.
    eq=s.Matrix([s.diff(L,zb[j])+s.I*dz[j]/2 for j in range(2)])
    assert s.simplify(eq-(s.I*dz-h*z+lam*z))==s.zeros(2,1)

def test_hermitian_generator_preserves_norm():
    x,y,z=s.symbols('x y z',real=True)
    h=s.Matrix([[x,y+s.I*z],[y-s.I*z,-x]])
    assert h==h.conjugate().T
    phi=s.Matrix(s.symbols('phi0:2',complex=True))
    phidot=-s.I*h*phi
    conservation=(phidot.conjugate().T*phi+phi.conjugate().T*phidot)[0]
    assert s.simplify(conservation)==0
