import sympy as s

def test_cp1_dirac_constraints_and_evolution():
    th,ph,pth,pph,h=s.symbols("theta phi p_theta p_phi h",real=True)
    A=(1-s.cos(th))/2
    H=h*s.cos(th)
    qs=[th,ph];ps=[pth,pph]
    def pb(f,g):
        return s.simplify(sum(s.diff(f,q)*s.diff(g,p)-s.diff(f,p)*s.diff(g,q) for q,p in zip(qs,ps)))
    chi=[pth,pph-A]
    C=s.Matrix([[pb(x,y) for y in chi] for x in chi])
    assert s.simplify(C[0,1]-s.sin(th)/2)==0
    Cinv=C.inv()
    def db(f,g):
        return s.trigsimp(pb(f,g)-sum(pb(f,chi[i])*Cinv[i,j]*pb(chi[j],g) for i in range(2) for j in range(2)))
    assert s.trigsimp(db(th,ph)+2/s.sin(th))==0
    assert db(th,H)==0
    assert s.trigsimp(db(ph,H)+2*h)==0
    # Direct EL for theta: dA/dtheta * dot(phi) - dH/dtheta = 0
    assert s.trigsimp(s.diff(H,th)/s.diff(A,th)+2*h)==0
    assert s.simplify(s.det(C)-(s.sin(th)/2)**2)==0

def test_gibbs_modular_identity():
    beta,h=s.symbols("beta h",positive=True,real=True)
    Z=s.exp(-beta*h)+s.exp(beta*h)
    K=s.diag(beta*h+s.log(Z),-beta*h+s.log(Z))
    assert s.simplify((K-s.log(Z)*s.eye(2))/beta-s.diag(h,-h))==s.zeros(2)
