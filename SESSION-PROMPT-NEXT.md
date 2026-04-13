# Session-Prompt für Session 16 — Goldoni Retail Extension

> Handoff von Session 15 (2026-04-13) an Session 16.

## Kurzstand

**Alle 20 Docs auf v2. 14/17 Inconsistencies aufgelöst. Silvio-Slides fertig.** 308 Findings, 45 Reviews, 12-Slide-Präsentation für das Übergabe-Gespräch an Silvio. Das Projekt ist inhaltlich komplett — der nächste Meilenstein ist **Germans Gespräch mit Silvio**.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-13-goldoni-d.md` — Session-15-Report.
2. `docs/silvio-derivatives/gesamt-ueberblick.md` — Persona-00 Gesamt-Überblick (12 Slides).
3. `docs/silvio-derivatives/slides-content.yaml` — editierbare Slide-Inhalte.
4. `session-state.md` — Stand nach Session 15.

## Was in Session 16 ansteht

### Priorität 1 — Silvio-Rückmeldungen verarbeiten

Falls Silvio auf offene Fragen geantwortet hat:

| SP | Thema | Was dann |
|---|---|---|
| SP-19 | Rezeptur (ohne Béchamel, Gramm) | Arbeitsannahme bestätigen/korrigieren, QUID + Allergene in Doc 04/06 befüllen |
| SP-09 | Vollständige Anschrift | Etikett-Pflichtfeld #8 in Doc 06 befüllen |
| SP-22 | Metro-/Lieferanten-Preise | [E]-Marker in Doc 02/07/11 durch echte Preise ersetzen |
| SP-23 | Nachfrage-Schätzung | Absatz-Szenarien in Doc 02 kalibrieren, Slides anpassen |
| SP-24 | Kartenpreise | Preisanker in Doc 07 validieren |

### Priorität 2 — Slides verfeinern

- YAML-Texte prüfen und Formulierungen schärfen
- Ggf. italienische Version (`slides-content-it.yaml`)
- PPTX in Keynote/PowerPoint visuell prüfen und ggf. Layout-Korrekturen

### Priorität 3 — Backlog-Items (falls Zeit)

| # | Item | Effort |
|---|---|---|
| 52 | Sensitivity-Analyse Doc 02 (Break-Even bei 30/40/50/60 Einheiten) | S |
| 54 | Geschenkebox-Konzept (Sugo + Rummo-Nudeln) | M |
| 56 | Q4Me QM-Software evaluieren | S |

### Priorität 4 — Inconsistency #17 (Öffnungszeiten)

17–22 vs. 18–22:30. Falls Silvio antwortet → direkt korrigieren. Falls nicht → als offenen Punkt belassen.

## Offene Blocker

Alle 6 Blocker warten auf Silvio (SP-09, SP-19, SP-22, SP-23, SP-24, Inconsistency #17).

## Wichtige Präferenzen

- **Commit + Push zusammen** — keine Lücke
- **AskUserQuestion bei 2+ Optionen Pflicht (Rule 11)**
- **Eine Frage nach der anderen (Rule 12)**
- **Pushback erwartet — nicht blind ausführen**
- **Silvio ist kein Reviewer — Silvio-Paket als Artefakt (Rule 10)**
