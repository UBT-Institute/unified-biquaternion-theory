# Inverzní UBT: rekonstrukce metriky z kauzální konformní struktury a objemové hustoty

## Rozsah výsledku

Jde o podmíněnou matematickou rekonstrukci, nikoli o důkaz gravitační dynamiky nebo informačního původu časoprostoru. Lorentzova konformní třída spolu s nezávisle určenou kladnou kovariantní objemovou hustotou jednoznačně určuje úplnou metriku v dané třídě.

## Rekonstrukce metriky

Předpokládejme hladkého Lorentzova konformního reprezentanta \(\widehat g_{\mu\nu}\), kladnou kovariantní objemovou hustotu \(\nu\) a kladný faktor \(\Omega\). V dimenzi 4:

\[
g_{\mu\nu}=\Omega^2\widehat g_{\mu\nu}.
\]

\[
\sqrt{|\det g|}=\Omega^4\sqrt{|\det\widehat g|}.
\]

Zadaná fyzikální hustota tedy vybírá:

\[
\Omega=\left(\frac{\nu}{\sqrt{|\det\widehat g|}}\right)^{1/4}.
\]

\[
g_{\mu\nu}=\left(\frac{\nu}{\sqrt{|\det\widehat g|}}\right)^{1/2}\widehat g_{\mu\nu}.
\]

Výsledek nezávisí na volbě konformního reprezentanta: změna \(\widehat g\) se kompenzuje opačnou změnou rekonstruovaného \(\Omega\). Objemová hustota se při změně souřadnic musí transformovat jako hustota, nikoliv jako obyčejný skalár. Kladný faktor je jednoznačný.

## Hranice formálního důkazu

Přiložený soubor Lean formalizuje skalární ekvivalenci nulové podmínky, čtvrtou mocninu objemového faktoru a jednoznačnost nezáporných faktorů při pevném nenulovém referenčním objemu. **Neformalizuje** úplnou diferenciální geometrii obecných Lorentzových metrik ani jejich pohybové rovnice. Modul sestavuje GitHub Actions; rozhodující je skutečný výsledek CI.

Doprovodné testy Python/SymPy kontrolují determinant a vzorec při změně konformního reprezentanta na příkladu ploché Lorentzovy metriky. Neprokazují fyzikální ztotožnění objemu s informací.

## Fyzikální informační hypotéza

Přístupnost informace ani kvantové provázání samy nezaručují kladnou, na regularizaci nezávislou, souřadnicově kovariantní objemovou hustotu. Počítání informačních buněk navíc potřebuje fundamentální rozměrovou kalibraci a spojitý limit. Mikroskopické měřítko nelze získat z bezrozměrného bikvaternionového násobení.

Lorentzova konformní třída je v tomto lemmatu stále předpokladem. Skutečná inverzní rekonstrukce musí kauzální uspořádání a hustotu odvodit ze společné informační dynamiky, nikoliv nenápadně převzít metriku.

## Důkazové podmínky gravitace

Stále musíme odvodit operacionální lokální pozorovatelné a kauzalitu, kovariantní míru a měřítko, kompozitní tetrádu splňující hodnostní omezení UBT, kompatibilní vazbu na hmotu a stabilní dynamiku metriky, konexe a torze. Plošný zákon entropie horizontu a Newtonova vazba vyžadují nezávislé odvození.

Tyto výsledky neodvozují Einsteinovy rovnice ani nevybírají \(\mathbb C\otimes\mathbb H\) jednoznačně proti obecné komplexní maticové kvantové teorii.

## Odkazy a stav

Navazujeme na [konformní neurčitost Cliffordovy struktury](CLIFFORD_CONFORMAL_CONE_SCALE_OBSTRUCTION_2026_11_10.md). Termodynamickým srovnáním je [lokální odvození z horizontů](LOCAL_HORIZON_INFORMATION_EINSTEIN_CLOSURE_2026_11_10.md).

**Podmíněně dokázáno:** jednoznačnost měřítka metriky z kladné objemové hustoty. **OPEN:** fyzikální hustota, emergentní Lorentzův časoprostor, úplná dynamika UBT a gravitace.
