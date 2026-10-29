<!-- BILINGUAL-UNIT: observer-info-hamiltonian -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Informace pozorovatele, kauzalita a Hamiltonián: pracovní odvození

<!-- BILINGUAL-UNIT: scope -->
## Rozsah a vztah ke kanonické UBT

Tato výzkumná poznámka zaznamenává diskusi o informaci pozorovatele, sdílené realitě a Hamiltoniánu z 27. října 2026. Je **nekanonická**. Uzamčená architektura UBT zachovává jediné fundamentální pole $\Theta(q,\tau)\in\mathbb C\otimes\mathbb H$, komplexní čas $\tau=t+i\psi$, tetrádu $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$ a centrální antikomutátorovou metriku. Níže používané pomocné qubity, Hilbertovy prostory detektorů, reálná komponentní pole a Minkowského pozadí jsou **efektivní testovací modely**, nikoli náhrady či další fundamentální pole UBT.

**Stav:** pracovní odvození a explicitní protipříklady; žádný jednoznačný fundamentální Hamiltonián ani akce UBT nebyly odvozeny.

<!-- BILINGUAL-UNIT: capacity -->
## Kapacita pozorovatele a sdílená realita

Pro fyzikálně přípustný protokol $\pi\in\Pi_O$ definujeme $\mathcal I_O(X)=\sup_\pi I(X;Y_\pi)$. Množinu $\Pi_O$ omezují přípravy stavů, povolená měření, paměť, energie, čas a kauzální dostupnost. Jestliže $\Pi_1\subseteq\Pi_2$, pak $\mathcal I_1\le\mathcal I_2$; samotná složitost bez přístupu k měření nemusí zvýšit dostupnou informaci. Operacionální ekvivalence stavů je $\rho\sim_O\sigma$ právě tehdy, když $\mathrm{Tr}[(\rho-\sigma)A]=0$ pro všechny dostupné observably $A$. U dvou pozorovatelů rozlišujeme **individuálně sdílené** observably (průnik) a **kolektivně rekonstruovatelnou** informaci (společná měření a komunikace). Požadavek konzistence sdílené reality je navržen, **nikoli odvozen** jako axiom vybírající dynamiku.

<!-- BILINGUAL-UNIT: fisher -->
## Fisherova geometrie: explicitní příklad

Pro $\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2$ dává měření $\sigma_z$ s $z=r_z$ pravděpodobnosti $p_\pm=(1\pm z)/2$ a $F(z)=1/(1-z^2)$. Při symetrické citlivosti $\eta\in[0,1]$ platí $q_\pm=(1\pm\eta z)/2$ a $F_\eta(z)=\eta^2/(1-\eta^2z^2)$. Jde o operacionální statistickou metriku, **nikoli** fyzikální metriku prostoročasu. Substituce $z=\cos\vartheta$ vede v ideálním případě na $ds_F^2=d\vartheta^2$. Funkcionál $S_{\rm info}=\frac\kappa2\int\dot\vartheta^2dt$ je **zvolená** kinetická/geodetická akce, nikoli důsledek samotné Fisherovy geometrie.

<!-- BILINGUAL-UNIT: identifiability -->
## Dynamická identifikovatelnost Hamiltoniánu

Pro $H=h_0I+\mathbf h\cdot\boldsymbol\sigma$ a $i\hbar\dot\rho=[H,\rho]$ platí $\dot{\mathbf r}=(2/\hbar)\mathbf h\times\mathbf r$. Definujeme $H_1\sim_{\mathcal O}H_2$, pokud se shodují výsledky všech přípustných příprav, středních hodnot měření a časů pozorování. Pokud lze připravit **každou** počáteční hustotní matici a měření jsou ideální, rovnost ve všech časech implikuje $[H_1-H_2,A]=0$ pro každou dostupnou observablu $A$ (obecně nutná, ne postačující podmínka). Skalární komutant $\mathcal O'=\mathbb CI$ postačuje k identifikaci $H$ až na $\lambda I$. Pro jedinou observablu $\sigma_z$ určují časové derivace příčné složky $h_x,h_y$ a obecně také $h_z$, pokud $(h_x,h_y)\ne(0,0)$; jsou-li obě nulové, je $h_z$ neviditelné. Při přístupu k $\sigma_x$ a $\sigma_z$ je jejich společný komutant skalární. **Žádný pozorovatelský princip zatím nevybírá číselné hodnoty vazeb.**

<!-- BILINGUAL-UNIT: slits -->
## Dvojštěrbinový detektor: podmíněně odvozené výsledky

