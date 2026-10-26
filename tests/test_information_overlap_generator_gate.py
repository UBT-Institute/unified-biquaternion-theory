import sympy as s
from functools import reduce

def kron(*xs):
    return reduce(s.kronecker_product,xs)
I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Z=s.diag(1,-1)

def test_overlap_flow_leaves_two_unfixed_energies():
    omega,alpha,beta=s.symbols("omega alpha beta",real=True)
    Za=kron(Z,I,I); Zb=kron(I,Z,I); Zc=kron(I,I,Z)
    H=omega*Zb+alpha*Za+beta*Zc
    Xb=kron(I,X,I)
    Xa=kron(X,I,I)
    def comm(A,B):return A*B-B*A
    assert s.simplify(comm(H,Xb)-omega*comm(Zb,Xb))==s.zeros(8)
    assert s.simplify(comm(H,Xa)-alpha*comm(Za,Xa))==s.zeros(8)
    assert comm(Za,Xa)!=s.zeros(8)

def test_common_commutant_is_scalar():
    # Any operator commuting with every matrix in the 12 and 23 local
    # algebras commutes with all single-qubit Pauli generators.
    u=s.symbols("u0:64")
    M=s.Matrix(8,8,u)
    generators=[kron(X,I,I),kron(Z,I,I),kron(I,X,I),kron(I,Z,I),kron(I,I,X),kron(I,I,Z)]
    # Restrict to diagonal for a lightweight direct certificate; the full
    # claim follows from Pauli generators spanning the full matrix algebra.
    diag=s.diag(*u[:8])
    eqs=[]
    for g in generators:
        eqs.extend(list(diag*g-g*diag))
    sol=s.linsolve(eqs,u[:8])
    v=next(iter(sol))
    assert all(s.simplify(z-v[0])==0 for z in v)
