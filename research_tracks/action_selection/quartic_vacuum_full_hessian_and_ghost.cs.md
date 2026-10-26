<!-- BILINGUAL-UNIT: quartic_vacuum_full_hessian_and_ghost -->
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


# Stacionární kvartické vakuum a příčná nestabilita se zápornou kinetikou

**2026-10-26 — přesné ověření Hessovy matice, podmíněná minimálně vázaná větev Theta s nezávislou metrikou.** Model není dokončenou hlavní akcí UBT.

V souřadnicích X=z0 I+sum_{j=1}^3 zj i sigma_j, se z_j=x_j+i y_j a H=2(|z0|²-sum_j |zj|²), det X=sum_{j=0}^3 zj², uvažujme V=V0+m² H+lambda1 H²+lambda2 |det X|². V X0=i r I, r reálné !=0, vymizí gradient v osmi reálných složkách právě tehdy, když m²+(4lambda1+lambda2)r²=0. To připouští r²=-m²/(4lambda1+lambda2)>0 pro m²<0 a 4lambda1+lambda2>0.

Při q=(x0,x1,x2,x3,y0,y1,y2,y3) je Hessova matice po vynucení stacionarity přesně diag(0,0,0,0, 8r²(4lambda1+lambda2),8lambda2 r²,8lambda2 r²,8lambda2 r²). Pro lambda1>=0,lambda2>0 je tedy pozitivně semidefinitní (nikoli pozitivně definitní), se čtyřmi plochými směry souvisejícími s orbitou. V tomto stacionárním vakuu V(X0)=V0-(4lambda1+lambda2)r^4. Minkowského pozadí vyžaduje další rovnici kompatibility kosmologické konstanty a vakuové energie; v nejjednodušší ploché normalizaci s nezávislou metrikou a nulovou kosmologickou konstantou je třeba V0=(4lambda1+lambda2)r^4. Jde o ladění parametrů, nikoli předpověď či odvození z UBT.

Pro dříve přijaté kinetické párování s maticí v reálných souřadnicích G=diag(2,-2,-2,-2,2,-2,-2,-2) jsou tři směry y_j v X0 nekalibrační v kongruenční reprezentaci a mají zobecněný kvadrát hmotnosti (G^{-1} V'')_y_j=-4lambda2 r². Pro lambda2>0 proto mají kinetickou kvadratickou formu nesprávného znaménka A exponenciální infračervené módy v linearizovaných rovnicích na pevném pozadí. Linearizované Einsteinovy hybnostní a hamiltonovské vazby mají v konstantním stacionárním vakuu nulový hmotový zdroj prvního řádu, takže v obvyklém regulárním poruchovém uspořádání tyto módy neodstraňují. Jde o podmíněný test, nikoli úplnou vázanou nelineární větu ADM.

Radiální směr y0 má zobecněné mass²=4(4lambda1+lambda2)r²>0. Čtyři směry s nulovou Hessovou maticí zahrnují tři směry boostové orbity a jeden směr fázové orbity, ale samotná nulová vlastní hodnota neudává počet fyzikálních částic.

Pro lambda2=0 dané tři příčné zobecněné hmotnosti vymizí; záporná kinetická setrvačnost zůstává, takže odstranění tachyonu automaticky neodstraňuje ducha. Pro lambda2<0 má Hessova matice potenciálu stacionárního vakua záporné příčné křivosti a nesplňuje stejné kritérium lokálního minima. O jiných vakuích ani jiných kinetických či složených modelech se nic netvrdí.

Ověřeno pomocí tools/verify_theta_quartic_vacuum_hessian.py a tests/test_theta_quartic_vacuum_hessian.py. Jde o falzifikační výsledek pro explicitně testovanou minimální větev, nikoli celou UBT.
