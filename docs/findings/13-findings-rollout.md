# Findings: Doc 13 – 6-Wochen-Rollout-Plan

**Quelle:** [Lead-Review CFO](../reviews/13-rollout-cfo.md)
**Datum:** 2026-04-13
**Status:** **Alle 17 Findings adressiert in v2** (2026-04-13, Session 14). CFO-Stopp aufgelöst: v2 basiert auf `docs/plans/rollout-plan.md` (10–12 Wochen, Gate-basiert). **17 Findings** (9 Lead + 4 Co Thomas + 4 Co Dr. Steiger).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **6-Wochen-Timeline unrealistisch.** Vetamt 2–4 Wochen, Geräte 2–6 Wochen, Labor 2–3 Wochen. Realistisch: 10–12 Wochen. Widerspricht `rollout-plan.md`. | P1 | M | CFO + Lebensmittelrechtler + Gastronom | — | ✅ v2 | Falsches Timing erzeugt falsche Erwartungen bei Silvio. |
| 2 | **Kein Pilot-Gate.** Rollout-Plan hat explizites Gate nach Pilot (Schritt 6). Doc 13 geht von Soft-Launch direkt zu Launch. | P1 | S | CFO | — | ✅ v2 | Ohne Gate riskiert Silvio den Launch mit ungetesteten Produkten. |
| 3 | **Vetamt-Kontaktdaten falsch.** 0711 216-98670 → korrigiert 0711 21688590. "Luca-Portal" → service-bw.de. | P1 | XS | — | — | ✅ v2 | Silvio ruft die falsche Nummer an. |
| 4 | **fddb.info statt Labor.** Online-Nährwertrechner reicht nicht für Verkaufs-Etiketten. Musterwerte = sofortiger Ablehnungsgrund (Doc 04 Co-Review Behördenkontrolleur). Labor: SP-11. | P1 | XS | Lebensmittelrechtler | — | ✅ v2 | LMIV-Verstoß, Bußgeld-Risiko. |
| 5 | **Nur 2 Produkte (Lasagne + Ragù).** Doc 02 v2: 5 Produkte. Mindestens 3 zum Start (2× Lasagne + Sugo). | P2 | S | CFO + Küchenchef | — | ✅ v2 | Engeres Sortiment = weniger Testdaten aus Pilot. |
| 6 | **Fehlende Schritte.** Gewerbeanzeige, IfSG, Labor, Anwalt, Versicherung, Webshop fehlen komplett. | P1 | M | CFO | — | ✅ v2 | Plan ist unvollständig — Silvio vergisst kritische Schritte. |
| 7 | **Kein Budget pro Woche.** Aktivitäten ohne Kosten-Zuordnung. Verweis auf Doc 12 v2 Cashflow-Timing fehlt. | P2 | XS | CFO | — | ✅ v2 | Silvio weiß nicht, wann er wie viel Geld braucht. |
| 8 | **"Di Gennaro" unklar.** In Doc 11 nicht als Lieferant verifiziert. Etikett-Risiko (UWG, Inconsistency #13). | P3 | XS | Brand/Marketing | — | ✅ v2 | Klärung nötig: Lieferant, Marke, oder Fiktion? |
| 9 | **Canva für Etikett.** Nicht falsch, aber suggeriert kreativen statt regulatorischen Prozess. Muss gegen LMIV-Checkliste (Doc 04 v2) validiert werden. | P3 | XS | Lebensmittelrechtler | — | ✅ v2 | Kosmetisch, aber Tonalitäts-Problem: Etikett ist Pflicht, kein Design-Projekt. |
| 10 | **Parallele Streams-Risiko.** Vetamt, Equipment, Labor, Personal laufen gleichzeitig. Kein kritischer Pfad identifiziert — wenn einer hängt, verzögert sich alles. | P1 | S | Thomas CF-01 | CFO | ✅ v2 | Kritischer Pfad muss explizit definiert werden: Vetamt → Equipment → Testchargen → Labor → Launch. |
| 11 | **Haltbarkeitstest braucht Iterationen.** Eine Testrunde reicht nicht. Mindestens 2–3 Durchläufe pro Produkt bis MHD belastbar ist. Zeitplan: +2–3 Wochen. | P2 | S | Thomas CF-02 | Küchenchef | ✅ v2 | MHD ohne Iteration ist Schätzwert, kein Messwert. |
| 12 | **Pilot-Abbruchkriterien fehlen.** Wann wird der Pilot gestoppt? Kein Schwellenwert für Ausschuss, Reklamationen, Verderb definiert. | P1 | XS | Thomas CF-03 | CFO | ✅ v2 | Ohne Abbruchkriterien kein echtes Gate — nur ein Datum. |
| 13 | **Personal-Meilenstein fehlt.** Wenn Szenario B/C (Doc 20): Wann muss Silvio jemanden einstellen? Muss im Rollout-Plan als Meilenstein stehen. | P2 | XS | Thomas CF-04 | Persona 11 | ✅ v2 | Cross-Ref Doc 20. Personal-Entscheidung vor Pilot, nicht danach. |
| 14 | **Vetamt 4–8 Wochen realistisch.** CFO-Finding 1 sagt 2–4 Wochen, aber Erfahrungswert Stuttgart: eher 4–8 Wochen inkl. Nachforderungen. Puffer einplanen. | P1 | S | Dr. Steiger CF-01 | — | ✅ v2 | Timeline-Korrektur: Vetamt ist der längste Vorlauf-Posten. |
| 15 | **Labor 2–3 Wochen Durchlaufzeit.** Nährwert + Mikrobiologie zusammen: 2–3 Wochen ab Probeneingang. Muss vor Etikett-Druck abgeschlossen sein. | P2 | XS | Dr. Steiger CF-02 | — | ✅ v2 | Sequenz-Abhängigkeit: Labor → Etikett → Launch. |
| 16 | **Regulatorische Stichtage als Meilensteine.** Listerien-VO 1.7., PPWR 12.8.2026 — müssen als fixe Meilensteine im Rollout stehen, nicht nur in Doc 16. | P1 | XS | Dr. Steiger CF-03 | CFO | ✅ v2 | Launch vor/nach Stichtag ändert Compliance-Anforderungen. |
| 17 | **IfSG-Belehrung als Required Step.** § 43 IfSG für alle Personen mit Lebensmittelkontakt. Fehlt als Rollout-Schritt. Gesundheitsamt Stuttgart: Termin 2–4 Wochen Vorlauf. | P1 | XS | Dr. Steiger CF-04 | — | ✅ v2 | Ohne IfSG kein legaler Produktionsstart. Cross-Ref Doc 13 Finding 6 (fehlende Schritte). |

## Nächste Schritte

1. [x] v2-Rewrite: 10–12 Wochen, 4 Phasen, gate-basiert, alle fehlenden Schritte, Budget pro Phase, Mermaid-Gantt, Pilot-Abbruchkriterien. Erledigt in Session 14.
2. [ ] Co-Reviews ausstehend: Bruno Logistiker (Geräte-Timing), Persona 11 (Personal-Meilensteine). Thomas + Dr. Steiger eingeflossen.
