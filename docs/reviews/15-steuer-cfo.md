# Review: 15 – Steuerliche Behandlung

**Reviewer:** CFO (Persona 01, Co-Review)
**Datum:** 2026-04-12
**Doc-Version:** v1
**Lead-Review:** [Steuerberaterin (Persona 03)](15-steuer-steuerberaterin.md), 2026-04-11

## Kurzurteil (1 Satz)

Die Steuerberaterin hat die handwerklichen Lücken von Doc 15 sauber auseinandergenommen — aus CFO-Sicht bestätige ich das "Rework erforderlich" und verschärfe an zwei Stellen: die fehlende Netto/Brutto-Deklaration in Doc 02 und Doc 07 ist nicht nur ein formales Problem, sondern macht die gesamte Wirtschaftlichkeitsrechnung unbelastbar, und die fehlende Verderb-Buchungslogik erzeugt ein stilles Margen-Leck, das in der Pilot-Phase zwischen 3 und 8 Prozentpunkte Bruttomarge kosten kann.

## Scoring (1–5)

- **Fachliche Korrektheit: 3** — Einverstanden mit der Steuerberaterin. Die 7-%-Grundannahme ist seit dem Steueränderungsgesetz 2025 gesetzlich abgesichert. Abzüge für fehlende Norm-Anker und die nicht-behandelte Kombi-Beleg-Frage.
- **Vollständigkeit: 2** — Bestätige den Befund der Steuerberaterin. Aus CFO-Sicht ist die fehlende Brücke zu Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) das gravierendste Problem: ein Steuer-Doc, das die eigene Zahlen-Landschaft nicht mit der Margen-Rechnung verbindet, ist ein Silo. Zusätzlich fehlt: Investitionsvorsteuer als Liquiditäts-Hebel, Verderb als laufender P&L-Effekt, Gewerbesteuer-Vorauszahlungs-Anpassung.
- **Umsetzbarkeit: 3** — Einverstanden. Die vier Schritte sind richtig, aber nicht prüfbar. Kein Akzeptanz-Kriterium, keine Kosten, kein Zeitrahmen.
- **Risiko-Abdeckung: 2** — Einverstanden. Der Nachtrag zum Steueränderungsgesetz 2025 hat den größten Risiko-Posten (19-%-Umstufung) entschärft. Das verbleibende Risiko liegt jetzt in operativen Fehlern (Kombi-Belege, Aufwärm-Grauzone) und in der ungeklärten Fixkosten-Allokation.

## Red Flags

1. **Netto/Brutto-Blindheit im gesamten Doc-Satz.** Doc 02 nennt Verkaufspreise ("Lasagne 12,90 €"), Doc 07 nennt Preis-Spannen — nirgends steht, ob das Brutto- oder Netto-Preise sind. Bei 7 % ist der Unterschied 6,5 %, bei einer Marge von 50–60 % auf Wareneinsatz klingt das verkraftbar, aber: die Marge wird auf einen Netto-Erlös gerechnet, nicht auf den Brutto-Preis. Wenn Doc 02 Brutto meint (was wahrscheinlich ist, weil Silvio in Endkunden-Preisen denkt), dann fehlen 6,5 % vom Erlös in der Kalkulation. Bei 50 Einheiten/Woche à 12,90 € Brutto sind das **ca. 40 € pro Woche / 2.100 € pro Jahr**, die in der Margen-Rechnung verschwinden. Kein Stopper, aber ein systematischer Fehler.

2. **Verderb-Kosten sind ein stilles Margen-Leck.** Doc 16 (Risiken) nennt 5–10 % Verderb in der Pilot-Phase. Doc 15 adressiert das steuerlich nicht (Warenvernichtungsprotokoll, Buchungssatz, USt-Korrektur). Aus CFO-Sicht ist die Frage aber vor allem betriebswirtschaftlich: bei einem Wareneinsatz von 4,50 € pro Einheit und 10 % Verderb kostet das **ca. 22,50 € pro Woche / 1.170 € pro Jahr** — reiner Rohstoff, ohne Arbeitskraft. Das muss als fester Kostenblock in die Wirtschaftlichkeitsrechnung, nicht als Risiko-Fußnote.

3. **Fixkosten-Allokation fehlt komplett.** Das Doc behandelt den Retail-Strang so, als hätte er nur variable Kosten (Wareneinsatz, Beutel, Etiketten). Aber die Retail-Produktion nutzt Silvios Küche, Silvios Strom, Silvios Kühlschrank, Silvios Miete. Wenn der Retail-Strang keinen anteiligen Fixkosten-Block trägt, subventioniert das Restaurant den Retail-Verkauf verdeckt. Für die Steuer ist das kein Problem (alles derselbe Betrieb), aber für die betriebswirtschaftliche Entscheidung "lohnt sich Retail?" ist es tödlich: ein Retail-Strang, der nur auf variable Kosten gerechnet wird, sieht immer profitabel aus — selbst wenn er bei Vollkosten-Betrachtung Verlust macht.

## Fundierte Kritikpunkte

