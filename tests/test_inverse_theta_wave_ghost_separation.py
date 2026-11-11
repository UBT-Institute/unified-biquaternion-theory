"""Fixed-background full complex Theta: wave propagation is not energy stability."""
import sympy as sp

def matrices(l1,l2,r,c):
    K=sp.diag(2,-2,-2,-2,2,-2,-2,-2)
    M=sp.diag(0,8*l2*r*r,8*l2*r*r,8*l2*r*r,
              8*(4*l1+l2)*r*r,0,0,0)
    return c*K,M

def test_all_eight_mode_dispersion_exact():
    l1,l2,r,c,k2=sp.symbols("l1 l2 r c k2",nonzero=True,real=True)
    K,M=matrices(l1,l2,r,c)
    spec=[sp.factor(k2+M[i,i]/K[i,i]) for i in range(8)]
    assert spec==[k2,k2-4*l2*r*r/c,k2-4*l2*r*r/c,
                  k2-4*l2*r*r/c,k2+4*(4*l1+l2)*r*r/c,
                  k2,k2,k2]
    z=sp.symbols("z")
    determinant=sp.factor((K*(k2-z)+M).det())
    expected=sp.factor(K.det()*sp.prod([x-z for x in spec]))
    assert sp.factor(determinant-expected)==0

def test_high_k_real_frequency_but_negative_energy():
    # lambda1=0, lambda2=r=c=1; three transverse ghosts
    K,M=matrices(0,1,1,1)
    k2=9
    assert k2+M[1,1]/K[1,1]==5>0
    # Hamiltonian at q=0 and real nonzero velocity = K_j v²/2.
    assert K[1,1]*1**2/2==-1
    # Oscillatory solution: q(t)=sin(sqrt(5)t)/sqrt(5)
    t=sp.symbols("t",real=True)
    q=sp.sin(sp.sqrt(5)*t)/sp.sqrt(5)
    v=sp.diff(q,t)
    E=sp.simplify(K[1,1]*(v*v+k2*q*q)/2+M[1,1]*q*q/2)
    assert sp.simplify(E+1)==0

def test_negative_c_radial_ghost_persists_high_k():
    K,M=matrices(0,1,1,-1)
    k2=9
    assert k2+M[4,4]/K[4,4]==5
    assert K[4,4]/2==-1

def test_low_k_exp_growth_and_massless_orbit():
    K,M=matrices(0,1,1,1)
    assert 1+M[1,1]/K[1,1]==-3
    t=sp.symbols("t",real=True)
    q=sp.exp(sp.sqrt(3)*t)
    assert sp.simplify(sp.diff(q,t,2)-3*q)==0
    assert [M[i,i] for i in (0,5,6,7)]==[0,0,0,0]

def test_massless_principal_cone_independent_of_masses():
    z,k=sp.symbols("z k")
    KK,_=matrices(0,1,1,1)
    assert sp.factor((KK*(k-z)).det())==256*(k-z)**8
