<!-- BILINGUAL-UNIT: mm-finite-lift-quotient -->
<!-- UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Podmíněný lokální důkaz konečné kalibrační ekvivalence, ne úplná redukce UBT.
UBT-AI-PROVENANCE-END -->
# Konečná kalibrační ekvivalence split-jet nosiče: přesný lokální kvocient

**26. 10. 2026.** Navazuje na již existující `splitjet_auxiliary_kernel.en.md` (hodnost 16, pomocná nulita 12) a `split_jet_palatii_variational_lift.en.md` (surjektivní pravá inverze). Tyto starší výsledky nejsou novým odvozením.

Pro konstantní N0>0, fyzikální konexi omega a X²!=0 definujme E=(D_omega X+Q)/sqrt(N0), Q=K_J X+wX. Výměna nosiče za libovolné hladké X' s X'²!=0 je kompenzována
  Q'=Q+D_omega(X-X').
Tím E zůstává **přesně stejné i při konečné transformaci**. Na nové větvi najdeme přímo pomocná pole:
  w'=(X'·Q')/(X'²),
  Y'=Q'-w'X',
  K'_{J,ab}=(Y'_a X'_b-X'_a Y'_b)/(X'²).
Pak K'_J X'=Y' a Q'=K'_J X'+w'X'. Můžeme ještě přičíst libovolnou Lorentzovu matici, která anihiluje X'; jde o známé tři pomocné nulové směry na každý prostorčasový index.

Dvě konečné změny X->X'->X'' se skládají do X->X'' nezávisle na mezikroku. To popisuje celý lokální prostor redundantních parametrizací při pevných (E,omega), dokud se nedostaneme na singulární větev X²=0 nebo k nevhodným okrajovým podmínkám.

Na Palatiniho řešeních, při splnění linearizovaných rovnic a při pevném předpisu okrajových členů, je presymplektický proud složené akce pullbackem Palatiniho proudu, takže čisté vertikální posuny δE=δomega=0 jsou nulové. Lokální surjektivita variací také umožňuje zvednout přípustné Palatiniho variace. To poskytuje **lokální kvocient gravitační konfigurační a presymplektické struktury**, nikoli úplný důkaz globální kvantizace či úplné UBT.

**P0:** V gravitační split-jet reprezentaci jsou proměnné X redundantní. Zbývá dokázat, že připojené komplexní Theta a psi sektory tuto redundanci nerozbijí a nenesou negativní fyzikální módy.

Ověření: `tests/test_mm_finite_splitjet_lift.py`.
