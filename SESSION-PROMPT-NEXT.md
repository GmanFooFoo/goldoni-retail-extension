# Session-Prompt für Session 6 — Goldoni Retail Extension

> Handoff von Session 5 (2026-04-11) an Session 6. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 5 hat zwei große Dinge geleistet: (1) **Doc 15 Steuer und Doc 05 HACCP lead-reviewt** — beide Rework — und die Findings in den gleichen A/B/C-Gruppen strukturiert wie Doc 03. (2) **Ein strukturelles Problem entdeckt und gefixt:** Mein Knowledge-Cutoff ist Mai 2025, aber das Steueränderungsgesetz 2025 wurde am 4. Dezember 2025 beschlossen und senkt seit 1. Januar 2026 die Umsatzsteuer auf Speisen in der Gastronomie dauerhaft auf 7 %. Das löst den MwSt-Gate nach Rollout-Schritt 1 gesetzlich auf und macht einen großen Teil des Doc-15-Kernbefunds hinfällig. Als Reaktion wurde **Persona 10 Dr. Maldini** (Fachanwalt für Gastronomie/Food/Tech als horizontaler Regulatorik-Scout) angelegt plus **CLAUDE.md Rule 9**, die vor jedem Lead-Review eines Legal/Tax/Tech-Docs eine aktive WebSearch auf den aktuellen Stand der Rechtsgebiete erzwingt.

Außerdem **Persona 00 Silvio** als horizontale Übersetzungs-Schicht für die spätere Silvio-Kommunikation (nach Abschluss der Expert-Reviews). Außerdem Persona-Hygiene (Hard-Wraps gefixt, Claudia als Mutter mit Lieferservice-Alltag präzisiert) und Doc 03 Vetamt-Adresse und IHK-Kontakt präzisiert.

**Sequenz-Status:** 03 ✓ 15 ✓ 05 ✓ — **Doc 04 LMIV** und **Doc 14 Recht** stehen in der Gate-kritischen Sequenz noch aus.

