from tools.verify_theta_hamiltonian_bridge import verify


def test_adm_legendre_transform():
    r = verify()
    assert all(r[k] == 'PASS' for k in ('legendre_transform', 'momentum_inversion', 'hamilton_velocity_equation'))
