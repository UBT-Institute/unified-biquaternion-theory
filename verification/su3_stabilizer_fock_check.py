"""
verification/su3_stabilizer_fock_check.py
==========================================
Exact SymPy verification of the canonical UBT SU(3) stabiliser and
exterior/Fock derivation from su3_stabilizer_exterior_fock.tex.

All checks use exact symbolic/integer arithmetic (SymPy).  No floating-point
tolerances are used for theorem-critical algebra.

Run:
    python verification/su3_stabilizer_fock_check.py

Exit code 0 means all checks passed; nonzero means at least one failed.

© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
"""

import sys
from itertools import combinations

import sympy as sp
from sympy import (
    I as Im,
    Matrix,
    Rational,
    Symbol,
    symbols,
    sqrt,
    zeros,
    eye,
    conjugate,
    simplify,
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool) -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        print(f"  PASS  {name}")
        PASS_COUNT += 1
    else:
        print(f"  FAIL  {name}")
        FAIL_COUNT += 1


# ============================================================
# 1. Quaternion multiplication table
# ============================================================
print("\n[1] Quaternion multiplication — basic identities")

# Represent I,J,K as 2x2 complex matrices (standard):
# I -> -i sigma_1, J -> -i sigma_2, K -> -i sigma_3  ... BUT for
# product verification we use the direct multiplication table only.
# We encode quaternion multiplication as dictionaries.
# Basis: {1, I, J, K} with  I^2=J^2=K^2=-1, IJ=K, JK=I, KI=J (cyclic).

def quat_mul(a, b):
    """
    Multiply two quaternions given as (s, i, j, k) tuples (symbolic).
    Returns (s, i, j, k).
    """
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    s = a0*b0 - a1*b1 - a2*b2 - a3*b3
    i = a0*b1 + a1*b0 + a2*b3 - a3*b2
    j = a0*b2 - a1*b3 + a2*b0 + a3*b1
    k = a0*b3 + a1*b2 - a2*b1 + a3*b0
    return (s, i, j, k)

def scalar_part(q):
    return q[0]

ONE = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
QI  = (sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0))
QJ  = (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(0))
QK  = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))
NEG = (sp.Integer(-1), sp.Integer(0), sp.Integer(0), sp.Integer(0))

check("I^2 = -1", quat_mul(QI, QI) == NEG)
check("J^2 = -1", quat_mul(QJ, QJ) == NEG)
check("K^2 = -1", quat_mul(QK, QK) == NEG)
check("IJ = K",   quat_mul(QI, QJ) == QK)
check("JK = I",   quat_mul(QJ, QK) == QI)
check("KI = J",   quat_mul(QK, QI) == QJ)
check("JI = -K",  quat_mul(QJ, QI) == (0, 0, 0, -1))
check("KJ = -I",  quat_mul(QK, QJ) == (0, -1, 0, 0))
check("IK = -J",  quat_mul(QI, QK) == (0, 0, -1, 0))

# ============================================================
# 2. Symbolic determinant identity for Omega
# ============================================================
print("\n[2] Hermitian form h(v,w) = Sc(v^dagger w) and volume form Omega")

v1, v2, v3 = symbols("v1 v2 v3")
w1, w2, w3 = symbols("w1 w2 w3")
u1, u2, u3 = symbols("u1 u2 u3")

def make_v(a, b, c):
    return (sp.Integer(0), a, b, c)  # aI + bJ + cK

v_q = make_v(v1, v2, v3)
w_q = make_v(w1, w2, w3)
u_q = make_v(u1, u2, u3)

# Canonical Hermitian form from the biquaternionic adjoint.
def quat_dagger(q):
    s0, s1, s2, s3 = q
    return (conjugate(s0), -conjugate(s1), -conjugate(s2), -conjugate(s3))

