# Session-Prompt für Session 5 — Goldoni Retail Extension

> Handoff von Session 4 (2026-04-11 Nacht) an Session 5. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 4 hat den **Stufe-3 Deep Review gestartet**. Gate-kritische Sequenz fixiert: 03 → 15 → 05 → 04 → 14. Doc 03 Vetamt ist Lead-reviewt durch den Lebensmittelrechtler, 12 Findings konsolidiert in drei Auflösungs-Gruppen, v2-Plan-Skizze geschrieben, Cross-Drift #7 (MHD-Validierung) in `inconsistencies.md` nachgezogen.

**Doc 03 Urteil:** Rework erforderlich. Drei Pflicht-Bausteine fehlen (Rückruf-Prozess, HACCP-Beauftragter-Benennung, Tagesprotokolle), Timings und Gebühren nicht belastbar, Rework-Szenario bei Erstbegehung fehlt. Keine Stopp-Bedingung — die Grundrichtung stimmt.

**Commits Session 4:** `563d64b`, `5a02643`, `717e64b`, plus Session-Close-Commit.

**Offen außerhalb des Repos:** Gruppe-A-Aktionen für Silvio — zwei Telefonate (Vetamt Stuttgart + IHK Gastronomie-Erstberatung). Billig, schnell, klären vier Findings auf einen Schlag. Ergebnisse können asynchron als [TBD-Silvio]-Nachträge im v2-Plan landen, ohne eine Session zu binden.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-11-goldoni-d.md` — Session 4 Close mit Lessons und Commit-Log.
2. `docs/reviews/03-vetamt-lebensmittelrechtler.md` — der Lead-Review. Ist der Maßstab, gegen den der Co-Review (Variante A) gelesen wird.
3. `docs/findings/03-findings.md` — 12 Findings in drei Gruppen. Grundlage für jede weitere Doc-03-Arbeit.
4. `docs/plans/03-v2-plan.md` — v2-Plan-Skizze. Zeigt, welche Strukturänderungen in Doc 03 v2 eingebaut werden, sobald Silvios Anrufe durch sind.
5. `docs/findings/inconsistencies.md` — jetzt sieben Einträge, #7 MHD-Validierung neu.
6. `docs/findings/decisions.md` — D-01 bis D-08, besonders D-01 (Phase 1 Vakuum), D-06 (Arbeits-Level), D-08 (Phasen).
7. `docs/plans/rollout-plan.md` — der Gate-Maßstab.
8. `docs/personas/assignments.md` — Lead/Co-Matrix. Co für Doc 03: Behördenkontrolleur. Lead für Doc 15: Steuerberaterin (Co: CFO).
9. `CLAUDE.md` — Review-Standard-Format.
10. `session-state.md` — Stand nach Session 4.

## Session-5-Auftrag — drei Varianten, German entscheidet via AskUserQuestion

### Variante A — Co-Review Doc 03 durch Behördenkontrolleur

Parallel-Review zum Lead-Review aus Session 4. Der Behördenkontrolleur ist in `assignments.md` als Co hinterlegt und hat eine adversariale Perspektive (Persona 04 — "Behördenkontrolleur adversarial"). Er fragt: *Was würde ein Inspektor bei der Erstbegehung als erstes beanstanden?* Findet typischerweise andere Schwachstellen als der Jurist — operative Lücken statt rechtliche. Ergebnis: `docs/reviews/03-vetamt-behoerdenkontrolleur.md` im Standard-Format. Anschließend ggf. `03-findings.md` um Co-Findings erweitern.

**Effort:** S–M (1 Stunde bis halber Tag je nach Tiefe).

**Stop-Punkt:** Nach Co-Review committed. Keine weitere Arbeit an Doc 03 in Session 5.

### Variante B — Doc 15 Steuerliche Behandlung Lead-Review

Nächster Schritt in der Gate-kritischen Sequenz. Lead: Steuerberaterin (Persona 03). Co: CFO. Ausgangslage: Die MwSt-Frage (7 % oder 19 %) ist in `inconsistencies.md` als Eintrag #5 offen und gleichzeitig als Gate nach Rollout-Schritt 1 im `rollout-plan.md` definiert — also ein echter Pfad-Blocker für die Preis-Kalkulation. Ergebnis: `docs/reviews/15-steuer-steuerberaterin.md` plus `docs/findings/15-findings.md`, gleiche Struktur wie Doc 03.

**Effort:** M (halber Tag), wenn mit der gleichen Tiefe wie Doc 03.

**Stop-Punkt:** Nach Findings committed. v2-Plan-Skizze optional.

### Variante C — Silvio-Aktionen auslösen statt reviewen

Kein Review, sondern die Gruppe-A-Aktionen konkret auslösen: Briefing-Notiz für Silvio schreiben, was er bei den beiden Telefonaten (Vetamt + IHK) abfragen soll, in Form einer kurzen Sprech-Hilfe in `docs/silvio-derivatives/03-vetamt-briefing.md` (der Ordner wird bei dieser Gelegenheit angelegt). Erste echte Silvio-Ableitung seit D-06, folgt damit dem Leitsatz *"nicht überreden, nicht verkaufen, nicht drängen"*. Silvio-freundlicher Ton, einfache Sätze, keine Anglizismen.

**Effort:** S (1–2 Stunden), weil die Inhalte aus `03-findings.md` Gruppe A direkt übernehmbar sind.

**Stop-Punkt:** Briefing fertig, committet, an German übergeben.

## Empfehlung für Session 5

**Variante B (Doc 15 Steuer Lead-Review)**, aus drei Gründen:

1. Die MwSt-Frage ist der härteste offene Gate-Blocker im Rollout-Plan (Schritt 1). Sie blockt alle Wirtschaftlichkeits-Arbeit dahinter — ohne Klarheit bleibt jede Preis-Kalkulation und Marge-Rechnung wackelig.
2. Der Co-Review Doc 03 (Variante A) bringt Inkrement, aber keinen neuen Gate-Fortschritt. Ein Co-Review rechtfertigt sich erst, wenn der Lead-Review ambivalent war — bei Doc 03 ist das Urteil klar (Rework). Zweite Perspektive ist wertvoll, aber nicht eilig.
3. Variante C ist ideal asynchron (nicht-Session), weil die Silvio-Anrufe von Silvio gemacht werden, nicht von Claude. German kann die Briefing-Notiz selbst in 30 Minuten schreiben, ohne eine Session dafür zu binden — oder in eine Session einbauen, wenn Doc 15 schneller fertig ist als erwartet.

**Wenn Gruppe A aber dringlich wird (Silvio fragt nach), dann Variante C priorisieren.** Sie ist die einzige, die das Projekt *außerhalb* des Repos voranbringt.

## Start-Frage an German

Via `AskUserQuestion` am Anfang der Session:

- *Variante A (Co-Review Doc 03), Variante B (Doc 15 Steuer Lead-Review, Empfehlung) oder Variante C (Silvio-Briefing für Gruppe-A-Anrufe)?*

## Offene Punkte aus Session 4 und früher — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | Personas tragen noch Namen im Filename und Body. Memory: nur Rollen. | Eigener XS-Task. Kann in einen beliebigen Review-Warmup eingebaut werden. |
| 2 | Doc 01 nennt Tiefkühl in Phase 1 (widerspricht D-01). | Beim Doc-01-Review oder als XS-Einzel-Fix. |
| 3 | `docs/silvio-derivatives/` existiert nicht. Wird in Variante C angelegt, sonst bei erster Silvio-Ableitung. | On-demand |
| 4 | Gruppe-A-Silvio-Anrufe (Vetamt + IHK) ausstehend. Asynchron. | Kein Session-Block, eher Variante C als Briefing-Vorbereitung. |
| 5 | Co-Review Doc 03 (Behördenkontrolleur) ausstehend. | Variante A in Session 5 oder später. |
| 6 | Gruppe-B-Pflicht-Dokumente (Rückruf, HACCP-Beauftragter, Tagesprotokolle, Rückstellproben) entstehen im HACCP- und Recht-Review. | Session mit Doc 05 und Doc 14. |
| 7 | Deep Review Stufe 3 bleibt XL. Realistisch: ein Lead-Review pro Session plus Findings. | Dauerthema |

## Wichtige Präferenzen von German (Erinnerung)

- **Ton interne Arbeits-Docs (D-06):** präzise, direkt, Fach-Sprache erlaubt.
- **Ton Silvio-Ableitungen (Variante C):** einfache Sätze, keine Anglizismen, tentativ, warm, *"nicht überreden, nicht verkaufen, nicht drängen"*.
- **Pushback Pflicht.**
- **Review-Standard-Format** aus `CLAUDE.md`.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Personas als Rollen** (Files noch mit Namen, das ist offene Drift).
- **Commit nach jedem Work-Block.**
- **Plan-Mode** hat sich in Session 4 bewährt — bei neuen XL-Blöcken wieder sinnvoll.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 4 hat den Stufe-3 Deep Review gestartet. Doc 03 Vetamt: Lead-Review fertig (Rework erforderlich), 12 Findings in drei Gruppen, v2-Plan-Skizze da, Cross-Drift #7 MHD nachgezogen. Session 5 hat drei Varianten: (A) Co-Review Doc 03 durch Behördenkontrolleur. (B) Doc 15 Steuer Lead-Review — empfohlen, weil MwSt-Gate den Pfad hinter Rollout-Schritt 1 blockt. (C) Silvio-Briefing Gruppe A als erste Silvio-Ableitung. Welcher Pfad?"

Dann auf Germans Antwort warten und entsprechend starten.

---

*Ende des Session-Prompts.*
