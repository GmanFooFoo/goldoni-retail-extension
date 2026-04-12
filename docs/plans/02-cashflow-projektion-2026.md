# Cashflow-Projektion Retail-Extension — Mai bis Dezember 2026

**Erstellt von:** Marcus (CFO, Persona 01)
**Datum:** 2026-04-12 (Session 11)
**Hypothese:** Start 1. Mai 2026
**Scope:** Phase 1, nur Vakuum gekühlt, 4 Produkte, Abholung + Plattform-Lieferung (D-13)

> **Hinweis:** Diese Projektion ist eine hypothetische Rechnung auf Basis der aktuell verfügbaren Daten. Viele Eingangsgrößen sind Schätzungen (markiert mit `[E]`) oder Arbeitsannahmen (markiert mit `[A]`). Die Projektion wird belastbarer, sobald SP-19 (Rezepturen), SP-22 (Metro-Preise) und SP-23 (Nachfrage-Schätzung) aufgelöst sind.

## Annahmen

### Produkt-Mix und Stückpreise

Alle Preise **Brutto inkl. 7 % USt** (VK) bzw. **Netto** (Kosten).

| # | Produkt | VK brutto | Wareneinsatz [E] | Verpackung + Etikett [E] | Arbeitszeit [E] | Mix-Anteil [A] |
|---|---|---|---|---|---|---|
| 1 | Lasagne al Forno 400g | 13,50 € | 4,50 € | 0,50 € | 1,50 € | 30 % |
| 2 | Ragù Bolognese 350g | 9,00 € | 3,00 € | 0,45 € | 0,80 € | 25 % |
| 3 | Sugo Pomodoro 500g | 7,00 € [E] | 2,50 € [E] | 0,40 € | 0,50 € [E] | 25 % |
| 4 | Parmigiana 400g | 12,00 € [E] | 4,00 € [E] | 0,50 € | 1,30 € [E] | 20 % |

**Gewichtete Durchschnittswerte:**

| Kennzahl | Wert |
|---|---|
| ⌀ VK brutto | 10,45 € |
| ⌀ VK netto (÷ 1,07) | 9,77 € |
| ⌀ Variable Kosten/Stk (WE + Verpackung + Arbeit) | 5,03 € |
| ⌀ Deckungsbeitrag/Stk brutto | 5,42 € |
| ⌀ DB-Marge brutto | 51,9 % |

### Abzüge auf den Deckungsbeitrag

| Position | Rechnung | Effekt pro verkauftes Stk |
|---|---|---|
| **Plattform-Provision** (D-13) | 30 % der Bestellungen via Wolt/Uber [A], 25 % Provision [E] | −0,78 € |
| **Verderb** | 7,5 % der Produktion [A], Kosten umgelegt auf verkaufte Stk | −0,41 € |
| **Bereinigter DB/Stk** | 5,42 − 0,78 − 0,41 | **4,23 €** |

### Absatz-Ramp-Up

| Monat | Phase | Stk/Woche [A] | Wochen | Stk/Monat | Plattform-Anteil [A] | Verderb [A] |
|---|---|---|---|---|---|---|
| Mai | Vorbereitung | 0 | — | 0 | — | — |
| Juni | Beschaffung + Tests | 0 | — | 0 | — | — |
| Juli | Pilot | 20 | 4 | 80 | 0 % (nur Abholung) | 10 % |
| August | Ramp-Up | 35 | 4,5 | 158 | 15 % | 8 % |
| September | Regelbetrieb | 50 | 4,3 | 215 | 25 % | 7 % |
| Oktober | Regelbetrieb | 55 | 4,3 | 237 | 30 % | 6 % |
| November | Regelbetrieb | 55 | 4,3 | 237 | 30 % | 5 % |
| Dezember | Ferien-Monat | 40 | 3,5 | 140 | 30 % | 5 % |

**Annahme Dezember:** Weihnachtsferien, reduzierte Produktion. Aber möglicher Geschenkebox-Effekt (SP-20) ist **nicht** eingepreist.

### Monatliche Fixkosten Retail-Strang

| # | Position | Monatlich [E] | Erläuterung |
|---|---|---|---|
| 1 | Fixkosten-Allokation (Miete, Strom, Wasser, Reinigung anteilig) | 200 € | 10 % der geschätzten Restaurant-Fixkosten [E], Methodik TBD (Finding 2) |
| 2 | Produkthaftpflicht-Versicherung (Aufpreis) | 25 € | 300 €/Jahr [E], Angebot über SP-16 |
| 3 | HACCP-Dokumentation / QM-Software | 30 € | Q4Me oder Papier, Doc 22 |
| 4 | Datenlogger-Wartung / Kalibrierung | 10 € | Laufend |
| 5 | Verpackungs-Nachschub (Basis unabhängig von Stückzahl) | 0 € | In variablen Kosten enthalten |
| **Summe** | | **265 €/Monat** | |

