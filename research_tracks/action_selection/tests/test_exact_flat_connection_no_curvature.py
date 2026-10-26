"""Exact nonlinear coordinate-pullback flatness witness for zero-connection Theta branch."""
import unittest
import sympy as s
t,x,k=s.symbols('t x k',real=True)
coords=(t,x)
Y=s.Matrix([t,x+k*t**2])
J=Y.jacobian(coords)
g=s.simplify(J.T*s.diag(-1,1)*J)
gi=s.simplify(g.inv())
G=[[[s.simplify(sum(gi[a,d]*(s.diff(g[d,c],coords[b])+s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d])) for d in range(2))/2) for c in range(2)] for b in range(2)] for a in range(2)]
def curvature(a,b,c,d):
 return s.simplify(s.diff(G[a][b][d],coords[c])-s.diff(G[a][b][c],coords[d])+sum(G[a][c][m]*G[m][b][d]-G[a][d][m]*G[m][b][c] for m in range(2)))
class Tests(unittest.TestCase):
 def test_metric(self):self.assertEqual(g,s.Matrix([[4*k**2*t**2-1,2*k*t],[2*k*t,1]]))
 def test_nondegenerate(self):self.assertEqual(s.simplify(g.det()),-1)
 def test_nonzero_christoffel(self):self.assertEqual(G[1][0][0],2*k)
 def test_zero_curvature(self):
  for a in range(2):
   for b in range(2):
    for c in range(2):
     for d in range(2):
      self.assertEqual(curvature(a,b,c,d),0)
if __name__=='__main__':unittest.main()
