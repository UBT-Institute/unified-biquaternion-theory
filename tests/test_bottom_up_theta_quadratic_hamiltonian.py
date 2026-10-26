import sympy as s

def test_legendre_two_block_complex_modes():
    zr,zi,vr,vi,pr,pi,Z,M,C,n=s.symbols("zr zi vr vi pr pi Z M C n",real=True)
    L=Z*(vr*vr+vi*vi)-(M+C*n*n)*(zr*zr+zi*zi)
    assert s.diff(L,vr)==2*Z*vr
    assert s.diff(L,vi)==2*Z*vi
    H=s.expand((pr*vr+pi*vi-L).subs({vr:pr/(2*Z),vi:pi/(2*Z)}))
    assert s.simplify(H-(pr*pr+pi*pi)/(4*Z)-(M+C*n*n)*(zr*zr+zi*zi))==0

def test_same_symmetries_distinct_torus_spectra():
    Z,M,R,n=s.symbols("Z M R n",positive=True)
    omega1=(M+n*n/R**2)/Z
    omega2=(M+2*n*n/R**2)/Z
    assert s.simplify(omega2-omega1)==n*n/(Z*R**2)
