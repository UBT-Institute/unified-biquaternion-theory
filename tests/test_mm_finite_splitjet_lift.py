import sympy as s

def test_finite_nonnull_splitjet_reconstruction():
    eta=s.diag(-1,1,1,1)
    X=s.Matrix([2,1,0,0])
    Xnew=s.Matrix([3,0,1,0])
    Qnew=s.Matrix([5,0,0,3])
    inner=lambda a,b:(a.T*eta*b)[0]
    norm=inner(Xnew,Xnew)
    assert norm!=0
    w=inner(Xnew,Qnew)/norm
    Y=Qnew-w*Xnew
    Klow=(eta*Y*(eta*Xnew).T-eta*Xnew*(eta*Y).T)/norm
    K=eta*Klow
    assert Klow.T == -Klow
    assert s.simplify(K*Xnew+w*Xnew-Qnew)==s.zeros(4,1)
    # For arbitrary prescribed D_omega X and a new X', choose Q' accordingly.
    dX=s.Matrix([1,2,-1,4])
    dXnew=s.Matrix([2,0,1,1])
    Q=s.Matrix([2,1,0,-2])
    Qprime=Q+dX-dXnew
    assert dXnew+Qprime==dX+Q

def test_finite_shifts_compose():
    old,mid,new,der_old,der_mid,der_new,q=s.symbols("old mid new der_old der_mid der_new q")
    first=q+der_old-der_mid
    second=first+der_mid-der_new
    assert s.expand(second-(q+der_old-der_new))==0
