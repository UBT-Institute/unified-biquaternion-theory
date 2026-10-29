import sympy as s

def test_auxiliary_shift_and_el_equations():
    dx,u,deps=s.symbols("dx u deps")
    E=dx+u
    assert s.expand((dx+deps)+(u-deps)-E)==0
    L=E**2/2
    assert s.diff(L,u)==E
    assert s.solve(s.diff(L,u),u)==[-dx]

def test_chain_rule_integration_by_parts_analogue():
    # For L(E), E = dot(x)+u, δL = EL_x δx + EL_u δu + d_t (P_E δx).
    E, dE, dxvar, ddxvar, duvar=s.symbols("E dE dxvar ddxvar duvar")
    variation=E*(ddxvar+duvar)
    bulk=(-dE)*dxvar+E*duvar
    boundary_derivative=dE*dxvar+E*ddxvar
    assert s.simplify(variation-bulk-boundary_derivative)==0
