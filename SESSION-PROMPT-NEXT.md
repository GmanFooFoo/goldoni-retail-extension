# Session-Prompt für die nächste Goldoni-Session

> Diese Datei ist der Handoff von der vorigen Session (2026-04-11) an die kommende. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Stand Ende der Session 2026-04-11:

- **Stufe 1a** (Setup, Repo, GitHub) — ✅ Done
- **Stufe 1b** (MkDocs Reader-Site) — ❌ Gedroppt (war Overkill)
- **Stufe 1c** (Vercel Deploy) — ❌ Gedroppt (kein Hosting)
- **Stufe 2** (9 Personas + README + rollout-plan in Silvio-Ton) — ✅ Done
- **Stufe 3** (Deep Review aller 19 Docs) — 🔲 **Das ist die Aufgabe für dich**
- **Stufe 4** (Wrap-up dieser Session) — ✅ Done (daher diese Datei)

## Kontext-Reset — lies diese Dateien zuerst

Bevor du mit Stufe 3 anfängst, stelle sicher, dass du folgendes gelesen hast (Reihenfolge beachten, oberes zuerst):

1. `~/.claude/projects/-Users-germanrauhut-com-Developer-projects-goldoni-retail-extension/memory/MEMORY.md` — Index aller Projekt-Memories. Die wichtigsten:
   - `project_silvio_profile.md` — **Pflichtlektüre.** Wer ist Silvio, wie reden wir mit ihm, was braucht er, um "ja" zu sagen.
   - `project_no_marcello_persona.md` — keine Berater-Rolle, German ist der Owner
   - `project_scope_phase1_vakuum_only.md` — Phase 1 = nur gekühlte Vakuum-Produkte
   - `feedback_pushback_expected.md` — German erwartet Widerspruch und eigenes Urteil
   - `feedback_no_hard_wraps.md` — ein Paragraph = eine Zeile
   - `feedback_askuserquestion_preferred.md` — bei Wahlmöglichkeiten AskUserQuestion benutzen
   - `feedback_readme_is_customer_facing.md` — README = Silvios Seite
2. `CLAUDE.md` im Repo-Root — Projekt-Grundregeln, Review-Standard-Format, Structure
3. `session-state.md` im Repo-Root — Stage-Fortschritt, aktuell
4. `docs/personas/assignments.md` — wer reviewt was
5. Der Session-Report `docs/reports/2026-04-11-goldoni.md` — was in der letzten Session passiert ist
6. `docs/plans/rollout-plan.md` und `README.md` — Beispiele für den Silvio-Ton, zur Orientierung

## Was in dieser Session gemacht werden soll

**Stufe 3 — Deep Review der Business-Case-Dokumente.**

German hat die ursprüngliche Aufgabe erweitert: nicht nur 5 kritische Docs, sondern **alle 19**. Aber das ist XL-Aufwand, und in einer einzelnen Session wahrscheinlich zu viel. Sprich dich mit German am Anfang der Session ab, ob wir:

| # | Option | Was passiert | Wann sinnvoll |
|---|---|---|---|
| A | **Alle 19 Docs** in dieser Session | ~40 Review-Dateien, 19 Findings-Dateien, 19 v2-Pläne. Braucht voraussichtlich mehrere lange Sessions. | Nur wenn German explizit "wir machen alles" sagt. |
| B | **Priorisierte Teilmenge (5–8 Docs)** in dieser Session, Rest in Folge-Sessions | Fokus auf die Docs, die Silvio als erstes sehen sollen. Empfohlener Einstieg: Doc 01, 02, 05, 13, 17 (plus ggf. 04 LMIV und 07 Preisgestaltung). | Default, wenn German kein anderes Signal gibt. |
| C | **Einzelnes Doc im Tiefreview** als Pilot | Wir machen ein vollständiges Review (alle zuständigen Personas) für ein einziges Doc, z.B. Doc 02 (Wirtschaftlichkeit). Danach bewerten wir den Aufwand und entscheiden über die Fortsetzung. | Wenn German erstmal den Prozess testen will. |

**Empfehlung:** Option C — ein Pilot-Review für Doc 02. Das ist das finanziell wichtigste Dokument, wird von Marcus (Lead) und Frau Keller (Co) geprüft, und das Ergebnis zeigt German, wie gründlich oder knapp die Reviews ausfallen. Danach gemeinsam den Plan für die restlichen 18 schärfen.

**Frage als Session-Start an German:** via `AskUserQuestion`, A/B/C auswählen lassen, bevor du losarbeitest.

## Stage-3 Workflow (sobald die Option gewählt ist)

Für jedes Dokument, das reviewt wird:

