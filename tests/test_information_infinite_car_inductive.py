"""Finite exact-identity tests supporting the CAR inductive system (not a proof by sampling)."""
import sympy as sp
E=sp.eye(2)
P=sp.diag(1,-1)
e1=-sp.I*sp.Matrix([[0,1],[1,0]])
e2=-sp.I*sp.Matrix([[0,-sp.I],[sp.I,0]])
a=(e1+sp.I*e2)/2
n=a.conjugate().T*a
def kron(*factors):
    out=sp.eye(1)
    for f in factors: out=sp.kronecker_product(out,f)
    return out
def annihilators(N):
    return [kron(*([P]*j+[a]+[E]*(N-j-1))) for j in range(N)]
def freeH(weights):
    cs=annihilators(len(weights))
    return sum((w*c.conjugate().T*c for w,c in zip(weights,cs)),sp.zeros(2**len(weights)))
def test_one_quaternion_factor():
    assert a*a==sp.zeros(2)
    assert a*a.conjugate().T+a.conjugate().T*a==E
    assert P*a+a*P==sp.zeros(2)
    assert n==sp.diag(0,1)
def test_inductive_embeddings():
    for N in range(1,5):
        old,new=annihilators(N),annihilators(N+1)
        for j in range(N):
            assert kron(old[j],E)==new[j]
            assert kron(old[j].conjugate().T,E)==new[j].conjugate().T
def test_car_through_five_modes():
    for N in range(1,6):
        cs=annihilators(N)
        for j in range(N):
            for k in range(N):
                assert cs[j]*cs[k]+cs[k]*cs[j]==sp.zeros(2**N)
                assert cs[j]*cs[k].conjugate().T+cs[k].conjugate().T*cs[j]==(sp.eye(2**N) if j==k else sp.zeros(2**N))
def test_old_mode_heisenberg_flow_is_cutoff_stable():
    w=[2,3,5,7,11]
    for N in range(1,5):
        old,new=annihilators(N),annihilators(N+1)
        Hn,Hnext=freeH(w[:N]),freeH(w[:N+1])
        for j in range(N):
            comm=Hn*old[j]-old[j]*Hn
            commnext=Hnext*new[j]-new[j]*Hnext
            assert comm==-w[j]*old[j]
            assert commnext==kron(comm,E)
def test_finite_fock_spectra_are_nonnegative():
    w=[2,3,5,7]
    for N in range(1,5):
        H=freeH(w[:N])
        spec=sorted([v for v,mult in H.eigenvals().items() for _ in range(mult)])
        expected=sorted([sum(w[j] for j in range(N) if mask & (1<<j)) for mask in range(2**N)])
        assert spec==expected and min(spec)==0 and H==H.conjugate().T
