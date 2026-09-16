#!/usr/bin/env python3
"""Independent finite algebra for the chiral-current and winding audit.

No fundamental field, full-action selection or infinite operator is inferred.
© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]


def verify():
    eye,z=sp.eye(2),sp.zeros(2)
    pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
    g0=sp.Matrix(sp.BlockMatrix([[z,eye],[eye,z]]))
    gs=[g0]+[sp.Matrix(sp.BlockMatrix([[z,s],[-s,z]])) for s in pauli]
    C=sp.diag(-1,-1,1,1)
    PL,PR=(sp.eye(4)-C)/2,(sp.eye(4)+C)/2
    assert C.H*C==sp.eye(4)
    assert PL*PL==PL and PR*PR==PR and PL*PR==sp.zeros(4)
    for G in gs:
        assert C*G+G*C==sp.zeros(4)
        # bar(psi_R)=bar(psi) PL; thus the proposed opposite-chiral vector vanishes.
        assert PL*G*PL==sp.zeros(4) and PR*G*PR==sp.zeros(4)
        J=g0*G*PL
        assert C.H*J*C==J
    assert g0*g0*PL==PL and PL[0,0]==1  # actual nonzero even current
    # A general Hermitian chiral-diagonal interaction, not just a scalar shift.
    a,b,c,d,e,f,g,h,m,E=sp.symbols('a b c d e f g h m E',real=True)
    VL=sp.Matrix([[a,c+sp.I*d],[c-sp.I*d,b]])
    VR=sp.Matrix([[e,g+sp.I*h],[g-sp.I*h,f]])
    V=sp.diag(VL,VR)
    H=-sp.I*m*g0*C+V
    assert V.H==V and C*V==V*C
    assert H.H==H and sp.simplify(C*H*C-H.subs(m,-m))==sp.zeros(4)
    # Spatial kinetic alpha matrices and left chiral vector kernels commute with C.
    for G in gs:
        alpha=g0*G
        assert C*alpha==alpha*C
        assert C*(alpha*PL)==(alpha*PL)*C
    # Transparent two-component example: V_L and V_R may be unequal.
    H2=sp.Matrix([[a,-sp.I*m],[sp.I*m,b]])
    assert sp.expand((E*sp.eye(2)-H2).det()-((E-a)*(E-b)-m*m))==0
    # Reflection of the +1 coefficient is the -1 coefficient, not its negative.
    positive=lambda k: int(k==1)
    assert positive(-1)==0 and positive(-(-1))==1
    assert positive(-1)!=-positive(1) and positive(-1)!=positive(1)
    # Nondegenerate and degenerate cases: transport whole eigenbases by C.
    Cn=np.diag([-1,-1,1,1]).astype(complex)
    potentials=[np.diag([3.,3.,0.,0.]),np.diag([2.,-1.,0.,0.]),
                np.array([[1,2+1j,0,0],[2-1j,-2,0,0],[0,0,3,1j],[0,0,-1j,1]],complex)]
    cases=0
    for mu in [-2.,-.5,.5,2.]:
        H0=np.array((-sp.I*m*g0*C).subs(m,mu)).astype(complex)
        for interaction in potentials:
            Hp,Hn=H0+interaction,-H0+interaction
            energy,U=np.linalg.eigh(Hp)
            transformed=Cn@U
            assert np.allclose(Hn@transformed,transformed*energy,atol=1e-12,rtol=0)
            assert np.allclose(np.linalg.eigvalsh(Hn),energy,atol=1e-12,rtol=0)
            assert np.allclose(np.sum(np.abs(U[:2])**2,axis=0),
                               np.sum(np.abs(transformed[:2])**2,axis=0),atol=1e-12,rtol=0)
            cases+=1
    return {'all_four_vector_current_projector_identities':'PASS',
            'nonzero_left_current_even':'PASS','general_hermitian_diagonal_interaction':'PASS',
            'spatial_and_left_vector_terms_commute':'PASS','two_component_characteristic':'PASS',
            'reflection_counterexample':'PASS','numerical_eigenbasis_transport_cases':cases}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    checks=verify()
    paths=['formal/lean/UBT/Action/ChiralInteraction.lean','tools/verify_chiral_current_interaction.py',
           'tests/test_chiral_current_interaction.py']
    paths += [f'research_tracks/complex_time_branch_selection/chiral_current_interaction_audit.{lang}.md' for lang in ['en','cs']]
    report={'schema':'ubt-verification/v1','date':'2026-09-16','result':'PASS','checks':checks,
            'tools':{'sympy':sp.__version__,'numpy':np.__version__},
            'lean':{'status':'NOT_RUN_BY_THIS_SCRIPT','evidence_record':'reports/lean_chiral_interaction_2026_09_16.json'},
            'assumptions':['Declared Dirac-sector matrix representation','Same winding-independent C-even interaction for both signs'],
            'limitations':['No derived full UBT action or gauge representation dictionary.',
                           'No claim for winding-asymmetric backgrounds, boundary domains or C-odd interactions.',
                           'Formal eigenspace transport is an algebraic identity, not an infinite-operator domain theorem.'],
            'source_sha256':{s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in paths}}
    if args.output:args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(checks,indent=2))

if __name__=='__main__':main()
