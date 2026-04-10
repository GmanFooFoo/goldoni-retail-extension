# Session State — Goldoni Retail Extension

**Aktuelles Datum:** 2026-04-11
**Aktive Session:** German + Claude (diese Session)
**Status:** In Progress

## Aktive Sessions

| # | Session | Owner | Repo | Branch | Seit | Was |
|---|---|---|---|---|---|---|
| 1 | German + Claude | German | goldoni-retail-extension | main | 2026-04-10 | Stufe 2 abgeschlossen, Ton-Korrektur im Gange |

## Repo-Ownership

Nur **eine schreibende Session** gleichzeitig auf diesem Repo. Lese-Zugriff ist immer frei.

## Stage-Fortschritt

| # | Stufe | Status | Hinweis |
|---|---|---|---|
| 1a | Git, CLAUDE.md, README, Backlog | ✅ Done | Initial commit, GitHub-Repo angelegt, Labels gesetzt |
| 1b | MkDocs Reader-Site | ❌ Rolled back | MkDocs war Overkill. Alles entfernt, zurück zu plain markdown |
| 1c | Vercel Deploy | ❌ Dropped | Entfällt komplett. Nur GitHub + lokale Verzeichnisse |
| 2 | 9 Personas + README für Silvio + Frontmatter-Cleanup + Goldoni-Präfix raus + Marcello-Persona abgeschafft | ✅ Done | Marcello-Figur gestrichen, README im freundschaftlichen Ton, alle Personas im Format "Persona NN – Name – Rolle" |
| 3 | Deep Review aller 19 Docs (Scope erweitert von 5 kritischen) | 🔲 Offen | Wird eine eigene Session; XL-Aufwand |
| 4 | Wrap-up + Next-Session-Prompt | 🔲 Offen | — |

## Substanz aus Stufe 1b (behalten)

Folgende Inhalte aus Stufe 1b haben echten Wert und bleiben als plain
markdown im Repo:

- `docs/glossary.md` — HACCP, LMIV, CCP, Vakuum vs Schutzgas, Schockfroster, Vetamt
- `docs/findings/inconsistencies.md` — 5 Widersprüche aus MASCHIN-Voranalyse
- `docs/plans/rollout-plan.md` — Phase 1/2 Scope-Entscheidung (Vakuum-only, Tiefkühl später)

## Letzte Updates

- 2026-04-10 — Session gestartet, Lothar-Clone sauber abgelöst, frisches Git-Repo
- 2026-04-10 — Ordner-Rename `retail extension/` → `business-case/`
- 2026-04-10 — Initial commit + GitHub-Repo `GmanFooFoo/goldoni-retail-extension` angelegt
- 2026-04-10 — Stufe 1b (MkDocs) probiert, vom User als Overkill verworfen, komplett rausgeschmissen
- 2026-04-10 — Vercel/Reader-Site entfällt komplett — nur GitHub + lokale Verzeichnisse
