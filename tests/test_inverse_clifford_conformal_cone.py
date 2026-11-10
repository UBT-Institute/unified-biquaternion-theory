"""Exact 3+1D Dirac principal-symbol and conformal-ambiguity checks."""
import sympy as s

I=s.I
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
e=s.eye(2)
z=s.zeros(2)
gamma=[s.diag(1,1,-1,-1)]
for sigma in (sx,sy,sz):
    gamma.append(s.BlockMatrix([[z,sigma],[-sigma,z]]).as_explicit())


def test_clifford_relations():
    for a in range(4):
        for b in range(4):
            expected=2*(1 if a==b==0 else -1 if a==b else 0)*s.eye(4)
            assert gamma[a]*gamma[b]+gamma[b]*gamma[a]==expected


def test_dirac_symbol_determinant():
    p=s.symbols("p0:4",real=True)
    symbol=sum((p[i]*gamma[i] for i in range(4)),s.zeros(4))
    q=p[0]**2-sum(p[i]**2 for i in range(1,4))
    assert s.factor(symbol.det()-q**2)==0


def test_conformal_symbol_keeps_characteristics():
    p=s.symbols("p0:4",real=True)
    lam=s.symbols("lam",positive=True)
    symbol=sum((p[i]*gamma[i] for i in range(4)),s.zeros(4))
    q=p[0]**2-sum(p[i]**2 for i in range(1,4))
    assert s.factor((lam*symbol).det()-lam**4*q**2)==0


def test_conformal_curvature_differs_from_flat():
    x,alpha=s.symbols("x alpha",real=True)
    Omega=1+alpha*x**2
    # g'_cov=Omega^2 eta; □eta Omega = - d²_x Omega.
    R=-6*Omega**(-3)*(-s.diff(Omega,x,2))
    assert s.simplify(R-12*alpha/Omega**3)==0
    assert s.simplify(R.subs(alpha,0))==0
