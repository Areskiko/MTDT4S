Et sett med [[Transaksjon]]er som kan være sammenflettet. [[Operasjon]]ene til hver transaksjon må forekomme i samme rekkefølge som i [[Transaksjon]]ene, men kan flettes med [[Operasjon]]ene fra de andre [[Transaksjon]]ene.

## Recoverability
// TODO fix title


### Recoverable
Dersom $T_i$ leser fra et objekt som $T_j$ har skrevet til,  så må $c_j<c_i$

### Avoid cascading aborts
Dersom $T_i$ leser fra objekt $x$ som er skrevet av $T_j$, så må $c_j<r_i[x]$

### Strict
Dersom $T_i$ leser fra eller overskriver et objekt skrevet av $T_j$, så må $c_j<r_i[x]/w_i[x]$ eller $a_j<r_i[x]/w_i[x]$
