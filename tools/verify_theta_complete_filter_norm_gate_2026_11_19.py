"""Operational completeness selects the Hilbert-Schmidt weight conditionally.

A physical detector, Hermitian positive form, and projective filter maps
are still assumptions, not derived from full-Theta UBT dynamics.
"""
import sympy as s

I=s.I
unit=s.eye(2)
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
alpha,beta=s.symbols('alpha beta',positive=True,real=True)

def h(T):
    t0=s.trace(T)/2
    trless=T-t0*unit
    return s.simplify(2*alpha*t0*s.conjugate(t0)+
                      beta*s.trace(trless.H*trless))

T=s.Matrix([[1,2+I],[3-I,4]])
U=(unit+I*sx)/s.sqrt(2)
assert s.simplify(U.H*U-unit)==s.zeros(2)
assert s.simplify(h(U*T*U.H)-h(T))==0
assert s.simplify(h(T).subs({alpha:1,beta:1})-s.trace(T.H*T))==0

# Covariance alone permits 2 positive weights, singlet and triplet.
assert h(unit)==2*alpha
right_phase=I*sz
assert right_phase.det()==1 and right_phase.H*right_phase==unit
assert h(right_phase)==2*beta
assert s.solve(s.Eq(h(unit),h(right_phase)),alpha)==[beta]

# Information additivity for a COMPLETE orthogonal projective filter
# selects equal weights even without declaring right SU2 a physical gauge.
P=s.diag(1,0)
notP=unit-P
assert h(P)==(alpha+beta)/2
assert h(notP)==(alpha+beta)/2
sum_fraction=s.simplify((h(P)+h(notP))/h(unit))
assert s.simplify(sum_fraction-(alpha+beta)/(2*alpha))==0
assert s.solve(s.Eq(sum_fraction,1),beta)==[alpha]

# Once selected, the HS norm satisfies complete detector additivity
# for ALL matrices T and ALL Hermitian projectors P.
r=s.symbols('r',real=True)
projector=(unit+s.cos(r)*sz+s.sin(r)*sx)/2
assert s.trigsimp(projector*projector-projector)==s.zeros(2)
TP=s.simplify(projector*T)
TQ=s.simplify((unit-projector)*T)
lhs=s.simplify(h(TP).subs({alpha:beta})+h(TQ).subs({alpha:beta}))
rhs=s.simplify(h(T).subs({alpha:beta}))
assert s.trigsimp(lhs-rhs)==0

# If weights differ, the two-filter response is not normalized.
assert s.simplify(sum_fraction.subs({alpha:2,beta:1})-s.Rational(3,4))==0
print("PASS observer spin-frame conjugation allows independent singlet/triplet weights")
print("PASS complete orthogonal outcome additivity selects equal positive weights")
print("PASS selected norm is Hilbert-Schmidt for all tested projective axes")
print("PASS the same condition follows if operational right SU2 basis is invisible")
print("SCOPE microscopic positive detector, actual probabilities, collapse still OPEN")