Ab August: Webshop-Hosting + Zahlungsanbieter (Stripe) ca. **30 €/Monat** zusätzlich → **295 €/Monat**.

---

## Einmalige Ausgaben nach Monat

| # | Position | Mai | Juni | Juli | Summe brutto | Vorsteuer |
|---|---|---|---|---|---|---|
| 1 | Gewerbeanzeige (§ 14 GewO) | 40 € | | | 40 € | — |
| 2 | Vakuumierer Kammer (Henkelman o.ä.) | | 2.500 € | | 2.500 € | 399 € |
| 3 | Etikettendrucker (Brother QL-820NWB) | | 240 € | | 240 € | 38 € |
| 4 | Erstausstattung Verpackung (Beutel, Rollen) | | 400 € | | 400 € | 64 € |
| 5 | Testchargen Rohware | | 150 € | | 150 € | ~12 € |
| 6 | Labor-Nährwertanalyse (4 Produkte) | | | 500 € | 500 € | 80 € |
| 7 | Anwalt AGB + Datenschutz + Fernabsatz | | | 1.000 € | 1.000 € | 160 € |
| 8 | IfSG-Erstbelehrung (2 Personen) | 60 € | | | 60 € | — |
| 9 | HACCP-Berater (Update Eigenkontrollkonzept) | | 800 € | | 800 € | 128 € |
| 10 | Versicherung Produkthaftpflicht (Jahresprämie) | | | 300 € | 300 € | — |
| 11 | Webshop-Setup (Ecwid/Shopify, einmalig) | | | 200 € | 200 € | 32 € |
| | **Summe brutto** | **100 €** | **4.090 €** | **2.000 €** | **6.190 €** | |
| | **Vorsteuer-Erstattung** | — | 641 € | 272 € | | **913 €** |
| | **Effektiv netto** | **100 €** | **3.449 €** | **1.728 €** | **5.277 €** | |

---

## Monats-P&L (Gewinn- und Verlustrechnung)

### Mai — Vorbereitung

| Position | Betrag |
|---|---|
| Umsatz brutto | 0 € |
| Einmalige Ausgaben | −100 € |
| Fixkosten Retail | −265 € |
| **Ergebnis Mai** | **−365 €** |

### Juni — Beschaffung und Rezeptur-Tests

| Position | Betrag |
|---|---|
| Umsatz brutto | 0 € |
| Einmalige Ausgaben brutto | −4.090 € |
| Fixkosten Retail | −265 € |
| Vorsteuer-Erstattung (kommt in Juli-VA) | (+641 €) |
| **Cash-Abfluss Juni** | **−4.355 €** |
| **Ergebnis Juni (netto, nach Vorsteuer)** | **−3.714 €** |

### Juli — Pilot-Start (80 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **836 €** | 80 × 10,45 € |
| USt-Abführung (7 %) | −55 € | 836 / 1,07 × 0,07 |
| **Umsatz netto** | **781 €** | |
| Variable Kosten (80 Stk produziert, 72 verkauft bei 10 % Verderb) | −402 € | 80 × 5,03 € |
| Plattform-Provision | 0 € | Pilot nur Abholung |
| Fixkosten Retail | −265 € | |
| Einmalige Ausgaben brutto | −2.000 € | Labor, Anwalt, Versicherung, Webshop |
| Vorsteuer-Erstattung Juni + Juli | +913 € | |
| **Cash-Ergebnis Juli** | **−973 €** | |
| **Operatives Ergebnis (ohne Invest)** | **+114 €** | Umsatz − Variable − Fix |

### August — Ramp-Up (158 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **1.651 €** | 158 × 10,45 € |
| USt-Abführung | −108 € | |
| **Umsatz netto** | **1.543 €** | |
| Variable Kosten (158 produziert, 145 verkauft bei 8 % Verderb) | −795 € | 158 × 5,03 € |
| Plattform-Provision (15 % der Bestellungen, 25 % Rate) | −62 € | 145 × 0,15 × 10,45 × 0,25 |
| Fixkosten Retail (inkl. Webshop ab jetzt) | −295 € | |
| **Operatives Ergebnis** | **+391 €** | |

### September — Regelbetrieb (215 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **2.247 €** | 215 × 10,45 € |
| USt-Abführung | −147 € | |
| **Umsatz netto** | **2.100 €** | |
| Variable Kosten (215 produziert, 200 verkauft bei 7 % Verderb) | −1.081 € | 215 × 5,03 € |
| Plattform-Provision (25 %) | −104 € | 200 × 0,25 × 10,45 × 0,25 |
| Fixkosten Retail | −295 € | |
| **Operatives Ergebnis** | **+620 €** | |

