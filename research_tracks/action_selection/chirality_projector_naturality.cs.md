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

# Chirální projektory: překážka přirozenosti v M₂(C)

**24. 10. 2026. Podmíněná algebraická věta; ještě neodvozujeme fundamentální Hamiltonián.** Navazuje na draft #722. Zamčené axiomy neměníme.

Požadujme chirální operátor na bikvaternionu jako pravé násobení Gamma(X)=XG, G²=I₂. Pokud nesmí záviset na libovolné volbě pravé báze X→XV pro V∈SL(2,C), musí platit Gamma(XV)=Gamma(X)V. Odtud VG=GV pro každé V. Komutant fundamentální reprezentace SL(2,C) tvoří pouze komplexní násobky identity (Schurovo lemma). Tedy G=zI₂ a z²=1, takže G=±I₂.

**Při takto požadované plné pravé symetrii neexistují netriviální projektory P_L,P_R odvozené jako konstantní pravé násobení ze samotné algebry.**

Projektory P_L=diag(1,0), P_R=diag(0,1) z #722 tedy odpovídají výběru pravé báze G=diag(-1,1). Buď potřebujeme tento výběr odvodit dynamicky či geometricky, nebo prokázat, že není skutečnou fyzikální pravou kalibrační symetrií celé UBT. Tvrzení je **podmíněné**: obecná pravá SL(2,C) symetrie zatím není automaticky kanonickým požadavkem UBT.

Jiná možnost je odvozený chirální grading ze správné reprezentace Cliffordovy algebry časoprostoru a kompozitní tetrády. Nestačí ztotožnit centrální komplexní i s gamma5: na reálném prostoru má J²=-1; komplexní operátor iJ=-I je triviální.

**Další úkol:** zjistit přesnou dovolenou pravou symetrii ze stávající dvoustranné kovariantní derivace, a teprve potom klasifikovat Hamiltonovské symboly respektující reprezentaci. Bez nového pole a bez svévolného doplnění projektorů.

Test: python -m unittest discover -s research_tracks/action_selection/tests -p 'test_chirality_projector_naturality.py' -v.
