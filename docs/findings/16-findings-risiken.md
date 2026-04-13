# Findings: Doc 16 – Risiken & Gegenmaßnahmen

**Quelle:** [Lead-Review CFO](../reviews/16-risiken-cfo.md)
**Datum:** 2026-04-13
**Status:** Offen — v2-Rewrite (M-Effort, Risiko-Register aufbauen). **17 Findings** (8 Lead + 5 Co Thomas + 4 Co Vogel).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **"Nachfrage bleibt aus" falsch priorisiert.** Prio 3 / "Gering" → muss P1 / "Hoch" sein. Versunkene Kosten bei Scheitern: 3.100–4.600 €. | P1 | XS | CFO | — | Offen | Existenzielles Risiko als Nebensache dargestellt. |
| 2 | **Keine finanziellen Risiken.** Wareneinsatz-Schwankung, Provision, SP-06 Kasse, Verderb fehlen. Doc 02 v2 Kap. 9 hat die Sensitivity. | P1 | S | CFO | — | Offen | Risiko-Dokument ohne Geld-Perspektive ist unvollständig. |
| 3 | **Keine regulatorischen Stichtage.** Listerien 1.7., PPWR 12.8., ProdHaftG 9.12. — keiner erwähnt. | P1 | S | CFO + Lebensmittelrechtler | — | Offen | Compliance-Risiken bei Launch zwischen Stichtagen. |
| 4 | **Kein Haftungs-Risiko.** ProdHaftG, § 58 LFGB, Rückruf-Kosten (Doc 14). | P1 | S | Lebensmittelrechtler | — | Offen | Haftung ist das teuerste Risiko, fehlt komplett. |
| 5 | **Keine Quantifizierung.** Kein €-Betrag bei irgendeinem Risiko. | P2 | M | CFO | Doc 02 v2, Doc 14 | Offen | Ohne Zahlen keine Priorisierung und keine Investitions-Entscheidung für Gegenmaßnahmen. |
| 6 | **Personal-Risiko fehlt.** Ein-Personen-Abhängigkeit (Doc 20 Szenario C). | P2 | XS | Persona 11 | — | Offen | Cross-Ref zu Doc 20. |
| 7 | **Kein Risiko-Register.** Prosa statt Tabelle. Kein Owner, kein Trigger, keine Fälligkeit. | P2 | M | CFO | — | Offen | Standard für Business Case, fehlt. |
| 8 | **"Tagesspecial" als Verderb-Lösung buchhalterisch problematisch.** Retail-Ware als Restaurant-Portion = zwei Erlöskonten vermischt (Doc 15 v2). | P3 | XS | Steuerberaterin | — | Offen | Nicht verboten, aber sauber dokumentieren. |
| 9 | **SPOF quantifiziert: 1 Krankheitstag = 0 Retail-Output.** Silvio ist einziger Produzent. Kein Vertretungs-Szenario. Ausfall > 3 Tage = MHD-Verfall gesamter Bestand. | P1 | XS | Thomas CF-01 | Persona 11 / Doc 20 | Offen | Konkretisierung von Finding 6. Muss ins Risiko-Register mit Eintrittswahrscheinlichkeit. |
| 10 | **Einschwing-Chaos als eigenes Risiko.** Erste 4–6 Wochen: Prozess-Fehler, Chargen-Ausschuss, Kunden-Reklamationen. Kein Risiko-Eintrag dafür. | P2 | XS | Thomas CF-02 | — | Offen | Erfahrungswert Gastronomie: Einschwing-Phase produziert 20–30 % Ausschuss. |
| 11 | **Qualitäts-Drift nach Monat 3.** Anfangs hohe Motivation, dann Routine → Abkürzungen bei Temperatur-Kontrolle, Vakuum-Prüfung. Kein Monitoring-Mechanismus. | P2 | S | Thomas CF-03 | — | Offen | Risiko steigt mit der Zeit, nicht am Anfang. Checklisten-Pflicht als Gegenmaßnahme. |
| 12 | **Kannibalisierung Restaurant-Umsatz.** Stammgast kauft vakuumiert statt im Restaurant zu essen. Netto-Effekt unklar. Kein Szenario gerechnet. | P2 | S | Thomas CF-04 | CFO | Offen | Bei 5 % Substitution: ~200 €/Monat Restaurant-Verlust vs. ~150 € Retail-Gewinn = negativ. |
| 13 | **Verderb-Risiko bei 5 Produkten.** Mehr SKUs = mehr Restbestände. Bei 25 Stk/Woche und 5 Produkten: 5 Stk/Produkt — 1–2 Stk Verderb pro Woche realistisch. | P2 | XS | Thomas CF-05 | — | Offen | ~80–160 €/Monat Verderb-Kosten. Muss in Sensitivity (Doc 02 v2). |
| 14 | **Erstbegehungs-Risiko.** Vetamt kann bei Erstbegehung Auflagen erteilen, die Umbau erfordern. Kosten und Zeitverzug nicht als Risiko erfasst. | P1 | S | Inspektor Vogel CF-01 | Lebensmittelrechtler | Offen | Worst Case: 4–8 Wochen Verzögerung + 2.000–5.000 € Umbau-Kosten. |
| 15 | **Probennahme-Risiko.** Vetamt nimmt bei Kontrolle Proben — bei Beanstandung: Verkaufsstopp bis Nachprüfung. | P1 | XS | Inspektor Vogel CF-02 | — | Offen | Verkaufsstopp = Umsatz-Ausfall + Reputations-Schaden. |
| 16 | **Gebühren-Risiko unterschätzt.** Registrierung, Kontrollen, Labor-Nachprüfungen — 500–1.500 €/Jahr nicht im Budget. | P2 | XS | Inspektor Vogel CF-03 | CFO | Offen | Laufende Kosten, nicht nur einmalig. In Doc 02 v2 Fixkosten ergänzen. |
| 17 | **Rückruf als Worst Case.** Öffentlicher Rückruf (lebensmittelwarnung.de) bei Listerien-Fund. Kosten: Entsorgung + Kommunikation + ggf. Bußgeld. Nicht adressiert. | P1 | S | Inspektor Vogel CF-04 | Lebensmittelrechtler | Offen | Existenzielles Risiko. Cross-Ref Doc 14 (Haftung). |