### Oktober — Regelbetrieb (237 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **2.477 €** | 237 × 10,45 € |
| USt-Abführung | −162 € | |
| **Umsatz netto** | **2.315 €** | |
| Variable Kosten (237 produziert, 223 verkauft bei 6 % Verderb) | −1.192 € | 237 × 5,03 € |
| Plattform-Provision (30 %) | −174 € | 223 × 0,30 × 10,45 × 0,25 |
| Fixkosten Retail | −295 € | |
| **Operatives Ergebnis** | **+654 €** | |

### November — Regelbetrieb (237 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **2.477 €** | 237 × 10,45 € |
| USt-Abführung | −162 € | |
| **Umsatz netto** | **2.315 €** | |
| Variable Kosten (237 produziert, 225 verkauft bei 5 % Verderb) | −1.192 € | 237 × 5,03 € |
| Plattform-Provision (30 %) | −176 € | 225 × 0,30 × 10,45 × 0,25 |
| Fixkosten Retail | −295 € | |
| **Operatives Ergebnis** | **+652 €** | |

### Dezember — Ferien-Monat (140 Stk)

| Position | Betrag | Rechnung |
|---|---|---|
| **Umsatz brutto** | **1.463 €** | 140 × 10,45 € |
| USt-Abführung | −96 € | |
| **Umsatz netto** | **1.367 €** | |
| Variable Kosten (140 produziert, 133 verkauft bei 5 % Verderb) | −704 € | 140 × 5,03 € |
| Plattform-Provision (30 %) | −105 € | 133 × 0,30 × 10,45 × 0,25 |
| Fixkosten Retail | −295 € | |
| **Operatives Ergebnis** | **+263 €** | |

---

## Jahres-Zusammenfassung Mai–Dezember 2026

### Cashflow-Verlauf (kumuliert)

| Monat | Invest | Operativ | Monat gesamt | **Kumuliert** |
|---|---|---|---|---|
| Mai | −100 € | −265 € | −365 € | **−365 €** |
| Juni | −4.090 € | −265 € | −4.355 € | **−4.720 €** |
| Juli | −2.000 € | +114 € | +913 € VSt −973 € | **−5.693 €** |
| August | — | +391 € | +391 € | **−5.302 €** |
| September | — | +620 € | +620 € | **−4.682 €** |
| Oktober | — | +654 € | +654 € | **−4.028 €** |
| November | — | +652 € | +652 € | **−3.376 €** |
| Dezember | — | +263 € | +263 € | **−3.113 €** |

### Kennzahlen Gesamtjahr (8 Monate, davon 6 mit Umsatz)

| Kennzahl | Wert |
|---|---|
| **Gesamtproduktion** | 1.067 Stk |
| **Davon verkauft (nach Verderb)** | ~998 Stk |
| **Davon Verderb** | ~69 Stk (6,5 % gewichtet) |
| **Umsatz brutto** | 11.151 € |
| **Umsatz netto** | 10.421 € |
| **Variable Kosten gesamt** | −5.366 € |
| **Plattform-Provisionen** | −621 € |
| **Fixkosten Retail (8 Monate)** | −2.240 € |
| **Einmalige Investitionen brutto** | −6.190 € |
| **Vorsteuer-Erstattung** | +913 € |
| | |
| **Operatives Ergebnis (ohne Invest)** | **+2.694 €** |
| **Gesamt-Ergebnis inkl. Invest** | **−3.113 €** |

### Gewerbesteuer-Effekt

Bei einem operativen Ergebnis von 2.694 € (8 Monate, abzgl. Invest als AfA verteilt auf 8 Jahre) liegt der steuerliche Retail-Gewinn deutlich unter dem GewSt-Freibetrag von 24.500 €. **Keine zusätzliche Gewerbesteuer im ersten Jahr.**

### Break-Even-Analyse

| Kennzahl | Wert |
|---|---|
| Operativer Break-Even (ohne Invest) | **Juli 2026** (Monat 3, ab Pilot-Start) |
| Cashflow-Break-Even (inkl. Invest) | **ca. Mai/Juni 2027** (Monat 13–14) |
| Investition amortisiert nach | **ca. 10–11 Monate Regelbetrieb** |

Die Amortisations-Aussage "unter 3 Monate" aus Doc 02 v1 war **um Faktor 3–4 zu optimistisch**. Realistisch: die Investition ist nach **10–11 Monaten Regelbetrieb** zurückverdient — also ca. Mai/Juni 2027 bei Start Mai 2026.

---

## Sensitivity: Was kippt?

### Absatz-Untergrenze

Bei welcher Stückzahl ist das operative Ergebnis null (monatlich)?

Fixkosten: 295 €/Monat. Bereinigter DB/Stk: 4,23 €.
**Break-Even operativ: 70 Stk/Monat = ~16 Stk/Woche.**

