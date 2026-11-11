"""Two-mode theta degeneracies and prime filters: exact integer checks."""
from math import isqrt


def r2(n):
    bound = isqrt(n)
    return sum(1 for a in range(-bound, bound+1)
               for b in range(-bound, bound+1) if a*a+b*b==n)


def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def div_character(d):
    return 0 if d%2==0 else (1 if d%4==1 else -1)


def test_two_square_counts_jacobi():
    for n in range(1,181):
        target=4*sum(div_character(d) for d in range(1,n+1) if n%d==0)
        assert r2(n)==target, (n,r2(n),target)


def test_prime_residue_selection():
    for p in range(2,200):
        if not prime(p):
            continue
        target=4 if p==2 else 8 if p%4==1 else 0
        assert r2(p)==target


def test_137_vs_139():
    assert 11**2+4**2==137
    assert r2(137)==8
    assert r2(139)==0
    assert r2(139**2)==4


def test_dirichlet_euler_local_factors():
    # For p=1 mod 4: a_{p^k}=(k+1), since r2(p^k)/4=k+1.
    assert [r2(5**k)//4 for k in range(5)]==[1,2,3,4,5]
    # For p=3 mod 4: odd powers excluded; even powers carry four reps.
    assert [r2(3**k)//4 for k in range(7)]==[1,0,1,0,1,0,1]
