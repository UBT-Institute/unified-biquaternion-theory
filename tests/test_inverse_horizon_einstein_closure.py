"""Conditional horizon-to-Einstein algebra, not a microscopic UBT proof."""
import sympy as sp


def test_null_cone_tensor_proportional_to_metric():
    # S symmetric and S(k,k)=0 for all null directions.
    # Evaluating k=(1,+/-e_i) and k=(sqrt(2),e_i+e_j)
    # establishes all components of S = f eta.
    s=sp.symarray("s", (4,4))
    S=sp.Matrix(4,4,lambda i,j:s[min(i,j),max(i,j)])
    cons=[]
    for i in (1,2,3):
        for sign in (1,-1):
            k=sp.zeros(4,1); k[0]=1; k[i]=sign
            cons.append((k.T*S*k)[0])
    for i,j in ((1,2),(1,3),(2,3)):
        k=sp.zeros(4,1); k[0]=sp.sqrt(2); k[i]=k[j]=1
        cons.append((k.T*S*k)[0])
    unique=[s[i,j] for i in range(4) for j in range(i,4)]
    sol=sp.linsolve(cons,unique)
    assert sol != sp.EmptySet
    expression=next(iter(sol))
    inferred=dict(zip(unique, expression))
    f=sp.symbols("f")
    # Put f in place of free S00 and verify all 10 components.
    first=s[0,0]
    for i in range(4):
        for j in range(i,4):
            expected= (f if i==j==0 else
                       -f if i==j else sp.Integer(0))
            assert sp.simplify(inferred[s[i,j]].subs(first,f)-expected)==0


def test_area_entropy_density_recovers_gravitational_coefficient():
    G=sp.symbols("G",positive=True)
    eta=1/(4*G)
    assert sp.simplify(2*sp.pi/eta-8*sp.pi*G)==0


def test_raychaudhuri_first_order_focusing():
    lam,R=sp.symbols("lam R")
    theta=-lam*R
    assert sp.diff(theta,lam).subs(lam,0)==-R
    assert theta.subs(lam,0)==0


def test_null_contraction_cannot_detect_cosmological_term():
    eta=sp.diag(1,-1,-1,-1)
    f=sp.symbols("f")
    for i in (1,2,3):
        k=sp.zeros(4,1);k[0]=1;k[i]=1
        assert (k.T*(f*eta)*k)[0]==0
