"""Exact time-selection scope gates for generic biquaternion value versus real Lorentz jets.

Reuses *existing* phase-metric and mimetic-clock restrictions; new part is the
explicit SAME invariant-potential orbit between nonzero Lorentz-real and
non-Lorentz-real matrix carriers, plus constant-Theta split-jet witness.
"""
import sympy as s

def adj(X):
    return s.Matrix([[X[1,1], -X[0,1]], [-X[1,0], X[0,0]]])

def H(X):
    return s.simplify(s.trace(adj(X)*X.H))

X0 = s.I*s.sqrt(2)*s.eye(2)
S = s.diag(2**s.Rational(1,4), 2**(-s.Rational(1,4)))
X1 = s.diag(2, 1)
assert s.simplify(s.det(S)-1)==0
assert s.simplify(-s.I*S*X0*S.H-X1) == s.zeros(2)
assert X0.H == -X0
assert X1.H == X1 and X1 != -X1
assert H(X0)==H(X1)==4
assert abs(s.det(X0))**2==abs(s.det(X1))**2==4
assert s.simplify(H(X0)**2-4*abs(s.det(X0))**2)==0

# U(1) neutral value invariants cannot distinguish the two representatives.
# This is stronger than a degree-4 polynomial observation for any invariant F.
# The phase rotation in the explicit group orbit is a property of the
# declared potential-sector G action, NOT necessarily a physical metric gauge.

# Complex-linear sharp: the canonical central metric carries phase weight 2.
E0=s.I*s.eye(2)
phase=s.exp(s.I*s.pi/4)
def central_norm(E):
    return s.simplify(s.trace(adj(E)*E)/2)
assert central_norm(E0)==-1
assert s.simplify(central_norm(phase*E0)-s.I*central_norm(E0))==0

# In the pre-existing independent split-jet comparison (NOT pure Lorentz
# spin-lift), Theta may be constant while the coframe remains nondegenerate.
t=s.symbols("t", real=True, positive=True)
a=1+t*t
Theta=s.I*s.eye(2)
N0=s.Integer(1)
TH=s.sqrt(H(Theta)/(2*N0))
e=s.diag(1,a,a,a)
g=e.T*s.diag(-1,1,1,1)*e
assert s.simplify(s.det(e)-(1+t*t)**3)==0
assert TH==1 and s.diff(TH,t)==0
assert s.simplify(g.inv()[0,0]*s.diff(TH,t)**2)==0

print("PASS: phase+SL2 orbit preserves H and |det|² but moves off Lorentz-real slice")
print("PASS: canonical sharp metric has phase weight two in the tested orbit")
print("PASS: constant-Theta split-jet metric is regular yet field-value clock frozen")
print("SCOPE: no theorem that full on-shell UBT has no global time")
