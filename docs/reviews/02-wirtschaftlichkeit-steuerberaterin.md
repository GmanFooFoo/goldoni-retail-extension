# Co-Review: Doc 02 – Wirtschaftlichkeitsrechnung

**Reviewer:** Frau Keller (Steuerberaterin, Persona 03)
**Datum:** 2026-04-12
**Doc-Version:** v1
**Typ:** Co-Review (Lead: CFO Marcus)

## Kurzurteil (1 Satz)

Der CFO-Lead-Review deckt die Kernprobleme vollständig ab; die steuerliche Perspektive verschärft drei Punkte und ergänzt zwei, die der CFO nicht auf dem Schirm hat.

## Scoring (1–5)

- **Fachliche Korrektheit:** 2 — ohne Netto/Brutto-Deklaration ist keine Zahl steuerlich verwendbar
- **Vollständigkeit:** 1 — kein Steuer-Abschnitt, keine Abschreibung, keine Vorsteuer, keine GewSt
- **Umsetzbarkeit:** 2 — ein Steuerberater würde dieses Dokument zurückschicken
- **Risiko-Abdeckung:** 1 — steuerliche Risiken (Betriebsprüfung, Nachzahlung) nicht erwähnt

## Bestätigungen des Lead-Reviews

Findings 1 (Netto/Brutto), 2 (Fixkosten-Allokation), 7 (Verderb), 11 (Gewerbesteuer), 13 ("Gewinnbeitrag" ist kein Gewinn) und 17 (Abschreibung) — alle bestätigt. Nichts zu ergänzen, der CFO hat die richtigen Stellen markiert.

## Verschärfungen

### V1 — "Gewinnbeitrag" ist steuerlich ein falscher Begriff

Finding 13 des CFO nennt es "begrifflich falsch". Das ist es, aber die Konsequenz geht weiter: Silvios Steuerberater wird bei einer Betriebsprüfung nicht "Gewinnbeitrag 19.500 €" akzeptieren, wenn dahinter weder eine saubere Betriebsergebnis-Rechnung (EÜR oder Bilanz) noch eine nachvollziehbare Trennung Restaurant/Retail steht. Der richtige steuerliche Begriff ist **Betriebsergebnis vor Steuern** — und das ist, nach CFO-Korrektur, eher 8.000–12.000 € im ersten vollen Jahr.

### V2 — Vorsteuer-Effekt der Investitionen fehlt im Cashflow

Der CFO hat die Vorsteuer-Erstattung in seiner Cashflow-Projektion (`docs/plans/02-cashflow-projektion-2026.md`) korrekt berücksichtigt — aber Doc 02 v1 erwähnt den Effekt mit keinem Wort. Das ist relevant, weil die effektive Anfangsinvestition durch Vorsteuer-Erstattung um ca. 900 € niedriger ist als der Brutto-Betrag suggeriert. Silvio zahlt brutto, bekommt die Vorsteuer in der nächsten Voranmeldung zurück — das ist Liquidität, die den Cash-Burn im ersten Monat entschärft.

### V3 — Umsatzsteuer-Voranmeldung als laufender Prozess

Doc 02 tut so, als gäbe es keine USt. In der Realität muss Silvio monatlich oder vierteljährlich (je nach Finanzamt-Festsetzung) eine **Umsatzsteuer-Voranmeldung** abgeben, in der die Retail-Umsätze (7 %) den Retail-Vorsteuer-Abzügen gegenüberstehen. Das ist kein großer Aufwand, aber es ist ein laufender Prozess, der in der operativen Planung fehlt — und bei Nicht-Einhaltung Verspätungszuschläge auslöst (§ 152 AO, bis 10 % der Steuer).

## Ergänzungen

### E1 — EÜR-Struktur als Zielformat für Doc 02 v2

Doc 02 sollte im v2-Rewrite die Struktur einer vereinfachten **Einnahmenüberschussrechnung (EÜR)** annehmen — nicht als steuerliche Pflichtübung, sondern weil das die Sprache ist, die Silvios Steuerberater sofort versteht. Aufbau: Betriebseinnahmen (netto) − Betriebsausgaben (variabel + fix + AfA) = Betriebsergebnis vor Steuern. Darauf GewSt-Check, dann ESt-Belastung (grob, nach Steuertabelle). So sieht Silvio, was **nach Steuern** übrig bleibt — das ist die einzige Zahl, die zählt.

### E2 — Verderb ist steuerlich unproblematisch, aber muss dokumentiert sein

Die Verderb-Buchung (Finding 7 des CFO, ausführlich in Doc 15 v2) ist steuerlich klar: Warenverlust → Betriebsausgabe, Vorsteuer bleibt abzugsfähig. Aber ohne **Warenvernichtungsprotokoll** (Datum, Charge, Menge, Grund, Unterschrift) wird ein Betriebsprüfer bei auffällig hohen Verderb-Raten nachhaken. Das Protokoll ist keine Bürokratie, sondern Beweis-Sicherung.

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich (bestätigt Lead-Urteil)
- [ ] Stopp

Kein eigenständiger Stopp-Grund aus steuerlicher Sicht — aber die Wirtschaftlichkeitsrechnung ist in der aktuellen Form nicht steuerberater-vorzeigbar.
