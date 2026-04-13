# Session-Prompt für Session 15 — Goldoni Retail Extension

> Handoff von Session 14 (2026-04-13) an Session 15.

## Kurzstand

Session 14 hat die **7 verbleibenden v2-Rewrites** abgeschlossen (6 von 7; Doc 06 Mockups bewusst verschoben). Gesamt: 308 Findings, 45 Reviews, **19 von 20 Docs auf v2** (nur Doc 06 bleibt v1). 74 Findings in dieser Session adressiert.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-13-goldoni-c.md` — Session-14-Report. **Wichtigste Datei.**
2. `docs/findings/decisions.md` — D-01 bis D-13.
3. `docs/silvio-paket/offene-fragen.md` — 24 Einträge (SP-01 bis SP-24).
4. `session-state.md` — Stand nach Session 14.

## Was in Session 15 ansteht

### Priorität 1 — Inconsistencies schließen

17 Einträge, davon 4 bereits aufgelöst. Viele der 13 offenen werden durch die v2-Rewrites automatisch aufgelöst sein. Systematischer Durchlauf:

- Für jede Inconsistency prüfen: Ist der Widerspruch durch v2-Rewrites behoben?
- Status auf "Aufgelöst" oder "Offen mit Begründung" setzen
- Verbleibende offene Punkte als Aktionen zuordnen

Besonders prüfen: #1 (Rollout-Dauer, sollte durch Doc 13 v2 aufgelöst sein), #3 (Tiefkühl-Scope, durch v2-Rewrites überall korrigiert), #6 (Pilot-Gate, durch Doc 13 v2 aufgelöst), #8 (Netto/Brutto, durch Doc 02/07 v2 aufgelöst).

### Priorität 2 — Doc 06 Mockups

Entscheiden: Text-Rewrite (LMIV-Checkliste als Tabelle, Pflichtfelder dokumentieren, "Marco Antonelli" durch [TBD-Silvio] ersetzen) oder warten auf visuellen Entwurf. Ein Text-v2 ohne visuelles Design ist sinnvoll als Arbeitsgrundlage für Silvio/Designer.

### Priorität 3 — Silvio-Paket-Rückmeldungen

Falls Silvio geantwortet hat:
- SP-19 (Rezeptur ohne Béchamel) → Arbeitsannahme bestätigen
- SP-22 (Metro-/Lieferanten-Preise) → [E]-Marker in Doc 02/07/11 durch echte Preise ersetzen
- SP-23 (Nachfrage-Schätzung) → Absatz-Szenarien in Doc 02 kalibrieren
- SP-24 (aktuelle Kartenpreise) → Preisanker in Doc 07 validieren

### Priorität 4 — README aktualisieren

Doc-Status-Matrix auf 19/20 v2 (oder 20/20 falls Doc 06 v2 geschrieben wird).

### Priorität 5 — Optional: Persona-00-Silvio-Übersetzungsschicht

Vorbereitung für das Übergabe-Gespräch an Silvio. Persona 00 erstellt eine Silvio-Ableitung der wichtigsten Ergebnisse — nicht als 20-Doc-Dump, sondern als "Was muss Silvio wissen, um Ja oder Nein zu sagen?"

## Offene Blocker

| # | Blocker | Wartet auf | Impact |
|---|---|---|---|
| 1 | SP-19 Rezeptur (ohne Béchamel/Ei) | Silvio (WhatsApp 12.04.) | Arbeitsannahme gesetzt, Bestätigung offen |
| 2 | SP-22 Metro-/Lieferanten-Preise | Silvio | Doc 02/07/11 [E]-Marker |
| 3 | SP-23 Nachfrage-Schätzung | Silvio | Doc 02 Absatz-Szenarien |
| 4 | SP-24 Kartenpreise | Silvio | Doc 07 Preisanker |
| 5 | SP-06 Kassensystem TSE | Silvio | Doc 15 |
| 6 | Doc 06 visueller Etikett-Entwurf | Silvio + Designer | Doc 06 v2 (falls visuell) |

## Wichtige Präferenzen

- **Commit + Push zusammen** — keine Lücke
- **AskUserQuestion bei 2+ Optionen Pflicht (Rule 11)**
- **Eine Frage nach der anderen (Rule 12)**
- **Pushback erwartet — nicht blind ausführen**
