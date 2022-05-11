Du leser kun commitede verdier, og skriver kun over verdier som er committed til databasen. Ingen dirty reads eller dirty writes. Dette kan sikres på to måter:

* Låser
* Snapshot isolation. Du har alltid kopi av gamle verdier før de blir comitted