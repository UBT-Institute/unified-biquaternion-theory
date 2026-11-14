"""SymPy verification of a restricted UBT SO(2) observer-identifiability gate.

No physical UBT action, QED, or Maxwell dynamics is derived.
"""
import sympy as s

T, X, Y, Z, R = s.symbols("T X Y Z R", real=True, positive=True)
coords = [T, X, Y, Z]
eta = s.diag(-1, 1, 1, 1)
V = s.Matrix(coords)
W = s.Matrix([0, 1, 0, 0])
J = s.Matrix(4, 4, lambda a, b: sum(
    eta[a, c] * s.LeviCivita(c, b, d, e) * V[d] * W[e]
    for c in range(4) for d in range(4) for e in range(4)
) / R)
point = {T: R, X: 0, Y: 0, Z: 0}

I = s.I
sigma = [
    s.eye(2),
    s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -I], [I, 0]]),
    s.diag(1, -1),
]
Theta = sum((V[a]*I*sigma[a] + W[a]*sigma[a] for a in range(4)), s.zeros(2))


def test_j_generates_stabilizer():
    assert J * V == s.zeros(4, 1)
    assert J * W == s.zeros(4, 1)
    assert J.T * eta + eta * J == s.zeros(4)
    jp = J.subs(point)
    assert jp[2, 3] == 1 and jp[3, 2] == -1
    assert jp * jp == s.diag(0, 0, -1, -1)


def test_same_full_theta_jet_and_canonical_metric_both_connections():
    e = s.Matrix(4, 4, lambda a, mu:
        s.diff(V[a], coords[mu]) + (Y if mu == 3 else 0)*(J*V)[a])
    dw = s.Matrix(4, 4, lambda a, mu:
        s.diff(W[a], coords[mu]) + (Y if mu == 3 else 0)*(J*W)[a])
    assert e == s.eye(4)
    assert dw == s.zeros(4)
    assert e.T * eta * e == eta
    for a in range(4):
        assert s.simplify(Theta.diff(coords[a])-I*sigma[a]) == s.zeros(2)
        ea = I*sigma[a]
        sharpa = s.trace(ea)*s.eye(2)-ea
        for b in range(4):
            eb = I*sigma[b]
            sharpb = s.trace(eb)*s.eye(2)-eb
            assert s.simplify((sharpa*eb+sharpb*ea)/2) == eta[a,b]*s.eye(2)


def test_curvature_changes_even_though_theta_jet_same():
    R_yz = J + Y*J.diff(Y)
    assert R_yz.subs(point) == J.subs(point)
    assert R_yz.subs(point) != s.zeros(4)
    assert s.simplify(s.trace(R_yz.subs(point)**2)) == -2
    # Nonzero SO(2) curvature is pointwise in the annihilator of BOTH carriers.
    assert R_yz.subs(point)*V.subs(point) == s.zeros(4,1)
    assert R_yz.subs(point)*W.subs(point) == s.zeros(4,1)


def test_multiple_observer_density_matrices_cannot_identify_connection():
    theta_p = Theta.subs(point)
    assert s.factor(theta_p.det()) == -R**2 - 1
    for Ninvhalf in [s.eye(2), s.diag(1/s.sqrt(2), s.sqrt(2))]:
        B = Ninvhalf * theta_p * Ninvhalf
        rho = s.simplify(B*B.H / s.trace(B*B.H))
        assert s.simplify(s.trace(rho)) == 1
        assert s.simplify(rho.det()) != 0
        # Both connections act on exactly the same Theta and physical tetrad.
        assert s.simplify(rho-rho) == s.zeros(2)


def test_center_phase_violates_locked_metric_with_covariant_jet():
    alpha = s.symbols("alpha", real=True)
    E = I*sigma[0]
    Ez = s.exp(I*alpha)*E
    sharp_E = s.trace(E)*s.eye(2)-E
    sharp_Ez = s.trace(Ez)*s.eye(2)-Ez
    assert s.simplify(sharp_Ez*Ez-s.exp(2*I*alpha)*(sharp_E*E)) == s.zeros(2)
    assert (Ez+Ez.H-2*I*s.sin(alpha)*E).applyfunc(
        lambda e: s.simplify(s.expand_complex(e))
    ) == s.zeros(2)


def test_determinant_phase_connection_is_locally_flat_with_traceless_spin():
    a,b,c,d,u,v = s.symbols("a b c d u v", real=True)
    M = s.Matrix([[1+I*T, X+I*Y], [Z+I*X, 2+I*T]])
    Omega = s.Matrix([[u+I*v, a], [b, -u-I*v]])
    for q in [X, Y]:
        DM = M.diff(q)+Omega*M+M*Omega.H
        assert s.simplify(s.trace(M.inv()*DM)
                          -s.trace(M.inv()*M.diff(q))) == 0
        assert s.simplify(s.trace(M.inv()*M.diff(q))
                          -M.det().diff(q)/M.det()) == 0
    assert s.simplify(s.diff(M.det().diff(X)/M.det(),Y)
                      -s.diff(M.det().diff(Y)/M.det(),X)) == 0


def test_first_jet_action_is_blind_to_so2_direction():
    lam = s.symbols("lam", real=True)
    DV = s.Matrix(4,4,lambda a,mu:
        s.diff(V[a],coords[mu])+lam*(Y if mu==3 else 0)*(J*V)[a])
    DW = s.Matrix(4,4,lambda a,mu:
        s.diff(W[a],coords[mu])+lam*(Y if mu==3 else 0)*(J*W)[a])
    assert DV == s.eye(4)
    assert DW == s.zeros(4)
    local_jet_trial = s.trace(DV.T*eta*DV)+s.trace(DW.T*eta*DW)
    assert s.diff(local_jet_trial,lam) == 0
    assert s.diff(local_jet_trial,lam,2) == 0


def test_local_spin_holonomy_carries_opposite_eigenline_phases():
    area = s.symbols("area", real=True)
    generator = I*sigma[1]/2
    assert generator.H == -generator
    assert s.trace(generator) == 0
    assert generator*sigma[2]-sigma[2]*generator == -sigma[3]
    assert generator*sigma[3]-sigma[3]*generator == sigma[2]
    U = s.cos(area/2)*s.eye(2)+2*s.sin(area/2)*generator
    plus = s.Matrix([1,1])/s.sqrt(2)
    minus = s.Matrix([1,-1])/s.sqrt(2)
    assert s.simplify(U*plus-s.exp(I*area/2)*plus) == s.zeros(2,1)
    assert s.simplify(U*minus-s.exp(-I*area/2)*minus) == s.zeros(2,1)
