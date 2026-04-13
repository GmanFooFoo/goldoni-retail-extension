# Review: Doc 16 – Risiken & Gegenmaßnahmen

**Reviewer:** Marcus (CFO / Zahlen-Realist, Persona 01)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Kurzurteil (1 Satz)

Solide operative Risiko-Liste mit einer starken "Goldenen Regel" am Ende, aber es fehlt alles, was Geld kostet — keine Quantifizierung, keine finanziellen Risiken, keine regulatorischen Stichtage, und die Risiko-Priorisierung widerspricht dem, was die Reviews tatsächlich gefunden haben.

## Scoring (1–5)

- **Fachliche Korrektheit:** 3 — die operativen Risiken (Kühlkette, Charge, Inspektion) sind korrekt beschrieben, Gegenmaßnahmen praxistauglich
- **Vollständigkeit:** 1 — nur operative Risiken, keine finanziellen, regulatorischen oder Markt-Risiken. Kein einziger der drei Rechts-Stichtage H2/2026.
- **Umsetzbarkeit:** 3 — Gegenmaßnahmen sind konkret und direkt anwendbar
- **Risiko-Abdeckung:** 2 — Priorisierung falsch ("Nachfrage bleibt aus" = Prio 3, Auswirkung "Gering"? Das ist das existenzielle Risiko.)

## Red Flags

1. **"Nachfrage bleibt aus" = Prio 3, Auswirkung "Gering".** Das ist das größte finanzielle Risiko: bei dauerhaft <15 Stk/Woche amortisiert sich die Investition nie. Auswirkung "Gering" ist falsch — sie ist "Hoch" (versunkene Kosten 3.100–4.600 €).

2. **Keine finanziellen Risiken.** Wareneinsatz-Schwankung, Plattform-Provisions-Erhöhung, ungeplante Kassensystem-Kosten (SP-06), Verderb in der Pilotphase — alles fehlt.

3. **Keine regulatorischen Stichtage.** Drei harte Deadlines in H2/2026 (Listerien 1.7., PPWR 12.8., ProdHaftG 9.12.) erzeugen Compliance-Risiken, wenn Silvio zwischen den Stichtagen launched — keiner davon wird erwähnt.

4. **Kein Haftungs-Risiko.** Doc 14 hat umfangreiche Haftungs-Findings (ProdHaftG-Novelle, § 58 LFGB Strafbarkeit, 25-Jahre-Chargen-Doku). Doc 16 erwähnt Haftung nicht.

## Fundierte Kritikpunkte

### K1 — Keine Quantifizierung

Kein einziges Risiko hat einen €-Betrag. "Schlechte Charge" — was kostet das? Warenwert der Charge (~100–200 €) + Rückrufkosten (Doc 14: Kommunikation, ggf. Veterinäramts-Meldung) + Reputationsschaden (nicht bezifferbar, aber Stammgast-Verlust = Umsatz-Verlust). Ohne Zahlen kann Silvio nicht entscheiden, welche Gegenmaßnahme sich lohnt.

### K2 — Risiko-Matrix unvollständig

Die 7 Risiken decken nur den operativen Küchenbetrieb ab. Fehlende Kategorien:

| Kategorie | Beispiele | Quelle |
|---|---|---|
| **Finanziell** | Wareneinsatz +20 %, Provision steigt, Kasse nicht TSE-fähig | Doc 02 v2 Kap. 9, SP-06 |
| **Regulatorisch** | Listerien-Grenzwert 1.7., PPWR 12.8., ProdHaftG 9.12. | Rule-9-Scans Session 10/11 |
| **Haftung** | Produkthaftung, Rückruf-Kosten, Strafbarkeit § 58 LFGB | Doc 14 Findings |
| **Personal** | Ein-Personen-Abhängigkeit (Szenario C), Ausfall | Doc 20 |
| **Markt** | Nachfrage-Ausfall, Wettbewerber-Eintritt, Plattform-Abhängigkeit | Doc 17, D-13 |
| **Reputation** | Lebensmittelskandal (auch ohne eigenes Verschulden), Social Media | Doc 14 F16 |

### K3 — "Tagesspecial ins Restaurant" als Verderb-Lösung problematisch

"Produkte 2 Tage vor MHD als Tagesspecial ins Restaurant" — klingt clever, aber: (a) LMIV-Kennzeichnung fällt weg wenn das Produkt im Restaurant serviert wird (anders deklariert), (b) der Deckungsbeitrag als Restaurant-Portion ist ein anderer als als Retail-Produkt, (c) es vermischt zwei Geschäftsstränge, die buchhalterisch getrennt sein sollten (Doc 15 v2 Erlöskonten). Nicht verboten, aber buchhalterisch sauber dokumentieren.

### K4 — Kein Risiko-Register mit Owner und Fälligkeit

Die Risiken stehen als Prosa-Abschnitte ohne klare Zuordnung: wer ist verantwortlich? Wann wird die Gegenmaßnahme umgesetzt? Was ist der Trigger für die Eskalation? Ein Risiko-Register im Tabellenformat (Risk → Owner → Trigger → Maßnahme → Fälligkeit → Status) wäre für einen Business Case Standard.

## Was fehlt

1. **Finanzielle Risiken** mit €-Beträgen (Sensitivity aus Doc 02 v2 Kap. 9)
2. **Regulatorische Stichtage** als eigene Risiko-Kategorie
3. **Haftungs-Risiken** (Cross-Ref zu Doc 14)
4. **Personal-Risiken** (Cross-Ref zu Doc 20)
5. **Markt-Risiken** (Nachfrage-Ausfall korrekt priorisieren, Plattform-Abhängigkeit)
6. **Quantifizierung** jedes Risikos (Kosten im Eintrittsfall)
7. **Risiko-Register** statt Prosa (Tabellenformat mit Owner, Trigger, Maßnahme)
8. **Risiko-Priorisierung korrigieren** ("Nachfrage" = Prio 1, nicht 3)

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich
- [ ] Stopp

**Begründung:** Die operative Basis (Kühlkette, Charge, Inspektion) bleibt. Aber ein Risiko-Dokument in einem Business Case muss alle Risiko-Kategorien abdecken und quantifizieren — sonst ist es eine Küchen-Checkliste, kein Risiko-Management.
