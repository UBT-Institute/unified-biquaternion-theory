#!/usr/bin/env python3
"""Exact finite rest-mode algebra, with independent real-spectrum numerics.

The candidate Dirac-to-UBT bridge and infinite Fock construction are not proved.
Missing dependencies fail rather than silently turning unrun checks into PASS.

© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def rest_hamiltonian(n: int, radius: float) -> np.ndarray:
    if not np.isfinite(radius) or radius <= 0:
        raise ValueError('The circle radius must be finite and positive.')
    z, eye = np.zeros((2, 2), complex), np.eye(2, dtype=complex)
    return np.block([[z, -1j*n/radius*eye], [1j*n/radius*eye, z]])


def verify() -> dict:
    eye, zero = sp.eye(2), sp.zeros(2)
    g0 = sp.Matrix(sp.BlockMatrix([[zero, eye], [eye, zero]]))
    g5 = sp.diag(-1, -1, 1, 1)
    m, E = sp.symbols('m E', real=True)
    H = -sp.I*m*g0*g5
    p1,p2,p3 = sp.symbols('p1 p2 p3', real=True)
    sigma_dot_p = sp.Matrix([[p3,p1-sp.I*p2],[p1+sp.I*p2,-p3]])
    assert sp.simplify((E*eye-sigma_dot_p)*(E*eye+sigma_dot_p)
                       -(E*E-p1*p1-p2*p2-p3*p3)*eye) == sp.zeros(2)
    assert H.H == H
    assert sp.simplify(H*H - m*m*sp.eye(4)) == sp.zeros(4)
    assert sp.expand((E*g0+sp.I*m*g5).det()-(E*E-m*m)**2) == 0
    assert sp.expand((E*sp.eye(4)-H).det()-(E*E-m*m)**2) == 0
    assert g5*H*g5 == H.subs(m, -m)
    # Missing -i is detected before computing any energies.
    wrong = m*g0*g5
    assert wrong.H == -wrong and wrong.H != wrong
    # Exact positive-energy subspaces for both winding signs, arbitrary spinor.
    k = sp.Symbol('k', positive=True)
    a,b,c,d = sp.symbols('a b c d', real=True)
    L = sp.Matrix([a+sp.I*b, c+sp.I*d])
    for sign in [-1, 1]:
        R = sign*sp.I*L
        u = L.col_join(R)
        assert sp.simplify(H.subs(m, sign*k)*u-k*u) == sp.zeros(4,1)
        assert sp.simplify((L.H*L-R.H*R)[0]) == 0
    # Universal polynomial identity used by the equal-weight eigenstate proof.
    R = sp.Matrix([sp.Symbol('x', real=True)+sp.I*sp.Symbol('y', real=True),
                   sp.Symbol('z', real=True)+sp.I*sp.Symbol('w', real=True)])
    assert sp.simplify(sp.re((-sp.I*m*L.H*R)[0])-sp.re((sp.I*m*R.H*L)[0])) == 0
    ann = sp.Matrix([[0,1],[0,0]])
    assert ann*ann.H+ann.H*ann == sp.eye(2)
    assert -E*ann*ann.H+E*sp.eye(2) == E*ann.H*ann
    # Actual finite CAR matrices on a two-mode occupation space.
    z2 = sp.diag(1,-1)
    b0, b1 = sp.kronecker_product(ann,eye), sp.kronecker_product(z2,ann)
    assert b0*b1.H+b1.H*b0 == sp.zeros(4)
    e0,e1 = sp.symbols('e0 e1', nonnegative=True)
    N = e0*b0.H*b0+e1*b1.H*b1
    assert list(N.diagonal()) == [0,e1,e0,e0+e1]
    # No moduli of imaginary eigenvalues: first require Hermiticity, then eigh.
    tested = 0
    for radius in [0.5, 1.0, 2.5]:
        for n in [-3,-2,-1,0,1,2,3]:
            A = rest_hamiltonian(n,radius)
            assert np.allclose(A.conj().T,A,rtol=0,atol=1e-12)
            energies,U = np.linalg.eigh(A)
            expected = np.array([-abs(n)/radius]*2+[abs(n)/radius]*2)
            assert np.allclose(energies,expected,rtol=0,atol=1e-12)
            assert np.allclose(A@U,U*energies,rtol=0,atol=1e-12)
            if n:
                weightsL=np.sum(np.abs(U[:2,:])**2,axis=0)
                weightsR=np.sum(np.abs(U[2:,:])**2,axis=0)
                assert np.allclose(weightsL,weightsR,rtol=0,atol=1e-12)
            tested += 1
    return {'weyl_signature_identity':'PASS','hermitian_hamiltonian':'PASS','square_and_characteristic':'PASS',
            'winding_conjugation':'PASS','missing_factor_regression':'PASS',
            'exact_positive_energy_states_both_signs':'PASS',
            'equal_weight_identity':'PASS','finite_car_reordering':'PASS',
            'two_mode_occupation_positivity':'PASS', 'numerical_mode_radius_cases':tested}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    checks=verify()
    paths=['tools/verify_psi_fock_chirality_selection.py',
           'formal/lean/UBT/Action/PsiRestHamiltonian.lean',
           'tests/test_psi_fock_chirality_selection.py']
    paths += [f'research_tracks/complex_time_branch_selection/psi_fock_quantization_chirality_link.{lang}.md'
              for lang in ['en','cs']]
    record={'schema':'ubt-verification/v1','date':'2026-09-16','result':'PASS',
            'checks':checks,'tools':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__},
            'assumptions':['Declared free flat Dirac-sector candidate','Zero spatial momentum','R_psi>0',
                           'Fermionic CAR for the finite normal-ordering calculation'],
            'lean':{'status':'NOT_RUN_BY_THIS_SCRIPT','evidence_record':'reports/lean_psi_rest_hamiltonian_2026_09_16.json'},
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'limitations':['Numerical eigenvectors are examples, not a universal proof.',
                           'No infinite Fock-space operator or vacuum renormalization is constructed.',
                           'No full UBT action, physical chirality selection, Newton constant or RH proof.'],
            'canonical_claim_status_changes':[]}
    if args.output:
        args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(checks,indent=2))

if __name__=='__main__':
    main()
