# Findings: Doc 05 – HACCP-Erweiterung

**Quelle:** [Lead-Review Lebensmittelrechtler](../reviews/05-haccp-lebensmittelrechtler.md), [Co-Review Behördenkontrolleur](../reviews/05-haccp-behoerdenkontrolleur.md), [Co-Review Küchenchef](../reviews/05-haccp-kuechenchef.md), [Co-Review Logistiker](../reviews/05-haccp-logistiker.md)
**Datum:** 2026-04-11 (Lead), 2026-04-12 (Co-Reviews + Rule-9-Nachtrag)
**Status:** Co-Reviews abgeschlossen. Behördenkontrolleur sagt **"Stopp — nicht genehmigungsfähig"** (fehlende Gefahrenanalyse, verschärfter Listerien-Grenzwert ab 1.7.2026). Küchenchef und Logistiker sagen "Rework". Rule-9-Fund: ab 1.7.2026 gilt für Listerien in verzehrfertigen Lebensmitteln auf Handelsebene "nicht nachweisbar in 25g" (verschärft vs. bisheriger 100 KBE/g-Toleranz).

Konsolidierte Findings analog `03-findings-veterinaeramt.md` und `15-findings-steuer.md`. Gruppen-Logik einheitlich: A = Silvio/extern, B = eigenständige Arbeits-Blöcke im Repo, C = Doc-Rewrite.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | Gefahrenanalyse fehlt als Fundament (VO 852/2004 Art. 5 Abs. 2 a, Entscheidungsbaum Codex Alimentarius). | P1 | L | Lebensmittelrechtler | Ja, Gate nach Rollout-Schritt 2 | Offen | Ohne Analyse stehen die CCPs ohne Begründung; Vetamt kann Auswahl und Vollständigkeit bei Erstbegehung in Frage stellen. |
| 2 | MHD-Validierung fehlt — 7 Tage Lasagne, 8 Tage Ragù sind Schätzungen. Listeria-Risiko bei Béchamel + Vakuum + Kühlung. | P1 | L | Lebensmittelrechtler + Küche (Test-Protokoll) oder Labor | Ja, Gate nach Rollout-Schritt 4 (Haltbarkeitstests) | Offen | Unvalidiertes MHD ist persönliche Haftungs-Quelle § 58 LFGB; Cross-Ref inconsistencies #7, Doc 03 Finding 3. |
| 3 | Rückruf-Prozess fehlt (Art. 19 VO 178/2002). Schreibort jetzt entschieden (siehe 14-findings-recht-haftung.md #6): Doc 14 = Haftungs-/Krisen-Prozess, Doc 05 = Hygiene-/Chargen-Prozess. | P1 | S | Lebensmittelrechtler | Ja, vor erstem Verkauf | Offen | Cross-Ref Doc 03 Finding 1 und Doc 14 Finding 6. |
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
| 18 | **Verschärfter Listerien-Grenzwert ab 1. Juli 2026** — "nicht nachweisbar in 25g in jeder von 5 Proben" auf Handelsebene bis Ende MHD (VO 2073/2005 Änderungsverordnung). Béchamel-Lasagne ist Risiko-Kategorie (feuchtes, proteinreiches Milieu). MHD-Validierung muss Listerien-Nachweis am Ende des MHD einschließen. Rule-9-Fund. | P1 | L | Lebensmittelrechtler + Labor | Ja, vor Launch nach 1.7.2026 | Offen | Dritter harter Rechts-Stichtag neben PPWR 12.8.2026 und ProdHaftG 9.12.2026. Ohne Listerien-Nachweis ist Béchamel-Produkt ab dem Stichtag nicht verkehrsfähig. |
| 19 | Abkühlzeit für Lasagne unrealistisch ohne Schnellkühler — 400g-Portion ca. 6 cm hoch braucht 3–4 Stunden statt 2 Stunden im Standard-Gastro-Kühlschrank. Entweder CCP1 anpassen, Schockfroster in Phase 1 vorziehen, oder Lasagne erst Phase 2. Scope-Entscheidung. | P1 | S | Küchenchef + Lebensmittelrechtler | Ja, vor erstem Produktions-Tag | Offen | Betrifft Silvios Kern-Produkt Lasagne. Ohne realistischen Abkühlzeit-Nachweis ist CCP1 nicht validiert. |
| 20 | 7-Tage-Sensorik-Test nicht dokumentiert — Verkostung an Tag 0, 3, 5, 7 mit Protokoll (Aussehen, Geruch, Textur, Geschmack) pro Produkt fehlt. | P1 | M | Küchenchef (Test durchführen) | Ja, vor MHD-Festlegung | Offen | Béchamel wird wässrig, Pasta wird matschig — ohne Test ist MHD eine Wette, nicht eine Validierung. |
| 21 | Vormittags-Produktionsfenster nicht im HACCP verankert — zeitliche Trennung Retail (vormittags) vs. Restaurant (nachmittags) als Kreuzkontaminations-Schutz. | P2 | S | Küchenchef + Lebensmittelrechtler | — | Offen | Ohne zeitliche Trennung ist Kreuzkontamination zwischen Rohware (Restaurant) und fertigem Vakuumprodukt (Retail) nicht ausgeschlossen. |
| 22 | Kein CCP4 für Verkaufs-/Übergabephase — Temperatur im Verkaufsbereich, maximale Verweildauer, Rückführ-Regel. | P2 | S | Logistiker + Lebensmittelrechtler | — | Offen | Die meisten Kühlketten-Brüche in der Praxis passieren zwischen Kühllager und Kundenübergabe. |
| 23 | Datenlogger statt Punktmessung — 1× täglich um 08:00 ist Stichprobe, kein Monitoring. Kompressor-Ausfall um 22:00 wird 10 Stunden zu spät bemerkt. WiFi-Logger mit min/max und Alarm: 50–150 €. | P2 | XS | Logistiker | — | Offen | Ohne min/max-Aufzeichnung ist Kühlketten-Nachweis bei Reklamation oder Behördenprüfung lückenhaft. |
| 24 | FIFO-Regelung fehlt — ältere Chargen nach vorne, MHD-Datum sichtbar, Prüfung bei Entnahme. | P2 | XS | Logistiker | — | Offen | Ohne FIFO steigt Verderb-Quote und einzelne Kunden bekommen MHD-nahe Produkte. |
| 25 | Kunden-Kühlketten-Hinweis fehlt — "Gekühlt transportieren, innerhalb 2 Stunden in den Kühlschrank" auf Etikett (Art. 25 LMIV) und an Verkaufsstelle. Optionale Isoliertasche als Service. Cross-Ref Doc 04. | P2 | XS | Logistiker + Lebensmittelrechtler | — | Offen | Übergabe-Punkt-Verantwortung (Doc 14 Finding 17) und Kunden-Erwartung. |
| 26 | Lagerkapazitäts-Rechnung fehlt — bei 20–30 Portionen/Tag und 7 Tagen MHD bis 150 Portionen (≈60 kg) parallel zu Restaurant-Vorräten. Reicht Silvios Kühlraum? [TBD-Silvio] | P2 | S | Logistiker | — | Offen | Wenn der Kühlraum nicht reicht, ist entweder die Tages-Menge zu reduzieren oder ein zweiter Kühlschrank anzuschaffen. |
| 27 | Strom-Ausfall-/Kompressor-Ausfall-Plan fehlt — Handlungsanweisung, Entsorgungs-Schwelle (Temperatur × Dauer), Kontakt Kältetechniker. | P2 | S | Logistiker | — | Offen | Ohne Datenlogger weiß Silvio die Maximal-Temperatur nicht und muss im Zweifel alles entsorgen. |
| 28 | Rückläufer-Regelung fehlt — zurückgebrachte Produkte nie weiterverkaufen, dokumentiert entsorgen. | P3 | XS | Logistiker | — | Offen | Praktisch selten, aber ohne Regel entsteht ein Hygiene- und Haftungsrisiko. |

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
