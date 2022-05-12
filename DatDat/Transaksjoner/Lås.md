Låser gjør det slik at kun de [[Transaksjon]]ene med en lås til et [[databaseobjekt]] kan interagere med den. Om en transaksjon $T_i$ har en lås på $x$, og $T_j$ ønsker å oppdatere $x$, må $T_j$ vente på at $T_i$ har gjort seg ferdig, og slipper låsen.

## Binære låser
Binære låser gir eksklusiv tillgang til [[databaseobjekt]]er hvor kun en transaksjon har tillgang på [[databaseobjekt]]et.

Binære låser annsees som for strenge for database-sammenhenger, og brukes derfor i praksis ikke.

## Shared/Exclusive Låser
Det er mulig å tilldele låser basert på om en [[Transaksjon]]er ønsker å lese eller å skrive til [[databaseobjekt]]et
### Shared
Det er ikke noe i veien for at flere [[Transaksjon]]er skal kunne [[Operasjon#Read | lese]] fra det samme [[databaseobjekt]]et.

En kan derfor gi ut delete låser til alle som ønsker å [[Operasjon#Read | lese]] et [[databaseobjekt]]. Hensikten med denne typen lås er å stoppe [[Transaksjon]]er fra å få en [[Lås#Exclusive | eksklusiv]] lås på [[databaseobjekt]]et.

### Exclusive
Når en [[Transaksjon]] ønsker å [[Operasjon#Write | skrive]] til et [[databaseobjekt]] er det viktig at ingen andre prøver å [[Operasjon | lese]] eller [[Operasjon#Write | skrive]] til det samme [[databaseobjekt]]et.

Vi gir derfor ut en eksklusiv lås, som vil si at ingen andre kan få noen slags lås sammtidig. Dette sikrer at andre [[Transaksjon]]er venter på at den med eksklusiv lås har gjort seg ferdig før de gjør noe.