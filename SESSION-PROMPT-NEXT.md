# Session-Prompt für Session 3 — Goldoni Retail Extension

> Handoff von Session 2b (2026-04-11 abends) an Session 3. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Nach Session 2b sind drei von vier MASCHIN-Review-Maßnahmen erledigt:

- ✅ **Maßnahme 1:** `docs/findings/decisions.md` mit D-01 bis D-08 angelegt.
- ✅ **Maßnahme 4:** Phase A/B/C in `session-state.md`, Multi-Session-Suffix und Commit-Log-Pflicht in `docs/session-handoff.md`.
- ✅ **Maßnahme 3:** `docs/beteiligung.md` Gerüst angelegt, inhaltliche Sektionen bewusst leer, vier offene Fragen an German formuliert.
- 🔲 **Maßnahme 2:** Repo-Zweck-Umschwung — **das ist Session 3.**

Die **Stufe-3 Deep-Review-Arbeit** (19 Business-Case-Docs) ist in den Backlog gewandert. Sie kommt nach Maßnahme 2, weil der Tonlage-Umschwung die Grundlage für alle weiteren internen Arbeits-Dokumente ist — und es wäre Verschwendung, Reviews in einem Ton zu schreiben, der in Session 3 ohnehin umgedreht wird.

## Kontext-Reset — lies diese Dateien zuerst

1. `~/.claude/projects/-Users-germanrauhut-com-Developer-projects-goldoni-retail-extension/memory/MEMORY.md` — Projekt-Memories. Wichtig:
   - `project_silvio_profile.md`
   - `project_no_marcello_persona.md`
   - `feedback_pushback_expected.md`
   - `feedback_no_hard_wraps.md`
   - `feedback_readme_is_customer_facing.md` — **Achtung, diese Memory ist jetzt teilweise überholt:** D-06 hat festgelegt, dass das Repo für Germans Arbeits-Ebene geschrieben wird. README bleibt Silvio-facing *als Ableitung* oder wird in eine Arbeits-Version + eine Silvio-Ableitung gesplittet. Die Memory sollte in dieser Session aktualisiert oder ergänzt werden.
2. `docs/findings/decisions.md` — D-01 bis D-08, besonders D-06 (Germans Arbeits-Level), D-07 (offene Beteiligung), D-08 (Phase A/B/C).
3. `CLAUDE.md` im Repo-Root — Projekt-Grundregeln.
4. `session-state.md` — aktueller Stand.
5. `docs/reports/2026-04-11-goldoni.md` — Session 1 Close.
6. `docs/reports/2026-04-11-goldoni-b.md` — Session 2b Close (dieser Plan wurde aus der Fortsetzung dieses Reports generiert).
7. `docs/plans/rollout-plan.md` und `README.md` — die beiden Silvio-facing Dokumente, die in dieser Session auf Germans Level gehoben werden.
8. `docs/beteiligung.md` — das Gerüst, falls German Dimensionen 1–4 füllen will (separater Block, siehe unten).

## Session-3-Auftrag: Maßnahme 2 — Repo-Zweck-Umschwung

**Grund:** Session 1 hat das komplette Repo auf Silvio-facing Ton gedreht. Der MASCHIN-Review hat gezeigt, dass Silvio das Repo vermutlich nie selbst öffnet. Damit ist der Silvio-Ton in den internen Arbeits-Docs Ballast, der echte Tiefe verhindert (D-06).

**Scope (alle Punkte stehen an, aber nicht alle müssen in einer Session):**

### 2a — README auf Germans Level umschreiben (Pflicht)

Aktuell: freundschaftlicher Vorschlag an Silvio ("Caro Silvio, …"). Das wird zum **Arbeits-README** für German selbst: was ist in diesem Repo, wo steht was, welche Entscheidungen sind gefallen, in welcher Phase ist das Projekt, welche Personas gibt es, Stand der Business-Case-Reviews.

Ton: präzise, direkt, kein Verkaufs-Ton, keine italienischen Grüße, keine Marketing-Formulierungen.

### 2b — `rollout-plan.md` — Variante A oder B entscheiden (Pflicht)

Zwei Optionen:

- **Variante A (empfohlen im Review-Plan):** Eine interne Arbeits-Version `docs/plans/rollout-plan.md` auf Germans Level (mit echten Risiken, Alternativen, Open Questions), und eine abgeleitete Silvio-Version `docs/silvio-derivatives/rollout-vorschlag.md` für den Fall, dass Silvio es lesen soll.
- **Variante B:** Nur die interne Version. Silvio-Version entsteht ad-hoc wenn gebraucht.

