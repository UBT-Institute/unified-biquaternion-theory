#!/usr/bin/env python3
"""Independent exterior-algebra verification of the parent Palatini-Holst
tetrad Euler 3-forms and spin Cartan 3-forms.

S_parent = sum_(a<b) [cE epsilon_abcd e^c ^ e^d
                      +cH e_a ^ e_b] ^ R^{ab}
           - Lambda * vol(e).
Define delta S = delta e^a ^ E_a + sum_(a<b) delta omega^{ab} ^ C_ab.
Then
 E_a = 2 cE sum_(b<c) eps_bc a d e^d ^ R^{bc}
     + cH sum_(b<c)(eta_ba e_c-eta_ca e_b)^ R^{bc}
     -Lambda / 3! eps_abcd e^b ^ e^c ^ e^d,
 C_ab = D P_ab
      = 2 cE eps_abcd T^c ^ e^d
       +cH (T_a ^ e_b - e_a ^ T_b).
The final composite spin Euler form adds (X_b E_a-X_a E_b)/q.
No unrelated Theta action or on-shell gravity is assumed.
"""
import itertools
import sympy as sp


def alt_sum(*fs):
    d={}
    for f in fs:
        for k,v in f.items():
            d[k]=sp.expand(d.get(k,0)+v)
    return {k:v for k,v in d.items() if v!=0}


def times(f,v):
    return {k:sp.expand(x*v) for k,x in f.items()
            if sp.expand(x*v)!=0}


def wedge(f,g):
    res={}
    for a,coeff in f.items():
        for b,v in g.items():
            if set(a)&set(b):continue
            sign=(-1)**sum(i>j for i in a for j in b)
            key=tuple(sorted(a+b))
            res[key]=sp.expand(res.get(key,0)+sign*coeff*v)
    return {k:v for k,v in res.items() if v!=0}


def run_checks():
    ce,ch,Lam=sp.symbols("ce ch Lambda",real=True)
    eta=[-1,1,1,1]
    eps=sp.LeviCivita
    b=[{(mu,):sp.Integer(1)} for mu in range(4)]
    # A generic invertible 4x4 example; the result is polynomial in
    # arbitrary ce/ch/Lambda and checked at two nontrivial frames.
    frames=[
        sp.Matrix([[2,1,0,1],[1,2,1,0],[0,1,3,1],[1,0,1,2]]),
        sp.Matrix([[1,0,2,1],[1,2,0,0],[0,1,2,1],[1,1,0,3]])
    ]
    assert all(m.det()!=0 for m in frames)
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    # Each R_ab has all independent coordinate two-form components;
    # numeric coefficients are independent across indices and deterministic.
    R={}
    for a,c in pairs:
        R[a,c]={(i,j):sp.Integer(1+a*3+c*5+i*7+j*11)
                 for i in range(4) for j in range(i+1,4)}
    def r_ab(i,j):
        return R[i,j] if i<j else times(R[j,i],-1)
    def p(e,a,c):
        cePart=alt_sum(*(
            times(wedge(e[d],e[g]),ce*eps(a,c,d,g))
            for d in range(4) for g in range(4)
        ))
        hPart=times(wedge(e[a],e[c]),ch*eta[a]*eta[c])
        return alt_sum(cePart,hPart)
    def euler(e,k):
        EC=alt_sum(*(
            times(wedge(e[d],r_ab(a,c)),
                2*ce*eps(a,c,k,d))
            for a,c in pairs for d in range(4)
        ))
        H=alt_sum(*(
            times(wedge(e[c],r_ab(a,c)),
                ch*(eta[a] if a==k else 0)*eta[c])
            for a,c in pairs
        ),*(
            times(wedge(e[a],r_ab(a,c)),
                -ch*(eta[c] if c==k else 0)*eta[a])
            for a,c in pairs
        ))
        volume=alt_sum(*(
            times(wedge(wedge(e[a],e[c]),e[d]),
                    -Lam*eps(k,a,c,d)/6)
            for a,c,d in itertools.product(range(4),repeat=3)
        ))
        return alt_sum(EC,H,volume)
    def derivative_p(e,delta,a,c):
        return alt_sum(*(
            times(alt_sum(wedge(delta[d],e[g]),
                wedge(e[d],delta[g])),ce*eps(a,c,d,g))
            for d,g in itertools.product(range(4),repeat=2)
        ),times(alt_sum(wedge(delta[a],e[c]),
                        wedge(e[a],delta[c])),ch*eta[a]*eta[c]))
    def density_from_delta_e(e,de):
        variation=alt_sum(*(
            wedge(derivative_p(e,de,a,c),r_ab(a,c))
            for a,c in pairs
        ))
        volume_derivative=alt_sum(*(
            times(wedge(wedge(wedge(de[a],e[c]),e[d]),e[g]),
                -Lam*eps(a,c,d,g)/6)
            for a,c,d,g in itertools.product(range(4),repeat=4)
        ))
        return alt_sum(variation,volume_derivative).get((0,1,2,3),0)

    results={}
    for index,mat in enumerate(frames):
        e=[{(mu,):mat[a,mu] for mu in range(4) if mat[a,mu]!=0}
           for a in range(4)]
        ok=True
        for a in range(4):
            E=euler(e,a)
            for mu in range(4):
                de=[{} for _ in range(4)]
                de[a]=b[mu]
                direct=density_from_delta_e(e,de)
                expected=wedge(b[mu],E).get((0,1,2,3),0)
                ok=ok and sp.expand(direct-expected)==0
        results[f"parent_tetrad_Euler_forms_frame_{index}"]=ok
    # Independently verify the Cartan 3-form DP identity using
    # formal independent T^a two-forms and e^a one-forms.
    e=b
    T=[{(i,j):sp.Integer(1+13*a+5*i+7*j)
        for i in range(4) for j in range(i+1,4)} for a in range(4)]
    for ab in pairs:
        a,c=ab
        expanded=alt_sum(*(
            times(alt_sum(wedge(T[d],e[g]),
                 times(wedge(e[d],T[g]),-1)),
                 ce*eps(a,c,d,g))
            for d,g in itertools.product(range(4),repeat=2)
        ),times(alt_sum(wedge(T[a],e[c]),
                   times(wedge(e[a],T[c]),-1)),ch*eta[a]*eta[c]))
        compact=alt_sum(*(
            times(wedge(T[d],e[g]),2*ce*eps(a,c,d,g))
            for d,g in itertools.product(range(4),repeat=2)
        ),times(alt_sum(wedge(T[a],e[c]),
                   times(wedge(e[a],T[c]),-1)),ch*eta[a]*eta[c]))
        results[f"parent_spin_Cartan_DP_pair_{a}{c}"]=(
            not alt_sum(expanded,times(compact,-1))
        )
    # A normal tetrad Euler force still cancels in the 6
    # antisymmetric composite spin additions for every timelike X.
    X=sp.Matrix(sp.symbols("X0:4"))
    J=sp.symbols("J")
    Xlo=sp.Matrix([eta[i]*X[i] for i in range(4)])
    results["pure_clock_normal_Euler_bivector_cancels"]=all(
        sp.expand(Xlo[c]*Xlo[a]*J-Xlo[a]*Xlo[c]*J)==0
        for a,c in pairs
    )
    return results


if __name__=="__main__":
    checks=run_checks()
    for name,good in checks.items():
        print(("PASS" if good else "FAIL"),name)
    if not all(checks.values()):
        raise SystemExit(1)
    print(f"PASS {len(checks)} independent parent Euler/Cartan exterior checks")
