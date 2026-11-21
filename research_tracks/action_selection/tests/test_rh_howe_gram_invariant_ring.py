"""Polynomial invariant-ring check for the Gram-sector local Howe pair.

For two Lorentz vectors the scalar Gram variables Q,R,S transform under
the standard SL2 action. The exact invariant subring in R[Q,R,S] is R[QR-S^2].
This algebraic fact alone does not establish SL2 as physical UBT gauge.
"""
import unittest
import sympy as sp

Q, R, S = sp.symbols("Q R S")
Delta = Q*R - S**2


def e_operator(p):
    return sp.expand(2*S*sp.diff(p, Q)+R*sp.diff(p, S))


def f_operator(p):
    return sp.expand(2*S*sp.diff(p, R)+Q*sp.diff(p, S))


def h_operator(p):
    return sp.expand(2*Q*sp.diff(p, Q)-2*R*sp.diff(p, R))


class HoweGramInvariantRingTests(unittest.TestCase):
    def test_delta_is_annihilated_by_all_sl2_generators(self):
        for op in (e_operator, f_operator, h_operator):
            self.assertEqual(op(Delta), 0)

    def test_powers_of_delta_are_invariant(self):
        for n in range(1, 7):
            for op in (e_operator, f_operator, h_operator):
                self.assertEqual(op(Delta**n), 0)

    def test_h_invariance_forces_equal_q_r_exponents(self):
        for i in range(4):
            for j in range(4):
                monomial = Q**i*R**j*S**2
                self.assertEqual(h_operator(monomial), 2*(i-j)*monomial)

    def test_e_invariance_reduces_to_discriminant_pde(self):
        T = Q*R
        for a in range(1, 5):
            for b in range(0, 4):
                p = T**a*S**b
                # E[p]=R(2 S d_T p+d_S p).
                target = R*(2*S*a*T**(a-1)*S**b
                            + (b*T**a*S**(b-1) if b else 0))
                self.assertEqual(sp.expand(e_operator(p)-target), 0)

    def test_all_invariants_through_gram_degree_six(self):
        # Exhaustive linear invariant space in homogeneous R[Q,R,S]_m.
        # For m even: span{Delta**(m/2)}; for m odd: zero.
        for m in range(7):
            monomials = [
                Q**i*R**j*S**(m-i-j)
                for i in range(m+1) for j in range(m+1-i)
            ]
            cs = sp.symbols(f"c0:{len(monomials)}")
            p = sum(c*mon for c, mon in zip(cs, monomials))
            eqs = [
                a for op in (e_operator, f_operator, h_operator)
                for a in sp.Poly(op(p), Q, R, S).coeffs()
            ]
            if eqs:
                matrix, _ = sp.linear_eq_to_matrix(eqs, cs)
                kernel = matrix.nullspace()
            else:
                kernel = [sp.ones(1, 1)]
            self.assertEqual(len(kernel), int(m % 2 == 0))
            if m % 2 == 0:
                basis = sp.factor(sum(kernel[0][i]*monomials[i]
                                      for i in range(len(monomials))))
                self.assertEqual(sp.simplify(basis / Delta**(m//2)), 1)


if __name__ == "__main__":
    unittest.main()
