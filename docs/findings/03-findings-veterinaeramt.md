# Findings: Doc 03 – Veterinäramt Stuttgart

**Quelle:** [Lead-Review Lebensmittelrechtler](../reviews/03-vetamt-lebensmittelrechtler.md), [Co-Review Behördenkontrolleur](../reviews/03-vetamt-behoerdenkontrolleur.md)
**Datum:** 2026-04-11 (Lead), 2026-04-12 (Co-Review + Rule-9-Nachtrag)
**Status:** **Doc 03 v2 geschrieben** (2026-04-12). Doc 03 als Klammer-Dokument neu aufgebaut: Registrierungs-Weg korrigiert (service-bw.de), Kontaktdaten aktualisiert, IHK als Schritt 0, Rework-Szenario mit Kosten, "nicht vor Erstbegehung starten"-Empfehlung, simulierte Erstbegehungs-Checkliste (15 Punkte), vollständige Rechtsgrundlagen-Tabelle, Cross-Refs. Von 16 Findings sind 14 in v2 aufgelöst, 2 bleiben offen (abhängig von Doc 05 v2 für HACCP-Inhalte).

Konsolidierte Findings aus dem Lead-Review. Jedes Finding benennt den Auflösungs-Pfad und den Owner. Findings sind die Grundlage für den späteren v2-Plan (`docs/plans/03-v2-plan.md`) und für Cross-Drift-Einträge in `inconsistencies.md`.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Schriftlicher Rückruf-Prozess fehlt (Art. 19 VO 178/2002). Red Flag laut Persona, Stopp vor erstem Verkauf. | P1 | S | Lebensmittelrechtler (Lead) | Pflicht vor Gate nach Schritt 2 | Offen | Blockiert Vetamt-Bescheid; ohne schriftlichen Rückruf gibt es keine Freigabe. Schreibort-Entscheidung Doc 05 ↔ Doc 14 siehe 14-findings-recht-haftung.md #6. |
| 2 | HACCP-Beauftragter namentlich benennen (Art. 5 VO 852/2004). Selbstbenennung → Silvio-Paket SP-07. | P1 | XS | Lebensmittelrechtler (Dokumentation) | — | Offen | Pflichtfeld in der Vetamt-Unterlage; trivial, aber muss vor Einreichung dokumentiert sein. |
| 3 | MHD-Validierung ungeklärt — "Fachliteratur oder eigene Tests" ist zu weich. Haftungs-Quelle nach § 58 LFGB. | P1 | L | Lebensmittelrechtler + [TBD-Recherche Labor oder Haltbarkeits-Test-Protokoll] | Ja, Gate Schritt 2 und Gate Schritt 4 (Etiketten) | Offen | Ohne validiertes MHD kein LMIV-konformes Etikett, kein Verkauf, persönliche Haftung. |
| 4 | Timings fehlen (Erstkontakt → Bescheid). Realistischer Korridor: 3–8 Wochen. Vetamt-Erstkontakt → Silvio-Paket SP-01. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung nach Rückmeldung) | Ja, für Gate-Timing im Rollout-Plan | Offen | Ohne Timing ist der Rollout-Plan-Gate nach Schritt 2 nicht terminierbar. |
| 5 | Kosten / Gebühren fehlen (Registrierung, Erstbegehung, Nachbegehung, Laboranalyse). Vetamt-Erstkontakt → Silvio-Paket SP-01, Cross-Ref Doc 04 Labor. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung nach Rückmeldung) | — | Offen | Unbekannte Sunk-Cost-Komponente im Worst-Case-Budget 2.500–3.000 €. |
| 6 | "Onlineversand Grauzone" ist sachlich falsch (LMIV Art. 14 Fernabsatz klärt das). | P2 | XS | Lebensmittelrechtler (Korrektur) | — | Offen | Faktische Falschaussage im Doc; entweder korrigieren oder Onlineversand als "nicht in Phase 1" markieren (konsistent mit Rollout-Plan). |
| 7 | "ggf. über Luca-Portal" — Pflicht oder Option? Klärung im Vetamt-Telefonat → Silvio-Paket SP-01. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung nach Rückmeldung) | — | Offen | Verfahrens-TBD; klärt sich im selben Telefonat wie Findings 4 und 5. |
| 8 | Rework-Szenario bei Erstbegehung fehlt (Nachbesserungs-Frist, Zweitbegehung, Kosten). | P2 | S | Lebensmittelrechtler + Co-Review Behördenkontrolleur | — | Offen | Rollout-Plan-Risiko unterschätzt; die Wahrscheinlichkeit einer Beanstandung bei Erstbegehung ist nicht null. |
| 9 | Tagesprotokolle (Kühlkette, Reinigung, Produktion, Rückstellproben) nicht definiert. | P2 | M | Lebensmittelrechtler + Doc 05 HACCP (Cross-Ref) | — | Offen | Dokumentations-Pflicht nach LMHV § 5; Cross-Gate mit Doc 05. Wird im HACCP-Review (Schritt 3 der Sequenz) vertieft. |
| 10 | Rechtsgrundlagen unvollständig aufgeführt (es fehlen VO 178/2002, LFGB, § 42 IfSG, LMHV §§ 3–5). | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Reife-Problem, kein Gate-Problem. Löst sich im v2-Rewrite. |
| 11 | IHK-Erstberatung ist als "Empfehlung" weich formuliert; sollte Ablauf-Schritt 0 werden. Termin-Buchung → Silvio-Paket SP-02. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Billig, Risiko-Reduktion vor dem ersten Vetamt-Kontakt. |
| 12 | D-01-Konformität (Phase 1 nur Vakuum, kein Tiefkühl) nicht explizit im Doc-Kopf. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Konsistenz-Drift; verhindert Tiefkühl-Missverständnis bei Leser. |
| 13 | Registrierungs-Weg falsch: "Luca-Portal" → **service-bw.de**. Telefonnummer veraltet (0711/216-98670 → 0711/21688590). E-Mail fehlt (Poststelle.32-23Verbraucherschutz@Stuttgart.de). Behörde sendet **keine Registrierungs-Bestätigung** — Silvio muss nachfassen. Rule-9-Fund. | P1 | XS | Lebensmittelrechtler (Doc-Korrektur) | — | Offen | Factual-Fehler im Doc; Silvio würde auf dem falschen Portal landen. Bestätigungs-Lücke als operativer Hinweis an Silvio-Paket SP-01. |
| 14 | Simulierte Erstbegehungs-Checkliste fehlt — einseitige Tabelle "Was der Kontrolleur sehen will / Wo dokumentiert / Status", damit Silvio sich vor dem Vetamt-Termin selbst prüfen kann. Klammer-Funktion über Doc 04, 05, 14. | P1 | M | Lebensmittelrechtler + Behördenkontrolleur | — | Offen | Operativ wertvollstes neues Artefakt für Silvio. Reduziert Risiko einer Beanstandung bei Erstbegehung deutlich. |
| 15 | Empfehlung "nicht vor Erstbegehung starten" fehlt — rechtlich darf Silvio nach Registrierung sofort verkaufen, betrieblich riskant: bei nachträglicher Beanstandung greift § 58 LFGB auf bereits verkaufte Ware. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Risiko-Minimierung; ein Satz im Doc genügt. |
| 16 | Erstbegehungs-Timing realistisch (2–6 Wochen nach Registrierung, abhängig von Auslastung) und Nachbegehungs-Kosten (ca. 80–200 € pro Begehung) nicht beziffert. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Präzisiert Finding 4 und 5 mit Behörden-Erfahrungswerten. |

