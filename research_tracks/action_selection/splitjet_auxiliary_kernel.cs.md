# Přesné jádro pomocné split-jet mapy a redundance posunů

**Pracovní strukturální výsledek C-tier, 24. 10. 2026.** Pouze přijatý klasický gravitační sektor Palatini–HT; Hessian úplné mikroskopické UBT a Diracova algebra zůstávají otevřené.

Pro q=sqrt(N0)>0, nenulové časupodobné X a E_mu^a=q^-1(d_mu X^a+omega_mu^a_b X^b+K_J,mu^a_b X^b+w_mu X^a) máme pro každý index mu šest Lorentzovsky antisymetrických složek K_J,mu a jednu složku w_mu. V klidovém rámci X=(r,0,0,0), r!=0, zvolme sloupce z=(w,K^1_0,K^2_0,K^3_0,K^2_3,K^3_1,K^1_2). Jacobián je přesně
\[
J=\frac r q\begin{pmatrix}1&0&0&0&0&0&0\\0&1&0&0&0&0&0\\0&0&1&0&0&0&0\\0&0&0&1&0&0&0\end{pmatrix}.
\]
Má rank 4 a jádro dimenze 3. Pro čtyři prostorčasové indexy je bloková mapa rank 16 a nullita 12. Nejde o počet fyzikálních stupňů volnosti tetrády; dalších šest směrů tetráda→metrika tvoří standardní lokální Lorentzovu redundanci.

**Přesné tvrzení mimo hmotovou slupku:** při pevných X a omega posun δK_J s δK_J^a_b X^b=0 a δw=0 nijak nemění E ani přijatou gravitační akci. V časupodobné větvi je stabilizátor so(3), tři komponenty pro každý mu. Protože závislost E na K_J je lineární, symetrií je i konečný posun K_J→K_J+ΔK_J s ΔK_J X=0. Nejde nutně o obvyklou lokální Lorentzovu kalibraci celé UBT: další dynamický člen závislý přímo na K_J či jeho derivacích může redundanci porušit. U nenulového prostorupodobného X je stabilizátor so(1,2) a počet nezávislých směrů zůstává 3.

Z toho **nelze automaticky tvrdit 12 vazeb první třídy**. Je nutné sestavit kanonické proměnné, primární i sekundární vazby, jejich Poissonovy závorky a generátory kalibrace. Nejde ani o důkaz plné stability pole Theta. Výpočet platí při X² !=0 a nezávislých sedmi pomocných komponentách na index mu.

**Další brána:** předsymplektická forma prvního řádu pro (Theta,omega,K_J,w,Lambda,C3), potom analýza primárních/sekundárních vazeb včetně sektorů psi a zdrojů.

Test: \`python -m unittest discover -s research_tracks/action_selection/tests -p 'test_splitjet_kernel.py' -v\` (SymPy).