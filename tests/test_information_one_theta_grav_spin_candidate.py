import sympy as s

def test_theta_dirac_hamiltonian_factorization():
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    A=[s.diag(-1,1).kronecker_product(x) if hasattr(s.diag(-1,1),'kronecker_product') else s.kronecker_product(s.diag(-1,1),x) for x in sig]
    Z=s.zeros(2);B=s.BlockMatrix([[Z,s.eye(2)],[s.eye(2),Z]]).as_explicit()
    p=s.symbols('p0:3',real=True);m=s.symbols('m',real=True)
    H=sum((A[i]*p[i] for i in range(3)),s.zeros(4))+m*B
    assert s.simplify(H*H-(sum(t*t for t in p)+m*m)*s.eye(4))==s.zeros(4)

def test_mass_is_real_determinant():
    u0,u1,v0,v1=s.symbols("u0 u1 v0 v1",complex=True)
    u=s.Matrix([u0,u1]);v=s.Matrix([v0,v1]);eps=s.Matrix([[0,1],[-1,0]])
    R=eps*v.conjugate()
    assert s.simplify((R.conjugate().T*u)[0]-s.Matrix.hstack(u,v).det())==0
