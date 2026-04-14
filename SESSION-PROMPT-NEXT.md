# Session-Prompt für Session 18 — Goldoni Retail Extension

> Handoff von Session 17 (2026-04-14) an Session 18.

## Kurzstand

20 Docs v2. 15/17 Inconsistencies aufgelöst. Session 17 hat die Propagation der Session-16-Ergebnisse (Geschenkebox + Sensitivity) in Doc 02/07/08/19/SP-05 abgeschlossen. Haupt-Docs sind jetzt konsistent mit den neuen Plänen (`plans/22-q4me-evaluation.md`, `plans/52-sensitivity-analyse.md`, `plans/54-geschenkebox-konzept.md`).

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-14-goldoni-b.md` — Session-17-Report.
2. `docs/reports/2026-04-14-goldoni.md` — Session-16-Report (die drei Pläne).
3. `docs/silvio-paket/offene-fragen.md` — offene SP-Einträge.
4. `session-state.md` — Stand nach Session 17.

## Was in Session 18 ansteht

### Priorität 1 — Silvio-Rückmeldungen verarbeiten

Falls Silvio auf offene Fragen geantwortet hat — unverändert aus Session 16:

| SP | Thema | Was dann |
|---|---|---|
| SP-09 | Vollständige Anschrift | Etikett-Pflichtfeld #8 in Doc 06 befüllen |
| SP-19 | Rezeptur (ohne Béchamel, Gramm) | QUID + Allergene in Doc 04/06 befüllen |
| SP-20 | Geschenkebox — OK?, Rummo-Sorte, EK, Premium, Launch | Doc 19/07/08 finalisieren, Launch-Plan konkretisieren |
| SP-22 | Metro-/Lieferanten-Preise | [E]-Marker in Doc 02/07/11 durch echte Preise ersetzen |
| SP-23 | Nachfrage-Schätzung | Sensitivity-Baseline aktualisieren, Slides anpassen |
| SP-24 | Kartenpreise | Preisanker in Doc 07 validieren |
| SP-25 | DEHOGA-BW-Mitgliedschaft | Q4Me-Preis in Doc 22 und Cashflow anpassen |
| SP-26 | Produkthaftpflicht Handelsware | Versicherungs-Status für Geschenkebox-Launch klären |

### Priorität 2 — PPTX-Stand klären

`docs/silvio-derivatives/goldoni-retail-ueberblick.pptx` steht seit vor Session 16 als modified im git status (48k → 54k). Session 16 und 17 haben es bewusst nicht angefasst. In Session 18: German klärt, was geändert wurde, dann Commit oder Revert.

### Priorität 3 — Slides verfeinern (falls Zeit)

- YAML-Texte prüfen und Formulierungen schärfen
- Geschenkebox-Slide ergänzen (neu aus Session 16/17, Preise 19,90/22,90 € jetzt final in Doc 07/19)
- Ggf. italienische Version (`slides-content-it.yaml`) für Silvio-Präsentation

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
- **Zahlen-Pushback ernst nehmen** (neu aus Session 17): bei abgeleiteten Zahlen immer die Quell-Aufschlüsselung neben sich haben, nicht aus dem Gedächtnis aggregieren
