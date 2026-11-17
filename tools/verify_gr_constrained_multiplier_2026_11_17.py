"""Finite-dimensional adjoint check for constrained composite variation.

Verifies the multiplier Euler equations, their reduced-chain-rule equivalence
on invertible patches, and a singular Fredholm-compatibility counterexample.
This is NOT a complete PDE inversion or a derivation of a UBT action.
"""
import sympy as sp

q1,q2,e1,e2,k,l1,l2=sp.symbols("q1 q2 e1 e2 k l1 l2",real=True)
q=sp.Matrix([q1,q2]); e=sp.Matrix([e1,e2]); lam=sp.Matrix([l1,l2])
M=sp.Matrix([[sp.Rational(1,2),k],[0,sp.Rational(1,3)]])
N=sp.Matrix([[1,2],[2,1]])
z=sp.Matrix([1,0])
J=M*e+N*q+z*k
A=sp.eye(2)-M
S=sp.Rational(1,2)*(e.T*e)[0]+k**2/2+q1**2
F=S+(lam.T*(e-J))[0]

def eq(x,y):
    assert sp.simplify(x-y)==0,(x,y)

for idx,var in enumerate((e1,e2)):
    eq(sp.diff(F,var),sp.diff(S,var)+(A.T*lam)[idx])
for idx,var in enumerate((q1,q2)):
    eq(sp.diff(F,var),sp.diff(S,var)-(N.T*lam)[idx])
eq(sp.diff(F,k),sp.diff(S,k)-((M.diff(k)*e+z).T*lam)[0])
e_sol=A.inv()*(N*q+z*k)
replace={e1:e_sol[0],e2:e_sol[1]}
S_red=S.subs(replace)
p=sp.Matrix([sp.diff(S,ev) for ev in (e1,e2)])
y=(A.T.inv()*p).subs(replace)
for x in (q1,q2,k):
    jx=N[:,(q1,q2).index(x)] if x in (q1,q2) else M.diff(k)*e_sol+z
    eq(sp.diff(S_red,x),sp.diff(S,x).subs(replace)+(jx.T*y)[0])

# Noninvertible A: solvability, rather than an inverse, is the right question.
A0=sp.diag(1,0)
p_bad=sp.Matrix([0,1])
u=sp.Matrix([0,1])
assert A0*u==sp.zeros(2,1) and (u.T*p_bad)[0]!=0
assert sp.linsolve((A0.T,p_bad))==sp.EmptySet
p_good=sp.Matrix([3,0])
sol=sp.linsolve((A0.T,p_good))
assert len(sol.free_symbols)==1
print("PASS: multiplier Euler derivatives, reduced chain rule, singular compatibility")