h_biquat = sp.expand(scalar_part(quat_mul(quat_dagger(v_q), w_q)))
h_expected = conjugate(v1)*w1 + conjugate(v2)*w2 + conjugate(v3)*w3
check("Sc(v^dagger w) = sum conjugate(v_i) w_i", sp.expand(h_biquat-h_expected) == 0)
basis = [QI, QJ, QK]
gram = Matrix([[scalar_part(quat_mul(quat_dagger(a), b)) for b in basis] for a in basis])
check("Hermitian Gram matrix on (I,J,K) is identity", gram == eye(3))
check("h(I,I)=h(J,J)=h(K,K)=1", all(gram[i,i] == 1 for i in range(3)))

vw_q = quat_mul(v_q, w_q)
vwu_q = quat_mul(vw_q, u_q)

Omega_biquat = -scalar_part(vwu_q)
Omega_biquat = sp.expand(Omega_biquat)

M = Matrix([[v1, v2, v3], [w1, w2, w3], [u1, u2, u3]])
det_M = sp.expand(M.det())

diff_Omega = sp.expand(Omega_biquat - det_M)
check("Omega(v,w,u) = det([v;w;u]) (symbolic exact)", diff_Omega == sp.Integer(0))
check("Omega(I,J,K) = 1",
      sp.expand(
          -scalar_part(quat_mul(quat_mul(QI, QJ), QK))
      ) == sp.Integer(1))

# Verify alternating: swap v<->w, should negate
Omega_vwu = -scalar_part(quat_mul(quat_mul(make_v(v1,v2,v3), make_v(w1,w2,w3)), make_v(u1,u2,u3)))
Omega_wvu = -scalar_part(quat_mul(quat_mul(make_v(w1,w2,w3), make_v(v1,v2,v3)), make_v(u1,u2,u3)))
check("Omega alternating: Omega(w,v,u) = -Omega(v,w,u)",
      sp.expand(Omega_vwu + Omega_wvu) == sp.Integer(0))

# ============================================================
# 3. Gell-Mann matrices: Hermitian and traceless
# ============================================================
print("\n[3] Gell-Mann matrices: Hermitian and traceless")

# Standard Gell-Mann matrices (3x3, complex, exact)
lam = [None]  # 1-indexed

lam.append(Matrix([[0,1,0],[1,0,0],[0,0,0]]))           # lambda_1
lam.append(Matrix([[0,-Im,0],[Im,0,0],[0,0,0]]))         # lambda_2
lam.append(Matrix([[1,0,0],[0,-1,0],[0,0,0]]))           # lambda_3
lam.append(Matrix([[0,0,1],[0,0,0],[1,0,0]]))            # lambda_4
lam.append(Matrix([[0,0,-Im],[0,0,0],[Im,0,0]]))         # lambda_5
lam.append(Matrix([[0,0,0],[0,0,1],[0,1,0]]))            # lambda_6
lam.append(Matrix([[0,0,0],[0,0,-Im],[0,Im,0]]))         # lambda_7
lam.append(Matrix([[1,0,0],[0,1,0],[0,0,-2]])/sqrt(3))  # lambda_8

for a in range(1, 9):
    check(f"lambda_{a} is Hermitian", lam[a].conjugate().T == lam[a])
    check(f"lambda_{a} is traceless", lam[a].trace() == sp.Integer(0))

# Normalisation: Tr(lambda_a lambda_b) = 2 delta_ab
for a in range(1, 9):
    for b in range(a, 9):
        tr_val = sp.simplify((lam[a]*lam[b]).trace())
        expected = sp.Integer(2) if a == b else sp.Integer(0)
        check(f"Tr(lam_{a} lam_{b}) = {expected}", sp.simplify(tr_val - expected) == sp.Integer(0))

# ============================================================
# 4. su(3) structure constants from commutators
# ============================================================
print("\n[4] su(3) structure constants — all 28 commutator pairs")

T = [lam[a] / 2 for a in range(1, 9)]  # T_a = lambda_a / 2

