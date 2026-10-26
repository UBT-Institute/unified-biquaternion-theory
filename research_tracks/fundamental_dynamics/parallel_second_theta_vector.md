# A parallel second Theta vector is an exact gradient and annihilates torsion

**26 October 2026. Exact conditional geometric corollary of the two-vector Lorentz lift.** Not a dynamical field equation, not a selected unique connection/action, and not evidence of a physical time qubit.

## Hypotheses

Let `v^a` and `w^a` be real Lorentz-vector fields on a nondegenerate oriented tetrad patch. Assume a metric-compatible Lorentz connection `omega` with

```
D_mu v^a = sqrt(N0) e_mu^a,
D_mu w^a = 0,
N0 > 0 fixed.
```

Let `Gamma` be its metric-compatible affine connection obeying the tetrad postulate; choose `T^rho_{mu nu}=Gamma^rho_{mu nu}-Gamma^rho_{nu mu}`. These are the *restricted Lorentz-vector classical slice* hypotheses of the merged time-qubit and two-vector studies, not the general off-slice eight-real biquaternionic action.

Define the internal Lorentz scalar `f=eta_ab v^a w^b` and the spacetime covector `w_mu=e_mu^a eta_ab w^b`.

## Exact theorem

Metric compatibility and the Leibniz rule give:

```
partial_mu f = (D_mu v)·w + v·(D_mu w)
             = sqrt(N0) w_mu.
```

Consequently

```
w_flat = df / sqrt(N0);
d w_flat = 0;
g^mu nu (partial_mu f)(partial_nu f) = N0 (w·w) = constant;
```

where constancy of `w·w` follows from `Dw=0`.

From the tetrad postulate, `D_mu w^a=e_nu^a nabla^Gamma_mu w^nu`, hence `nabla^Gamma w=0`. For a parallel covector, antisymmetrizing the affine covariant derivative gives `d w_flat = T^rho_{mu nu} w_rho dx^mu∧dx^nu /2` under the stated torsion convention. Since `d w_flat=0`:

```
boxed: w_rho T^rho_{mu nu} = 0.
```

The commutator of covariant derivatives on a parallel vector additionally gives

```
boxed: R^rho_{sigma mu nu}(Gamma) w^sigma = 0.
```

In summary, a nonzero parallel second real carrier demands (i) a locally exact fixed-norm covector, (ii) torsion with no output along that covector, and (iii) affine holonomy fixing that vector. These are necessary geometric restrictions beyond the raw 12→4 algebraic stabilizer reduction.

## Scope and examples

- Flat inertial representer `N0=1, e_mu^a=delta_mu^a, omega=0, v^a=x^a, w^a=constant` satisfies all relations. For e.g. w=(0,1,0,0), f=x and w_flat=dx. Therefore these necessary conditions are not contradictory in all backgrounds.
- The canonical torsionful FLRW representer with spatial boost connection `omega^i_0=e^i/rho` has no nonzero parallel w and was already excluded in the merged time-qubit audit.
- Locally `w^2>0` can coexist with timelike v; a **spacelike** exact covector is not another arrow of physical time. An additional physical interpretation requires a derived dynamical coupling.
- Because w is a preexisting component of the single complex Theta, no new independent physical field has been posited. But its parallel transport and reality must be justified from the final canonical action, and it may vanish on shell.
- Neither `T·w=0` nor `Rw=0` fixes residual SO(2) curvature and neither yields a reduced physical Hamiltonian.

## Reproducible checks

`tests/test_parallel_theta_sector.py` checks the derivation using a nontrivial constant flat parallel vector, an explicitly torsionful stabilizer connection at one point, and analytic first-jet identities.
