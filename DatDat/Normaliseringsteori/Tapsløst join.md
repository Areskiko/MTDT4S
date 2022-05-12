Også kjent som ikke-adderende join

Når du dekomponerer vil du bevare Funksjonelle avhengigheter og helst øke normalform, *men* du må passe på at du ikke legger til nye rader når du joiner tabellene.

![[Pasted image 20220512092334.png]]

Regler:
Hvis R dekomponeres inn i andre tabeller R1 og R2

1. $R_1 \cup R_2 = R$

2. $R_1 \cap R_2 = \emptyset$

3. Snittet ovenfor må være kandidatnøkkel for minst en av $R_1 og R_2$




Treningsoppgave:
Du har følgende tabell R og med funksjonelle avhengigheter F
R(A,B,C,D,E,F)
F: {AB->C, C->D, D->EF, F->A, D->B}

Er dekomponeringen D' tapsløs?

D': {ABC, CDE, EF}


Alternativ oppgave:
Hvilke funksjonelle avhengigheter må du legge til for at denne dekomponeringen blir tapsløs?
