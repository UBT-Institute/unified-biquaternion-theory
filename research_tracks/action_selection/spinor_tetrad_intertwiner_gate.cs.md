<!-- BILINGUAL-UNIT: spinor_tetrad_intertwiner_gate -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Překážka reprezentačního proplétání: spinorové Theta a Lorentzova tetráda

**Přesný podmíněný reprezentační výsledek (2026-10-25), nikoli vyloučení všech implementací UBT či odvození hamiltoniánu.** Navazuje na sloučené #748 a návrh #749. Nezaměňovat spinorové působení na Theta s Lorentzovou kongruencí na E.

Předpokládejme, že fundamentální bikvaternion se transformuje jako **čistý levý spinor** Theta' = S Theta pro S ze SL2(C) a D je kovariantní derivace v *této* reprezentaci: D'_\mu Theta'=S D_\mu Theta. Uzamčená tetráda je E_\mu=N0^(-1/2)D_\mu Theta. Proto E'_\mu= S E_\mu. Musí-li se **také** transformovat Lorentzovou kongruencí E'_\mu=S E_\mu S†, pak pro každou invertibilní složku tetrády E_\mu platí E_\mu(S†-I)=0, tedy S=I. Taková invertibilní složka existuje pro nedegenerovanou kanonickou tetrádu W_L (každá složka nenulové normy je invertibilní; všechny čtyři souřadnicové nohy tetrády nedegenerované metriky totiž nemohou být současně nulové normy). Oba transformační zákony tedy za těchto předpokladů nemohou obecně koexistovat.

Jemnost: čisté levé násobení **zachovává** centrální metriku sharp, protože (SE)sharp(SF)=Esharp Ssharp S F=Esharp F při det S=1, s sharp=adjungovaná matice. SE však typicky neleží v **pevném** reálném Lorentzově řezu W_L=i Herm2. Příklad E=i I a S=diag(e^r,e^-r), r reálné nenulové, dává iS, které je antihermitovské (S hermitovské); tedy iS je pro čistý hermitovský boost S skutečně antihermitovské. Použijme rotaci SU2 S=[[cos θ,sin θ],[-sin θ,cos θ]], θ různé od 0 a pi: iS není antihermitovské, což dokazuje nezachování. Zachování centrální metriky je tedy slabší než přípustnost pevné reálné tetrádové kalibrace.

Zejména naivní řetězec „spinorové levé Theta + homogenní kovariantní derivace + kanonické E=DTheta + Lorentzovsky kongruenční E“ nemůže sám současně generovat standardní spinorovou hmotu a reálnou tetrádovou geometrii. Únikové cesty vyžadující **odvození místo postulování** zahrnují: (1) intrinsické nelineární spinorově vektorové připájení či proplétání zahrnující Theta a jeho složený adjungovaný rámec; (2) kovariantně transportovaný reálný Lorentzův řez místo pevného W_L spolu s důkazem kompatibility s uzamčeným axiomem C; (3) reprezentaci na Theta s pravým faktorem a nezávislý emergentní spinorový nosič prokázaný jako přirozený. Žádná dosud není doložena jako jednoznačná; volné vložení nového dynamického spinoru či nezávislé konexe by porušilo pravidlo jediného pole.

Přesný příklad SU2 a kontrola metriky sharp v tests/test_spinor_tetrad_intertwiner_gate.py. Žádné úpravy uzamčených axiomů.