1. **Vorsteuer-Hebel beim Vakuumierer-Kauf nicht modelliert.** Die Steuerberaterin nennt den Punkt (285–665 € Vorsteuer aus dem Kauf). Aus CFO-Sicht gehört das in eine einfache Investitions-Tabelle: Netto-Kaufpreis, 19 % USt, Vorsteuer-Erstattung im nächsten VA-Zeitraum, AfA über 8 Jahre (AfA-Tabelle Gastgewerbe), jährliche Abschreibung. Der Cash-Flow-Effekt ist real: Silvio zahlt den Vakuumierer brutto, bekommt die Vorsteuer in der nächsten Voranmeldung zurück, und schreibt den Netto-Betrag über 8 Jahre ab. Das reduziert die effektive Anfangsinvestition um 16 % (bei 19 % USt). Ohne diese Rechnung sieht die Capex-Hürde im Rollout-Plan höher aus als sie ist.

2. **Break-Even-Rechnung fehlt — und Doc 15 müsste sie triggern.** Die MwSt-Behandlung ist eine der Variablen in der Break-Even-Rechnung (Doc 02, Backlog #52). Doc 15 müsste explizit sagen: "Die Wirtschaftlichkeitsrechnung in Doc 02 muss mit folgenden steuerlichen Parametern gerechnet werden: USt-Satz 7 %, Netto-Erlös = Brutto-Preis / 1,07, Vorsteuer-Abzug auf alle Retail-spezifischen Einkäufe." Ohne diesen Brücken-Absatz bleibt Doc 15 ein Silo.

3. **Gewerbesteuer-Effekt nicht adressiert.** Der Retail-Gewinn erhöht Silvios Gesamtgewinn und damit die Gewerbesteuer-Last. Bei einem Hebesatz von 420 % in Stuttgart und einem Retail-Gewinn von (optimistisch) 10.000–15.000 € im ersten vollen Jahr sind das ca. 550–825 € zusätzliche Gewerbesteuer. Kein Stopper, aber ein Posten, der in die Wirtschaftlichkeitsrechnung gehört und die Vorauszahlungen beeinflusst.

4. **Kassensystem-Kosten im worst case.** Falls Silvios Kasse nicht TSE-fähig ist, muss sie nachgerüstet oder ersetzt werden. Nachrüstung: 300–500 €. Neue Kasse mit TSE: 1.500–3.000 €. Das ist ein potenzieller Capex-Block, der im Rollout-Budget (Doc 12) auftauchen muss. Worst case: Silvios Kasse ist so alt, dass sie weder TSE noch Zwei-Steuersatz kann — dann ist das ein Stopper, der den Rollout um Wochen verschiebt.

## Was fehlt (CFO-Ergänzung zum Lead)

1. **Brücken-Absatz zu Doc 02 und Doc 07** mit expliziter Netto/Brutto-Deklaration und den steuerlichen Parametern für die Margen-Rechnung.
2. **Investitions-Rechnung Vakuumierer** als konkretes Beispiel (Netto/USt/AfA/Cash-Flow-Effekt).
3. **Verderb-Kostenblock** als feste Position, nicht als Risiko-Fußnote. Buchungslogik plus P&L-Effekt.
4. **Fixkosten-Allokations-Hinweis** — mindestens als Verweis auf Doc 02, wo der Retail-Strang einen anteiligen Overhead tragen muss.
5. **Gewerbesteuer-Absatz** mit Hebesatz Stuttgart und Beispielrechnung.
6. **Kassensystem-worst-case-Kosten** als Budgetposition für Doc 12.

## Empfehlung

- [ ] Freigabe
- [x] **Rework erforderlich**
- [ ] Freigabe mit Auflagen
- [ ] Stopp — geht so nicht live

**Begründung:** Einverstanden mit der Steuerberaterin. Das Doc ist nicht falsch, aber es ist ein Steuer-Erklärstück, kein belastbares Planungsdokument. Aus CFO-Sicht ist die größte Schwäche nicht Doc 15 selbst, sondern die fehlende Brücke zu Doc 02 und Doc 07 — solange die Wirtschaftlichkeitsrechnung nicht weiß, ob sie mit Netto- oder Brutto-Preisen rechnet, ist jede Margen-Aussage Schätzung.

**Eskalationslogik:**
- Netto/Brutto-Frage in Doc 02/07 bleibt ungeklärt → **kein v2-Rewrite von Doc 15 sinnvoll**, weil die Zahlen-Basis fehlt. Empfehlung: Netto/Brutto-Deklaration als erstes Finding im CFO-Lead-Review von Doc 02 erzwingen, dann Doc 15 v2 darauf aufbauen.
- Kassensystem nicht TSE-fähig → **Stopp**, Budgetierung Kassen-Ersatz vor Rollout.

## Neue Findings (Kandidaten für 15-findings-steuer.md)

| # | Finding | Prio | Effort | Wer | Status |
|---|---|---|---|---|---|
| 14 | Fixkosten-Allokation Retail-Strang fehlt — ohne anteiligen Overhead sieht jede variable Kalkulation profitabel aus. Cross-Ref Doc 02. | P2 | S | CFO (Doc-02-Lead-Review) | Offen |
| 15 | Gewerbesteuer-Effekt (Hebesatz 420 % Stuttgart) nicht modelliert — ca. 550–825 € bei 10–15k Retail-Gewinn. Cross-Ref Doc 02 und Doc 18. | P3 | XS | CFO (Doc-02-Lead-Review) | Offen |
| 16 | Kassensystem-worst-case-Kosten (Nachrüstung 300–500 €, Ersatz 1.500–3.000 €) als Budgetposition in Doc 12. | P2 | XS | CFO (Doc-12-Lead-Review) | Offen |
