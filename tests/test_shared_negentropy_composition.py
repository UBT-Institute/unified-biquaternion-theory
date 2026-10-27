import sympy as s

def test_bell_negentropy_is_all_mutual_information():
    ln2=s.log(2)
    SA=SB=ln2
    SAB=s.Integer(0)
    JA=JB=0
    I=SA+SB-SAB
    assert I==2*ln2
    assert JA+JB+I==2*ln2

def test_ghz_chain_counts_three_party_correlations_once():
    z=s.log(2)
    SA=SB=SC=z
    SAB=z
    SABC=0
    IAB=SA+SB-SAB
    IAB_C=SAB+SC-SABC
    assert IAB==z and IAB_C==2*z
    assert s.simplify(IAB+IAB_C-3*z)==0

def test_mixed_state_cannot_select_hamiltonian():
    rho=s.eye(2)/2
    H1=s.diag(0,1)
    H2=s.Matrix([[0,1],[1,0]])
    assert H1 != H2
    assert H1*rho-rho*H1==s.zeros(2)
    assert H2*rho-rho*H2==s.zeros(2)
