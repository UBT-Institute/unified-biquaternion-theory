import unittest
import sympy as s
from itertools import permutations
eta=[-1,1,1,1]
T=s.MutableDenseNDimArray.zeros(4,4,4)
for a in range(4):
 for b in range(4):
  for c in range(b+1,4):
   T[a,b,c]=s.Integer((a+1)*(b+2)-(c+1))
   T[a,c,b]=-T[a,b,c]
t=[sum(eta[a]*T[a,a,b] for a in range(4)) for b in range(4)]
A=s.MutableDenseNDimArray.zeros(4,4,4)
Q=s.MutableDenseNDimArray.zeros(4,4,4)
for a in range(4):
 for b in range(4):
  for c in range(4):
   A[a,b,c]=(T[a,b,c]+T[b,c,a]+T[c,a,b])/3
   V=((eta[a]*t[c] if a==b else 0)-(eta[a]*t[b] if a==c else 0))/3
   Q[a,b,c]=T[a,b,c]-V-A[a,b,c]
class TestTorsion(unittest.TestCase):
 def test_tracefree(self):
  for b in range(4): self.assertEqual(s.simplify(sum(eta[a]*Q[a,a,b] for a in range(4))),0)
 def test_zero_three_form(self):
  for a,b,c in permutations(range(4),3):
   self.assertEqual(s.simplify(Q[a,b,c]+Q[b,c,a]+Q[c,a,b]),0)
 def test_antisymmetry(self):
  for a in range(4):
   for b in range(4):
    for c in range(4):self.assertEqual(s.simplify(Q[a,b,c]+Q[a,c,b]),0)
if __name__=='__main__': unittest.main()
