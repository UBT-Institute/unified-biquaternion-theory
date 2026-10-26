from math import gcd
from sympy import mobius, divisors

def test_binary_rotation_orbits():
    F=lambda n: 2**gcd(6,n)
    O=lambda n: sum(int(mobius(d))*F(n//d) for d in divisors(n))//n
    assert [F(n) for n in (1,2,3,6)] == [2,4,8,64]
    assert [O(n) for n in (1,2,3,6)] == [2,1,2,9]
    assert sum(n*O(n) for n in (1,2,3,6)) == 64
