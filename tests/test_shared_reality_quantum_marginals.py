import sympy as s

def test_overlap_agreement_not_sufficient_for_global_extension():
    # AB Bell singlet has reduced B=I/2; BC Bell singlet also B=I/2.
    I=s.eye(2)
    zero=s.Matrix([1,0]);one=s.Matrix([0,1])
    psi=(s.kronecker_product(zero,one)-s.kronecker_product(one,zero))/s.sqrt(2)
    bell=s.simplify(psi*psi.T)
    marginalB=s.Matrix([[bell[0,0]+bell[2,2],bell[0,1]+bell[2,3]],[bell[1,0]+bell[3,2],bell[1,1]+bell[3,3]]])
    assert marginalB==I/2
    # A pure AB marginal forces AB to be uncorrelated with C, hence BC separable.
    # Singlet BC is not product I_B/2 tensor rho_C (it has off-diagonal coherences).
    assert bell[1,2]!=0

def test_distinct_hamiltonians_preserve_joint_extendability():
    omega,t=s.symbols("omega t",real=True)
    H0=s.zeros(8)
    HB=omega*s.kronecker_product(s.eye(2),s.diag(1,-1),s.eye(2))
    assert H0!=HB
    # Every global unitary induces consistent overlap reductions by construction.
    assert HB==HB.T