# Standard f_abc table (nonzero values, up to antisymmetry)
# f_123=1, f_147=1/2, f_156=-1/2, f_246=1/2, f_257=1/2,
# f_345=1/2, f_367=-1/2, f_458=sqrt(3)/2, f_678=sqrt(3)/2
f_values = {}
f_raw = [
    (1,2,3,  sp.Integer(1)),
    (1,4,7,  sp.Rational(1,2)),
    (1,5,6, -sp.Rational(1,2)),
    (2,4,6,  sp.Rational(1,2)),
    (2,5,7,  sp.Rational(1,2)),
    (3,4,5,  sp.Rational(1,2)),
    (3,6,7, -sp.Rational(1,2)),
    (4,5,8,  sqrt(3)/2),
    (6,7,8,  sqrt(3)/2),
]
for (a,b,c,val) in f_raw:
    for (ia,ib,ic,sign) in [
        (a,b,c,1),(b,c,a,1),(c,a,b,1),
        (b,a,c,-1),(c,b,a,-1),(a,c,b,-1)
    ]:
        f_values[(ia,ib,ic)] = sign * val

def f_abc(a, b, c):
    return f_values.get((a,b,c), sp.Integer(0))

all_commutators_ok = True
for a in range(1, 9):
    for b in range(a+1, 9):
        comm = T[a-1]*T[b-1] - T[b-1]*T[a-1]
        expected = zeros(3)
        for c in range(1, 9):
            expected += Im * f_abc(a, b, c) * T[c-1]
        diff = sp.simplify(comm - expected)
        ok = diff == zeros(3)
        if not ok:
            print(f"    FAIL comm T_{a},T_{b}: diff = {diff}")
            all_commutators_ok = False

check("All 28 su(3) commutator pairs verified", all_commutators_ok)

# ============================================================
# 5-6. Fermionic Fock space: 8x8 matrices, CAR
# ============================================================
print("\n[5-6] Fermionic Fock space: creation/annihilation operators, CAR")

# Jordan-Wigner construction: 3 modes on 2^3=8-dimensional space.
# Basis: |n1 n2 n3> with n_i in {0,1}; n1 is the LEFTMOST (most significant) bit.
# So index = 4*n1 + 2*n2 + n3.
#
# Convention:  |0> = [1,0]^T  means "0 particles",
#              |1> = [0,1]^T  means "1 particle".
# Creation operator raises: c^dag |0> = |1>, so c^dag uses sm_ = [[0,0],[1,0]].
# Annihilation uses sp_ = [[0,1],[0,0]].
#
# c_1^dag = sm_ ⊗ I ⊗ I          (mode 1, leftmost; no JW string needed)
# c_2^dag = sz  ⊗ sm_ ⊗ I        (mode 2, JW string over mode 1)
# c_3^dag = sz  ⊗ sz  ⊗ sm_      (mode 3, JW string over modes 1,2)

sz  = Matrix([[1, 0], [0, -1]])
sp_ = Matrix([[0, 1], [0,  0]])   # lowers: sp_|1> = |0>
sm_ = Matrix([[0, 0], [1,  0]])   # raises: sm_|0> = |1>
I2  = eye(2)

def tensor3(A, B, C):
    return sp.kronecker_product(A, sp.kronecker_product(B, C))

c_dag = [
    tensor3(sm_, I2, I2),
    tensor3(sz, sm_, I2),
    tensor3(sz, sz, sm_),
]
c_ann = [m.H for m in c_dag]  # c_i = (c_i^dag)^†

