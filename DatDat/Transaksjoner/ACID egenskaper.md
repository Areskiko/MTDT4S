## Atomisk (Atomicity)
Enten så gjennomføres [[Transaksjon]]en fullstendig, eller ikke i det heletatt. Om den ikke kan gjennomføres vil alt som har skjedd hitil i [[Transaksjon]]en bli rullet tilbake.

## Konsistens preservasjon (Consistency)
Dersom en transaksjon blir gjennomført skal den mappe en gyldig databasetilstand til en annen gyldig databasetilstand.

## Isolasjon (Isolation)
Transaksjoner skal ikke måtte forrholde seg til at de kjører sammtidig som andre transaksjoner.

## Permanenthet (Durability)
Endringer begått av en en [[Commit]]et transaksjon må være permanente, og ikke mistes på grunn av feil.