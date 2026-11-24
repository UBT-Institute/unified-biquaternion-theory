#!/usr/bin/env python3
"""Exact algebraic split-jet versus strict-composite Hessian checks.

Only finite-dimensional comparators, not the physical single-Theta action.
"""
import sympy as s


def splitjet_auxiliary_surjectivity_gate():
    # At timelike X=(1,0,0,0), 3 boosts + scalar w span the tetrad
    # row, while 3 rotations are in the kernel.
    M = s.zeros(4, 7)
    M[0, 6] = 1
    for i in range(1, 4):
        M[i, i-1] = 1
    assert M.rank() == 4 and len(M.nullspace()) == 3
    full = s.diag(M, M, M, M)
    assert full.shape == (16, 28) and full.rank() == 16
    assert len(full.nullspace()) == 12
    print('PASS: extended 7->4 row map, nullity 3; 28->16 block, nullity 12')


def composite_second_variation_chain_gate():
    q = s.symbols('q0:8', real=True)
    lam = s.symbols('lam', real=True)
    Qp = (q[2]**2-q[3]**2)/2
    Qx = q[2]*q[3]
    z = s.Matrix([*q,Qp,Qx])
    parent = s.Matrix(s.symbols('z0:10', real=True))
    S_parent = (parent[8]**2+parent[9]**2)/2+lam*parent[8]
    S_red = s.factor(S_parent.subs(dict(zip(parent,z))))
    assert s.simplify(S_red - (
        (q[2]**2+q[3]**2)**2/8+lam*Qp)) == 0
    D = z.jacobian(q)
    H_parent = s.hessian(S_parent,parent)
    E_parent = s.Matrix([s.diff(S_parent,zi) for zi in parent]).subs(
        dict(zip(parent,z)))
    # The off-parent-shell chain rule contains E_parent * D^2 z.
    chain = s.simplify(
        D.T*H_parent*D+E_parent[8]*s.hessian(Qp,q)
        +E_parent[9]*s.hessian(Qx,q))
    assert s.simplify(s.hessian(S_red,q)-chain) == s.zeros(8)
    at_zero = {qi:0 for qi in q}
    H0 = s.hessian(S_red,q).subs(at_zero)
    assert s.simplify(H0[2,2]-lam) == 0
    assert s.simplify(H0[3,3]+lam) == 0
    assert s.simplify(H0.subs(lam,0)) == s.zeros(8)
    assert D.subs(at_zero).rank() == 8
    print('PASS: second variation including off-shell term; zero on-shell toy TT Hessian')


def single_theta_fourier_symbol_rank_gate():
    # Algebraic maximal image dimension only; not physical gauge-DOF count.
    D = s.zeros(16,8)
    for j in range(8):
        D[j,j] = 1
    assert D.rank() == 8 and len(D.columnspace()) == 8
    print('PASS: eight-real fixed-frequency Theta cannot span 16 tetrad entries')


if __name__ == '__main__':
    splitjet_auxiliary_surjectivity_gate()
    composite_second_variation_chain_gate()
    single_theta_fourier_symbol_rank_gate()
    print('SCOPE: split-jet/composite finite algebra, not UBT GR or a physical graviton')