# Verify CAR
car_ok = True
for i in range(3):
    for j in range(3):
        # {c_i, c_j^dag} = delta_ij
        anticomm = c_ann[i]*c_dag[j] + c_dag[j]*c_ann[i]
        expected_anticomm = eye(8) if i == j else zeros(8)
        ok = anticomm == expected_anticomm
        if not ok:
            print(f"    FAIL {{c_{i+1}, c_{j+1}^dag}} != {'I' if i==j else '0'}")
            car_ok = False
        # {c_i, c_j} = 0
        anticomm2 = c_ann[i]*c_ann[j] + c_ann[j]*c_ann[i]
        ok2 = anticomm2 == zeros(8)
        if not ok2:
            print(f"    FAIL {{c_{i+1}, c_{j+1}}} != 0")
            car_ok = False
        # {c_i^dag, c_j^dag} = 0
        anticomm3 = c_dag[i]*c_dag[j] + c_dag[j]*c_dag[i]
        ok3 = anticomm3 == zeros(8)
        if not ok3:
            print(f"    FAIL {{c_{i+1}^dag, c_{j+1}^dag}} != 0")
            car_ok = False

check("All CAR relations verified exactly", car_ok)

# ============================================================
# 7-8. Second-quantised T_hat_a and their commutators
# ============================================================
print("\n[7-8] Second-quantised T_hat_a and commutator algebra")

def make_T_hat(T_fund):
    """dGamma(T_fund) = sum_{i,j} c_i^dag (T_fund)_ij c_j  (8x8 matrix)"""
    result = zeros(8)
    for i in range(3):
        for j in range(3):
            result += T_fund[i, j] * c_dag[i] * c_ann[j]
    return result

T_hat = [make_T_hat(T[a]) for a in range(8)]

all_T_hat_comm_ok = True
for a in range(8):
    for b in range(a+1, 8):
        comm_hat = T_hat[a]*T_hat[b] - T_hat[b]*T_hat[a]
        expected_hat = zeros(8)
        for c in range(8):
            expected_hat += Im * f_abc(a+1, b+1, c+1) * T_hat[c]
        diff = sp.simplify(comm_hat - expected_hat)
        ok = diff == zeros(8)
        if not ok:
            print(f"    FAIL [T_hat_{a+1}, T_hat_{b+1}]: diff nonzero")
            all_T_hat_comm_ok = False

check("All 28 T_hat commutators verified (dGamma homomorphism)", all_T_hat_comm_ok)

# ============================================================
# 9. Number operator commutes with all T_hat_a
# ============================================================
print("\n[9] Number operator N commutes with all T_hat_a")

N_op = zeros(8)
for i in range(3):
    N_op += c_dag[i]*c_ann[i]
num_comm_ok = True
for a in range(8):
    comm = N_op * T_hat[a] - T_hat[a] * N_op
    ok = comm == zeros(8)
    if not ok:
        print(f"    FAIL [N, T_hat_{a+1}] != 0")
        num_comm_ok = False
check("Number operator commutes with all T_hat_a", num_comm_ok)

# ============================================================
# 10-13. Particle-number blocks and representation content
# ============================================================
print("\n[10-13] Particle-number block structure and representation content")

# The 8 basis states |n1 n2 n3> have index = 4*n1 + 2*n2 + n3.
# Number eigenvalue = number of 1-bits.
n_eigenvalues = [bin(k).count('1') for k in range(8)]

# Block indices by particle number (sorted)
blocks = {n: [k for k in range(8) if n_eigenvalues[k] == n] for n in range(4)}
check("dim(Lambda^0 V) = 1", len(blocks[0]) == 1)
check("dim(Lambda^1 V) = 3", len(blocks[1]) == 3)
check("dim(Lambda^2 V) = 3", len(blocks[2]) == 3)
check("dim(Lambda^3 V) = 1", len(blocks[3]) == 1)

def extract_block(M, idx):
    """Submatrix of M with rows and cols in idx."""
    return Matrix([[M[i,j] for j in idx] for i in idx])

# Vacuum and full sectors: T_hat_a should vanish there
vac_singlet_ok = True
full_singlet_ok = True
for a in range(8):
    blk0 = extract_block(T_hat[a], blocks[0])
    blk3 = extract_block(T_hat[a], blocks[3])
    if blk0 != zeros(1):
        vac_singlet_ok = False
    if blk3 != zeros(1):
        full_singlet_ok = False
