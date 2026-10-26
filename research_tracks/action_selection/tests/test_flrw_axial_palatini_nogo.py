"""Axial SO(3)-isotropic Lorentz connection; scope: independent Palatini candidate."""
import sympy as s
from sympy import LeviCivita as eps
H,f,h,fd,hd=s.symbols('H f h fd hd')

def plus(*forms):
    d={}
    for z in forms:
        for k,v in z.items():d[k]=s.expand(d.get(k,0)+v)
    return {k:v for k,v in d.items() if v!=0}

def wedge(a,b):
    d={}
    for i,x in a.items():
        for j,y in b.items():
            if i==j:continue
            idx=tuple(sorted((i,j)))
            d[idx]=s.expand(d.get(idx,0)+(1 if i<j else -1)*x*y)
    return {i:c for i,c in d.items() if c!=0}

def exterior_d(a):
    # d(e^0)=0; d(e^i)=H e^0 wedge e^i; dot f=fd,dot h=hd
    return {(0,i):s.expand(s.diff(c,f)*fd+s.diff(c,h)*hd+H*c)
            for i,c in a.items() if i>0 and s.expand(s.diff(c,f)*fd+s.diff(c,h)*hd+H*c)!=0}

omega={}
for i in range(1,4):
    omega[(i,0)]={i:f}; omega[(0,i)]={i:f}
    for j in range(1,4):
        if i!=j:
            omega[(i,j)]={k:h*eps(i,j,k) for k in range(1,4) if eps(i,j,k)}

def curvature(a,b):
    out=exterior_d(omega.get((a,b),{}))
    for c in range(4):out=plus(out,wedge(omega.get((a,c),{}),omega.get((c,b),{})))
    return out

def test_spatial_boost_curvature():
    assert curvature(1,0)=={(0,1):fd+H*f,(2,3):-2*f*h}

def test_spatial_rotation_curvature():
    assert curvature(1,2)=={(0,3):hd+H*h,(1,2):f*f-h*h}

def test_euler_connection_conditions_obstruct_composite_boost():
    # d(V²)=-2 rho e0, rho !=0, hence spatial F vanishes
    assert s.solve([f*h, f*f-h*h],(f,h))==[(0,0)]
    rho=s.symbols('rho', real=True, nonzero=True)
    assert s.simplify((f*f-h*h).subs({f:1/rho,h:0}))==rho**-2

def test_isotropic_axial_cyclic_curvature():
    assert curvature(2,3)=={(0,1):hd+H*h,(2,3):f*f-h*h}
