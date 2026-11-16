"""Exact local-tetrad Schwarzschild observer benchmarks.
GR tensor identity only; does not derive any on-shell UBT solution.
"""
import sympy as s
from itertools import product

b, k=s.symbols("b k", real=True)
E=s.diag(-2*k,k,k)
eps=s.LeviCivita
R=s.MutableDenseNDimArray.zeros(4,4,4,4)
for i in range(1,4):
    for j in range(1,4):
        R[i,0,j,0]=E[i-1,j-1]
        R[0,i,j,0]=-E[i-1,j-1]
        R[i,0,0,j]=-E[i-1,j-1]
        R[0,i,0,j]=E[i-1,j-1]
for i,j,m,n in product(range(1,4),repeat=4):
    R[i,j,m,n]=-sum(eps(i-1,j-1,z)*eps(m-1,n-1,z)*E[z,z] for z in range(3))

gamma=1/s.sqrt(1-b*b)
def tidal(direction):
    v=s.zeros(4,1); v[0]=gamma; v[direction]=gamma*b
    triad=[]
    for j in range(1,4):
        p=s.zeros(4,1)
        if j==direction:
            p[0]=gamma*b;p[j]=gamma
        else:p[j]=1
        triad.append(p)
    return s.Matrix(3,3,lambda i,j:s.factor(sum(
        triad[i][a]*v[c]*triad[j][d]*v[e]*R[a,c,d,e]
        for a,c,d,e in product(range(4),repeat=4))))

tan=tidal(2)
rad=tidal(1)
goal=s.diag(-gamma**2*(2+b*b)*k,k,gamma**2*(1+2*b*b)*k)
assert all(s.simplify((tan-goal)[i,j])==0 for i in range(3) for j in range(3))
assert all(s.simplify((rad-E)[i,j])==0 for i in range(3) for j in range(3))
assert s.simplify(s.trace(tan*tan)-s.trace(E*E)-
    18*k*k*b*b/(1-b*b)**2)==0
metric=[-1,1,1,1]
invariant=sum(metric[a]*metric[c]*metric[d]*metric[e]*R[a,c,d,e]**2
    for a,c,d,e in product(range(4),repeat=4))
assert s.simplify(invariant-48*k*k)==0
assert s.simplify(s.trace(tan))==0
print("PASS: tangential and radial boost, Weyl norm, invariant 48 k^2")
