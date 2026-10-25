# Bianchi identities do not dynamically select torsion

**Exact geometry-only counterexample; 2026-10-25. NOT a verified canonical DTheta solution or fundamental Hamiltonian/action.** Continues merged #757 and #742.

Given a tetrad \(e^a\) and metric-compatible spin connection \(\omega^a{}_b\), Cartan's structure equations are \(T^a=de^a+\omega^a{}_b\wedge e^b\), \(R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b\). Differentiating yields the first and second Bianchi identities \(DT^a=R^a{}_b\wedge e^b\), \(DR^a{}_b=0\). These are *identities*, not equations of motion.

An explicit continuous family with **nonzero Lorentz connection and nonzero torsion**: on \(\mathbb R^{1,3}\), set \(e^a=dx^a\), let \(\omega^0{}_1=\omega^1{}_0=k\,dx^2\) with constant arbitrary real \(k\), all other connection components zero. This is a boost-valued, metric-compatible \(\mathfrak{so}(1,3)\) connection because \(\omega_{01}=-\omega_{10}\). Then
\[
T^0=k\,dx^2\wedge dx^1,\quad T^1=k\,dx^2\wedge dx^0,\quad T^2=T^3=0,\quad R^a{}_b=0.
\]
Hence \(DT^a=0=R^a{}_b\wedge e^b\) and \(DR=0\) for every k, including k≠0. Curvature of the Lorentz connection and Levi-Civita Riemann both vanish, yet the **specified spin connection has torsion**.

This is **not** an assertion of gauge-equivalence among different k at fixed e, and not an explicit single-Theta curved solution. In UBT the composite connection and locked \(E=D\Theta/\sqrt{N_0}\) may constrain permissible k; whether they do is precisely the open implicit reconstruction/dynamics problem. The example rules out the *proposal that Bianchi identities alone select a unique torsion*. Flatness of the Lorentz connection is not required by UBT and was selected here only to demonstrate the ambiguity cleanly; this does not recommend a flat UBT connection.

The next constructive requirement is a closed formula or variational equation selecting \(T[\Theta]\), compatible with the composite fixed-point problem and a **derived**, not inserted, unique kinetic principle. Only then can one calculate an actual reduced \(H_{\rm UBT}\), its constraints, and the fundamental action.