check("Vacuum sector (Lambda^0) is singlet under all T_hat_a", vac_singlet_ok)
check("Full sector (Lambda^3) is singlet under all T_hat_a", full_singlet_ok)

# One-particle block in MODE ORDER.
# With sm_ as creation: c_i^dag|vac> creates state index:
#   mode 1 -> |100> = 4,  mode 2 -> |010> = 2,  mode 3 -> |001> = 1
# Using this ordering, the block equals T[a] exactly (no JW signs in 1-particle sector).
one_p_mode_idx = [4, 2, 1]  # modes 1, 2, 3

one_particle_block_ok = True
for a in range(8):
    blk1 = extract_block(T_hat[a], one_p_mode_idx)
    diff = sp.simplify(blk1 - T[a])
    if diff != zeros(3):
        print(f"    FAIL: one-particle block (mode order) != T_{a+1}: {diff}")
        one_particle_block_ok = False
check("One-particle block (Lambda^1, mode order) = fundamental T_a", one_particle_block_ok)

# Two-particle block in MODE-PAIR ORDER.
# mode-pair (1,2)->|110>=6, (1,3)->|101>=5, (2,3)->|011>=3
two_p_mode_idx = [6, 5, 3]  # mode-pairs (1,2),(1,3),(2,3)

# Two-particle commutator algebra check
two_particle_comm_ok = True
for a in range(8):
    for b in range(a+1, 8):
        blk2_a = extract_block(T_hat[a], two_p_mode_idx)
        blk2_b = extract_block(T_hat[b], two_p_mode_idx)
        comm_blk = blk2_a * blk2_b - blk2_b * blk2_a
        exp_blk = zeros(3)
        for c in range(8):
            exp_blk += Im * f_abc(a+1,b+1,c+1) * extract_block(T_hat[c], two_p_mode_idx)
        diff = sp.simplify(comm_blk - exp_blk)
        if diff != zeros(3):
            print(f"    FAIL two-particle block comm [{a+1},{b+1}]")
            two_particle_comm_ok = False
check("Two-particle block (Lambda^2) satisfies su(3) commutation relations", two_particle_comm_ok)

# The Lambda^2 representation of T_a in mode-pair basis [(1,2),(1,3),(2,3)]:
#   T_a(e_i ^ e_j) = (T_a e_i)^e_j + e_i^(T_a e_j)
# gives the matrix (with 1-indexed modes T_{ij}):
#   [[T11+T22,   T23,  -T13],
#    [T32,   T11+T33,   T12],
#    [-T31,     T21,  T22+T33]]
# The minus signs arise from re-ordering e_k^e_l when k>l (antisymmetry).
# This is the anti-fundamental (3-bar) representation of su(3).

def expected_lambda2(Ta):
    T11, T12, T13 = Ta[0,0], Ta[0,1], Ta[0,2]
    T21, T22, T23 = Ta[1,0], Ta[1,1], Ta[1,2]
    T31, T32, T33 = Ta[2,0], Ta[2,1], Ta[2,2]
    return Matrix([
        [T11+T22,  T23,  -T13],
        [T32,  T11+T33,   T12],
        [-T31,     T21,  T22+T33],
    ])

antifund_ok = True
for a in range(8):
    blk2 = extract_block(T_hat[a], two_p_mode_idx)
    exp = expected_lambda2(T[a])
    diff = sp.simplify(blk2 - exp)
    if diff != zeros(3):
        print(f"    FAIL: two-particle block != Lambda^2 formula for T_{a+1}: {diff}")
        antifund_ok = False
check("Two-particle block (Lambda^2) = anti-fundamental Lambda^2 formula", antifund_ok)


# ============================================================
# Summary
# ============================================================
print(f"\n{'='*60}")
print(f"TOTAL: {PASS_COUNT} PASS, {FAIL_COUNT} FAIL")
print(f"{'='*60}")

if FAIL_COUNT > 0:
    sys.exit(1)
else:
    print("\nAll checks PASSED. Algebraic claims verified exactly.")
    sys.exit(0)
