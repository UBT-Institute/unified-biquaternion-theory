"""Exact two-source auxiliary torsion elimination and coupling observability.

This is a two-channel toy. The canonical UBT 24x24 torsion Hessian, its
current normalization, full composite variations and parity assignments
are NOT supplied or established by this test.
"""
import sympy as s
a,b,c,Jv,Ja=s.symbols("a b c Jv Ja",real=True)
V,A=s.symbols("V A",real=True)
M=s.Matrix([[a,b],[b,c]])
J=s.Matrix([Jv,Ja]);K=s.Matrix([V,A])
L=(J.T*K)[0]+s.Rational(1,2)*(K.T*M*K)[0]
D=s.factor(M.det())
assert D==a*c-b*b
grad=s.Matrix([s.diff(L,z) for z in K])
assert grad==M*K+J
Ks=-M.inv()*J
assert s.simplify(M*Ks+J)==s.zeros(2,1)
eff=s.factor(L.subs({V:Ks[0],A:Ks[1]}))
expected=-(c*Jv**2-2*b*Jv*Ja+a*Ja**2)/(2*D)
assert s.simplify(eff-expected)==0
assert s.simplify(s.diff(eff,b)-s.factor(
    -(Ja*a-Jv*b)*(Ja*b-Jv*c)/D**2))==0
# At the singular locus the equation M*K=-J is soluble iff the source
# is orthogonal to the left null vector.
M0=M.subs({a:1,c:1,b:1})
assert M0.det()==0
null=M0.nullspace()[0]
assert null==s.Matrix([-1,1])
assert (null.T*J)[0]==Ja-Jv
print("PASS: 2-source elimination, b-dependence, singular source compatibility")
