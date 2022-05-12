Faser:
*	Analyse: Finn vinnere og tapere. Lag [[Lage Dirty Page Table (DPT) | dpt]] og [[Lage transaksjonstabell (TT)|TT]]
*	Redo: Redo alle vinnerne
*	Undo: reversere alle tapertransaksjonene.

(Kan være feil)

## Analyse
Vinnerne er alle transaksjoner som har commited.
Taperne er alle som ikke har commited.

## Redo-fase
Start å gå gjennom fra elste recLSN i [[Lage Dirty Page Table (DPT) | dpt]]. En rad i loggposten må redoes hvis alle følgende er usanne:

* Loggposten er ikke i dpt. Da har den blitt skrevet til disk
* Loggpost lsn er eldre enn recLSN
* Blokkens pageLSN er større eller lik loggpostens LSN. Du må lese blokken for å vite dette

## Undo
Dette er punkter som blir lagt til i loggen mens du holder på. Du går baklengs gjennom loggen og gjør clear (CLR) på alle update verdier til transaksjoner som ikke har commited og en abort når du er ferdig.

#aries #recovery