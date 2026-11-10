"""Conditional area-law and Bell correlation vs causal-interaction checks."""
import sympy as s


def test_boundary_count():
    for L in range(1, 6):
        pts = {(x,y,z) for x in range(L) for y in range(L) for z in range(L)}
        dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        count = sum(tuple(p[i]+d[i] for i in range(3)) not in pts
                    for p in pts for d in dirs)
        assert count == 6*L*L


def test_gate_bound():
    q,d,L = s.symbols("q d L", positive=True, integer=True)
    N = 6*L**2
    assert s.simplify(s.log(q**(2*d*N))-2*d*N*s.log(q)) == 0


def test_bell_mutual_info():
    bell = s.Matrix([1,0,0,1])/s.sqrt(2)
    rho = bell*bell.T
    reduced = s.Matrix(2,2,lambda i,j:
                       sum(rho[2*i+k,2*j+k] for k in range(2)))
    assert reduced == s.eye(2)/2
    assert s.trace(rho*rho) == 1
    # S(A)=S(B)=ln 2, S(AB)=0.
    assert s.simplify(s.log(2)+s.log(2)-2*s.log(2)) == 0


def test_zero_coupling_entanglement_counterexample():
    H = s.zeros(4)
    psi = s.Matrix([1,0,0,1])/s.sqrt(2)
    rho = psi*psi.T
    assert H*psi == s.zeros(4,1)
    assert s.trace(rho*rho) == 1
    assert s.Matrix(2,2,lambda i,j:
                    sum(rho[2*i+k,2*j+k] for k in range(2))) == s.eye(2)/2
