#!/usr/bin/env python3
"""Exact algebra checks for a UBT candidate on C^4 x C.

These checks validate the identities stated in README.en.md / README.cs.md.
They do not derive an action, solve its constrained dynamics, or establish
physical equivalence to string theory. General proofs are in the report.
Requires SymPy. Run: python verify_c5.py
"""
import json
import platform
from pathlib import Path
import sympy as s

checks = []
details = {}

def zero(name, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    good = all(s.simplify(e) == 0 for e in entries)
    checks.append({'name': name, 'passed': good})
    if not good:
        raise AssertionError((name, expression))

I2, I4 = s.eye(2), s.eye(4)
pauli = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]), s.diag(1,-1)]
sharp = lambda X: s.trace(X)*I2-X
def lift(X):
    return s.zeros(2).row_join(X).col_join(sharp(X).row_join(s.zeros(2)))
e = [s.I*I2]+[-s.I*p for p in pauli]
gamma = [lift(x) for x in e]+[s.diag(1,1,-1,-1)]
eta = s.diag(-1,1,1,1,1)
for a in range(5):
    for b in range(a,5):
        zero(f'Clifford5_{a}_{b}', gamma[a]*gamma[b]+gamma[b]*gamma[a]-2*eta[a,b]*I4)

xi = s.symbols('xi0:5')
symbol = sum((xi[i]*gamma[i] for i in range(5)),s.zeros(4))
qform = (s.Matrix(xi).T*eta*s.Matrix(xi))[0]
zero('five_channel_symbol_square', symbol*symbol-qform*I4)
zero('five_channel_symbol_determinant', symbol.det()-qform**2)

# Every complex 4x4 matrix anticommuting with all five gammas is zero.
unknown = s.symbols('x0:16')
X = s.Matrix(4,4,unknown)
constraints = [v for g in gamma for v in g*X+X*g]
coeffs, rhs = s.linear_eq_to_matrix(constraints,unknown)
zero('no_sixth_4x4_gamma_rank', coeffs.rank()-16)
details['sixth_gamma_linear_system'] = {'rows':coeffs.rows,'columns':coeffs.cols,'rank':coeffs.rank()}

# A representative of the general rank theorem g=J eta J^T, J of size 5x4.
v = s.symbols('v0:4')
lam = s.symbols('lambda', nonzero=True)
J = I4.col_join(s.Matrix([v]))
eta4 = s.diag(-1,1,1,1)
g5 = J*eta4*J.T
null = s.Matrix([-x for x in v]+[1])
zero('canonical_5x5_metric_is_degenerate',g5.det())
zero('explicit_metric_null_vector',g5*null)
u=s.Matrix([0,0,0,0,lam])
completed=g5+u*u.T
zero('rank_one_completion_determinant',completed.det()+lam**2)
lifted = [sum((J[a,b]*gamma[b] for b in range(4)),s.zeros(4))+u[a]*gamma[4] for a in range(5)]
for a in range(5):
    for b in range(a,5):
        zero(f'completed_metric_Clifford_{a}_{b}',lifted[a]*lifted[b]+lifted[b]*lifted[a]-2*completed[a,b]*I4)
details['completion_determinant'] = str(s.factor(completed.det()))

# Metric realification and the standard complex structure.
Z=s.zeros(5); Id=s.eye(5)
Jc=Z.row_join(-Id).col_join(Id.row_join(Z))
real_holomorphic=eta.row_join(Z).col_join(Z.row_join(-eta))
real_hermitian=eta.row_join(Z).col_join(Z.row_join(eta))
zero('holomorphic_real_metric_anti_isometry',Jc.T*real_holomorphic*Jc+real_holomorphic)
zero('hermitian_real_metric_isometry',Jc.T*real_hermitian*Jc-real_hermitian)
details['real_signatures_negative_positive']={
 'real_part_complex_symmetric':[5,5], 'real_part_hermitian_1_4':[2,8]}

# Fixed-background, ordinary-derivative FRW ansatz: cross terms survive.
t,x,y,z=s.symbols('t x y z',real=True)
a=s.Function('a')(t); f=s.Function('f')(t)
coords=[t,x,y,z]
old_embedding=s.Matrix([f,a*x,a*y,a*z])
old_metric=old_embedding.jacobian(coords).T*eta4*old_embedding.jacobian(coords)
zero('old_FRW_g00',old_metric[0,0]+s.diff(f,t)**2-s.diff(a,t)**2*(x*x+y*y+z*z))
zero('old_FRW_g0x',old_metric[0,1]-a*s.diff(a,t)*x)
zero('old_FRW_spatial_block',old_metric[1:4,1:4]-a*a*s.eye(3))
details['ordinary_derivative_FRW_g00']=str(old_metric[0,0])
details['ordinary_derivative_FRW_g0x']=str(old_metric[0,1])

