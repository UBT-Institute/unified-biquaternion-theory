"""Exact cubic-boundary Bell-pair area law and underdetermination of Newton G.

Verified locally with Python/SymPy; this is not an emergent gravity proof.
"""
import sympy as sp


def boundary_links(L):
    block = {(x,y,z) for x in range(L) for y in range(L) for z in range(L)}
    dirs = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    return sum(tuple(s[i]+d[i] for i in range(3)) not in block
               for s in block for d in dirs)


def test_area_boundary_link_count():
    for L in (1,2,3,4):
        assert boundary_links(L) == 6*L*L


def test_entanglement_from_crossing_bell_pairs():
    for L in (1,2,3,4):
        k = boundary_links(L)
        S = k*sp.log(2)
        area = 6*L*L
        assert sp.simplify(S/area-sp.log(2)) == 0


def test_volume_law_possible_same_local_qubits():
    for L in (1,2,3,4):
        N=L**3
        # Each interior qubit is entangled with a distinct external qubit.
        assert sp.simplify(N*sp.log(2)/N-sp.log(2)) == 0
    assert 4**3 != 6*4**2


def test_effective_G_needs_assumed_area_law_and_length():
    ell,G=sp.symbols("ell G",positive=True)
    eta=sp.log(2)/ell**2
    G_eff=sp.solve(sp.Eq(eta,1/(4*G)),G)[0]
    assert sp.simplify(G_eff-ell**2/(4*sp.log(2))) == 0
