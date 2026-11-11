# Bikvaternionová Jordanova metrika a informační objemová podmínka

## Matematický rozsah

Existující kanonická UBT metrika z prvních kovariantních derivací používá tetrádu na reálné Lorentzově větvi. Rozlišujeme zde úplnou komplexní centrální Jordanovu identitu a *fyzikálně reálnou* metriku. Konjugace sharp obrací tři kvaternionové jednotky, ale nikoliv komutující komplexní koeficienty. Pro obecné komplexní z a w je symetrizovaný součin centrální, jeho koeficient však může být komplexní.

Na reálné Lorentzově větvi je časový koeficient imaginární v komutující komplexní jednotce a prostorové koeficienty reálné. Vzniká bilineární forma s Lorentzovou signaturou. Identita determinantů platí pro každou invertibilní reálnou tetrádu.

## Rovnice a nové omezení pevného objemu


\[
\frac{X^\sharp Y+Y^\sharp X}{2}=\left(\sum_{a=0}^3z_aw_a\right)\mathbf1.
\]

\[
\eta(X,Y)=-tu+\sum_{k=1}^3x^ky^k.
\]

\[
g=e\eta e^{\mathsf T},\quad \eta=\operatorname{diag}(-1,1,1,1).
\]

\[
\det g=-(\det e)^2,\quad\sqrt{|\det g|}=|\det e|.
\]

\[
|\det e|=\nu_{\mathrm{info}}.
\]

\[
\delta|\det e|=|\det e|\operatorname{tr}(e^{-1}\delta e)=0.
\]


Podmínka informačního objemu představuje *nové kandidátní fyzikální omezení* jen tehdy, pokud je nu_info odvozena nezávisle na tetrádě a transformuje se jako kovariantní hustota. Definovat ji pomocí determinantu tetrády by bylo kruhové.

Pevně nezávisle zadaná hustota omezí přípustné tetrádové variace ze 16 na 15 dimenzí. Neomezený diferenciál tetráda–metrika má hodnost 10 a Lorentzovo jádro dimenze 6. Při pevném objemu má hodnost 9 a Lorentzovo jádro zůstává dimenze 6. Odstraní stopovou variaci, nikoliv všechny fyzikální variace metriky. Pokud je nu_info dynamická, omezení neplyne.

## Vztah k fyzice a formálnímu důkazu

Jde pouze o algebraickou a kinematickou konstrukci, nikoliv nový gravitační zákon. Variace s pevným objemem připomínají unimodulární přístupy, ale neodvozují Einsteinovu dynamiku. Kanonická akce je stále DEFINED_FAMILY_NOT_FINALIZED a platí existující omezené no-go výsledky pro pomocnou konexi a kompozitní akci. Nové omezení nesmíme bez odvození přidávat do fundamentální akce. Výběr reálné větve, integrabilita konexe, původ nu_info, Hessian, Newtonovo G a horizontová entropie zůstávají OPEN.

Lean soubor formal/BiquaternionJordan.lean dokazuje centrálnost úplné komplexní algebry, symetrii párování a příklad nereálného koeficientu. Neformalizuje celý teorém hodnosti tetrády ani dynamiku. SymPy testuje centrálnost, reálnou Lorentzovu větev, příklad determinantu a hodnost v jednotkové tetrádě.

Kanonický zdroj: canonical/gr_closure/covariant_tetrad_rank_theorem.tex; hranice akce: canonical/ACTION.en.md.
