Et sett med [[Transaksjon]]er som kan være sammenflettet. [[Operasjon]]ene til hver transaksjon må forekomme i samme rekkefølge som i [[Transaksjon]]ene, men kan flettes med [[Operasjon]]ene fra de andre [[Transaksjon]]ene.

## Recoverability
// TODO fix title


### Recoverable
Dersom $T_i$ leser fra et objekt som $T_j$ har skrevet til,  så må $c_j<c_i$

### Avoid cascading aborts
Dersom $T_i$ leser fra objekt $x$ som er skrevet av $T_j$, så må $c_j<r_i[x]$

### Strict
Dersom $T_i$ leser fra eller overskriver et objekt skrevet av $T_j$, så må $c_j<r_i[x]/w_i[x]$ eller $a_j<r_i[x]/w_i[x]$


## Serielle transaksjoner
En historie er seriell dersom alle transaksjonene foregår etterhverande i sin helhet. Altså vil $T_i$ fullføres før $T_j$ begynner.

### Serialiserbar
En historie er serialiserbar dersom resultatet av den er [[Historie#Konflikt ekvivalent]] med en seriell historie med de samme [[Transaksjon]]ene

## Ekvivalens
### Konflikt ekvivalent
To historier annses å være konfliktekvivalente dersom den relative rekkefølgen av to [[Conflikt]]ige operasjoner er den samme for alle operasjoner i begge historiene.


Nettside som sier om en historie er recoverable, ACA osv + contflict-serializable + L + ratio+ B+tre: 
[https://fereidani.com/tools/scheduleparser](https://fereidani.com/tools/scheduleparser "https://fereidani.com/tools/scheduleparser")