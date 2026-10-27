import sympy as s

def test_integer_quadratic_form_with_half_integer_offdiagonal():
    B=s.Matrix([[1,s.Rational(1,2)],[s.Rational(1,2),2]])
    for i in range(-5,6):
        for j in range(-5,6):
            n=s.Matrix([i,j])
            assert (n.T*B*n)[0].is_integer
    assert B[0,1].q==2

def test_irrational_diagonal_ratios_cannot_share_full_revival():
    ratio=s.sqrt(2)
    assert ratio.is_rational is False
    # If both beta/R1² and beta/R2² are integers, their ratio is rational.
    # R2²/R1²=sqrt(2) violates this necessary requirement.

def test_basis_and_pair_sums_characterize_integral_quadratic_form():
    a,b,c=s.symbols("a b c")
    B=s.Matrix([[a,b],[b,c]])
    e1=s.Matrix([1,0]);e2=s.Matrix([0,1])
    q=lambda n:(n.T*B*n)[0]
    assert s.simplify(q(e1+e2)-q(e1)-q(e2))==2*b
