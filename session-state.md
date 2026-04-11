# Session State — Goldoni Retail Extension

**Aktuelles Datum:** 2026-04-11
**Letzte aktive Session:** Session 6 (German + Claude, 2026-04-11) — abgeschlossen
**Status:** Stufe 3 Deep Review läuft. **Doc 03, 15, 05, 04 lead-reviewt, alle Rework.** Session 6 hat Doc 04 LMIV mit Rule 9 und Dr. Maldini als ersten Lackmustest bearbeitet — fünf Regulatorik-Funde, davon EU 2018/775 Primärzutat-Herkunft als Haupt-Trophäe (P1, seit 2020 Pflicht, im Doc komplett übergangen) und PPWR 12.8.2026 als erster echter Zukunfts-Stichtag. 17 Findings in A/B/C; inconsistencies #7 um Los-Kennzeichnung erweitert, #9 (Doc 04 ↔ Doc 11) und #10 (Doc 04 ↔ Doc 06) neu. Silvio-Paket wächst auf vier Blöcke (neu: Etikett-Vorbereitung). Nur noch **Doc 14 Rechtliche Absicherung** in der Gate-kritischen Sequenz.
**Aktuelle Phase:** **A — aktiv** (siehe Lebenszyklus unten)

## Lebenszyklus (D-08)

Das Repo hat drei Phasen mit klar unterschiedlichem Aktivitäts-Niveau:

- **Phase A — aktiv:** Arbeit an Business-Case, Reviews, Scope und Rollout, bis Silvio eine Entscheidung trifft (Ja / Nein / Später). Hoher Session-Takt erlaubt.
- **Phase B — reduziert aktiv:** Nur bei Silvio-"Ja". Begleitung der Pilot-Phase bis der Verkauf stabil läuft. Sessions seltener, fokussiert auf konkrete Hindernisse.
- **Phase C — niedrige Flamme:** Danach nur noch Kontext-Speicher. Keine Weiterentwicklung, kein Over-Engineering. Lesbar, aber inaktiv.

Jede Maßnahme, die eine Session einführt, muss die Frage bestehen: *"Brauchen wir das in der aktuellen Phase?"* Wenn die Antwort "vielleicht später" lautet, fällt sie raus.

## Aktive Sessions

Keine aktive Session. Session 6 (2026-04-11) abgeschlossen. Session-Report: `docs/reports/2026-04-11-goldoni-f.md`. Die nächste Session sollte zuerst `SESSION-PROMPT-NEXT.md` lesen und dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Repo-Ownership

Nur **eine schreibende Session** gleichzeitig auf diesem Repo. Lese-Zugriff ist immer frei. Die nächste Session sollte `SESSION-PROMPT-NEXT.md` als ersten Schritt lesen.

## Stage-Fortschritt

