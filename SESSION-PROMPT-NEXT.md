# Session-Prompt für Session 17 — Goldoni Retail Extension

> Handoff von Session 16 (2026-04-14) an Session 17.

## Kurzstand

**20 Docs v2. 15/17 Inconsistencies aufgelöst. Drei Backlog-Items in Session 16 durch** (Q4Me, Geschenkebox, Sensitivity). Das Projekt hat inhaltlich mehr Substanz als je, der nächste Meilenstein bleibt **Germans Gespräch mit Silvio**.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-14-goldoni.md` — Session-16-Report mit allen drei Blöcken.
2. `docs/plans/22-q4me-evaluation.md`, `docs/plans/54-geschenkebox-konzept.md`, `docs/plans/52-sensitivity-analyse.md` — die drei neuen Pläne.
3. `docs/silvio-paket/offene-fragen.md` — SP-20 präzisiert, SP-25 + SP-26 neu, SP-05 erweitert.
4. `session-state.md` — Stand nach Session 16.

## Was in Session 17 ansteht

### Priorität 1 — Silvio-Rückmeldungen verarbeiten

Falls Silvio auf offene Fragen geantwortet hat:

| SP | Thema | Was dann |
|---|---|---|
| SP-09 | Vollständige Anschrift | Etikett-Pflichtfeld #8 in Doc 06 befüllen |
| SP-19 | Rezeptur (ohne Béchamel, Gramm) | QUID + Allergene in Doc 04/06 befüllen |
| SP-20 | Geschenkebox — OK?, Rummo-Sorte, EK, Premium, Launch | Doc 19/07/08 anpassen, Launch-Plan konkretisieren |
| SP-22 | Metro-/Lieferanten-Preise | [E]-Marker in Doc 02/07/11 durch echte Preise ersetzen |
| SP-23 | Nachfrage-Schätzung | Sensitivity-Baseline aktualisieren, Slides anpassen |
| SP-24 | Kartenpreise | Preisanker in Doc 07 validieren |
| SP-25 | DEHOGA-BW-Mitgliedschaft | Q4Me-Preis in Doc 22 und Cashflow anpassen |
| SP-26 | Produkthaftpflicht Handelsware | Versicherungs-Status für Geschenkebox-Launch klären |

### Priorität 2 — Propagation der Session-16-Ergebnisse in die Haupt-Docs

Kleine Folge-Arbeiten, die in Session 16 bewusst nicht durchgeschleift wurden:

| # | Item | Effort |
|---|---|---|
| 1 | Doc 07 v2: Geschenkebox-Zeile auf 19,90/22,90 € aktualisieren, DB-Aussage "marginal negativ" streichen | XS |
| 2 | Doc 02 v2: "Was kippt?"-Abschnitt um Cross-Ref zur neuen Sensitivity-Analyse ergänzen | XS |
| 3 | Doc 19 v2: Geschenkebox-Tabelle präzisieren (19,90/22,90 €, Rummo-Format noch offen) | XS |
| 4 | Doc 08 v2: Kraft-Kartonbox-Position präzisieren (1,20 € + Füllung 0,60 € = 1,80 €) | XS |
| 5 | Inconsistency #17 (Öffnungszeiten): falls Silvio antwortet → korrigieren | XS |
| 6 | SP-05 Hand-Out `sp-05-briefing-steuerberater.md` um USt-Geschenkebox-Frage ergänzen | S |

### Priorität 3 — PPTX-Stand klären

Vor Session 16 stand `docs/silvio-derivatives/goldoni-retail-ueberblick.pptx` als Modified im git status — bewusst nicht angefasst. Beim Session-17-Start: German klärt, was geändert wurde, dann Commit oder Revert.

### Priorität 4 — Slides verfeinern (falls Zeit)

- YAML-Texte prüfen und Formulierungen schärfen
- Ggf. italienische Version (`slides-content-it.yaml`)
- Ggf. Geschenkebox-Slide ergänzen (neu in Session 16)

## Offene Blocker

Warten auf Silvio: SP-09, SP-19, SP-20, SP-22, SP-23, SP-24, SP-25, SP-26, Inconsistency #17.

## Wichtige Präferenzen

- **Commit + Push zusammen** — keine Lücke
- **AskUserQuestion bei 2+ Optionen Pflicht (Rule 11)**
- **Eine Frage nach der anderen (Rule 12)**
- **Pushback erwartet — nicht blind ausführen**
- **Silvio ist kein Reviewer — Silvio-Paket als Artefakt (Rule 10)**
- **Keine Hard-Wraps in Markdown-Fließtexten**
- **Leitsatz der Session statt Easter Eggs**