Das liegt unter dem konservativen Szenario (20 Stk/Woche). **Die Retail-Extension trägt sich operativ schon bei geringen Mengen** — das Problem ist die Amortisation der Einmal-Investition.

### Provisions-Sensitivity

| Plattform-Anteil | Bereinigter DB/Stk | Monatl. Ergebnis (55 Stk/Woche) |
|---|---|---|
| 0 % (nur Abholung) | 5,01 € | +893 € |
| 15 % | 4,62 € | +798 € |
| 30 % (Annahme) | 4,23 € | +654 € |
| 50 % | 3,70 € | +584 € |
| 100 % (nur Plattform) | 2,81 € | +367 € |

**Selbst bei 100 % Plattform-Anteil bleibt das operative Ergebnis positiv.** Die Provision drückt die Marge, kippt aber das Geschäft nicht.

### Wareneinsatz-Sensitivity

| Wareneinsatz-Änderung | Bereinigter DB/Stk | Monatl. Ergebnis (55 Stk/Woche) |
|---|---|---|
| −10 % (günstigere Zutaten) | 4,58 € | +789 € |
| Basis | 4,23 € | +654 € |
| +10 % (Preisanstieg Rohware) | 3,88 € | +620 € |
| +20 % (deutlicher Preisanstieg) | 3,52 € | +533 € |

**Robustes Modell:** Selbst bei 20 % Wareneinsatz-Anstieg bleibt das operative Ergebnis positiv.

---

## Was diese Projektion nicht enthält

1. **Silvios Opportunitätskosten.** Wenn Silvio selbst produziert statt einen Minijobber einzustellen, fehlt seine Zeit anderswo (Restaurant-Vorbereitung, Erholung). Die Arbeitskosten in der Kalkulation (1,04 €/Stk gewichtet) unterstellen eine **externe Kraft**, nicht Silvio.
2. **Marketing-Kosten.** Kein Budget für Flyer, Social Media Ads, Plattform-Listing-Gebühren (Wolt verlangt teils Onboarding-Fee).
3. **Geschenkebox-Upside (SP-20).** Weihnachtsgeschäft könnte Dezember deutlich heben — nicht eingepreist.
4. **Saisonalität.** Alle Monate ab September gleich angenommen. Realität: Winter evtl. stärker (Comfort Food), Sommer schwächer (Terrassen-Saison).
5. **Phase-2-Investitionen.** Schockfroster, Tiefkühl — nicht in diesem Zeitraum.
6. **BAFA-Zuschuss.** Bis zu 1.750 € Rückerstattung für Germans Beratungskosten (D-11) — fließt an Silvio, nicht direkt in die Retail-P&L, verbessert aber den Gesamt-Cashflow.

---

## CFO-Fazit

**Die Retail-Extension ist kein Geld-Drucker, aber ein solides Nebengeschäft.** Das erste Teiljahr (Mai–Dezember 2026) endet mit ca. −3.100 € kumuliertem Cashflow — das ist die Investition, die sich im Laufe von 2027 amortisiert. Ab Monat 4 (August) ist die Linie operativ profitabel.

**Die ehrliche Botschaft an Silvio:** Du steckst rund 5.000–6.000 € rein, verdienst davon im ersten Jahr ca. 2.700 € operativ zurück, und bist Mitte 2027 im Plus. Ab dann sind 600–800 €/Monat Zusatzverdienst realistisch — bei 55 Stück/Woche und einer Mischung aus Abholung und Lieferung. Das sind ca. 7.000–9.000 €/Jahr netto zusätzlich zu deinem Restaurant-Geschäft.

**Risiko-Kapital:** Im Worst Case (Projekt scheitert nach Pilot) ist der Vakuumierer mit 50–70 % Restwert auf dem Gebrauchtmarkt verkäufbar. Versunkene Kosten: ca. 2.500–3.500 €. Das ist ein überschaubarer Lernverlust.

---

**Quellen Regulatorik-Scan:**
- [IHK Darmstadt — Mehrwertsteuersenkung Gastronomie 2026](https://www.ihk.de/darmstadt/produktmarken/recht-und-fair-play/steuerinfo/mehrwertsteuersenkung-fuer-die-gastronomie-ab-2026-6927450)
- [sevdesk — Gewerbesteuerhebesatz Stuttgart 2026](https://sevdesk.de/ratgeber/buchhaltung-finanzen/steuern/gewerbesteuer/gewerbesteuerhebesatz-stuttgart/)
- [IHK Stuttgart — Kleinunternehmerregelung § 19 UStG](https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/steuerrecht/umsatzsteuer-national/kleinunternehmerregelung-in-der-umsatzsteuer-1843632)

[← Zurück zur Übersicht](../../README.md)