| # | Stufe | Status | Hinweis |
|---|---|---|---|
| 1a | Git, CLAUDE.md, README, Backlog | ✅ Done | Initial commit, GitHub-Repo angelegt, Labels gesetzt |
| 1b | MkDocs Reader-Site | ❌ Rolled back | MkDocs war Overkill. Alles entfernt, zurück zu plain markdown |
| 1c | Vercel Deploy | ❌ Dropped | Entfällt komplett. Nur GitHub + lokale Verzeichnisse |
| 2 | 9 Personas + README für Silvio + Frontmatter-Cleanup + Goldoni-Präfix raus + Marcello-Persona abgeschafft + Ton-Reset | ✅ Done | Alle Silvio-facing Dokumente im freundschaftlichen Ton, Personas im Format "Persona NN – Name – Rolle", Marcello-Figur komplett gestrichen |
| 3 | Deep Review der Business-Case-Docs | ⚠️ In Progress | Sequenz: 03 → 15 → 05 → 04 → 14. **Doc 03, 15, 05, 04 Lead-reviewt**, alle Rework. Doc 15 durch 7%-USt-Nachtrag strukturell entschärft. Doc 04 mit Rule 9 reviewt, fünf Regulatorik-Funde, EU 2018/775 Primärzutat als Haupt-Trophäe. Co-Reviews (Behördenkontrolleur 03+04, CFO 15, Küche/Logistik/Behörde 05, Küchenchef 04) ausstehend plus **rückwirkender Regulatorik-Scan durch Dr. Maldini** auf Doc 03 und Doc 05 (vor v2-Rewrite). Doc 14 ausstehend. |
| 4 | Wrap-up Session 1 | ✅ Done | Session-Report, Handoff, SESSION-PROMPT-NEXT geschrieben |
| 5 | MASCHIN-Review + Maßnahmen 1/3/4 (Session 2b) | ✅ Done | decisions.md, Phase A/B/C, beteiligung.md-Gerüst, Prozess-Fixes |
| 6 | Maßnahme 2 — Repo-Zweck-Umschwung | ✅ Done | README und rollout-plan auf Germans Arbeits-Level. Variante B gewählt (keine parallele Silvio-Version). Memory aktualisiert. Spot-Check 2d/2e ohne Rewrite-Bedarf. |

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
- 2026-04-11 — Session 1 Close: Stufe 2 + 4 done, SESSION-PROMPT-NEXT für Stufe 3 geschrieben
- 2026-04-11 — MASCHIN-Review im OMNIXIS-planning Repo korrigiert vier Grundannahmen (Leser = German, offene Beteiligung, Phase A/B/C, lean-Prinzip)
- 2026-04-11 — Session 2b: decisions.md (D-01 bis D-08), Phase-A/B/C-Absatz, beteiligung.md-Gerüst, Prozess-Fixes in handoff. Maßnahme 2 auf Session 3 verschoben.
- 2026-04-11 — Session 3: Maßnahme 2 abgeschlossen. README und rollout-plan auf Arbeits-Level (Variante B). Memory-Update. Spot-Checks ohne Rewrite. Konsistenz-Findings 1/3/6 in `inconsistencies.md` präzisiert. Commits: e5a415e, 68d4493, 49f1b0a.
- 2026-04-11 — Session 4: Stufe 3 Deep Review gestartet. Gate-kritische Sequenz 03 → 15 → 05 → 04 → 14. Doc 03 Vetamt Lead-Review durch Lebensmittelrechtler. Findings + v2-Plan-Skizze. inconsistencies #7 neu (MHD-Validierung). Commits: 563d64b, 5a02643, 717e64b.
- 2026-04-11 — Session 5: Doc 15 Steuer Lead-Review durch Steuerberaterin. 13 Findings in drei Gruppen. inconsistencies #5 präzisiert (Pfad: Silvio-Briefing + § 89 AO), #8 neu (Doc 02/07 erwähnen MwSt gar nicht). Commits: 096e571, 8e79394, 5bf4db7.
- 2026-04-11 — Session 5 (Fortsetzung): Doc 05 HACCP Lead-Review durch Lebensmittelrechtler. 17 Findings in drei Gruppen. Gefahrenanalyse, Rohware-Eingang, Rückstellproben, Reinigungsplan, Rückruf-Prozess, MHD-Validierung fehlen. inconsistencies #3 und #7 präzisiert. Silvio-Paket wächst auf drei Bündel. Commits: 7d0ced9, 7f97add.
- 2026-04-11 — Session 5 Close: Persona-Hard-Wraps gefixt, Persona 00 Silvio und Persona 10 Dr. Maldini angelegt, CLAUDE.md Rule 9 (Regulatorik-Scan vor Legal/Tax/Tech-Reviews) eingebaut. Doc 03 Adresse (Hauptstätter Straße 58) und IHK-Kontakt präzisiert. 7%-USt-Finding (Steueränderungsgesetz 2025) als Nachtrag in Doc 15, löst Gate nach Rollout-Schritt 1 gesetzlich auf. inconsistencies #5 aufgelöst, #8 entschärft. Claudia als Mutter mit Lieferservice-Alltag präzisiert. 13 Commits: 096e571, 8e79394, 5bf4db7, 739c1b9, 7d0ced9, 7f97add, 61bce53, 480a9ca, c8406de, 15fb7c3, acf708d, 5c98350, 4e4ca61.
- 2026-04-11 — Session 6: Doc 04 LMIV Lead-Review durch Lebensmittelrechtler mit Rule 9 als erstem Praxistest. Regulatorik-Nachtrag Dr. Maldini mit fünf Funden, davon EU 2018/775 Primärzutat-Herkunft als P1-Haupt-Trophäe (seit 2020 Pflicht, im Doc komplett übergangen) und PPWR 12.8.2026 als erster Zukunfts-Stichtag. 17 Findings in A/B/C-Gruppen. inconsistencies #7 um Los-Kennzeichnung erweitert, #9 (Doc 04 ↔ Doc 11 Lieferanten-Herkunft) und #10 (Doc 04 ↔ Doc 06 Mockups) neu. Silvio-Paket wächst auf vier Blöcke (neu: Etikett-Vorbereitung — Adresse, Labor-Nährwerte, PPWR-Konformitätserklärung). Commits: 1e6c9dd, 28f74d3, 48534cf.
