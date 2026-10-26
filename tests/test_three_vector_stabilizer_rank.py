import sympy as s

def _rank_for_carriers(carriers):
    eta=s.diag(-1,1,1,1)
    params=s.symbols("a0:6")
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    B=s.zeros(4)
    for a,(i,j) in zip(params,pairs):
        B[i,j]=a
        B[j,i]=-a
    C=eta*B
    assert C.T*eta+eta*C==s.zeros(4)
    images=s.Matrix.vstack(*[C*x for x in carriers])
    return images.jacobian(params).rank()

def test_stabilizer_ranks():
    v=s.Matrix([1,0,0,0])
    w=s.Matrix([0,1,0,0])
    u=s.Matrix([0,0,1,0])
    assert _rank_for_carriers([v])==3
    assert _rank_for_carriers([v,w])==5
    assert _rank_for_carriers([v,w,u])==6