Předpokládejme měření dráhy bez jejího přepínání a dvouhladinový detektor. Obecná interakce zachovávající dráhu je $H_{\rm int}=|L\rangle\langle L|\otimes V_L+|R\rangle\langle R|\otimes V_R=I\otimes V_++\sigma_z\otimes V_-$. **Volba** $V_-=(\hbar g/2)\sigma_y$ (nikoli její jednoznačné odvození) dává $H_{\rm int}=(\hbar g/2)\sigma_z^{(S)}\otimes\sigma_y^{(O)}$. Pro počáteční $(|L\rangle+|R\rangle)|0\rangle/\sqrt2$ je překryv podmíněných stavů detektoru $\cos(gT)$, viditelnost interference částice $\mathcal V=|\cos(gT)|$ a optimální rozlišitelnost dráhy se stejnými apriorními pravděpodobnostmi $\mathcal D=|\sin(gT)|$, takže v tomto ideálním čistém modelu $\mathcal V^2+\mathcal D^2=1$. Nerozlišitelnost či rozlišitelnost stavů detektoru, nikoli vědomé čtení, rozhoduje o potlačení nepodmíněné interference. Větší kapacita následného zpracování při nezměněné interakci tuto viditelnost nemění.

<!-- BILINGUAL-UNIT: causality -->
## Symetrie, geometrie a konečná rychlost světla

Hermitovská bikvaternionová reprezentace $X=ct+i\sum_kx^k\mathbf e_k$ splňuje $X\bar X=c^2t^2-|\mathbf x|^2$ při kvaternionové konjugaci; reprezentuje plochou Lorentzovu geometrii, ale **neodvozuje** geometrii prostoročasu ani $c$ z UBT. Lokální relativistický efektivní model skalárního multipletu s osmi reálnými poli $q_A$ lze **zvolit** jako $\mathcal L=K\dot q_A\dot q_A/(2c^2)-K(\nabla q_A)^2/2-V(q)$, kde $V=M^2q_Aq_A/2+\lambda(q_Aq_A)^2/4$. Potom $\pi_A=K\dot q_A/c^2$ a $\mathcal H=c^2\pi_A\pi_A/(2K)+K(\nabla q_A)^2/2+V$. Rovnice je $c^{-2}\ddot q_A-\nabla^2q_A+K^{-1}\partial_AV=0$. Jde o podmíněný **efektivní skalární multiplet** na pevném Minkowského pozadí, nikoli kanonickou akci UBT. Lorentzova invariance omezuje hlavní část šíření; úplný kvantový důkaz kauzality vyžaduje lokalitu a mikrokauzalitu. Detektor navázaný lokálně podél světočáry, např. $g_O\chi(\tau)m_O(\tau)\Phi(z_O(\tau))$, je vhodnější než okamžité vzdálené vazby. Vazba detektoru i $c$ jsou zde nadále vnější vstupy.

<!-- BILINGUAL-UNIT: algebra -->
## Bikvaternionově specifická interakce a nevyřešený výběr

Při $\mathbf e_k\leftrightarrow-i\sigma_k$ lze zvolenou dvouqubitovou interakci vyjádřit jako $\mathbb H_{\rm int}=-(\hbar g/2)\mathbf e_3^{(S)}\otimes\mathbf e_2^{(O)}$ v $\mathbb B\otimes_{\mathbb C}\mathbb B$. Samotný izomorfismus $\mathbb B\cong M_2(\mathbb C)$ **nedává odlišnou předpověď**. Pro ryzí kvaternionové vektory platí $[\mathbf a,\mathbf b]=2\mathbf a\times\mathbf b$ a $\{\mathbf a,\mathbf b\}=-2\mathbf a\cdot\mathbf b$; kvadrát komutátoru zvýhodňuje komutující (rovnoběžné) konfigurace, nikoli ortogonalitu, zatímco kvadrát antikomutátoru může zvýhodňovat ortogonalitu. Takové další vazby jsou průzkumné, mohou narušit postulovanou vnitřní symetrii $U(4)$ a bez explicitního architektonického posouzení nesmějí zavádět další fundamentální pole. Jejich koeficienty jsou neurčené.

<!-- BILINGUAL-UNIT: gaps -->
## Mezery, falzifikace a plán ověření

1. **Kanonický most:** odvodit lokální observablu dostupnou pozorovateli a vazbu detektoru z uzamčeného $\Theta$, oboustranné derivace $D_\mu$, tetrády a antikomutátorové metriky; nenahrazovat je.
2. **Audit symetrií:** vyjmenovat povolené členy ze skutečných transformačních zákonů UBT, nikoli z předpokládané $U(4)$.
3. **Kauzalita:** odvodit charakteristické kužely z kanonické emergentní metriky a ověřit mikrokauzalitu/nepřenos signálu s prostorově rozloženou vazbou detektoru.
4. **Informační výběr:** podat nekruhový extremální princip, který vyloučí konkurenční Hamiltoniány nebo omezí vazbu; zůstává protipříklad $H=0$ proti $H=\omega\sigma_z$ při měření pouze dráhy.
5. **Testy:** ověřit komutátory qubitu a viditelnost numericky/CAS; testovat variaci akce, pozitivitu a identifikovatelnost parametrů; porovnat s dvojštěrbinovými experimenty a kvantovým mazáním.
6. **Brány důkazů/překladu:** **LEAN-PENDING** (Lean nezkompilován), **CAS-PENDING**, **BILINGUAL-SEMANTICS-PENDING**. Nemergovat ani nepovyšovat tvrzení bez vyžadovaných kontrol; shoda dvojjazyčného obsahu a nezávislá významová revize zůstávají povinné.
