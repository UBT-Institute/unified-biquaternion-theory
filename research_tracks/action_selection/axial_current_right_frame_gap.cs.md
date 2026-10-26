# Axiální proud závisí na volbě pravého sloupcového rámce

**Přesná algebraická kontrola, 25. 10. 2026; nikoli odvození Hamiltoniánu.** Navazuje na #746.

Pro Theta=[xi,chi] a převod F(Theta)=(xi,epsilon chi*) má časová složka axiálního Diracova proudu ve Weylově bázi tvar
\[
j_5^0=\|\chi\|^2-\|\xi\|^2
=-\operatorname{Tr}(\Theta^\dagger\Theta\sigma_3)
\]
při gamma^5=diag(-I,+I). Tento výraz není invariantní vůči libovolnému pravému promíchání sloupců Theta→Theta U, U∈SU(2). Např. Theta=[(1,0)^T,0] dává j5^0=-1; po U=epsilon se sloupce prohodí (a jeden může změnit znaménko), takže j5^0=+1, zatímco norma Tr(Theta†Theta)=1 zůstává stejná.

**Fyzikální omezení tvrzení:** zatím není dokázáno, že celé pravé SU(2) je skutečná gauge symetrie úplné UBT s kanonickým reálným Lorentzovým tetrádovým řezem. Výsledek tedy **nevyvrací** všechny axiální proudy. Ukazuje však, že právě proud z převodu F není nezávislý na volbě pravého rámce. Chceme-li z něj odvozovat torzi, musíme rámec či chirální projektory odvodit, ne je jen vybrat.

Následuje výpočet skutečné přípustné pravé symetrie po dosazení kompozitní konexe, fyzikální symplektiky a tetrádových vazeb.
