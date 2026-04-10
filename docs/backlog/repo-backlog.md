# Repo-Backlog — Goldoni Retail Extension

> Status-Tabelle im MASCHIN-Format. `#` = Referenz-ID (nicht Priorität).
> Prio: P1 / P2 / P3 / Backlog. Effort: XS/S/M/L/XL.
> Status: Offen / In Progress / Blocked / Done.

## P1 — Diese Session (2026-04-10)

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Repo-Setup (Stufe 1a): .gitignore, CLAUDE.md, README, session-state, backlog, rollout-plan, initial commit | P1 | S | German | — | ✅ Done | Arbeitsgrundlage für alle weiteren Stufen |
| 2 | GitHub-Repo `GmanFooFoo/goldoni-retail-extension` privat anlegen + push | P1 | XS | German | — | ✅ Done | Remote-Backup |
| 3 | Labels anlegen: `feedback-silvio`, `quality-issue`, `new-info`, `decision-needed` | P1 | XS | German | — | ✅ Done | Issue-Taxonomie |
| 4 | ~~MkDocs Material Reader-Site (Stufe 1b)~~ | — | — | — | — | ❌ Dropped | MkDocs war Overkill; User will plain markdown |
| 5 | ~~Vercel-Deploy `retail.restaurante-goldoni.de` (Stufe 1c)~~ | — | — | — | — | ❌ Dropped | Kein Hosting. Nur GitHub + lokal |
| 6 | Persona-Refresh: 9 neue Personas schreiben (Stufe 2) + README-Rewrite für Silvio | P1 | M | German | — | In Progress | Review-Basis für Stufe 3; README als Silvio-Landing |
| 6b | Frontmatter-Cleanup aus allen MD-Dateien (Obsidian-Leftover) | P1 | XS | German | #6 | Offen | Einheitliches, GitHub-optimiertes Markdown |
| 6c | "Goldoni"-Präfix aus 19 Original-Dateinamen und H1 entfernen | P1 | S | German | #6b | Offen | Lesbarere Navigation, Redundanz raus |
| 7 | **Stufe 3 Scope-Erweiterung:** Deep Review aller **19 Docs** in Reihenfolge 01–19 (statt nur 5 kritische). User-Entscheidung 2026-04-10. | P1 | XL | German | #6 | Offen | Vollständige Prüfung des Business Case |
| 12 | Session-Report + Next-Session-Prompt (Stufe 4) | P1 | XS | German | #7–#11 | Offen | Handoff für nächste Session |

## P2 — Nächste Session

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 20 | v2-Rewrite der 5 kritischen Docs auf Basis der Revisionspläne | P2 | L | German | Silvio-Feedback zu #30 | Offen | Saubere v2 für Bank/Steuerberater |
| 21 | Review der 🟡 lückenhaften Docs (01, 07, 09, 11, 14, 15, 16, 18) | P2 | L | German | #20 | Offen | Vollständigkeit Business Case |
| 22 | Doc 06 Mockups: echte HTML/Design-Assets besorgen oder als Skizze deklarieren | P2 | M | Silvio + Jana | — | Offen | Doc 06 aktuell 🔴 kritisch |

## P3 — Silvio-Fragen (werden als GitHub Issues angelegt)

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 30 | Silvios echter Nachname, Adresse, Steuernummer | P3 | XS | Silvio | — | Offen | Ersetzt `[TBD-Silvio]` überall |
| 31 | MwSt-Vorklärung mit Steuerberater: 7% oder 19%? | P3 | S | Silvio + Frau Keller | — | Offen | Kippt Wirtschaftlichkeit Doc 02 |
| 32 | Vorgespräch mit Veterinäramt Stuttgart: welcher Antragspfad? | P3 | S | Silvio | — | Offen | Timing Rollout Doc 13 |
| 33 | Metro-Angebote für Vakuumiergerät + Schockfroster (Lieferzeit?) | P3 | S | Silvio | — | Offen | Timing Rollout Doc 13 |
| 34 | ~~Domain-DNS bei DomainFactory: CNAME für `retail.restaurante-goldoni.de`~~ | — | — | — | — | ❌ Dropped | Hosting entfällt |

## Backlog

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 50 | Scoring-Matrix Claudia (Stammgast) als wiederverwendbares Tool | Backlog | S | German | — | Offen | Skalierbare Kundenbefragung |
| 51 | Brand-Konsistenz-Checkliste Jana als Review-Tool | Backlog | S | German | — | Offen | Wiederverwendbar für weitere Goldoni-Projekte |
| 52 | Sensitivity-Analyse Doc 02 (Break-Even bei 30/40/50/60 Einheiten/Woche) | Backlog | S | German | #31 | Offen | Risiko-Transparenz |
| 53 | Rechtscheck Produkthaftung (Doc 14) durch echten Anwalt | Backlog | M | Silvio + Anwalt | — | Offen | Haftungsrisiko Silvio persönlich |