**Commits Session 5:** 096e571, 8e79394, 5bf4db7, 739c1b9, 7d0ced9, 7f97add, 61bce53, 480a9ca, c8406de, 15fb7c3, acf708d, 5c98350, 4e4ca61, 7c5d06d.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-11-goldoni-e.md` — Session 5 Close mit Lessons, Commit-Log und der strukturellen Begründung für Persona 10 und Rule 9.
2. `CLAUDE.md` — **Rule 9 Regulatorik-Aktualität** ist neu und direkt relevant für Session 6, weil Doc 04 LMIV ein Legal-Doc ist.
3. `docs/personas/Persona 10 – Dr. Maldini – Fachanwalt Gastro Food Tech.md` — die neue Persona und das Nachtrag-Template.
4. `docs/personas/Persona 00 – Silvio – Der Gastronom.md` — die Übersetzungs-Schicht, die Session 6 nicht aktivieren muss, aber im Hinterkopf halten.
5. `docs/reviews/15-steuer-steuerberaterin.md` — besonders der Nachtrag, als Muster für den Umgang mit aufgelösten Findings per Strike-through.
6. `docs/findings/15-findings.md` und `05-findings.md` — die zweite und dritte Findings-Datei, als Vorlage für das Doc-04-Findings-Dokument.
7. `docs/findings/inconsistencies.md` — Einträge #3, #5 (aufgelöst), #7, #8 sind in Session 5 bewegt worden.
8. `docs/plans/rollout-plan.md` — Gate 1 aufgelöst, Offene-Annahme MwSt aufgelöst. Der Plan ist ein Stück leichter geworden.
9. `docs/findings/decisions.md` — D-01 bis D-08 unverändert.
10. `docs/personas/assignments.md` — Doc 04 LMIV: Lead Dr. Steiger, Co Inspektor Vogel + Pietro + **Dr. Maldini (neu, horizontal)**.
11. `session-state.md` — Stand nach Session 5.

## Session-6-Auftrag — drei Varianten, German entscheidet via AskUserQuestion

### Variante A — Doc 04 LMIV Lead-Review mit Dr. Maldini als erstem Lackmustest (Recommended)

Doc 04 ist das nächste Doc in der Gate-kritischen Sequenz und gleichzeitig das erste Doc, an dem die neue Rule 9 in der Praxis laufen muss. Lead: Dr. Steiger (Lebensmittelrechtler). Co: Pietro (Küchenchef), Inspektor Vogel (Behörde), **Dr. Maldini als horizontaler Regulatorik-Scout**.

**Ablauf als Block-Kette:**

1. **Rule 9 ausführen:** Aktive WebSearch auf LMIV-Änderungen 2025/2026, EU-Verordnung 1169/2011 Novellen, nationale LMIV-Durchführungsgesetze, aktuelle Gerichtsurteile zu Allergenkennzeichnung, Herkunftsangaben, Nährwert-Toleranzen. Quellen-Priorität: bundestag.de, bmel.de, EUR-Lex, BVL, Lebensmittelverband, IHK.
2. **Regulatorik-Nachtrag** im Kopf des Doc-04-Reviews schreiben, nach dem Template aus Persona 10.
3. **Lead-Review** schreiben im Standard-Format, mit dem Regulatorik-Nachtrag als erstem Abschnitt nach Metadaten.
4. **Findings konsolidieren** in `docs/findings/04-findings.md` mit A/B/C-Gruppen, analog 03/15/05.
5. **Cross-Drift** in `inconsistencies.md` nachziehen, besonders #7 (MHD-Validierung) und neue Einträge falls gefunden.
6. **Commit pro Work-Block.**

**Effort:** M (halber Tag), realistisch länger wenn die Regulatorik-Recherche Fundstellen produziert.

**Stop-Punkt:** Nach Findings committed.

### Variante B — Rückwirkender Regulatorik-Scan auf Doc 03 und Doc 05

Dr. Maldini existierte bei den Doc-03- und Doc-05-Reviews noch nicht. Beide Reviews sind damit aus Rule-9-Sicht "unbeschrieben" — es gibt keine Aktualitäts-Prüfung. Session 6 könnte diese Lücke schließen, bevor die Sequenz weiterläuft.

**Ablauf:**

1. WebSearch für Doc 03 Vetamt: laufende Änderungen an VO 852/2004, aktuelle LMHV-Novellen, § 4 LMHV Schulungs-Anforderungen, IfSG § 42/43 Änderungen 2025/2026, Stuttgart-spezifische Verwaltungs-Anpassungen.
2. WebSearch für Doc 05 HACCP: aktuelle HACCP-Leitlinien-Updates, Codex-Alimentarius-Änderungen, Listerien-Risiko-Empfehlungen BfR/EFSA, aktuelle Urteile zu § 58 LFGB bei MHD.
3. Regulatorik-Nachträge in beide Review-Dateien einfügen.
4. Bei Findings: die bestehenden findings-Dateien erweitern, nicht parallel neue anlegen.

**Effort:** S–M (1 Stunde bis halber Tag).

**Stop-Punkt:** Nach den Nachträgen committed.

**Vorteil:** Konsolidierung vor dem nächsten Fortschritt. **Nachteil:** Kein Gate-Fortschritt auf der Sequenz.

### Variante C — Silvio-Paket 1 konsolidieren (Briefing-Notiz)

Die drei Silvio-Pakete (Vetamt/IHK, Steuer/Kasse/Gewerbeamt — ohne MwSt-Briefing, IfSG/Schädlinge/HACCP-Benennung) sind beschrieben, aber nicht in ein silvio-facing Dokument gegossen. Persona 00 wäre dafür die richtige Brille. Output in `docs/silvio-derivatives/silvio-paket-1-anrufe-und-termine.md`.

**Effort:** S (1–2 Stunden), weil der Inhalt aus den Gruppe-A-Findings direkt übernehmbar ist und die Übersetzung in Silvios Ton die eigentliche Arbeit ist.

**Stop-Punkt:** Silvio-Ableitung committet, an German übergeben.

**Vorteil:** Erste echte Silvio-Ableitung, erster Praxis-Test für Persona 00. **Nachteil:** Kein Review-Fortschritt.

## Empfehlung für Session 6

**Variante A (Doc 04 LMIV Lead-Review mit Rule 9)**, aus drei Gründen:

1. Doc 04 ist das nächste Gate-Doc, und es ist wichtig, dass Rule 9 von Anfang an greift, nicht erst bei Doc 14. Session 5 hat gezeigt, wie massiv eine verpasste Regulatorik-Änderung den Business-Case verschiebt — Doc 04 LMIV hat ähnliches Potential (Allergenkennzeichnung, E-Label, Herkunftsangaben werden in der EU laufend bewegt).
2. Variante B ist sinnvoll, aber nicht dringend. Die rückwirkenden Regulatorik-Scans auf Doc 03 und 05 können auch in einer kürzeren Session 7 oder als Vorspiel zu Doc 14 laufen.
3. Variante C wäre ein Sprung, der sich stilistisch lohnt, aber Session 6 sollte Substanz liefern, nicht Stilübung. Silvio-Paket 1 wird sinnvoller, wenn Doc 04 auch durch ist und wir vier statt drei Expert-Reviews im Rücken haben.

**Wenn aber die rückwirkende Lücke aus Rule-9-Hygiene-Gründen dringlich wird, Variante B priorisieren.**

## Start-Frage an German

Via `AskUserQuestion` am Anfang der Session: *Variante A (Doc 04 LMIV mit Dr. Maldini — Empfehlung), Variante B (rückwirkender Regulatorik-Scan Doc 03 + 05) oder Variante C (Silvio-Paket 1 Briefing-Notiz)?*

## Offene Punkte aus Session 5 — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | Silvio-Verifikation 7 %-USt beim nächsten Steuerberater-Kontakt — Routine-Check, kein Gate | On-demand |
| 2 | Vetamt-Umzug Schlossstraße — Silvio fragt beim Erstkontakt nach | On-demand |
| 3 | Rückwirkender Regulatorik-Scan Doc 03 und Doc 05 (Variante B) | Spätestens vor v2-Rewrite |
| 4 | Silvio-Paket 1 als Briefing-Notiz (Variante C) | Wenn Doc 04 und Doc 14 durch sind |
| 5 | Co-Reviews Doc 03/15/05 (Behördenkontrolleur, CFO, Küche/Logistik/Behörde) | Nach Abschluss der Gate-kritischen Sequenz |
| 6 | Gruppe-B-Pflicht-Dokumente (Rückruf, HACCP-Beauftragter, Tagesprotokolle, Rückstellproben) entstehen im HACCP- und Recht-Review — Schreibort klärt sich beim Doc-14-Review | Doc 14 |
| 7 | Deep Review Stufe 3 bleibt XL. Realistisch: ein Lead-Review pro Session plus Findings plus ggf. Regulatorik-Nachtrag | Dauerthema |

## Wichtige Präferenzen von German (Erinnerung)

- **Ton interne Arbeits-Docs (D-06):** präzise, direkt, Fach-Sprache erlaubt.
- **Ton Silvio-Ableitungen (Variante C):** einfache Sätze, keine Anglizismen, tentativ, warm, *"nicht überreden, nicht verkaufen, nicht drängen"*.
- **Pushback Pflicht.**
- **Review-Standard-Format** aus `CLAUDE.md`.
- **Rule 9 Regulatorik-Scan** ist neu — **nicht vergessen**, bevor ein Lead-Review eines Legal/Tax/Tech-Docs geschrieben wird.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Commit nach jedem Work-Block.**
- **Session-Session-Regel:** Genau ein Schreibender pro Repo gleichzeitig. Vor Session-Start `session-state.md` prüfen.
- **Strike-through statt Löschen** bei aufgelösten Findings und Inconsistencies, damit die Historie nachvollziehbar bleibt.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 5 hat Doc 15 und Doc 05 lead-reviewt und strukturell zwei Dinge eingeführt: Persona 10 Dr. Maldini als Regulatorik-Scout und CLAUDE.md Rule 9, die vor Legal/Tax/Tech-Reviews eine aktive WebSearch erzwingt. Außerdem hat das 7%-USt-Finding den MwSt-Gate nach Rollout-Schritt 1 gesetzlich aufgelöst. Session 6 hat drei Varianten: (A) Doc 04 LMIV Lead-Review mit Dr. Maldini als erstem Lackmustest für Rule 9 — Empfehlung. (B) Rückwirkender Regulatorik-Scan auf Doc 03 und Doc 05, um die Lücke vor v2-Rewrites zu schließen. (C) Silvio-Paket 1 Briefing-Notiz als erste Silvio-Ableitung über Persona 00. Welcher Pfad?"