# Constructive local embedding of k=0 FLRW in a flat 5D ambient geometry.
F=s.Function('F')(t)
Y=s.Matrix([a,a*(x*x+y*y+z*z)+F,a*x,a*y,a*z])
ambient=s.zeros(5);ambient[0,1]=ambient[1,0]=-s.Rational(1,2)
for j in range(2,5):ambient[j,j]=1
pullback=Y.jacobian(coords).T*ambient*Y.jacobian(coords)
pullback=pullback.applyfunc(s.simplify).subs(s.diff(F,t),1/s.diff(a,t))
zero('FLRW_embedding_all_components',pullback-s.diag(-1,a*a,a*a,a*a))
details['FLRW_embedding_assumptions']=['a(t)>0','a_dot(t)!=0 locally','F_dot=1/a_dot','kinematics only']

# Independent Christoffel/Ricci calculation for the 10D product ansatz.
b=s.Function('b')(t)
diag=[-s.Integer(1)]+[a*a]*3+[b*b]*6
N=len(diag)
def d(mu,expr):return s.diff(expr,t) if mu==0 else s.Integer(0)
conn={}
for r in range(N):
    for m in range(N):
        for n in range(N):
            val=(d(m,diag[r]) if r==n else 0)+(d(n,diag[r]) if r==m else 0)-(d(r,diag[m]) if m==n else 0)
            if val!=0:conn[r,m,n]=s.simplify(val/(2*diag[r]))
def C(r,m,n):return conn.get((r,m,n),s.Integer(0))
ric=[]
for m in range(N):
    expr=sum(d(r,C(r,m,m))-d(m,C(r,m,r)) for r in range(N))
    expr+=sum(C(r,m,m)*C(k,r,k)-C(k,m,r)*C(r,m,k) for r in range(N) for k in range(N))
    ric.append(s.simplify(expr))
scalar=s.simplify(sum(ric[m]/diag[m] for m in range(N)))
ein=[s.simplify(ric[m]-scalar*diag[m]/2) for m in range(N)]
H,S,Hd,Sd=s.symbols('H S Hdot Sdot',real=True)
replacement={s.diff(a,t,2):a*(Hd+H*H),s.diff(b,t,2):b*(Sd+S*S),s.diff(a,t):a*H,s.diff(b,t):b*S}
E0=s.expand(ein[0].subs(replacement))
E3=s.expand((ein[1]/a**2).subs(replacement))
E6=s.expand((ein[4]/b**2).subs(replacement))
zero('Einstein10_00',E0-(3*H*H+18*H*S+15*S*S))
zero('Einstein10_external',E3-(-2*Hd-3*H*H-6*Sd-21*S*S-12*H*S))
zero('Einstein10_internal',E6-(-3*Hd-6*H*H-5*Sd-15*S*S-15*H*S))
zero('static_internal_pressure_constraint',(E0-3*E3+2*E6).subs({S:0,Sd:0}))
# This combination equals kappa*(rho-3p+2p_internal) when Einstein equations hold.
details['Einstein10_flat_3_plus_6']={'G00':str(E0),'Gii_over_ai_squared':str(E3),'Gmm_over_b_squared':str(E6)}
details['static_internal_equation_of_state']={'radiation_pI_over_rho':'0','dust_pI_over_rho':'-1/2','four_dimensional_vacuum_pI_over_rho':'-2'}

# Analytic continuation of a unitary group: exact finite-dimensional witness.
K=s.diag(-2,0,3)
monodromy=s.diag(s.Rational(1,4),1,8)  # exp(log(2)*K)
zero('periodic_imaginary_time_only_zero_eigenmode',len((monodromy-s.eye(3)).nullspace())-1)
zero('periodic_mode_is_kernel_of_generator',K*(monodromy-s.eye(3)).nullspace()[0])

# Closed-string zero-mode momentum/winding terms are additional structure.
n,w,R,ap=s.symbols('n w R alpha_prime',nonzero=True)
pL=n/R+w*R/ap; pR=n/R-w*R/ap
zero('string_winding_quadratic_energy',(pL*pL+pR*pR)/2-(n*n/R**2+w*w*R**2/ap**2))
zero('string_T_duality_quadratic_energy',(n*n/R**2+w*w*R**2/ap**2).subs({R:ap/R,n:w,w:n},simultaneous=True)-(n*n/R**2+w*w*R**2/ap**2))
zero('RNS_central_charge_count',s.Rational(3,2)*10-26+11)

result={
 'scope':'Exact encoded identities; no complete UBT dynamics or string equivalence claim.',
 'date':'2026-10-08','python':platform.python_version(),'sympy':s.__version__,
 'lean_status':'LEAN-PENDING: lean and lake executables were unavailable in this runtime; generic claims have not been formalized.',
 'passed':all(c['passed'] for c in checks),'checks_count':len(checks),'checks':checks,'details':details}
path=Path(__file__).with_name('c5_verification_results.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':result['passed'],'checks_count':len(checks),'details':details},ensure_ascii=False,indent=2))
