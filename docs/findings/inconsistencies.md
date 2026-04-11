# Inconsistencies zwischen Dokumenten

Widersprüche, die **zwischen** Original-Dokumenten auftreten. Laufend
aktualisiert während der Review-Phase.

## Status: Arbeitshypothesen aus MASCHIN-Voranalyse + Session-3-Spot-Check

Werden in Stufe 3 (Deep Review) von den jeweiligen Rollen validiert. Einträge 1 und 3 wurden in Session 3 erweitert, nachdem der neue Rollout-Plan (`docs/plans/rollout-plan.md`, Gate-basiert, 10–12 Wochen) und D-02 (Phase 1 = nur Vakuum gekühlt) in Kraft traten. Eintrag 6 ist neu aus dem Spot-Check.

| # | Widerspruch | Doc A | Doc B | Wer klärt |
|---|---|---|---|---|
| 1 | **Rollout-Dauer:** 6 Wochen (Doc 13), 8 Wochen (Doc 10) und 10–12 Wochen (neuer `rollout-plan.md`, Gate-basiert) | Doc 13, Doc 10 | `docs/plans/rollout-plan.md` (Gate-Logik) | CFO + Lebensmittelrecht |
| 2 | **Launch-Mengen:** 25–30 vs konservativ 20 | Doc 13 (25–30/Woche) | Doc 02 (20/Woche) | CFO |
| 3 | **Scope:** Vakuum + Tiefkühl gleichzeitig (v1) vs Phase 1 nur Vakuum gekühlt (D-02) | Doc 01, 02, 05, 12, 13, 17, 18, 19 | D-02 in `docs/findings/decisions.md` | Cross-Review durch CFO, Lebensmittelrecht, Küche — mit Scope-Rewrite-Plan |
| 4 | **Name:** "Marco Antonelli" (Mockup) vs Silvio (echt) | Doc 06 | alle anderen | Silvio (echter Name + Adresse) |
| 5 | **MwSt:** 7 % oder 19 %? | Doc 02 (implizit 7 %) | Doc 15 (offen) | Steuer-Rolle + Silvios Steuerberater |
| 6 | **Pilot-Pflicht:** neuer Plan verlangt Pilot als Gate vor Launch; Doc 13 sieht keinen expliziten Gate-Pilot, sondern "Soft-Launch" in Woche 5 parallel zur Launch-Vorbereitung | Doc 13 | `docs/plans/rollout-plan.md` (Schritt 6 als Pflicht-Gate) | Gastronom-Rolle + CFO |
| 7 | **MHD-Validierung:** Doc 03 sagt "Fachliteratur oder eigene Tests" — ohne Protokoll. Doc 04 (LMIV) und Doc 05 (HACCP) setzen validierte MHDs implizit voraus, ohne den Validierungs-Pfad zu benennen. Haftungs-Quelle nach § 58 LFGB. | Doc 03, 04, 05 | Persona-Red-Flag Lebensmittelrechtler, [Finding 3 Doc 03](03-findings.md#findings-tabelle) | Lebensmittelrechtler + Küche (Test-Protokoll) oder Labor |

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
