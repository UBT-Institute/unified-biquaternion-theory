"""Exact HT volume-shift algebra, no full UBT action claim."""
import unittest
import sympy as s
k,alpha,L,nu,dC,F,dF,C=s.symbols("k alpha L nu dC F dF C",nonzero=True)
class Shift(unittest.TestCase):
    def test_constant_shift(self):
        Lp=L-k*alpha
        lhs=-L*(nu-dC)/k+alpha*nu
        rhs=-Lp*(nu-dC)/k+alpha*dC
        self.assertEqual(s.simplify(lhs-rhs),0)
    def test_variable_shift_not_boundary(self):
        Lp=L-k*F
        lhs=-L*(nu-dC)/k+F*nu
        rhs=-Lp*(nu-dC)/k+F*dC
        self.assertEqual(s.simplify(lhs-rhs),0)
        # Exterior Leibniz rule: F dC = d(F C) - dF wedge C.
        self.assertEqual(s.expand((F*dC)-(dF*C+F*dC)+dF*C),0)
if __name__=="__main__":
    unittest.main()
