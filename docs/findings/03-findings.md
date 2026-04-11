# Findings: Doc 03 – Veterinäramt Stuttgart

**Quelle:** [Lead-Review Lebensmittelrechtler](../reviews/03-vetamt-lebensmittelrechtler.md)
**Datum:** 2026-04-11
**Status:** In Klärung — Co-Review durch Behördenkontrolleur folgt in Session 5.

Konsolidierte Findings aus dem Lead-Review. Jedes Finding benennt den Auflösungs-Pfad und den Owner. Findings sind die Grundlage für den späteren v2-Plan (`docs/plans/03-v2-plan.md`) und für Cross-Drift-Einträge in `inconsistencies.md`.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Schriftlicher Rückruf-Prozess fehlt (Art. 19 VO 178/2002). Red Flag laut Persona, Stopp vor erstem Verkauf. | P1 | S | Lebensmittelrechtler (Lead) + Silvio (Benennung) | Pflicht vor Gate nach Schritt 2 | Offen | Blockiert Vetamt-Bescheid; ohne schriftlichen Rückruf gibt es keine Freigabe. |
| 2 | HACCP-Beauftragter namentlich benennen (Art. 5 VO 852/2004). | P1 | XS | Silvio (Selbstbenennung) | — | Offen | Pflichtfeld in der Vetamt-Unterlage; trivial, aber muss vor Einreichung dokumentiert sein. |
| 3 | MHD-Validierung ungeklärt — "Fachliteratur oder eigene Tests" ist zu weich. Haftungs-Quelle nach § 58 LFGB. | P1 | L | Lebensmittelrechtler + [TBD-Recherche Labor oder Haltbarkeits-Test-Protokoll] | Ja, Gate Schritt 2 und Gate Schritt 4 (Etiketten) | Offen | Ohne validiertes MHD kein LMIV-konformes Etikett, kein Verkauf, persönliche Haftung. |
| 4 | Timings fehlen (Erstkontakt → Bescheid). Realistischer Korridor: 3–8 Wochen. | P2 | XS | Silvio (Erstkontakt-Telefonat) | Ja, für Gate-Timing im Rollout-Plan | Offen | Ohne Timing ist der Rollout-Plan-Gate nach Schritt 2 nicht terminierbar. |
| 5 | Kosten / Gebühren fehlen (Registrierung, Erstbegehung, Nachbegehung, Laboranalyse). | P2 | XS | Silvio (Erstkontakt-Telefonat) + Cross-Ref Doc 04 (Labor) | — | Offen | Unbekannte Sunk-Cost-Komponente im Worst-Case-Budget 2.500–3.000 €. |
| 6 | "Onlineversand Grauzone" ist sachlich falsch (LMIV Art. 14 Fernabsatz klärt das). | P2 | XS | Lebensmittelrechtler (Korrektur) | — | Offen | Faktische Falschaussage im Doc; entweder korrigieren oder Onlineversand als "nicht in Phase 1" markieren (konsistent mit Rollout-Plan). |
| 7 | "ggf. über Luca-Portal" — Pflicht oder Option? | P2 | XS | Silvio (Erstkontakt) oder [TBD-Recherche] | — | Offen | Verfahrens-TBD; klärt sich mit Finding 4 im selben Telefonat. |
| 8 | Rework-Szenario bei Erstbegehung fehlt (Nachbesserungs-Frist, Zweitbegehung, Kosten). | P2 | S | Lebensmittelrechtler + Co-Review Behördenkontrolleur | — | Offen | Rollout-Plan-Risiko unterschätzt; die Wahrscheinlichkeit einer Beanstandung bei Erstbegehung ist nicht null. |
| 9 | Tagesprotokolle (Kühlkette, Reinigung, Produktion, Rückstellproben) nicht definiert. | P2 | M | Lebensmittelrechtler + Doc 05 HACCP (Cross-Ref) | — | Offen | Dokumentations-Pflicht nach LMHV § 5; Cross-Gate mit Doc 05. Wird im HACCP-Review (Schritt 3 der Sequenz) vertieft. |
| 10 | Rechtsgrundlagen unvollständig aufgeführt (es fehlen VO 178/2002, LFGB, § 42 IfSG, LMHV §§ 3–5). | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Reife-Problem, kein Gate-Problem. Löst sich im v2-Rewrite. |
| 11 | IHK-Erstberatung ist als "Empfehlung" weich formuliert; sollte Ablauf-Schritt 0 werden. | P3 | XS | Silvio (Termin buchen) | — | Offen | Billig, Risiko-Reduktion vor dem ersten Vetamt-Kontakt. |
| 12 | D-01-Konformität (Phase 1 nur Vakuum, kein Tiefkühl) nicht explizit im Doc-Kopf. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Konsistenz-Drift; verhindert Tiefkühl-Missverständnis bei Leser. |

