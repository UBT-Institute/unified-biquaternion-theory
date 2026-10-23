# Lorentzovy boosty jako test spinorové reprezentace UBT

**Podmíněný reprezentační výsledek C-tier, 24. 10. 2026.** Zpřesňuje #721 a #720. Zamčené axiomy ani kompozitní definice metriky neměníme.

Levé násobení X→UX při prostorových rotacích U∈SU(2) dává dvě spinové reprezentace 1/2 a správné znaménko při 2π. Jenže pro obecný S∈SL(2,C) působení X→SX představuje dvě kopie **levé Weylovy chirality** (1/2,0). Diracův spinor se skládá z levé a pravé chirality (1/2,0)⊕(0,1/2); liší se při Lorentzových boostech.

Každé lineární propletení, které respektuje všechny SU(2) rotace, má na 2×2 blocích tvar násobků identity (Schurovo lemma). Při boostu S(u)=exp(uσ₃/2) pro u≠0 vyžaduje převod levého bloku na pravý aS=aS⁻¹, takže a=0. **Neexistuje invertibilní Lorentzovo propletení** mezi uniformním levým násobením a běžným Diracovým spinorem. Samotný test rotace 2π tedy nestačí.

Lze ale konstruovat testovací reprezentaci na stále stejných čtyřech komplexních komponentách Theta:
\[
\mathcal D_S(X)=SXP_L+(S^\dagger)^{-1}XP_R,\quad
P_L=\operatorname{diag}(1,0),\ P_R=\operatorname{diag}(0,1).
\]
První sloupec pak nese levou a druhý pravou Weylovu chiralitu. Při rotaci U se oba transformují jako UX a při 2π dostávají minus; při boostu se chovají opačně. Kompoziční zákon grupy platí.

**Velké omezení:** pravé projektory a výběr sloupců dosud nebyly odvozeny z uzamčených axiomů. Testovací spinorové působení navíc není automaticky kompatibilní s reálnou tetrádovou větví E_mu∈W_L, kterou používáme k definici metriky. Musíme odvodit kovariantní mapu mezi spinorovou reprezentací Theta a vektorovou reprezentací tetrády, ne ji prohlásit za samozřejmou.

**Další krok směrem k Hamiltoniánu:** odvodit chiralitu z bikvaternionové nebo komplexně-časové struktury, symplektickou formu a rovnice kovariance; pak prověřit Diracovu faktorizaci, fyzikální energii a vazby. Bez nového postulovaného Hamiltoniánu.

Kontrola: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chiral_boost_gate.py' -v\`.
