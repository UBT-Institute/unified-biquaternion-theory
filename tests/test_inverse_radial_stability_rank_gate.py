"""Conditional radial stability and rank gate on the auxiliary connection branch."""
import sympy as sp

c,A,r,rho,p,g2,k2=sp.symbols("c A r rho p g2 k2",real=True)
energy=p*p/(4*c)+c*g2+A*(rho*rho-r*r)**2

def test_exact_canonical_radial_legendre():
    v=sp.symbols("v",real=True)
    lag=c*v*v-A*(rho*rho-r*r)**2
    pi=sp.diff(lag,v)
    h=sp.expand((pi*v-lag).subs(v,p/(2*c)))
    assert sp.simplify(h-(p*p/(4*c)+A*(rho*rho-r*r)**2))==0

def test_positive_vacuum_and_mass():
    assert sp.simplify(energy.subs({rho:r,p:0,g2:0}))==0
    hess=sp.diff(A*(rho*rho-r*r)**2,rho,2)
    assert sp.expand(hess.subs(rho,r))==8*A*r*r
    # L=c[(d_t rho)^2-|grad rho|²]-U; m² = U''/(2c).
    assert sp.simplify(hess.subs(rho,r)/(2*c)-4*A*r*r/c)==0

def test_nonnegative_energy_samples():
    for C in (sp.Rational(1,4),1,4):
        for aa in (sp.Rational(1,7),2):
            for R in (1,sp.Rational(3,2)):
                for x in (0,R,2*R):
                    for pp in (-2,0,3):
                        for gg in (0,3):
                            assert energy.subs({c:C,A:aa,r:R,rho:x,p:pp,g2:gg})>=0

def test_composite_rank_one_reproduces_no_metric():
    e=sp.Matrix([[1,0,0,0]]).T*sp.Matrix([[3,2,0,1]])
    assert e.rank()==1
    eta=sp.diag(-1,1,1,1)
    metric=e.T*eta*e
    assert metric.rank()<=1
    assert metric.det()==0
    # All possible 2x2 minors of a generic outer product vanish.
    u=sp.symbols("u0:4",real=True)
    v=sp.symbols("v0:4",real=True)
    E=sp.Matrix(u)*sp.Matrix([v])
    assert all(sp.expand(E[i,j]*E[k,l]-E[i,l]*E[k,j])==0
               for i in range(4) for k in range(i+1,4)
               for j in range(4) for l in range(j+1,4))
