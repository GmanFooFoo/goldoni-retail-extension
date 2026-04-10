# Repo-Backlog — Goldoni Retail Extension

> Status-Tabelle im MASCHIN-Format. `#` = Referenz-ID (nicht Priorität).
> Prio: P1 / P2 / P3 / Backlog. Effort: XS/S/M/L/XL.
> Status: Offen / In Progress / Blocked / Done.

## P1 — Diese Session (2026-04-10)

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Repo-Setup (Stufe 1a): .gitignore, CLAUDE.md, README, session-state, backlog, rollout-plan, initial commit | P1 | S | Marcello | — | In Progress | Arbeitsgrundlage für alle weiteren Stufen |
| 2 | GitHub-Repo `GmanFooFoo/goldoni-retail-extension` privat anlegen + push | P1 | XS | Marcello | gh auth status | Offen | Remote-Backup + Vercel-Source |
| 3 | Labels anlegen: `feedback-silvio`, `quality-issue`, `new-info`, `decision-needed` | P1 | XS | Marcello | #2 | Offen | Issue-Taxonomie |
| 4 | MkDocs Material Reader-Site (Stufe 1b) | P1 | M | Marcello | #1 | Offen | Silvio-freundliche Lese-Oberfläche |
| 5 | Vercel-Deploy `retail.restaurante-goldoni.de` (Stufe 1c) | P1 | S | Marcello + User | DNS DomainFactory | Offen | Silvio braucht URL für Review |
| 6 | Persona-Refresh: 9 neue Personas schreiben (Stufe 2) | P1 | M | Marcello | — | Offen | Review-Basis für Stufe 3 |
| 7 | Deep Review Doc 02 (Wirtschaftlichkeit) — Marcus + Frau Keller | P1 | S | Marcello | #6 | Offen | MwSt-Frage klären, Wareneinsatz-Quellen |
| 8 | Deep Review Doc 04 (LMIV) — Dr. Steiger | P1 | S | Marcello | #6 | Offen | Juristisches Risiko Nährwerte |
| 9 | Deep Review Doc 05 (HACCP) — Dr. Steiger | P1 | S | Marcello | #6 | Offen | CCP-Grenzwerte belegen |
| 10 | Deep Review Doc 13 (Rollout-Plan) — Marcus + Dr. Steiger | P1 | S | Marcello | #6 | Offen | Timing-Widerspruch 6 vs 8 Wochen auflösen |
| 11 | Deep Review Doc 17 (Wettbewerb) — Marcus | P1 | S | Marcello | #6 | Offen | "Kein Wettbewerb"-Claim validieren |
| 12 | Session-Report + Next-Session-Prompt (Stufe 4) | P1 | XS | Marcello | #7–#11 | Offen | Handoff für nächste Session |

## P2 — Nächste Session

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 20 | v2-Rewrite der 5 kritischen Docs auf Basis der Revisionspläne | P2 | L | Marcello | Silvio-Feedback zu #30 | Offen | Saubere v2 für Bank/Steuerberater |
| 21 | Review der 🟡 lückenhaften Docs (01, 07, 09, 11, 14, 15, 16, 18) | P2 | L | Marcello | #20 | Offen | Vollständigkeit Business Case |
| 22 | Doc 06 Mockups: echte HTML/Design-Assets besorgen oder als Skizze deklarieren | P2 | M | Silvio + Jana | — | Offen | Doc 06 aktuell 🔴 kritisch |

## P3 — Silvio-Fragen (werden als GitHub Issues angelegt)

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 30 | Silvios echter Nachname, Adresse, Steuernummer | P3 | XS | Silvio | — | Offen | Ersetzt `[TBD-Silvio]` überall |
| 31 | MwSt-Vorklärung mit Steuerberater: 7% oder 19%? | P3 | S | Silvio + Frau Keller | — | Offen | Kippt Wirtschaftlichkeit Doc 02 |
| 32 | Vorgespräch mit Veterinäramt Stuttgart: welcher Antragspfad? | P3 | S | Silvio | — | Offen | Timing Rollout Doc 13 |
| 33 | Metro-Angebote für Vakuumiergerät + Schockfroster (Lieferzeit?) | P3 | S | Silvio | — | Offen | Timing Rollout Doc 13 |
| 34 | Domain-DNS bei DomainFactory: CNAME für `retail.restaurante-goldoni.de` | P3 | XS | User | Vercel-Projekt-URL | Offen | Reader-Site live |

## Backlog

| # | Item | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 50 | Scoring-Matrix Claudia (Stammgast) als wiederverwendbares Tool | Backlog | S | Marcello | — | Offen | Skalierbare Kundenbefragung |
| 51 | Brand-Konsistenz-Checkliste Jana als Review-Tool | Backlog | S | Marcello | — | Offen | Wiederverwendbar für weitere Goldoni-Projekte |
| 52 | Sensitivity-Analyse Doc 02 (Break-Even bei 30/40/50/60 Einheiten/Woche) | Backlog | S | Marcello | #31 | Offen | Risiko-Transparenz |
| 53 | Rechtscheck Produkthaftung (Doc 14) durch echten Anwalt | Backlog | M | Silvio + Anwalt | — | Offen | Haftungsrisiko Silvio persönlich |
