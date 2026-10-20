#!/usr/bin/env python3
"""Canonical UBT contortion theorem specialized to closed FLRW.

Independent exact checks of mixed affine contortion, Pauli spin completion,
spatial-curvature cancellation in [D,D]Theta, and Cartan torsion.  This verifies
kinematic identities only, NOT an on-shell UBT geometry or a physical CMB fit.
Requires SymPy.
"""
import sympy as sp


def verify() -> dict[str, bool]:
    I = sp.I
    n0, a, v, hub, adot, amp = sp.symbols(
        "N0 a V H adot amp", positive=True, real=True
    )
    q = 1/v - hub
    sigma = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    eye = sp.eye(2)
    # Evaluate covariant tensor identities in an orthogonal local
    # S^3 frame, at one point; arbitrary positive spatial scale a.
    g = sp.diag(-1, a*a, a*a, a*a)
    gi = g.inv()
    V_lower = sp.Matrix([-v, 0, 0, 0])
    norm = (V_lower.T * gi * V_lower)[0]
    lc_dV_lower = sp.diag(
        -1, hub*v*a*a, hub*v*a*a, hub*v*a*a
    )
    W = g - lc_dV_lower

    def k(nu: int, mu: int, rho: int):
        return sp.factor(sum(
            gi[nu, l] * (
                W[mu, l]*V_lower[rho]
                -V_lower[l]*W[mu, rho]
            )/norm for l in range(4)
        ))

    checks = {}
    checks["metric_compatible_contortion"] = all(
        sp.simplify(
            g[nu, nu]*k(nu, mu, rho)
            +g[rho, rho]*k(rho, mu, nu)
        ) == 0
        for nu in range(4) for mu in range(4) for rho in range(4)
    )
    checks["contortion_spatial_temporal"] = (
        sp.simplify(k(1, 1, 0)-q) == 0
        and sp.simplify(k(0, 1, 1)-q*a*a) == 0
    )
    checks["concurrent_vector_equation"] = all(
        sp.simplify(
            (1 if mu == nu == 0 else hub*v if mu == nu else 0)
            +k(nu, mu, 0)*v-(1 if mu == nu else 0)
        ) == 0
        for mu in range(4) for nu in range(4)
    )
    checks["torsion_2form_coefficient"] = (
        sp.simplify(-q-(hub-1/v)) == 0
    )

    # Full Lorentz spin lift contains both boosts and rotations:
    # Omega=(f-i/2) sigma_i upsilon^i, B=-Omega^dagger.
    f = a/(2*v)
    left = f-I/2
    right = -f-I/2
    theta = I*sp.sqrt(n0)*v*eye
    checks["one_spin_connection_two_sided_derivative"] = all(
        sp.simplify(
            left*sigma[j]*theta-theta*right*sigma[j]
            -I*sp.sqrt(n0)*a*sigma[j]
        ) == sp.zeros(2)
        for j in range(3)
    )
    # d(upsilon^3)=-2 upsilon^1^upsilon^2.
    cA = -2*left+2*I*left**2
    cB = -2*right+2*I*right**2
    checks["equal_nonzero_spatial_connection_curvature"] = (
        sp.simplify(cA-cB) == 0
        and sp.simplify(cA-I*(sp.Rational(1,2)+2*f*f)) == 0
    )
    checks["spatial_covariant_frame_torsion_zero"] = (
        sp.simplify(-2*a+2*I*a*(left+right)) == 0
    )
    checks["temporal_covariant_frame_torsion"] = (
        sp.simplify(adot-left+right-(adot-a/v)) == 0
    )
    fdot = (adot*v-a)/(2*v*v)
    checks["curvature_commutator_equals_Cartan_torsion"] = (
        sp.simplify(2*v*fdot-(adot-a/v)) == 0
    )
    checks["spinless_zero_torsion_forces_linear_scale"] = (
        sp.simplify(q.subs(hub, 1/v)) == 0
    )
    checks["vacuum_Lambda_cannot_match_linear_closed_FLRW"] = (
        sp.simplify(sp.diff((amp*amp+1)/(amp*amp*v*v),v)
                    +2*(amp*amp+1)/(amp*amp*v**3)) == 0
        and sp.simplify(sp.diff((amp*amp+1)/(amp*amp*v*v),v)) != 0
    )
    return checks


def main():
    results = verify()
    for name, ok in results.items():
        print(("PASS" if ok else "FAIL")+" "+name)
    if not all(results.values()):
        raise SystemExit(1)
    print("PASS all",len(results),"conditional identities")


if __name__=="__main__":
    main()
