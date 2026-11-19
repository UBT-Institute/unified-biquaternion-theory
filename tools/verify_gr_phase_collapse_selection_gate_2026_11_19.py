"""UBT phase-versus-selection diagnostic; exact finite matrices only.

The full canonical UBT quantum measurement dynamics is NOT derived here.
Existing phase-metric, strict-real-tetrad and observer-readout results are
inputs.  This checks a scalar-phase pointwise counterexample and that
a selective state update differs from invertible unitary phase changes.
"""
import sympy as sp

I=sp.I
E=sp.diag(1,I)
A=sp.simplify((E+E.H)/2)
B=sp.simplify((E-E.H)/(2*I))
assert A==sp.diag(1,0) and B==sp.diag(0,1)
# A general central phase on the entire complex matrix can make E
# anti-Hermitian iff cos(phi)*A-sin(phi)*B=0; impossible here.
cs,sn=sp.symbols("cs sn",real=True)
sol=sp.solve([cs*A[0,0]-sn*B[0,0],
              cs*A[1,1]-sn*B[1,1]],(cs,sn))
assert sol=={cs:0,sn:0}  # violates cos^2 + sin^2 = 1
assert sp.simplify(sol[cs]**2+sol[sn]**2-1)==-1

# Matrix model of a candidate observer-local density readout:
# Theta=I, N=I => rho=I/2. A global phase does not change rho.
theta=sp.eye(2)
rho=theta*theta.H/sp.trace(theta*theta.H)
assert rho==sp.eye(2)/2
for z in [1, -1, I, (1+I)/sp.sqrt(2)]:
    new=z*theta
    assert sp.simplify(new*new.H/sp.trace(new*new.H)-rho)==sp.zeros(2)
assert sp.trace(rho*rho)==sp.Rational(1,2)
P=sp.diag(1,0)
p=sp.trace(P*rho)
after=P*rho*P/p
assert p==sp.Rational(1,2)
assert after==P and sp.trace(after*after)==1
# Selective update cannot be a unitary conjugation of the mixed rho:
# purity/rank is preserved under U rho U^dagger.

# ψ is a complex-time coordinate, not automatically a U(1) phase:
t,psi=sp.symbols("t psi",real=True)
hol=sp.exp(I*(t+I*psi))
assert sp.simplify(hol-sp.exp(I*t-psi))==0
assert sp.simplify(sp.diff(hol,psi)-I*sp.diff(hol,t))==0
print("PASS no generic central phase rotates full complex jet onto i-Hermitian W_L")
print("PASS central phase invisibility of candidate rho and nonunitary selective update")
print("PASS imaginary complex time coordinate psi changes magnitude in exp(i*tau)")
print("SCOPE conditional observer protocol; no derived objective quantum collapse")
