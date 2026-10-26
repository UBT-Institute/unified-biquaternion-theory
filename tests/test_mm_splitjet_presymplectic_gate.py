import sympy as s

def test_splitjet_shift_is_exact_null_direction():
    x,u,dx,du,e,de=s.symbols("x u dx du e de")
    # E = xdot+u; gauge δxdot=edot, δu=-edot.
    xdot,edot=s.symbols("xdot edot")
    E=xdot+u
    assert s.simplify(E.subs({xdot:xdot+edot,u:u-edot})-E)==0
    # Pullback of Ω=d p_E wedge d E has a null parameter direction.
    # Jacobian of (xdot,u) -> E is [1,1].
    J=s.Matrix([[1,1]])
    assert J*s.Matrix([1,-1])==s.zeros(1,1)

def test_reduced_hamiltonian_is_nonnegative():
    p=s.symbols("p",real=True)
    H=p**2/2
    assert s.diff(H,p,2)==1
    assert s.solve(s.diff(H,p),p)==[0]
    assert H.subs(p,0)==0
