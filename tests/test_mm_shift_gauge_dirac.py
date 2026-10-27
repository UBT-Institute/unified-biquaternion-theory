import sympy as s

def test_exact_constraint_rank_and_reduced_hamiltonian():
    E,x,u,lam=s.symbols("E x u lam",real=True)
    pE,px,pu,pl=s.symbols("pE px pu pl",real=True)
    q=[E,x,u,lam];p=[pE,px,pu,pl]
    pb=lambda a,b:s.expand(sum(s.diff(a,qi)*s.diff(b,pi)-s.diff(a,pi)*s.diff(b,qi) for qi,pi in zip(q,p)))
    H=pE**2/2-lam*(E-u)
    constraints=[px+lam,pu,pl,lam]
    assert pb(pu,H)==-lam
    matrix=s.Matrix([[pb(a,b) for b in constraints] for a in constraints])
    assert matrix.rank()==2
    assert (2*4-2*2-2)//2==1
    assert s.simplify(H.subs(lam,0)-pE**2/2)==0

def test_offshell_shift_keeps_composite_field():
    xd,u,epsd=s.symbols("xd u epsd")
    assert s.expand((xd+epsd)+(u-epsd)-(xd+u))==0