1. **Original-Doc lesen** (`docs/business-case/NN – XYZ.md`)
2. **`docs/personas/assignments.md`** öffnen — welche Personas sind Lead und Co für dieses Doc?
3. **Pro zuständiger Persona ein Review schreiben** in `docs/reviews/[persona]-NN.md`, nach dem Review-Standard-Format aus `CLAUDE.md` (Kurzurteil, Scoring 1–5 auf 4 Dimensionen, Red Flags, Kritikpunkte, Was fehlt, Empfehlung)
4. **Eine konsolidierte Findings-Datei** `docs/findings/NN-findings.md` — dedupliziert aus den Persona-Reviews, priorisiert nach Schwere (Stopp / Qualität / Nice-to-have)
5. **Ein Revisionsplan** `docs/plans/NN-v2-plan.md` — was muss geändert werden, welche Infos fehlen, wer muss was liefern
6. **Commit nach jedem Doc**, nicht Sammel-Commit
7. **`docs/findings/inconsistencies.md`** aktualisieren, wenn während des Reviews neue Widersprüche auffallen

## Besondere Hinweise für Stufe 3

- **Phase 1 = nur Vakuum.** Jede Persona bewertet mit diesem Scope im Kopf. Tiefkühl-spezifische Kritik wird als "Phase 2" markiert, nicht im Hauptteil.
- **Wo Persona XY Lead ist**, schreibt sie die konsolidierte Einschätzung. Wo sie nur Co ist, liefert sie nur ihren Fachbeitrag.
- **Keine Berater-Pose.** Die Personas sind Analyse-Brillen. Der Output darf kritisch und pointiert sein, aber das Dokument **für Silvio** (die Findings) muss wieder in einfacher Sprache geschrieben werden — Silvio soll am Ende verstehen, was wir gefunden haben, ohne BWL-Studium.
- **Silvio-Fragen als GitHub Issues.** Wenn beim Review eine Frage auftaucht, die nur Silvio beantworten kann, direkt ein Issue anlegen (`gh issue create --label feedback-silvio --title "..."`), nicht nur im Review notieren.

## Offene Punkte aus der vorigen Session (FYI, kein Action-Item für dich)

- **MwSt-Klärung (7% oder 19%)**: Silvio sollte mit seinem Steuerberater reden. Ohne Klarheit kippen alle Wirtschaftlichkeitsrechnungen.
- **Silvios echter Nachname, Adresse, Steuernummer**: aktuell `[TBD-Silvio]` überall. Bleibt bis Silvio die Infos liefert.
- **Vetamt-Vorgespräch**: sollte Silvio selbst machen, sobald er die Idee weitertreiben will.
- **Metro-Angebote für Vakuumiergerät**: Lieferzeit und Modell-Vergleich.
- **README + rollout-plan**: Silvio hat die noch nicht gesehen. German entscheidet, wann er sie ihm zeigt.

## Wichtige Präferenzen von German (aus den Memories)

- **Ton für Silvio-facing Texte**: einfache Sätze, keine Anglizismen, kein Fachjargon ohne Erklärung, tentativ ("wenn du willst"), warm, Freundschaft statt Kunde. Siehe `project_silvio_profile.md`.
- **Ton für interne Arbeits-Dokumente** (Reviews, Findings-Arbeitsdokumente, CLAUDE.md): präzise, direkt, pointiert, kein Consulting-Geschwurbel aber auch keine Überförmlichkeit. Normal-professionell.
- **Pushback**: German erwartet, dass du widersprichst wenn etwas nicht passt. "Ich mach einfach alles was er sagt" ist der falsche Modus. Siehe `feedback_pushback_expected.md`.
- **Tabellen**: Status- und To-Do-Tabellen im MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`), nicht vereinfacht.
- **Markdown**: ein Paragraph = eine Zeile im Source (keine Hard-Wraps auf 72/80 Zeichen). Tabellen/Listen/Code natürlich ausgenommen.
- **AskUserQuestion**: bei 2+ Optionen immer die strukturierte Variante benutzen, nicht nummerierte Chat-Listen.
- **Keine Marcello-Persona**: du bist Claude, du hilfst German, du bist kein Berater. Silvio-facing Texte sind in Germans Stimme signiert.
- **Keine Easter Eggs am Session-Ende**, stattdessen ein **Leitsatz der Session** im Report. Siehe `project_no_easter_eggs.md`.

## Start-Nachricht Template

So könnte deine erste Antwort in der neuen Session aussehen, nach dem Lesen der oben genannten Dateien:

> "Kontext geladen. Letzte Session war 2026-04-11, Stufe 2 ist abgeschlossen (9 Personas, README und rollout-plan im Silvio-Ton, alles gepusht). Für heute steht Stufe 3 an: Deep Review der Business-Case-Dokumente.
>
> Ich habe drei Vorschläge, wie wir den Scope handhaben: (a) alle 19 Docs in mehreren Sessions, (b) eine priorisierte Teilmenge von 5–8 Docs heute, (c) ein einzelnes Doc als Pilot-Review, um den Prozess zu kalibrieren. Ich empfehle (c) — Pilot an Doc 02 (Wirtschaftlichkeit). Wie möchtest du vorgehen?"

Dann warte auf Germans Antwort und fang entsprechend an.

---

*Ende des Session-Prompts.*