**Empfehlung an German:** Variante B starten, weil weniger Parallelarbeit. Ableitung erst erzeugen, wenn sie konkret gebraucht wird. Das bleibt lean.

**Entscheidung via `AskUserQuestion`** am Anfang des Blocks.

### 2c — Neuer Ordner `docs/silvio-derivatives/` (nur bei Variante A)

Falls Variante A gewählt wird: Ordner anlegen, README darin mit dem Leitsatz *"nicht überreden, nicht verkaufen, nicht drängen"* als Tone-Anker.

### 2d — Business-Case-Docs (19 Stück) — Spot-Check, kein Rewrite (Optional)

Die 19 Original-Docs waren bereits arbeits-nah strukturiert. Review, ob in einzelnen Passagen Silvio-Empfindlichkeits-Rücksicht dazu geführt hat, dass Substanz verloren ging. Falls ja: nachziehen. Falls nein: nichts tun. Kein flächendeckender Rewrite.

**Zeitbudget:** Höchstens 30 Minuten. Wenn mehr nötig wäre, als Einzel-Task flaggen, nicht in dieser Session mit rein.

### 2e — Persona-Files Spot-Check (Optional)

Die 9 Review-Personas sind Analyse-Linsen, keine Silvio-facing Texte — sollten bereits auf Germans Level sein. Spot-Check erwartet: keine Überarbeitung.

### 2f — Memory `feedback_readme_is_customer_facing.md` aktualisieren (Pflicht)

Die Memory muss den neuen Stand widerspiegeln: README ist standardmäßig Germans Arbeits-README. Silvio-Version entsteht als explizite Ableitung, wenn gebraucht. Die alte Memory-Formulierung "README = Silvios Seite" wird ersetzt oder ergänzt.

## Start-Frage an German

Am Anfang der Session via `AskUserQuestion`:

- *Variante A (zwei Versionen) oder B (nur interne Version)?*
- *Willst du in dieser Session auch `docs/beteiligung.md` Dimensionen befüllen, oder bleibt das ein eigener Block?*

## Offene Punkte aus Session 2b (keine Blocker)

| # | Punkt | Owner | Wann |
|---|---|---|---|
| 1 | `docs/beteiligung.md` Dimensionen 1–4 und vier Vor-Fragen | German | Eigener ruhiger Arbeits-Block, nicht unter Zeitdruck |
| 2 | Maßnahme 2 — diese Session | German + Claude | Jetzt |
| 3 | Stufe-3 Deep Review der 19 Docs | Nach Maßnahme 2 | Backlog |

Operative Silvio-Blocker (MwSt, Vetamt, Nachname, Metro) bleiben unverändert offen bei Silvio.

## Wichtige Präferenzen von German (aus Memories + Session 2b)

- **Ton für interne Arbeits-Dokumente (Default nach D-06):** präzise, direkt, pointiert. Fach-Sprache erlaubt. Keine Consulting-Pose, keine Überförmlichkeit. Echte Risiko-Analyse ohne Silvio-Empfindlichkeits-Rücksicht.
- **Ton für Silvio-Ableitungen (wenn sie entstehen):** einfache Sätze, keine Anglizismen, kein Jargon ohne Erklärung, tentativ, warm, Freundschaft statt Kunde. Leitsatz: "nicht überreden, nicht verkaufen, nicht drängen."
- **Pushback bleibt Pflicht.** Session 2b hat z.B. vom Review-Plan abgewichen, wo das bestehende decisions.md-Schema in `session-handoff.md` sinnvoller war. Das ist richtig so.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Keine Marcello-Persona** (D-03), keine Easter Eggs (D-05).

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 2b hat drei Review-Maßnahmen abgeschlossen (decisions.md D-01 bis D-08, Phase A/B/C + Prozess-Fixes, beteiligung.md-Gerüst). Session 3 startet mit Maßnahme 2 — Repo-Zweck-Umschwung. Zwei Entscheidungen bevor ich anfange: (a) rollout-plan als Variante A (zwei Versionen) oder B (nur interne Version)? Ich empfehle B. (b) Soll `docs/beteiligung.md` heute mit befüllt werden, oder bleibt das ein eigener Block?"

Dann warte auf Germans Antwort und fang entsprechend an.

---

*Ende des Session-Prompts.*
