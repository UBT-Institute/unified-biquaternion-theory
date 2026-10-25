# Rozhodující podmínka stopy torze pro zachování Diracova náboje v UBT

Stav: přesná diferenciálně-geometrická identita při uvedených konvencích, nikoli odvození fundamentálního Hamiltoniánu. Navazuje na #727.

Konvence: \(\nabla_\mu V^\lambda=\partial_\mu V^\lambda+\Gamma^\lambda{}_{\mu\nu}V^\nu\), \(T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}\). Pro metrickou konexi a \(e=\sqrt{|g|}\) platí \(\partial_\mu\log e=\Gamma^\lambda{}_{\mu\lambda}\). Proto
\[
\boxed{\nabla_\mu j^\mu=\frac1e\partial_\mu(ej^\mu)+t_\nu j^\nu,\quad t_\nu=T^\mu{}_{\mu\nu}.}
\]
Z rovnice \(\nabla_\mu j^\mu=0\) tudíž obecně **neplyne** \(\partial_\mu(ej^\mu)=0\). Přesná lokální podmínka na daný proud je \(t_\mu j^\mu=0\), silnější postačující podmínka pro všechny proudy je \(t_\mu=0\). Podmínky musíme teprve vyvodit z dynamiky pole Theta, nikoli tiše předpokládat.

Konkrétní protipříklad: na Minkowského metrice zvolme konstantní kovektor \(v_\mu\ne0\) a metrickou konexi
\[
\Gamma^\lambda{}_{\mu\nu}=\delta^\lambda_\mu v_\nu-\eta_{\mu\nu}v^\lambda.
\]
Její kovariantní derivace metriky je nulová, ale stopa torze je v 4D \(t_\nu=3v_\nu\). Tedy ani metrická kompatibilita nezaručuje zákon zachování objemového proudu. Pro zcela antisymetrickou torzi je stopa nulová, ale takový tvar torze v UBT ještě není odvozen.

Důsledek: než použijeme Diracův proud ke konstrukci fyzikální symplektické formy, musíme z UBT získat správnou rovnici torze či vylepšený zachovávaný proud. Variace kompozitní tetrády a konexe se navíc musí objevit v úplném předsymplektickém proudu. Samotná standardní Diracova identita nestačí.
