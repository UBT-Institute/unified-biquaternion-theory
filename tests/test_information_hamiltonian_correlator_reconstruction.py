import sympy as s

def test_bell_entropy_history_cannot_reconstruct_h():
    t,w=s.symbols('t w',real=True)
    v=s.Matrix([s.exp(-s.I*w*t)/s.sqrt(2),0,0,s.exp(s.I*w*t)/s.sqrt(2)])
    XX=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.Matrix([[0,1],[1,0]]))
    correl=s.simplify((s.conjugate(v).T*XX*v)[0])
    assert s.trigsimp(s.expand_complex(correl)-s.cos(2*w*t))==0
    # Both reduced density matrices stay maximally mixed.
    assert s.simplify(v[0]*s.conjugate(v[0]))==s.Rational(1,2)
    assert s.simplify(v[3]*s.conjugate(v[3]))==s.Rational(1,2)

def test_inverse_commutator_reconstructs_only_offdiagonal_h():
    p,q,k=s.symbols('p q k',real=True)
    rho=s.diag(p,q)
    H=s.Matrix([[0,k],[k,0]])
    drho=-s.I*(H*rho-rho*H)
    assert s.simplify(s.I*drho[0,1]/(q-p)-k)==0
    a,b=s.symbols('a b',real=True)
    assert s.diag(a,b)*rho-rho*s.diag(a,b)==s.zeros(2)
