## Atomisk
Enten så gjennomføres [[Transaksjon]]en fullstendig, eller ikke i det heletatt. Om den ikke kan gjennomføres vil alt som har skjedd hitil i [[Transaksjon]]en bli rullet tilbake.

## Konsistens preservasjon
Dersom en transaksjon blir gjennomført skal den mappe en konsistent database state til en annen konsistent database state.

## Isolasjon
Transaksjoner skal ikke måtte forrholde seg til at de kjører sammtidig som andre transaksjoner.

## Permanenthet
Endringer begått av en en [[Commit]]et transaksjon må være permanente, og ikke mistes på grunn av feil.