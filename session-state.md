# Session State — Goldoni Retail Extension

**Aktuelles Datum:** 2026-04-14
**Letzte aktive Session:** Session 16 (German + Claude, 2026-04-14) — abgeschlossen
**Status:** **Alle 20 Docs auf v2. 15/17 Inconsistencies aufgelöst.** 308 Findings, 45 Reviews. Persona-00 Gesamt-Überblick + PPTX. Backlog #52/#54/#56 in Session 16 durch (Q4Me evaluiert, Geschenkebox-Konzept, Sensitivity-Analyse). 2 offene Inconsistencies (#2, #17) und 6 SP-Blocker warten auf Silvio, zusätzlich SP-25 und SP-26 neu.
**Aktuelle Phase:** **A — aktiv** (siehe Lebenszyklus unten)

## Lebenszyklus (D-08)

Das Repo hat drei Phasen mit klar unterschiedlichem Aktivitäts-Niveau:

- **Phase A — aktiv:** Arbeit an Business-Case, Reviews, Scope und Rollout, bis Silvio eine Entscheidung trifft (Ja / Nein / Später). Hoher Session-Takt erlaubt.
- **Phase B — reduziert aktiv:** Nur bei Silvio-"Ja". Begleitung der Pilot-Phase bis der Verkauf stabil läuft. Sessions seltener, fokussiert auf konkrete Hindernisse.
- **Phase C — niedrige Flamme:** Danach nur noch Kontext-Speicher. Keine Weiterentwicklung, kein Over-Engineering. Lesbar, aber inaktiv.

Jede Maßnahme, die eine Session einführt, muss die Frage bestehen: *"Brauchen wir das in der aktuellen Phase?"* Wenn die Antwort "vielleicht später" lautet, fällt sie raus.

## Aktive Sessions

Session 16 (German + Claude, 2026-04-14) — abgeschlossen. Session-Report: `docs/reports/2026-04-14-goldoni.md`.

## Repo-Ownership

Nur **eine schreibende Session** gleichzeitig auf diesem Repo. Lese-Zugriff ist immer frei. Die nächste Session sollte `SESSION-PROMPT-NEXT.md` als ersten Schritt lesen.

## Stage-Fortschritt

| # | Stufe | Status | Hinweis |
|---|---|---|---|
| 1a | Git, CLAUDE.md, README, Backlog | ✅ Done | Initial commit, GitHub-Repo angelegt, Labels gesetzt |
| 1b | MkDocs Reader-Site | ❌ Rolled back | MkDocs war Overkill. Alles entfernt, zurück zu plain markdown |
| 1c | Vercel Deploy | ❌ Dropped | Entfällt komplett. Nur GitHub + lokale Verzeichnisse |
| 2 | 9 Personas + README für Silvio + Frontmatter-Cleanup + Goldoni-Präfix raus + Marcello-Persona abgeschafft + Ton-Reset | ✅ Done | Alle Silvio-facing Dokumente im freundschaftlichen Ton |
| 3 | Deep Review der Business-Case-Docs | ✅ Done | **20/20 Docs lead-reviewt, 20/20 auf v2.** 308 Findings, 45 Reviews, 14/17 Inconsistencies aufgelöst. |
| 4 | Wrap-up Session 1 | ✅ Done | Session-Report, Handoff |
| 5 | MASCHIN-Review + Maßnahmen 1/3/4 | ✅ Done | decisions.md, Phase A/B/C, Prozess-Fixes |
| 6 | Maßnahme 2 — Repo-Zweck-Umschwung | ✅ Done | README und rollout-plan auf Germans Arbeits-Level |
| 7 | Silvio-Übersetzungsschicht + Slides | ✅ Done | Persona-00 Gesamt-Überblick, PPTX-Generator, 12 Slides |

## Letzte Updates

- 2026-04-14 — Session 16: Backlog-Abarbeitung ohne Silvio-Blocker. Q4Me-Evaluation (29,90 €/19,90 € DEHOGA, 4 Wochen Test). Geschenkebox-Konzept "Sugo + Rummo" mit LMIV-Warenzusammenstellung, 19,90 € Einstieg / 22,90 € Premium, DB 40–49 % netto. Sensitivity-Analyse Doc 02 mit Absatz-Matrix 15–70 Stk/W, Kombi-Worst 39 Monate Amortisation, 6 Go/No-Go-Checkpoints bis Q1 2027. Inconsistency #16 aufgelöst → 15/17. SP-25, SP-26 neu, SP-20 präzisiert, SP-05 erweitert. 3 Commits.
- 2026-04-13 — Session 15: Konsolidierung + Silvio-Übersetzungsschicht. Inconsistencies 4/17 → 14/17 aufgelöst. Doc 06 v2 Etikett-Spezifikation (11/12 Findings). Silvio Brunetti bestätigt und propagiert. README auf 20/20 v2. Persona-00 Gesamt-Überblick (12 Slides). PPTX-Generator mit YAML-Content-Trennung. 6 Commits.
