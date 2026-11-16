"""Exact test of observable-source restriction in a two-channel torsion toy.
The example is intentionally not interpreted as a canonical UBT source space.
"""
import sympy as s
j,x,y=s.symbols("j x y",real=True)
M1=s.eye(2)
M2=s.Matrix([[2,1],[1,1]])
assert M1.det()==1 and M2.det()==1
J1=s.Matrix([j,0])
assert s.simplify((J1.T*(M1.inv()-M2.inv())*J1)[0])==0
J2=s.Matrix([x,y])
difference=s.factor((J2.T*(M1.inv()-M2.inv())*J2)[0])
assert s.simplify(difference-y*(2*x-y))==0
assert M1!=M2
# Full source tests: equal symmetric quadratic forms for every J => equal inverses.
H=s.Matrix([[s.symbols("h11"),s.symbols("h12")],
            [s.symbols("h12"),s.symbols("h22")]])
Q=s.expand((J2.T*H*J2)[0])
assert s.solve([Q.coeff(x,2),Q.coeff(x,1).coeff(y,1),Q.coeff(y,2)],
               [H[0,0],H[0,1],H[1,1]])=={H[0,0]:0,H[0,1]:0,H[1,1]:0}
print("PASS: restricted source cannot distinguish distinct matrices; full source space can")
