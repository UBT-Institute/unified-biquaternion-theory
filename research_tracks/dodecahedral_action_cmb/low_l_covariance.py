#!/usr/bin/env python3
"""Quadrature projection of synthetic Sachs-Wolfe sky covariance into REAL a_lm.

This is NOT a Planck prediction: arbitrary P_n, χ, no cosmological transfer,
noise, mask, polarization or theta-to-zeta derivation. Uses standard library.
For a physical fit, quantify angular quadrature convergence at each ell/n.
"""
from __future__ import annotations

from math import acos, cos, factorial, pi, sin, sqrt
from typing import Sequence

from cmb_sachs_wolfe_kernel import sw_sky_covariance


def _legendre_with_prev(n: int, x: float) -> tuple[float,float]:
    """Return Legendre P_n(x), P_(n-1)(x)."""
    if n == 0:
        return (1.0, 0.0)
    prev,current=1.0,x
    if n == 1:
        return (current,prev)
    for k in range(2,n+1):
        prev,current=current, ((2*k-1)*x*current-(k-1)*prev)/k
    return current,prev


def gauss_legendre(n: int) -> tuple[tuple[float,float], ...]:
    """Roots and weights of Gauss-Legendre integration on [-1,1]."""
    if n < 1:
        raise ValueError("n>=1 required")
    results=[]
    for i in range(1,n+1):
        x=cos(pi*(i-0.25)/(n+0.5))
        for _ in range(30):
            p,prior=_legendre_with_prev(n,x)
            derivative=n*(x*p-prior)/(x*x-1)
            delta=p/derivative
            x-=delta
            if abs(delta)<2e-15:
                break
        p,prior=_legendre_with_prev(n,x)
        derivative=n*(x*p-prior)/(x*x-1)
        weight=2/((1-x*x)*derivative*derivative)
        results.append((x,weight))
    return tuple(sorted(results))


def associated_legendre(l: int,m: int,x: float) -> float:
    """Condon-Shortley P_l^m(x), nonnegative m<=l."""
    if not (0 <= m <= l) or not -1.0 <= x <= 1.0:
        raise ValueError("0<=m<=l and |x|<=1 required")
    pmm=1.0
    for k in range(1,m+1):
        pmm*=-(2*k-1)*sqrt(max(0.0,1-x*x))
    if l==m:
        return pmm
    pm1=x*(2*m+1)*pmm
    if l==m+1:
        return pm1
    prev,cur=pmm,pm1
    for degree in range(m+2,l+1):
        prev,cur=cur,((2*degree-1)*x*cur-(degree+m-1)*prev)/(degree-m)
    return cur


def real_spherical_harmonic(l: int,m: int,mu: float,phi: float) -> float:
    if abs(m)>l or l<0:
        raise ValueError("Bad angular degree")
    k=abs(m)
    norm=sqrt((2*l+1)/(4*pi)*factorial(l-k)/factorial(l+k))
    base=norm*associated_legendre(l,k,mu)
    if m==0:
        return base
    return sqrt(2)*base*(cos(k*phi) if m>0 else sin(k*phi))


def sky_nodes(n_mu: int,n_phi: int) -> tuple[tuple[tuple[float,float,float],float,float,float], ...]:
    """Direction, integration weight, cos(theta), phi."""
    if n_phi < 1:
        raise ValueError("n_phi>=1 required")
    nodes=[]
    for mu,wi in gauss_legendre(n_mu):
        theta_factor=sqrt(max(0.0,1-mu*mu))
        for j in range(n_phi):
            phi=2*pi*j/n_phi
            nodes.append(((theta_factor*cos(phi),theta_factor*sin(phi),mu),
                          wi*2*pi/n_phi,mu,phi))
    return tuple(nodes)


def angular_covariance(chi: float, Pn: dict[int,float],lmax: int=2,
                       n_mu: int=6,n_phi: int=12
                       ) -> tuple[tuple[tuple[int,int], ...],list[list[float]]]:
    """Full covariance <a_lm a_l'm'> in a real orthonormal harmonic basis.

    Computation cost O(Nsky^2 * #deck * max spatial n); use small toy grids
    for unit tests, production requires convergence tests and acceleration.
    """
    if lmax<0:
        raise ValueError("lmax>=0 required")
    modes=tuple((l,m) for l in range(lmax+1) for m in range(-l,l+1))
    grid=sky_nodes(n_mu,n_phi)
    vectors=[]
    for _,weight,mu,phi in grid:
        vectors.append([weight*real_spherical_harmonic(l,m,mu,phi)
                        for l,m in modes])
    count=len(modes)
    result=[[0.0]*count for _ in range(count)]
    for i,(ni,_,_,_) in enumerate(grid):
        v_i=vectors[i]
        for j in range(i,len(grid)):
            nj=grid[j][0]
            c=sw_sky_covariance(ni,nj,chi,Pn)
            if c==0.0:
                continue
            v_j=vectors[j]
            for p in range(count):
                for q in range(count):
                    result[p][q]+=c*(v_i[p]*v_j[q]
                                    +(v_j[p]*v_i[q] if j!=i else 0.0))
    return modes,result


def angular_cl(modes: Sequence[tuple[int,int]],
               cov: Sequence[Sequence[float]]) -> dict[int,float]:
    """Trace over m: C_l = sum_m C_lm,lm/(2l+1)."""
    degrees=sorted(set(l for l,_ in modes))
    return {l:sum(cov[i][i] for i,(ell,_) in enumerate(modes) if ell==l)/(2*l+1)
            for l in degrees}


if __name__=="__main__":
    print("Synthetic low-l example: chi=0.40, P_12=1, P_20=0.2")
    m,c=angular_covariance(0.4,{12:1.0,20:0.2},lmax=2,n_mu=6,n_phi=12)
    for ell,val in angular_cl(m,c).items():
        print(f"ell={ell} C_ell={val:.8g} arbitrary dimensionless units")
    print("These values are not UBT/Planck predictions.")