## Auflösungs-Gruppen

Die 12 Findings zerfallen in drei natürliche Gruppen, die unterschiedliche Arbeits-Stränge auslösen.

**Gruppe A — Silvio-Aktionen (Erstkontakt-Telefonat):** Findings 4, 5, 7, 11. Ein Telefonat mit Stuttgart Vetamt plus eines mit der IHK Gastronomie-Erstberatung klärt vier von zwölf Findings auf. Empfehlung: Silvio macht beide Anrufe, bevor Session 5 Doc 15 (Steuer) reviewt.

**Gruppe B — Pflicht-Dokumente neu erstellen:** Findings 1, 2, 3, 9. Rückruf-Prozess, HACCP-Beauftragten-Benennung, MHD-Validierung, Tagesprotokolle. Diese gehören nicht in Doc 03, sondern in Doc 05 (HACCP) und Doc 14 (Recht). Doc 03 referenziert sie nur. MHD-Validierung hat den größten Aufwand (Labor-Test oder dokumentierter Haltbarkeits-Test mit mindestens drei Chargen über den geplanten MHD-Zeitraum) und wird zum eigenen Arbeits-Block.

**Gruppe C — Doc-Rewrite-Arbeit:** Findings 6, 8, 10, 12. Korrekturen und Ergänzungen, die in Doc 03 v2 gehören. Klein, aber nur sinnvoll, wenn Gruppe A beantwortet ist — sonst werden die Lücken mit neuen [TBD]-Markern überschrieben statt gefüllt.

## Cross-Drift in inconsistencies.md

Zwei Findings erzeugen neuen Drift, der in `docs/findings/inconsistencies.md` nachgezogen werden muss:

1. **Finding 3 (MHD-Validierung)** betrifft auch Doc 04 (LMIV/Etiketten) und Doc 05 (HACCP). Die aktuelle `inconsistencies.md` hat dazu keinen Eintrag. Empfehlung: Eintrag 7 neu aufnehmen als "MHD-Validierung ungeklärt, wirkt auf Doc 03, 04, 05". Wird am Ende von Session 4 nachgezogen.
2. **Finding 6 (Onlineversand)** ist keine Drift zwischen Docs, sondern ein Einzel-Fehler in Doc 03. Kein neuer `inconsistencies.md`-Eintrag nötig.

## Nächste Schritte

1. [ ] Gruppe A: Silvio macht die beiden Anrufe (Vetamt + IHK). Ergebnis als [TBD-Silvio] in Doc 03 v2 einpflegen.
2. [ ] Gruppe B: In Session 5 oder später, wenn Doc 05 HACCP reviewt wird, werden Rückruf, HACCP-Beauftragter und Tagesprotokolle als eigenständige Dokumente designt.
3. [ ] Gruppe C: v2-Rewrite Doc 03 nach Abschluss von Gruppe A. Nicht vor Session 6.
4. [ ] `inconsistencies.md` Eintrag 7 neu anlegen (MHD-Validierung), bevor Session 4 schließt.
5. [ ] Optional in Session 4: v2-Plan-Skizze Doc 03 als `docs/plans/03-v2-plan.md`, falls Kontext-Budget reicht.
