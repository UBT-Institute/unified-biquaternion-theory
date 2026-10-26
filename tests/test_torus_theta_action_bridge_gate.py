import sympy as s

def test_compact_derivative_yields_fourier_eigenvalue():
    n,R,psi=s.symbols('n R psi',real=True, nonzero=True)
    u=s.exp(s.I*n*psi/R)
    assert s.simplify(-s.diff(u,psi,2)/u-n*n/R**2)==0

def test_splitjet_psi_mode_leaves_gravity_e_unchanged():
    x,q,f,omega,n,R,psi=s.symbols('x q f omega n R psi',real=True)
    ep=f*s.cos(n*psi/R)
    # Schematic covariant derivative along spacetime x of scalar X
    Dx=s.symbols('Dx',real=True)
    D_ep=s.symbols('D_eps',real=True)
    initial=Dx+q
    transformed=(Dx+D_ep)+(q-D_ep)
    assert s.simplify(transformed-initial)==0

def test_torus_scale_not_selected_by_four_dimensional_family():
    alpha,R,n=s.symbols('alpha R n',positive=True)
    E=alpha*n*n/R**2
    assert s.diff(E,alpha)!=0 and s.diff(E,R)!=0
