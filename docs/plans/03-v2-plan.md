# Plan: Doc 03 v2 – Veterinäramt Stuttgart

**Status:** Skizze
**Quelle:** [Findings Doc 03](../findings/03-findings.md), [Lead-Review Lebensmittelrechtler](../reviews/03-vetamt-lebensmittelrechtler.md)
**Datum:** 2026-04-11
**Vorbedingung:** Gruppe-A-Findings (Silvio-Erstkontakt + IHK) beantwortet. **Kein v2 vor Beantwortung.**

## Ziel von v2

Doc 03 v2 ist ein Gate-taugliches Dokument: ein Leser kann anhand des Dokuments beurteilen, ob der Gate nach Rollout-Schritt 2 (Vetamt-Bescheid) pass oder fail ist, mit welchem Timing er rechnen muss und welche Kosten im Worst Case anfallen. v2 ist kein Rewrite aus Schönheits-Gründen, sondern schließt die drei Gate-Lücken: Timing, Kosten, Rework-Szenario.

## Strukturänderungen gegenüber v1

| # | Abschnitt v1 | Änderung in v2 |
|---|---|---|
| 1 | Zuständige Behörde | bleibt; ergänzt um: Ansprechpartner-Name und Sprechzeiten nach Erstkontakt |
| 2 | Registrierung vs. Zulassung | Tabelle bleibt; "Onlineversand Grauzone" streichen (Finding 6), stattdessen: "Onlineversand nicht in Phase 1 (siehe D-01, Rollout-Plan)" |
| 3 | **NEU: Scope-Hinweis** | Neuer Abschnitt am Kopf: "Dieses Dokument beschreibt Phase 1 (vakuumiert, gekühlt, Abholung). Tiefkühl und Onlineversand sind Phase 2." — schließt Finding 12 |
| 4 | Ablauf Schritt für Schritt | Ergänzt um **Schritt 0 IHK-Erstberatung** (Finding 11), ergänzt um **Timings** pro Schritt (Finding 4), ergänzt um **Kosten** pro Schritt (Finding 5), ergänzt um **Rework-Pfad** bei Beanstandung (Finding 8) |
| 5 | Einzureichende Unterlagen | Ergänzt um: Rückruf-Konzept (Finding 1, Cross-Ref Doc 14), HACCP-Beauftragten-Benennung (Finding 2, Cross-Ref Doc 05), Tagesprotokolle-Schema (Finding 9, Cross-Ref Doc 05), Rückstellproben-Konzept, Betriebsspiegel LMHV § 3 |
| 6 | Häufige Stolpersteine | Ergänzt um: Haftungs-Folge bei unvalidierten Nährwerten (§ 58 LFGB), Persönliche Haftung bei falscher Allergenkennzeichnung |
| 7 | Empfehlung (IHK) | Streichen als separater Abschnitt — IHK-Kontakt ist jetzt Schritt 0 im Ablauf |
| 8 | **NEU: Rechtsgrundlagen** | Neuer Abschnitt am Ende: Liste der einschlägigen Normen (VO 852/2004 Art. 5+6, VO 178/2002 Art. 19, LMIV Art. 14, LMHV §§ 3–5, § 42 IfSG, LFGB § 58) mit einer Zeile je Norm, was sie regelt. Schließt Finding 10. |
| 9 | **NEU: Gate-Auswertung** | Neuer Abschnitt am Ende: "Wie wird der Gate nach Rollout-Schritt 2 ausgewertet?" mit drei Zeilen Pass-Kriterium / Fail-Kriterium / Hold-Kriterium. Ist der eigentliche Grund für v2. |

## Offene TBDs, die vor v2 beantwortet sein müssen

**Gruppe A (Silvio-Aktionen, Findings 4, 5, 7, 11):**
- Timing-Korridor Erstkontakt → Bescheid
- Gebühren Registrierung, Erstbegehung, Nachbegehung
- Luca-Portal Pflicht oder Option in Stuttgart
- IHK-Termin gebucht

**Gruppe B (Pflicht-Dokumente, Findings 1, 2, 3, 9):**
- Rückruf-Konzept existiert und ist cross-referenziert aus Doc 14
- HACCP-Beauftragter benannt, dokumentiert in Doc 05
- MHD-Validierung hat ein Protokoll (Labor oder interner Haltbarkeits-Test mit mindestens drei Chargen)
- Tagesprotokolle sind in Doc 05 definiert

## Reihenfolge

1. **Silvio macht beide Anrufe** (Vetamt + IHK). Ergebnis als Notizen an German.
2. **Session 5+ reviewt Doc 15 (Steuer), 05 (HACCP), 04 (LMIV), 14 (Recht)** entlang der Gate-kritischen Sequenz. Pflicht-Dokumente für Gruppe B entstehen im HACCP- und Recht-Review.
3. **Danach v2-Rewrite Doc 03** — kurz, vermutlich < 1 Stunde, weil die Inhalte aus den anderen Reviews gesammelt und nur zusammengefasst werden.

## Nicht in v2

- Keine Visualisierung / Grafik / Flussdiagramm. Markdown reicht.
- Keine doppelte Dokumentation der Pflicht-Dokumente — Rückruf und HACCP-Beauftragter leben in Doc 14 und Doc 05, Doc 03 referenziert nur.
- Kein Onlineversand-Abschnitt in Phase 1.

## Verifikation von v2

- Der Gate-Abschnitt liefert drei explizite Kriterien (Pass/Fail/Hold).
- Timings und Kosten sind entweder mit konkreten Zahlen oder mit einem expliziten [TBD-Silvio]-Marker versehen (nicht implizit offen wie in v1).
- Cross-References auf Doc 04, 05, 14 sind explizit als Markdown-Links, nicht prosaisch angedeutet.
- Keine sachlich falschen Aussagen (Finding 6 "Onlineversand Grauzone" ist raus).
- D-01 ist im Scope-Hinweis zitiert.
