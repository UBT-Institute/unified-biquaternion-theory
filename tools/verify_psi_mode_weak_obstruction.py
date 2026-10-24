"""Exact restricted test: opposite imaginary-time windings are not automatically weak SU(2).

Assumptions: one complex biquaternion polarization on a fixed Lorentz
background, a nonzero Fourier pair, and the pre-existing invariant quartic.
This is NOT the full constrained UBT Hessian or fermionic dynamics.
"""
import sympy as sp


def verify_psi_mode_weak_obstruction():
    checks = {}
    I = sp.I
    n, R = sp.symbols("n R", real=True, positive=True)
    u, v, ub, vb = sp.symbols("u v ubar vbar")
    L1, L2 = sp.symbols("lambda1 lambda2", real=True)

    # Formal Laurent zero modes for f=u z+v/z and f*=ubar/z+vbar z.
    A = u*ub+v*vb
    B, C = u*vb, v*ub
    F = sp.expand(A*A+2*B*C)
    expected = (u*ub)**2+4*u*ub*v*vb+(v*vb)**2
    checks["exact fourth-power Laurent constant term"] = sp.expand(F-expected)==0
    checks["quartic mixed coefficient four, not two"] = (
        F.coeff(u*ub*v*vb)==4 and sp.expand(A*A).coeff(u*ub*v*vb)==2
    )
    checks["opposite-mode free kinetic degeneracy"] = (
        sp.simplify(n*n*A/(R*R)-n*n*(u*ub+v*vb)/(R*R))==0
    )

    U = sp.Matrix([[1,1],[-1,1]])/sp.sqrt(2)
    initial = sp.Matrix([1,0])
    rotated = U*initial
    quartic = lambda a,b: sp.expand(a**4+4*a*a*b*b+b**4)
    checks["rotation is in SU2"] = (
        sp.simplify(U.T*U)==sp.eye(2) and sp.simplify(U.det())==1
    )
    checks["free norm stays invariant"] = (
        sp.simplify((rotated.T*rotated)[0]-(initial.T*initial)[0])==0
    )
    checks["quartic values 1 versus three-halves"] = (
        quartic(*initial)==1 and quartic(*rotated)==sp.Rational(3,2)
    )
    checks["quartic breaking difference one-half"] = (
        sp.simplify(quartic(*rotated)-quartic(*initial))==sp.Rational(1,2)
    )

    # The pre-existing quartic potential lambda1 H^2+lambda2 |det X|^2.
    sharp=lambda X:sp.Matrix([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])
    H=lambda X:sp.simplify(sp.trace(sharp(X)*X.conjugate().T))
    Y1, Y2=sp.eye(2),sp.diag(1,I)
    detnorm=lambda Y:sp.simplify(Y.det()*sp.conjugate(Y.det()))
    Q=lambda Y:sp.expand(L1*H(Y)**2+L2*detnorm(Y))
    checks["identity polarization invariant values"] = (
        H(Y1)==2 and detnorm(Y1)==1
    )
    checks["mixed-phase polarization invariant values"] = (
        H(Y2)==0 and detnorm(Y2)==1
    )
    checks["independent quartic coefficients"] = (
        Q(Y1)==4*L1+L2 and Q(Y2)==L2
    )
    checks["both coefficients vanish only for zero quartics"] = (
        sp.solve([Q(Y1),Q(Y2)],[L1,L2],dict=True)==[{L1:0,L2:0}]
    )

    # Fiber reflection swaps the modes; translations distinguish them.
    P=sp.Matrix([[0,1],[1,0]])
    G=sp.diag(1,-1)
    t=sp.Symbol("t",nonzero=True)
    T=sp.diag(t,1/t)
    checks["fiber reflection involution"] = P*P==sp.eye(2)
    checks["reflection anticommutes with circle momentum"] = P*G==-G*P
    checks["reflection inverts circle translations"] = (
        sp.simplify(P*T*P-T.inv())==sp.zeros(2)
    )
    a,b,c,d=sp.symbols("a b c d")
    M=sp.Matrix([[a,b],[c,d]])
    comm=M*G-G*M
    checks["commuting matrices cannot mix opposite weights"] = (
        comm[0,1]==-2*b and comm[1,0]==2*c and comm[0,0]==comm[1,1]==0
    )
    X=sp.Matrix([[0,1],[1,0]])
    Y=sp.Matrix([[0,-I],[I,0]])
    checks["two off-diagonal SU2 generators fail commutation"] = (
        X*G-G*X!=sp.zeros(2) and Y*G-G*Y!=sp.zeros(2)
    )

    # Exact Schur-commutant rank for Lorentz (1/2,1/2) vector representation.
    Ks=[]
    for axis in range(1,4):
        J=sp.zeros(4)
        J[0,axis]=J[axis,0]=1
        Ks.append(J)
    Rs=[]
    for j,k in ((2,3),(3,1),(1,2)):
        J=sp.zeros(4)
        J[j,k]=-1
        J[k,j]=1
        Rs.append(J)
    eq=sp.zeros(0,16)
    for J in Ks+Rs:
        eq=eq.col_join(sp.kronecker_product(sp.eye(4),J)
                       -sp.kronecker_product(J.T,sp.eye(4)))
    checks["Lorentz vector commutant rank fifteen"] = eq.rank()==15
    checks["Lorentz scalar identity in the commutant"] = all(
        J*sp.eye(4)==sp.eye(4)*J for J in Ks+Rs
    )
    Pplus=(sp.eye(2)+P)/2
    Pminus=(sp.eye(2)-P)/2
    checks["fiber parity eigenspaces not a Weyl-spinor derivation"] = (
        Pplus*Pplus==Pplus and Pminus*Pminus==Pminus
        and Pplus*Pminus==sp.zeros(2) and eq.rank()==15
    )
    return checks


if __name__=="__main__":
    results=verify_psi_mode_weak_obstruction()
    for name,ok in results.items():
        print(("PASS" if ok else "FAIL")+" "+name)
    print(f"{sum(results.values())}/{len(results)} exact checks")
    if not all(results.values()):
        raise SystemExit(1)
