# Session-Prompt für Session 14 — Goldoni Retail Extension

> Handoff von Session 13 (2026-04-13) an Session 14.

## Kurzstand

Session 13 hat **alle 20 Docs lead-reviewt (100 %)**, 14 Tier-1-Co-Reviews geschrieben und 6 v2-Rewrites fertiggestellt. Gesamt: 308 Findings, 45 Reviews, 13 v2-Rewrites. **7 Docs sind noch v1** und brauchen v2-Rewrites.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-13-goldoni-b.md` — Session-13-Report. **Wichtigste Datei.**
2. `docs/findings/decisions.md` — D-01 bis D-13.
3. `docs/silvio-paket/offene-fragen.md` — 24 Einträge (SP-01 bis SP-24).
4. `session-state.md` — Stand nach Session 13.

## Was in Session 14 ansteht

### Priorität 1 — v2-Rewrites der 7 verbleibenden Docs

Reihenfolge nach Abhängigkeit:

1. **Doc 13 — Rollout** (Neustrukturierung auf 10–12 Wochen, CFO-Stopp aus Session 12 adressieren, Personal-Meilenstein, Stichtag-Markierungen, Gantt-Diagramm)
2. **Doc 09 — Verkaufsstrategie** (Wolt/Uber als Phase-1-Kanal, Webshop Phase 1, Launch-Story, DSGVO-WhatsApp, Kellner-Skript konkret, Abo → Phase 2)
3. **Doc 07 — Preisgestaltung** (Propagation Doc 02 v2, Claudia-Findings: Sugo 6,90 → 7,90 €, Portions-Angabe, Plattform-Preis max. +2 € über Restaurant)
4. **Doc 11 — Lieferanten** (Zutaten-Steckbrief-Tabelle, Backup-Lieferant, Preise teilweise SP-22-abhängig, Pietro-Findings: Büffelmozzarella-Haltbarkeit, Basilikum)
5. **Doc 17 — Wettbewerb** (Plattform-Scan Wolt/Uber Stuttgart, Substitut-Analyse, "Di Gennaro" klären)
6. **Doc 01 — Übersicht** (Dach-Dokument, reine Propagation aus allen anderen v2s — als Letztes)
7. **Doc 06 — Mockups** (LMIV-Compliance-Checkliste gegen Doc 04 v2, braucht visuelle Etikett-Entwürfe — ggf. eigene Session)

### Priorität 2 — Silvio-Paket-Rückmeldungen

Falls Silvio auf SP-19 (Rezeptur/Béchamel) oder SP-22 (Metro-Preise) geantwortet hat: Arbeitsannahmen bestätigen oder korrigieren, betroffene v2-Docs anpassen.

### Priorität 3 — Inconsistencies schließen

17 Einträge, 4 aufgelöst, 13 offen. Viele werden durch die v2-Rewrites automatisch aufgelöst. Nach allen v2-Rewrites: Konsistenz-Durchlauf.

## Offene Blocker

| # | Blocker | Wartet auf | Impact |
|---|---|---|---|
| 1 | SP-19 Rezeptur (ohne Béchamel/Ei) | Silvio (WhatsApp 12.04.) | Arbeitsannahme gesetzt, Bestätigung offen |
| 2 | SP-22 Metro-/Lieferanten-Preise | Silvio | Doc 02 v2 [E]-Marker, Doc 11 v2 |
| 3 | SP-23 Nachfrage-Schätzung | Silvio | Doc 02 v2 Absatz-Szenarien |
| 4 | SP-06 Kassensystem TSE | Silvio | Doc 15 |

## Wichtige Präferenzen

- **Commit + Push zusammen** — keine Lücke
- **AskUserQuestion bei 2+ Optionen Pflicht (Rule 11)**
- **Eine Frage nach der anderen (Rule 12)**
- **Pushback erwartet — nicht blind ausführen**
