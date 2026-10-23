# Oprava interpretace spinu: levé kvaternionové násobení versus kongruence

**24. 10. 2026, podmíněný reprezentační rozbor C-tier.** Zamčené axiomy UBT se nemění. Zpřesňuje příliš širokou interpretaci draftu #720.

Pro U∈SU(2)=Spin(3) a X∈Mat(2,C) rozlišujme dvě různá působení:

* **Spinorové zleva** L_U(X)=UX: při otočení o 2π je U=-I₂, tedy X→-X. Dva sloupce X tvoří dvě kopie spinové reprezentace 1/2.
* **Kongruence/adjungované působení** C_U(X)=UXU†: při 2π vyjde X→X. Pod rotacemi jde o reprezentaci 0⊕1.

**Samotná bikvaternionová algebra tedy spin 1/2 dovoluje.** Závěr draftu #720 vylučuje přímé propletení s Diracovou reprezentací **jen při požadavku, aby se celé pole Theta transformovalo kongruencí**. Není to obecný zákaz spinorů v UBT.

Přesto samotná levá SU(2) reprezentace nedokazuje úplnou Lorentzovu spinorovou transformaci včetně dvou chiralit, hmotového členu, fyzikální energie ani Hamiltoniánu. Je nutno respektovat kanonickou tetrádu E_mu=D_mu Theta/sqrt(N0) a metriku definovanou centrálním antikomutátorem na W_L: levé násobení E_mu bez další transformace konexe nemusí zachovat tuto geometrickou větev. Spinorová reprezentace fundamentálního pole a vektorová reprezentace odvozené geometrie mohou být různé; jejich kompatibilitu musíme teprve odvodit.

**Další ostrá brána:** odvodit správné působení Spin(1,3) na Theta, propojit jej s dvěma chiralitami, symplektickou strukturou, kovariantní derivací a tetrádou, potom teprve vybírat Diracův Hamiltonián. Neprohlašovat ani levou, ani kongruenční reprezentaci automaticky za finální.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_left_spin_rep.py' -v\`.
