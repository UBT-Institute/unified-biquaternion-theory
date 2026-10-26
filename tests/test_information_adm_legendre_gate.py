import sympy as s

def test_adm_one_component_legendre_with_shift_and_connection():
    N,sqrt_h,g,v,d_x,shift,B,X,P,V=s.symbols("N sqrt_h g v dx shift B X P V", nonzero=True,real=True)
    # D_t X = dot X+B X ; v=D_t X-shift D_x X.
    dotX=s.symbols("dotX",real=True)
    velocity=dotX+B*X-shift*d_x
    L=sqrt_h*g*velocity**2/(2*N)-N*(sqrt_h*g*d_x**2/2+sqrt_h*V)
    momentum=s.diff(L,dotX)
    solved=s.solve(momentum-P,dotX)[0]
    H=s.expand(P*solved-L.subs(dotX,solved))
    expected=N*(P**2/(2*sqrt_h*g)+sqrt_h*g*d_x**2/2+sqrt_h*V)+shift*P*d_x-P*B*X
    assert s.simplify(H-expected)==0
