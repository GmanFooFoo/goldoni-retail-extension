# Inconsistencies zwischen Dokumenten

Widersprüche, die **zwischen** Original-Dokumenten auftreten. Laufend
aktualisiert während der Review-Phase.

## Status: Arbeitshypothesen aus MASCHIN-Voranalyse + Session-3-Spot-Check + Deep-Review

Werden in Stufe 3 (Deep Review) von den jeweiligen Rollen validiert. Einträge 1 und 3 wurden in Session 3 erweitert, nachdem der neue Rollout-Plan (`docs/plans/rollout-plan.md`, Gate-basiert, 10–12 Wochen) und D-02 (Phase 1 = nur Vakuum gekühlt) in Kraft traten. Eintrag 6 ist aus dem Spot-Check, Eintrag 7 aus dem Doc-03-Lead-Review (Session 4), Einträge 5 (Präzisierung) und 8 aus dem Doc-15-Lead-Review (Session 5).

| # | Widerspruch | Doc A | Doc B | Wer klärt |
|---|---|---|---|---|
| 1 | **Rollout-Dauer:** 6 Wochen (Doc 13), 8 Wochen (Doc 10) und 10–12 Wochen (neuer `rollout-plan.md`, Gate-basiert) | Doc 13, Doc 10 | `docs/plans/rollout-plan.md` (Gate-Logik) | CFO + Lebensmittelrecht |
| 2 | **Launch-Mengen:** 25–30 vs konservativ 20 | Doc 13 (25–30/Woche) | Doc 02 (20/Woche) | CFO |
| 3 | **Scope:** Vakuum + Tiefkühl gleichzeitig (v1) vs Phase 1 nur Vakuum gekühlt (D-02) | Doc 01, 02, 05 (MHD-Tabelle Tiefkühl-Spalte), 12, 13, 15 (Einordnungstabelle Tiefkühl-Zeile), 17, 18, 19 | D-02 in `docs/findings/decisions.md` | Cross-Review durch CFO, Lebensmittelrecht, Küche — mit Scope-Rewrite-Plan |
| 4 | **Name:** "Marco Antonelli" (Mockup) vs Silvio (echt) | Doc 06 | alle anderen | Silvio (echter Name + Adresse) |
| 5 | ~~**MwSt-Einordnung nicht prüfungsfest:** 7 % vs. 19 % offen.~~ **Aufgelöst durch Steueränderungsgesetz 2025 (Bundestag 04.12.2025, Inkrafttreten 01.01.2026): 7 %-Umsatzsteuer auf Speisen in der Gastronomie dauerhaft, gilt auch für Retail-Mitnahme.** Damit ist das Gate nach Rollout-Schritt 1 für die reine MwSt-Frage gesetzlich erledigt; verbindliche Auskunft nach § 89 AO nicht mehr nötig. Silvio-Verifikation beim nächsten Steuerberater-Kontakt als Routine-Check. | Doc 02, Doc 07, Doc 15 | [Nachtrag im Doc-15-Review](../reviews/15-steuer-steuerberaterin.md), Persona-10-Regulatorik-Scout | Aufgelöst, Silvio-Verifikation offen |
| 6 | **Pilot-Pflicht:** neuer Plan verlangt Pilot als Gate vor Launch; Doc 13 sieht keinen expliziten Gate-Pilot, sondern "Soft-Launch" in Woche 5 parallel zur Launch-Vorbereitung | Doc 13 | `docs/plans/rollout-plan.md` (Schritt 6 als Pflicht-Gate) | Gastronom-Rolle + CFO |
| 7 | **MHD-Validierung:** Doc 03 sagt "Fachliteratur oder eigene Tests" — ohne Protokoll. Doc 05 listet konkrete MHD-Werte (Lasagne 7 Tage, Ragù 8 Tage) als Schätzung, nicht validiert. Doc 04 (LMIV) setzt validierte MHDs implizit voraus, ohne den Validierungs-Pfad zu benennen. Listeria-Risiko bei Béchamel + Vakuum + Kühlung. Haftungs-Quelle nach § 58 LFGB. | Doc 03, 04, 05 | Persona-Red-Flag Lebensmittelrechtler, [Finding 3 Doc 03](03-findings.md#findings-tabelle), [Finding 2 Doc 05](05-findings.md#findings-tabelle) | Lebensmittelrechtler + Küche (Test-Protokoll) oder akkreditiertes Labor |
| 8 | **Netto/Brutto nirgends fixiert:** Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) erwähnen MwSt nicht und sagen nicht, ob die genannten Preise netto oder brutto sind. Durch die 7 %-Auflösung von #5 hat der Punkt an Schärfe verloren, bleibt aber gültig, weil eine Marge-Rechnung ohne Netto/Brutto-Flag weiterhin unpräzise ist — nur der worst-case-Spread (bis zu 16 Prozentpunkte bei 19 %) ist weggefallen und durch einen kleinen 6,5-Prozent-Spread ersetzt. | Doc 02, Doc 07 | Doc 15, [Finding 2 Doc 15](15-findings.md#findings-tabelle), Persona-Red-Flag Steuerberaterin | Steuerberaterin + CFO (Cross-Review) |

## Format pro Eintrag

Wenn ein Eintrag hier "zugewiesen" wird, wird er mit folgender Struktur erweitert:

```markdown
### #X — [Kurzname]

**Doc A sagt:** ...
**Doc B sagt:** ...
**Warum ist das ein Problem?** ...
**Auflösung:** ...
**Wer hat es geklärt:** [Persona oder User]
**Status:** Offen / In Klärung / Aufgelöst
```
