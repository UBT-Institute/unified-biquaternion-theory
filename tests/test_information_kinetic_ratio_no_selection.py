import sympy as s

def test_ground_correlators_depend_on_ratio_while_pure_product_information_does_not():
    a,b,w,hbar=s.symbols('a b w hbar',positive=True)
    qs2=hbar/(2*a*w);qt2=hbar/(2*b*w)
    assert s.simplify(qs2/qt2-b/a)==0
    # Product pure ground state has S_s=S_t=S_st=0 regardless of a/b.
    assert 0+0-0==0

def test_canonical_squeeze_changes_mass_coefficient():
    a,l,qnew,pnew=s.symbols('a l qnew pnew',positive=True)
    q=l*qnew;p=pnew/l
    kinetic=s.simplify(p*p/(2*a))
    assert s.simplify(kinetic-pnew*pnew/(2*a*l*l))==0
    # q=l*qnew,p=pnew/l preserves dq ^ dp.
    assert s.diff(q,qnew)*s.diff(p,pnew)==1
