"""Exact algebraic SU(3) exterior-Fock conditional gauge-anomaly checks.

Assumes, solely for anomaly diagnostics, that each exterior-degree block is
one left-handed Weyl multiplet. This does not derive physical UBT fermions.
"""
from itertools import combinations
import sympy as sp


def verify_su3_fock_anomalies():
    I = sp.I
    lam = [
        sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
        sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
        sp.diag(1,-1,0),
        sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
        sp.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),
        sp.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
        sp.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),
        sp.diag(1,1,-2)/sp.sqrt(3),
    ]
    T = [m/2 for m in lam]
    states = [tuple(c) for k in range(4) for c in combinations(range(3),k)]
    idx = {v:i for i,v in enumerate(states)}

    def create(j):
        C = sp.zeros(8)
        for occ, col in idx.items():
            if j in occ:
                continue
            target = tuple(sorted(occ+(j,)))
            C[idx[target],col] = (-1)**sum(i<j for i in occ)
        return C

    cdag = [create(j) for j in range(3)]
    c = [m.T for m in cdag]
    def lift(m):
        return sum((cdag[i]*c[j]*m[i,j]
                    for i in range(3) for j in range(3)),sp.zeros(8))

    D = [lift(t) for t in T]
    N = sum((cdag[i]*c[i] for i in range(3)),sp.zeros(8))
    checks = {}
    checks["exterior degrees 1,3,3,1"] = (
        [sum(len(v)==k for v in states) for k in range(4)]==[1,3,3,1])
    checks["number operator"] = N==sp.diag(0,1,1,1,2,2,2,3)
    checks["eight Hermitian lifted generators"] = all(
        x==x.conjugate().T for x in D)
    checks["fundamental degree-one sector"] = all(
        x[1:4,1:4]==t for x,t in zip(D,T))
    checks["singlet and number block preservation"] = all(
        x[0,:]==sp.zeros(1,8) and x[7,:]==sp.zeros(1,8)
        and x*N==N*x for x in D)
    checks["Lie commutators"] = all(
        sp.simplify(D[a]*D[b]-D[b]*D[a]-lift(T[a]*T[b]-T[b]*T[a]))
            ==sp.zeros(8) for a in range(8) for b in range(a+1,8))
    cubic = [
        sp.simplify(sp.trace(D[a]*(D[b]*D[d]+D[d]*D[b])))
        for a in range(8) for b in range(8) for d in range(b,8)
    ]
    checks["288 cubic anomaly entries cancel"] = (
        len(cubic)==288 and all(x==0 for x in cubic))
    fundamental = sp.simplify(2*sp.trace(T[7]**3))
    antifundamental = sp.simplify(2*sp.trace(D[7][4:7,4:7]**3))
    checks["nonzero triplet/antitriplet anomaly witnesses"] = (
        fundamental!=0 and sp.simplify(fundamental+antifundamental)==0)
    checks["opposite chirality does not cancel"] = (
        sp.simplify(fundamental-antifundamental)!=0)

    y0,y1,y2,y3 = sp.symbols("y0 y1 y2 y3",real=True)
    Y = sp.diag(y0,y1,y1,y1,y2,y2,y2,y3)
    checks["U1 colour commutator"] = all(Y*x==x*Y for x in D)
    checks["diagonal SU3^2 U1 anomaly"] = all(
        sp.simplify(sp.trace(Y*x*x)-(y1+y2)/2)==0 for x in D)
    checks["off diagonal SU3^2 U1 anomaly"] = all(
        sp.simplify(sp.trace(Y*D[a]*D[b]))==0
        for a in range(8) for b in range(8) if a!=b)
    checks["mixed gravitational U1 trace"] = (
        sp.simplify(sp.trace(Y)-(y0+3*y1+3*y2+y3))==0)
    checks["cubic U1 trace"] = (
        sp.simplify(sp.trace(Y**3)-
                    (y0**3+3*y1**3+3*y2**3+y3**3))==0)
    paired = Y.subs({y2:-y1,y3:-y0})
    checks["paired block-charge anomalies cancel"] = (
        all(sp.simplify(sp.trace(paired*x*x))==0 for x in D)
        and sp.simplify(sp.trace(paired))==0
        and sp.simplify(sp.trace(paired**3))==0)

    a,b = sp.symbols("a b",real=True)
    Ya = a*N+b*sp.eye(8)
    checks["affine charge anomaly coefficient"] = (
        sp.simplify(sp.trace(Ya*D[7]*D[7])-(3*a+2*b)/2)==0)
    checks["unique affine charge offset"] = (
        sp.solve(3*a+2*b,b,dict=True)==[{b:-3*a/2}])
    Ypaired = Ya.subs(b,-3*a/2)
    checks["particle-hole paired charge spectrum"] = (
        [sp.simplify(Ypaired[i,i]) for i in [0,1,4,7]]
        ==[-3*a/2,-a/2,a/2,3*a/2])
    checks["paired affine cubic and grav anomalies"] = (
        sp.simplify(sp.trace(Ypaired))==0
        and sp.simplify(sp.trace(Ypaired**3))==0)
    checks["SM quark SU3^3 reference"] = (2-1-1)==0
    checks["SM quark SU3^2 U1 reference"] = (
        sp.Rational(2,6)-sp.Rational(2,3)+sp.Rational(1,3)==0)
    checks["one triplet and one antitriplet, not full SM quarks"] = (
        [sum(len(v)==k for v in states)//sp.binomial(3,k)
         for k in (1,2)]==[1,1])
    return checks


if __name__=="__main__":
    checks=verify_su3_fock_anomalies()
    for name,ok in checks.items():
        print(("PASS" if ok else "FAIL")+" "+name)
    if not all(checks.values()):
        raise SystemExit(1)
    print("PASS: "+str(len(checks))+" exact checks")
