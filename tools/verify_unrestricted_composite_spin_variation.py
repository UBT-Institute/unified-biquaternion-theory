#!/usr/bin/env python3
"""Exact unrestricted (non-FLRW) composite spin first-variation identity.

Take X^a as a Lorentz four-vector (the positive-Hermitian sector of Theta),
q=sqrt(N0), e^a_mu=(partial_mu X^a+omega_mu^a_b X^b)/q.
For a general independent tetrad/connection parent action with Euler
3-forms E_a and C_ab (upper antisymmetric spin variations, a<b), its
composite Euler forms satisfy
    E_X,a = -(D E)_a/q          (if no explicit X in parent action)
    C_comp,ab = C_ab+(X_b E_a-X_a E_b)/q.
The spin correction vanishes for E_a=X_a J (pure normal projection).
At every timelike point the map delta omega -> delta e (fixed X, dX)
has rank 12 and 12 rotational-kernel directions.

Checks include direct finite-dimensional polynomial variational derivatives,
a full 4-vector Lorentz-covariance identity, normal projection annihilation,
and 16x24 pointwise Jacobian. This does not derive the parent UBT action.
"""
import sympy as sp


def verify_unrestricted_composite_spin():
    q=sp.symbols("q",positive=True)
    eta=sp.diag(-1,1,1,1)
    x=sp.Matrix(sp.symbols("x0:4",real=True))
    dx=sp.Matrix(sp.symbols("dx0:4",real=True))
    pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
    Wvars=sp.symbols("w0:6",real=True)
    EPSvars=sp.symbols("eps0:6",real=True)
    DEPSvars=sp.symbols("deps0:6",real=True)
    def matrix(variables):
        up=sp.zeros(4)
        for (a,b),value in zip(pairs,variables):
            up[a,b]=value
            up[b,a]=-value
        return up*eta
    Om=matrix(Wvars)
    Ep=matrix(EPSvars)
    dEp=matrix(DEPSvars)
    e=(dx+Om*x)/q
    checks={}
    checks["antisymmetric_spin_is_Lorentz"]=Om.T*eta+eta*Om==sp.zeros(4)
    checks["infinitesimal_Lorentz_lift_covariant"]=(
        sp.simplify(
            (dEp*x+Ep*dx) + Om*(Ep*x)
            +(-dEp-Om*Ep+Ep*Om)*x-Ep*(dx+Om*x)
        )==sp.zeros(4)
    )
    checks["metric_invariant_under_local_Lorentz"]=(
        sp.simplify(
           (e.T*eta*(Ep*e))[0]+((Ep*e).T*eta*e)[0]
        )==0
    )
    # A generic local parent functional with nonzero independent
    # connection Euler source Q and nontrivial coframe Hessian.
    Pa=sp.Matrix(sp.symbols("P0:4",real=True))
    Qa=sp.Matrix(sp.symbols("Q0:6",real=True))
    k=sp.symbols("k",real=True)
    L=(Pa.dot(e)+k*e.dot(e)/2+sum(Qa[j]*Wvars[j] for j in range(6)))
    E=Pa+k*e
    checks["chain_spin_all_six_components"]=all(
        sp.simplify(sp.diff(L,Wvars[j])-Qa[j]
            -( (eta*x)[b]*E[a]-(eta*x)[a]*E[b])/q)==0
        for j,(a,b) in enumerate(pairs)
    )
    checks["chain_first_jet_all_four_components"]=all(
        sp.simplify(sp.diff(L,dx[a])-E[a]/q)==0
        for a in range(4)
    )
    # Check that a derivative of the invariant clock is a fixed-norm
    # covector for an invertible 4x4 tetrad (algebraic identity).
    Emat=sp.Matrix([[2,1,0,0],[0,2,1,0],[0,0,2,1],[0,0,0,2]])
    xv=sp.Matrix([3,1,1,0])  # norm is -7
    r=sp.sqrt(-(xv.T*eta*xv)[0])
    clockgrad=-Emat*eta*xv/r
    metric=Emat*eta*Emat.T/q**2
    checks["invariant_clock_unit_norm_from_invertible_coframe"]=(
        sp.simplify((clockgrad.T*metric.inv()*clockgrad)[0]+q**2)==0
    )
    # Spin variation has twelve independent pointwise coframe columns,
    # NOT the full sixteen: timelike Lorentz orbit has dimension 3 per mu.
    v=sp.symbols("v",positive=True)
    x0=sp.Matrix([v,0,0,0])
    rows=[]
    for mu in range(4):
        local=matrix(Wvars)*x0/q
        rows.extend(list(local))
    # Re-evaluate each spacetime spin connection independently:
    Wmu=sp.symbols("O0:24")
    Eall=sp.Matrix(16,1,lambda idx,j:
        (matrix(Wmu[6*(idx//4):6*(idx//4)+6])*x0/q)[idx%4])
    J=Eall.jacobian(Wmu)
    checks["spin_only_coframe_Jacobian_16_by_24"]=J.shape==(16,24)
    checks["spin_only_coframe_pointwise_rank_12"]=J.rank()==12
    checks["spin_only_spatial_rotation_kernel_dim_12"]=len(J.nullspace())==12
    checks["spin_only_normal_tetrad_component_fixed"]=all(
        J[4*mu,:]==sp.zeros(1,24) for mu in range(4)
    )
    # A normal residual E_a = X_a Jscalar is annihilated
    # algebraically by the antisymmetric spin correction.
    Jscalar=sp.symbols("Jscalar")
    Enorm=eta*x*Jscalar
    checks["normal_Euler_residual_in_spin_kernel"]=all(
        sp.simplify((eta*x)[b]*Enorm[a]-(eta*x)[a]*Enorm[b])==0
        for a,b in pairs
    )
    # Mechanical (one-dimensional) analogue checks scalar
    # functional derivative, including the TOTAL derivative of E.
    tt=sp.symbols("tt",real=True)
    xt=sp.Matrix([sp.Function(f"X{i}")(tt) for i in range(4)])
    wt=[sp.Function(f"W{i}")(tt) for i in range(6)]
    omt=matrix(wt)
    et=(xt.diff(tt)+omt*xt)/q
    Pm=sp.Matrix(sp.symbols("Pmech0:4"))
    qst=sp.symbols("km",real=True)
    Lm=Pm.dot(et)+qst*et.dot(et)/2
    Em=Pm+qst*et
    scalarEL=sp.Matrix([
        sp.diff(Lm,xt[i])-sp.diff(sp.diff(Lm,sp.diff(xt[i],tt)),tt)
        for i in range(4)
    ])
    normalD=(omt.T*Em-Em.diff(tt))/q
    checks["full_scalar_functional_chain_rule"]=all(
        sp.simplify(scalarEL[i]-normalD[i])==0
        for i in range(4)
    )
    return checks


if __name__=="__main__":
    outcomes=verify_unrestricted_composite_spin()
    for label,good in outcomes.items():
        print(("PASS" if good else "FAIL"),label)
    if not all(outcomes.values()):
        raise SystemExit(1)
    print(f"PASS {len(outcomes)} unrestricted geometric variational identities")