## Auflösungs-Gruppen

Die 16 Findings (12 Lead + 4 Co-Review) zerfallen in drei natürliche Gruppen, die unterschiedliche Arbeits-Stränge auslösen.

**Gruppe A — Aktionen im Silvio-Paket** (`docs/silvio-paket/offene-fragen.md`, Block 1): Findings 4/5/7/**13** → SP-01 (Vetamt-Erstkontakt — jetzt mit korrigierter Nummer und Hinweis "nachfassen, weil keine Bestätigung kommt"), 11 → SP-02 (IHK-Termin), 2 → SP-07 (HACCP-Beauftragter Selbstbenennung). Ein Vetamt-Telefonat plus ein IHK-Termin klärt zusammen sechs von sechzehn Findings auf.

**Gruppe B — Pflicht-Dokumente neu erstellen:** Findings 1, 2, 3, 9. Rückruf-Prozess, HACCP-Beauftragten-Benennung, MHD-Validierung, Tagesprotokolle. Diese gehören nicht in Doc 03, sondern in Doc 05 (HACCP) und Doc 14 (Recht). Doc 03 referenziert sie nur. MHD-Validierung hat den größten Aufwand (Labor-Test oder dokumentierter Haltbarkeits-Test mit mindestens drei Chargen über den geplanten MHD-Zeitraum) und wird zum eigenen Arbeits-Block.

**Gruppe B2 — Neue Artefakte aus Co-Review:** Finding **14** (Erstbegehungs-Checkliste) ist ein eigenständiger Arbeits-Block mit M-Effort, der auf Doc 04, 05, 14 aufbaut und erst nach deren v2 sinnvoll ist. Finding **15** (Empfehlung "nicht vor Erstbegehung starten") und **16** (Timing + Kosten) sind XS-Ergänzungen für Doc 03 v2.

**Gruppe C — Doc-Rewrite-Arbeit:** Findings 6, 8, 10, 12, **13** (Portal-Korrektur), **15**, **16**. Korrekturen und Ergänzungen, die in Doc 03 v2 gehören. Klein, aber nur sinnvoll, wenn Gruppe A beantwortet ist — sonst werden die Lücken mit neuen [TBD]-Markern überschrieben statt gefüllt.

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
