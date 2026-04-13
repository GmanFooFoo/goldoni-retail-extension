# Findings: Doc 13 – 6-Wochen-Rollout-Plan

**Quelle:** [Lead-Review CFO](../reviews/13-rollout-cfo.md)
**Datum:** 2026-04-13
**Status:** **Stopp** — erste Stopp-Bewertung vom CFO. v2 muss sich an `docs/plans/rollout-plan.md` (10–12 Wochen, Gate-basiert) orientieren.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **6-Wochen-Timeline unrealistisch.** Vetamt 2–4 Wochen, Geräte 2–6 Wochen, Labor 2–3 Wochen. Realistisch: 10–12 Wochen. Widerspricht `rollout-plan.md`. | P1 | M | CFO + Lebensmittelrechtler + Gastronom | — | Offen | Falsches Timing erzeugt falsche Erwartungen bei Silvio. |
| 2 | **Kein Pilot-Gate.** Rollout-Plan hat explizites Gate nach Pilot (Schritt 6). Doc 13 geht von Soft-Launch direkt zu Launch. | P1 | S | CFO | — | Offen | Ohne Gate riskiert Silvio den Launch mit ungetesteten Produkten. |
| 3 | **Vetamt-Kontaktdaten falsch.** 0711 216-98670 → korrigiert 0711 21688590. "Luca-Portal" → service-bw.de. | P1 | XS | — | — | Offen | Silvio ruft die falsche Nummer an. |
| 4 | **fddb.info statt Labor.** Online-Nährwertrechner reicht nicht für Verkaufs-Etiketten. Musterwerte = sofortiger Ablehnungsgrund (Doc 04 Co-Review Behördenkontrolleur). Labor: SP-11. | P1 | XS | Lebensmittelrechtler | — | Offen | LMIV-Verstoß, Bußgeld-Risiko. |
| 5 | **Nur 2 Produkte (Lasagne + Ragù).** Doc 02 v2: 5 Produkte. Mindestens 3 zum Start (2× Lasagne + Sugo). | P2 | S | CFO + Küchenchef | — | Offen | Engeres Sortiment = weniger Testdaten aus Pilot. |
| 6 | **Fehlende Schritte.** Gewerbeanzeige, IfSG, Labor, Anwalt, Versicherung, Webshop fehlen komplett. | P1 | M | CFO | — | Offen | Plan ist unvollständig — Silvio vergisst kritische Schritte. |
| 7 | **Kein Budget pro Woche.** Aktivitäten ohne Kosten-Zuordnung. Verweis auf Doc 12 v2 Cashflow-Timing fehlt. | P2 | XS | CFO | — | Offen | Silvio weiß nicht, wann er wie viel Geld braucht. |
| 8 | **"Di Gennaro" unklar.** In Doc 11 nicht als Lieferant verifiziert. Etikett-Risiko (UWG, Inconsistency #13). | P3 | XS | Brand/Marketing | — | Offen | Klärung nötig: Lieferant, Marke, oder Fiktion? |
| 9 | **Canva für Etikett.** Nicht falsch, aber suggeriert kreativen statt regulatorischen Prozess. Muss gegen LMIV-Checkliste (Doc 04 v2) validiert werden. | P3 | XS | Lebensmittelrechtler | — | Offen | Kosmetisch, aber Tonalitäts-Problem: Etikett ist Pflicht, kein Design-Projekt. |

## Nächste Schritte

1. [ ] v2-Rewrite: `docs/plans/rollout-plan.md` als Basis nehmen, Wochentags-Granularität auf 10–12 Wochen verteilen, alle fehlenden Schritte ergänzen, Budget pro Phase zuordnen.
2. [ ] Co-Reviews: Lebensmittelrechtler (Regulatory), Thomas Gastronom (Praxis), Bruno Logistiker (Geräte-Timing), Persona 11 (Personal-Meilensteine).
