# Findings: Doc 05 – HACCP-Erweiterung

**Quelle:** [Lead-Review Lebensmittelrechtler](../reviews/05-haccp-lebensmittelrechtler.md)
**Datum:** 2026-04-11
**Status:** In Klärung — Co-Reviews durch Küchenchef, Logistiker, Behördenkontrolleur ausstehend.

Konsolidierte Findings analog `03-findings.md` und `15-findings.md`. Gruppen-Logik einheitlich: A = Silvio/extern, B = eigenständige Arbeits-Blöcke im Repo, C = Doc-Rewrite.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Gefahrenanalyse fehlt als Fundament (VO 852/2004 Art. 5 Abs. 2 a, Entscheidungsbaum Codex Alimentarius). | P1 | L | Lebensmittelrechtler | Ja, Gate nach Rollout-Schritt 2 | Offen | Ohne Analyse stehen die CCPs ohne Begründung; Vetamt kann Auswahl und Vollständigkeit bei Erstbegehung in Frage stellen. |
| 2 | MHD-Validierung fehlt — 7 Tage Lasagne, 8 Tage Ragù sind Schätzungen. Listeria-Risiko bei Béchamel + Vakuum + Kühlung. | P1 | L | Lebensmittelrechtler + Küche (Test-Protokoll) oder Labor | Ja, Gate nach Rollout-Schritt 4 (Haltbarkeitstests) | Offen | Unvalidiertes MHD ist persönliche Haftungs-Quelle § 58 LFGB; Cross-Ref inconsistencies #7, Doc 03 Finding 3. |
| 3 | Rückruf-Prozess fehlt (Art. 19 VO 178/2002). Schreibort jetzt entschieden (siehe 14-findings.md #6): Doc 14 = Haftungs-/Krisen-Prozess, Doc 05 = Hygiene-/Chargen-Prozess. | P1 | S | Lebensmittelrechtler | Ja, vor erstem Verkauf | Offen | Cross-Ref Doc 03 Finding 1 und Doc 14 Finding 6. |
| 4 | Rohware-Eingangskontrolle fehlt komplett (Akzeptanz-Kriterien, Temperaturmessung, Lieferanten-Spezifikationen). | P1 | M | Lebensmittelrechtler + Küchenchef (Co-Review) | Ja, Teil der Gefahrenanalyse | Offen | Vakuum-Produktion verträgt keine Fehlertoleranz in der Rohware; ohne Wareneingangs-Kontrolle versagt die Ketten-Logik bei lieferanten-seitiger Kontamination. |
| 5 | Reaktion auf geschwollenen Beutel unvollständig ("sofort entsorgen" statt Charge sperren, Rückstellproben prüfen, ggf. Rückruf). | P1 | S | Lebensmittelrechtler | Ja, vor erstem Verkauf | Offen | Geschwollener Beutel ist das deutlichste Symptom für Clostridium-Wachstum — Einzel-Entsorgung lässt das Systemrisiko ungeprüft. |
| 6 | CCP1-Grenzwert Ein-Stufen ("≤ 10 °C in 2 h") statt Zwei-Stufen-Regel. | P2 | XS | Lebensmittelrechtler (Korrektur) | — | Offen | B. cereus-Sporen-Keimbereich offen gelassen; fachlich und rechtlich nicht haltbar. |
| 7 | CCP2 als Prozess-Regel statt Produkt-Grenzwert; Kerntemperatur sollte ≤ +4 °C sein, nicht ≤ +10 °C. | P2 | XS | Lebensmittelrechtler (Umformulierung) | — | Offen | +10 °C ist für das Clostridium-Risiko zu locker; strenger Produkt-Grenzwert entkoppelt den CCP vom Prozess. |
| 8 | CCP3 Zwischenzone +4–+7 °C undefiniert. Vorschlag: Normal ≤ +4, Warn +5, Alarm +7. | P2 | XS | Lebensmittelrechtler (Schwellen-Definition) | — | Offen | Aktuelle Binär-Logik lässt Silvio ohne Reaktions-Gradation; erhöht Fehl-Alarme oder verschleppte Reaktion. |
| 9 | Reinigungs- und Desinfektionsplan fehlt (LMHV § 3). Muster-Tabelle Flächen / Vakuumier-Kammer (Dichtring Biofilm) / Messtechnik / Kühlraum. | P2 | M | Lebensmittelrechtler + Küchenchef | — | Offen | Standard-Vetamt-Prüfpunkt; ohne Reinigungsplan harte Beanstandung bei Erstbegehung. |
| 10 | Rückstellproben-Konzept fehlt (Branchen-Standard: pro Charge, ≤ +4 °C, MHD + 7 Tage). | P2 | S | Lebensmittelrechtler | — | Offen | Ohne Rückstellproben ist der Rückruf-Prozess aus Finding 3 operativ nicht ausführbar. |
| 11 | Chargen-Rückverfolgbarkeit zur Rohware (Hackfleisch-LOT, Tomaten-LOT) fehlt im Chargenprotokoll. | P2 | XS | Lebensmittelrechtler (Spalte ergänzen) | — | Offen | Rückruf bei lieferanten-seitiger Kontamination nur lückenhaft möglich. |
| 12 | IfSG § 43 Erstbelehrung und jährliche Folgebelehrung fehlen im Schulungs-Abschnitt. Gesundheitsamt-Termin → Silvio-Paket SP-04. | P2 | XS | Lebensmittelrechtler (Doc-Ergänzung) | Ja, vor erstem Verkauf für Personal, das am Vakuum arbeitet | Offen | Ohne Belehrung kein Einsatz am Vakuum zulässig; formaler Stopp-Grund. |
| 13 | Tiefkühl-Spalte in MHD-Tabelle widerspricht D-01. | P2 | XS | Lebensmittelrechtler (Doc-Korrektur) | — | Offen | Drift zu decisions.md; Cross-Ref inconsistencies #3. |
| 14 | Schädlingsbekämpfungsplan fehlt oder Cross-Ref zum bestehenden Restaurant-Plan mit Retail-Erweiterung. Bestand klären → Silvio-Paket SP-08. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Standard-Vetamt-Prüfpunkt; meist mit Frist behoben, kein Launch-Blocker. |
| 15 | HACCP-Beauftragter nicht namentlich benannt (Art. 5 VO 852/2004). Selbstbenennung → Silvio-Paket SP-07. | P3 | XS | Lebensmittelrechtler (Dokumentation) | — | Offen | Cross-Ref Doc 03 Finding 2. |
| 16 | Aufbewahrungspflicht pauschal "3 Jahre" — sollte differenziert sein (Rückverfolgbarkeit 5 Jahre, Tagesprotokolle 2 Jahre). | P3 | XS | Lebensmittelrechtler (Differenzierung) | — | Offen | Reife-Problem, kein Gate-Problem. |
| 17 | Cross-Refs zu Doc 03 (Vetamt), Doc 04 (LMIV), Doc 14 (Recht) fehlen. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Reife-Problem; verhindert Doppel-Aufbau von Pflicht-Dokumenten. |

## Auflösungs-Gruppen

**Gruppe A — Aktionen im Silvio-Paket** (`docs/silvio-paket/offene-fragen.md`, Block 3): Findings 12 → SP-04 (Gesundheitsamt § 43 IfSG-Termin), 14 → SP-08 (Schädlingsbekämpfungsvertrag klären), 15 → SP-07 (HACCP-Beauftragter Selbstbenennung, gemeinsam mit Doc 03 Finding 2).

**Gruppe B — Eigenständige Arbeits-Blöcke im Repo:** Findings 1 (Gefahrenanalyse), 2 (MHD-Validierungs-Pfad), 3 (Rückruf-Prozess), 4 (Rohware-Eingangskontrolle), 9 (Reinigungsplan), 10 (Rückstellproben). Diese sind zu groß für eine einzelne Doc-Überarbeitung und werden eigene Arbeits-Blöcke mit jeweils Rechercheanteil, Muster-Tabellen, Cross-Refs. Reihenfolge:

1. **Gefahrenanalyse (Finding 1)** zuerst — sie ist das Fundament, aus dem sich CCPs, Reinigung, Rückstellproben automatisch ergeben. Eigener Block, vermutlich eine Session oder ein halber Tag.
2. **Rückruf-Prozess (Finding 3)** kann parallel laufen. Schreibort (Doc 05 vs. Doc 14) wird beim Doc-14-Review entschieden. Bis dahin als Platzhalter in beiden Docs referenzieren.
3. **MHD-Validierung (Finding 2)** ist der größte inhaltliche Block. Entscheidung zwischen drei Optionen: (a) eigene Haltbarkeits-Tests mit sensorischer + mikrobiologischer Kontrolle, (b) Labor-Analyse akkreditiert, (c) konservative Branchen-Werte mit Sicherheits-Marge. Kosten- und Risiko-Entscheidung, die Silvio treffen muss — aber Claude kann die drei Optionen mit Kosten-Korridoren, Dauer und Rechts-Konsequenzen aufbereiten. Separater Arbeits-Block, nicht Teil eines Doc-Rewrites.
4. **Rohware-Eingangskontrolle (Finding 4), Reinigungsplan (Finding 9), Rückstellproben (Finding 10)** sind Muster-Tabellen, die aus der Gefahrenanalyse abfallen. Werden in einer zweiten Runde als Anhang oder direkt in Doc 05 v2 eingebaut.

**Gruppe C — Doc-Rewrite:** Findings 5 (Reaktions-Kaskade geschwollener Beutel), 6 (CCP1 Zwei-Stufen), 7 (CCP2 Produkt-Grenzwert), 8 (CCP3 Schwellen), 11 (Chargen-Rückverfolgbarkeit Spalte), 13 (Tiefkühl-Zeile streichen), 16 (Aufbewahrungs-Differenzierung), 17 (Cross-Refs). Text- und Tabellen-Arbeit, sinnvoll als letzter Schritt nach Gruppe B, weil die neuen CCP-Formulierungen aus der Gefahrenanalyse folgen.

## Cross-Drift in inconsistencies.md

Zwei Verbindungen:

1. **Finding 2 (MHD-Validierung)** zahlt auf den bestehenden Eintrag #7 (MHD-Validierung Doc 03 / 04 / 05) ein. Doc 05 ist jetzt explizit als dritter betroffener Ort bestätigt. Eintrag #7 muss um "Doc 05 Finding 2" als Ankerpunkt erweitert werden.
2. **Finding 13 (Tiefkühl-Spalte)** zahlt auf Eintrag #3 (Scope: Tiefkühl vs. D-01) ein. Doc 05 ist bisher in der Doc-A-Liste von #3 genannt — das stimmt, aber der konkrete Ankerpunkt (MHD-Tabelle) sollte dort präzisiert werden.

Keine neuen Inconsistencies-Einträge, nur Präzisierungen. Effort: XS, wird in einem Durchgang mit Doc 05 committed.

## Nächste Schritte

1. [ ] inconsistencies.md präzisieren: #7 um Doc-05-Anker, #3 um MHD-Tabelle als konkretes Ziel.
2. [ ] Gruppe A mit Doc 03 und Doc 15 Gruppe A zum **Silvio-Paket v1** konsolidieren (eigene Silvio-Briefing-Notiz, frühestens Session 6).
3. [ ] Gruppe B Block 1 (Gefahrenanalyse) als erste Maßnahme nach Doc 14 Review — oder vorgezogen, wenn Silvio das MHD-Thema dringend macht.
4. [ ] Gruppe B Block 3 (MHD-Validierungs-Optionen) als eigener Entscheidungs-Block mit Silvio, unabhängig vom Repo-Rhythmus.
5. [ ] Gruppe C (Doc-Rewrite Doc 05 v2) nicht vor Gruppe B Block 1–2.
6. [ ] Sequenz-Fortschritt: 03 ✓ 15 ✓ 05 ✓ 04 offen 14 offen. Nächstes Doc in der Gate-kritischen Sequenz: Doc 04 LMIV.
