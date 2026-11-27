"""Exact arithmetic checks for the E8 integration proposal; not a physical model."""
from itertools import combinations, product
import unittest

class TestE8Integration(unittest.TestCase):
    def test_order_five(self):
        # Exponents modulo 5 on the four matrix units under conjugation by diag(z,1).
        weights = (0, 1, -1, 0)
        self.assertTrue(all(5*w % 5 == 0 for w in weights))
        self.assertTrue(all(any(n*w % 5 for w in weights) for n in range(1,5)))

    def test_roots_and_second_moment(self):
        # Doubled coordinates; exact integers throughout.
        roots = set()
        for i,j in combinations(range(8),2):
            for a,b in product((-2,2),repeat=2):
                r=[0]*8
                r[i],r[j]=a,b
                roots.add(tuple(r))
        roots.update(r for r in product((-1,1),repeat=8) if sum(r)%4==0)
        self.assertEqual(len(roots),240)
        for r in roots:
            self.assertEqual(sum(x*x for x in r),8)
            # Diagonal D4 glue: both halves have the same coset.
            self.assertEqual(sum(r[:4])%4,sum(r[4:])%4)
        for i,j in product(range(8),repeat=2):
            self.assertEqual(sum(r[i]*r[j] for r in roots),240 if i==j else 0)

if __name__ == "__main__":
    unittest.main()
