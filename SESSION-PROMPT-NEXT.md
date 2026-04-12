# Session-Prompt für Session 11 — Goldoni Retail Extension

> Handoff von Session 10 (2026-04-12) an Session 11.

## Kurzstand

Session 10 hat die **gesamte Gate-kritische Sequenz abgeschlossen**: 9 Co-Reviews, 5 v2-Rewrites, 94 von 108 Findings aufgelöst. Drei neue Entscheidungen: D-11 (BAFA-Förderung für Germans Beratung), D-12 (Vorbestellungen ab Phase 1), SP-19-Arbeitsannahme (Lasagne ohne Béchamel, ohne Ei). Fördermittel-Recherche (Doc 21, bis 3.670 € Zuschuss) und Software-Tools-Übersicht (Doc 22, 12 Tools) sind neu. Decision-Log steht bei D-01 bis D-12.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-12-goldoni-c.md` — Session-10-Report mit Block-Chronik, Zahlen, Lessons. **Wichtigste Datei.**
2. `docs/findings/decisions.md` — D-01 bis D-12. Prüfe beim Start, ob eine Entscheidung, die du triffst, gegen einen der Einträge verstößt.
3. `docs/silvio-paket/offene-fragen.md` — 21 Einträge (SP-01 bis SP-21) in 7 Blöcken. SP-19 (Béchamel → Arbeitsannahme "ohne", Bestätigung Silvio ausstehend). SP-14 aufgelöst (D-12). SP-21 (BAFA-Antrag) neu.
4. `docs/plans/21-foerdermittel.md` — Drei Programme (BAFA, BW-Beratungsrichtlinie, L-Bank), German als BAFA-Berater (D-11).
5. `docs/plans/22-software-tools.md` — 12 Tools, Phase 1 inkl. Webshop/Stripe/PayPal (D-12).
6. Die fünf v2-Rewrites: `docs/business-case/03`, `04`, `05`, `14`, `15`. Alle auf aktuellem Stand.
7. `session-state.md` — Stand nach Session 10.

## Was in Session 11 ansteht

### Priorität 1 — SP-19-Antwort verarbeiten

Wenn Silvio auf die WhatsApp-Frage geantwortet hat: Arbeitsannahme bestätigen oder korrigieren. Wenn Béchamel doch drin ist → betroffene Abschnitte in Doc 04 v2 und Doc 05 v2 anpassen (Allergen Ei zurück, Listerien-Risiko-Kategorie hoch, Abkühlzeit-Problem wieder offen).

### Priorität 2 — Sekundär-Reviews starten

14 Docs (01, 02, 06, 07, 08, 09, 10, 11, 12, 13, 16, 17, 18, 19) sind noch unreviewed. Empfohlene Reihenfolge nach Business-Impact:

1. **Doc 02 Wirtschaftlichkeit** (CFO-Lead) — hängt an Netto/Brutto-Deklaration aus Doc 15 v2 und Fixkosten-Allokation
2. **Doc 13 6-Wochen-Rollout-Plan** (CFO-Lead) — integriert die drei Rechts-Stichtage und das Vormittags-Fenster
3. **Doc 06 Mockups** (Brand/Marketing-Lead) — muss gegen Doc 04 v2 Pflichtfelder validiert werden
4. **Doc 09 Verkaufsstrategie** (Brand/Marketing-Lead) — WhatsApp-Kanal, Webshop, Fernabsatz (D-12)

### Priorität 3 — Operatives

- BAFA-Berater-Registrierung vorantreiben (Backlog #55, German hat Seminar besucht)
- Q4Me evaluieren (Backlog #56)
- Webshop-Plattform-Entscheidung (Shopify vs. WooCommerce vs. Ecwid)

## Offene Blocker

| # | Blocker | Wartet auf | Impact |
|---|---|---|---|
| 1 | SP-19 Bestätigung "ohne Béchamel/Ei" | Silvio | Doc 04/05 v2 ggf. Korrektur |
| 2 | SP-10 Primärzutat-Herkunft | Silvio + Lieferanten | Doc 04 v2 Etikett nicht druckfertig |
| 3 | SP-11 Labor-Nährwertanalyse | Silvio + Rezept-Fixierung | Doc 04 v2 Nährwerttabelle offen |
| 4 | MHD-Validierung (Haltbarkeitstest) | Silvio + Labor | Doc 05 — vor erstem Verkauf |

## Wichtige Präferenzen von German

- **Commit + Push zusammen** — keine Lücke (neu Session 10)
- **AskUserQuestion bei 2+ Optionen Pflicht (Rule 11)**
- **Eine Frage nach der anderen (Rule 12)**
- **Pushback erwartet — nicht blind ausführen**
- **Silvio ist im Chance-Modus** — Informations-Asymmetrie respektieren
- **Personas ohne Personennamen bei neuen Personas**
- **Review-Standard-Format** aus CLAUDE.md
- **MASCHIN-Tabellen-Format**
