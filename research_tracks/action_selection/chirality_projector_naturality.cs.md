<!-- BILINGUAL-UNIT: chirality_projector_naturality -->
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


# Chirální projektory: překážka přirozenosti v Mat(2,C)

**2026-10-24. Podmíněná algebraická věta, nikoli výběr fundamentálního hamiltoniánu.** Pokračování návrhu #722. Neměnit uzamčené axiomy UBT.

Nechť A=M_2(C) a požadujme *intrinsický operátor chirality pravým násobením* Gamma=R_G, Gamma(X)=XG, pro pevnou komplexní matici G splňující Gamma²=1. Při libovolných změnách pravého rámce X↦XV, V∈SL(2,C), vyžadujme neměnnost chirality: Gamma(XV)=Gamma(X)V. Pak VG=GV pro všechna V, takže G leží v komutantu fundamentální reprezentace SL(2,C). Tento komutant je C·I₂ (Schurovo lemma; alternativně stačí generátory sigma1 a sigma3). Tedy G=zI₂; G²=I₂ implikuje z=+1 nebo -1. Proto P±=(I±G)/2 jsou pouze (I,0) či (0,I): **při neomezené symetrii pravého rámce SL(2,C) neexistuje netriviální intrinsická dvojice pravých projektorů hodnosti jedna**.

Dvojice projektorů z #722, P_L=diag(1,0), P_R=diag(0,1), odpovídá volbě G=diag(-1,+1), která omezuje neomezenou změnu pravého rámce na stabilizátor G (diagonální podgrupu). Jde o platnou **kandidátní dodatečnou strukturu či fixaci kalibrace**, nikoli výstup samotné holé algebry. Věta se konkrétně týká projektorů *pevného pravého násobení* a neomezené přirozenosti pravého rámce. Není-li pravý modul fyzikální symetrií UBT, toto vyloučení neplatí jako fyzikální požadavek; skutečná přípustná pravá kalibrační grupa musí být určena z uzamčených dat kovariantní derivace.

**Jiná možná, dosud nedoložená cesta:** chirální gradace v úplné sudé prostoročasové Cliffordově reprezentaci s objemovým pseudoskalárem nebo gradovaný modul indukovaný ze skutečné kovariantní tetrády a konexe Spin(1,3). Taková gradace musí být definována na správném nosiči, zachovávat reálný Lorentzův metrický řez a být kompatibilní s hamiltoniánem prvního řádu a invariantním symplektickým párováním. Nestačí ztotožnit komutující imaginární jednotku i s gamma5: násobení i splňuje J²=-1 jako *reálný* operátor, nikoli netriviální komplexně lineární involuci, zatímco i·J=-I je triviální.

**Falzifikace a další podmínka:** odvodit skutečnou pravou kalibrační symetrii Theta z kanonické oboustranné D_mu a určit, zda připouští netriviální chirální projektor; teprve potom klasifikovat ekvivariantní lineární hamiltonovské symboly prvního řádu. Nepřidávat stupeň volnosti typu gamma5 ani nezdvojovat pole bez odvození.

Reprodukce: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chirality_projector_naturality.py' -v.
