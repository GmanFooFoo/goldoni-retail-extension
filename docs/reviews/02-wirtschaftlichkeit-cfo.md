# Review: Doc 02 – Wirtschaftlichkeitsrechnung

**Reviewer:** Marcus (CFO / Zahlen-Realist, Persona 01)
**Datum:** 2026-04-12
**Doc-Version:** v1

## Regulatorik-Nachtrag (Rule 9 — Dr. Maldini, Persona 10)

**Scan-Datum:** 2026-04-12
**Betroffene Rechtsgebiete:** Umsatzsteuer, Gewerbesteuer, Kleinunternehmerregelung

| Thema | Status | Quelle | Relevanz für Doc 02 |
|---|---|---|---|
| 7 % USt auf Speisen (Gastronomie + Mitnahme) | Bestätigt seit 1.1.2026 (Steueränderungsgesetz 2025) | [IHK Darmstadt](https://www.ihk.de/darmstadt/produktmarken/recht-und-fair-play/steuerinfo/mehrwertsteuersenkung-fuer-die-gastronomie-ab-2026-6927450), [Bundesregierung](https://www.bundesregierung.de/breg-de/aktuelles/steueraenderungsgesetz-bundesrat-2383684) | Doc 02 muss alle Preise als "Brutto inkl. 7 % USt" deklarieren. Kein 19 %-Risiko mehr. |
| Gewerbesteuer-Hebesatz Stuttgart | 420 % (unverändert 2026) | [sevdesk](https://sevdesk.de/ratgeber/buchhaltung-finanzen/steuern/gewerbesteuer/gewerbesteuerhebesatz-stuttgart/), [stuttgart.de](https://www.stuttgart.de/rathaus/finanzen/steuern-und-abgaben/gewerbesteuer) | Effektiver GewSt-Satz: 3,5 % × 420 % = 14,7 %. Muss in die Jahresbetrachtung. |
| Kleinunternehmerregelung § 19 UStG | Grenzen: 25.000 € Vorjahr / 100.000 € laufend (seit 1.1.2025) | [IHK Stuttgart](https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/steuerrecht/umsatzsteuer-national/kleinunternehmerregelung-in-der-umsatzsteuer-1843632) | Realistisches Szenario (54.000 €/Jahr) überschreitet 25.000 €-Grenze — Silvio ist **kein** Kleinunternehmer im Retail-Strang. USt-Voranmeldung Pflicht. |

**Keine Gesetzesänderungen seit Doc-15-Review (2026-04-11).** Die drei Rechts-Stichtage H2/2026 (Listerien 1.7., PPWR 12.8., ProdHaftG 9.12.) betreffen Doc 02 nicht direkt, aber ihre Kosten-Implikationen (Laborkosten, Verpackungs-Konformität, Chargen-Doku-Aufwand) fehlen in der Kalkulation.

## Kurzurteil (1 Satz)

Das Dokument ist eine Skizze mit groben Spannen statt einer belastbaren Wirtschaftlichkeitsrechnung — es fehlen Netto/Brutto-Deklaration, Fixkosten-Allokation, Verderb, Personalkosten, Gewerbesteuer und Sensitivity-Analyse, sodass keine der genannten Margen oder Gewinnzahlen verwendbar ist.

## Scoring (1–5)

- **Fachliche Korrektheit:** 2 — Grundstruktur (Wareneinsatz → Deckungsbeitrag) korrekt, aber keine Zahl ist belegt, Netto/Brutto unklar, Rohwaren-Tabelle widerspricht SP-19 (Béchamel-Zutaten trotz "ohne Béchamel"-Annahme)
- **Vollständigkeit:** 1 — Fixkosten-Allokation, Verderb, Personalkosten Retail, Gewerbesteuer, Abschreibung, Compliance-Kosten, Sensitivity-Analyse — alles fehlt
- **Umsetzbarkeit:** 2 — Break-Even-Aussage ("unter 3 Monate") ist ungeprüft und basiert auf dem optimistischen 50-Einheiten-Szenario, nicht auf dem konservativen
- **Risiko-Abdeckung:** 1 — kein einziges Risiko modelliert, kein Worst Case, keine Nachfrage-Varianz, keine Preisschwankung

## Red Flags

1. **Netto/Brutto nirgends deklariert.** Sämtliche Preise (Verkauf, Einkauf, Kosten) tragen kein Flag. Bei 7 % USt ist der Fehler ~6,5 % auf jede Zahl — in absoluten Zahlen ca. 2.100 €/Jahr Verzerrung im realistischen Szenario. Ohne Deklaration ist die gesamte Margen-Rechnung nicht interpretierbar.

2. **Fixkosten-Allokation fehlt komplett.** "Energie + Overhead: 0,30–0,50 €" ist eine Pauschalschätzung ohne Herleitung. Keine anteilige Miete, keine Küchen-Abschreibung, keine Reinigung, kein Versicherungs-Anteil. Ohne Allokation subventioniert das Restaurant den Retail-Strang verdeckt — die Antwort "lohnt sich Retail?" ist nicht beantwortbar.

3. **Rohwaren-Tabelle widerspricht SP-19.** Position "Butter, Mehl, Milch — pauschal 12–16 €" sind klassische Béchamel-Zutaten. SP-19-Arbeitsannahme: "ohne Béchamel, ohne Ei". Entweder stimmt die Kalkulation nicht, oder die Rezeptur-Annahme ist falsch. Beides macht den Wareneinsatz unbelastbar.

4. **Amortisation "unter 3 Monate" basiert auf 50 Einheiten/Woche** — das ist das "realistische" Szenario, nicht das konservative. Bei 20 Einheiten/Woche (konservativ) liegt die Amortisation bei 6–9 Monaten. Die pauschale Aussage ist irreführend.

## Fundierte Kritikpunkte

### K1 — Nur zwei von vier Produkten kalkuliert

Doc 02 rechnet Lasagne und Ragù. Sugo Pomodoro und Parmigiana di Melanzane fehlen. Ohne alle vier Phase-1-Produkte ist kein Produkt-Mix möglich, keine Kannibalisierungs-Prüfung, kein gewichteter Deckungsbeitrag.

### K2 — Wareneinsatz ohne Quellen

Alle Preise tragen Spannen ("4,50–5,50 €") ohne Lieferantenbeleg. Kein Metro-Preis, kein Großhändler-Angebot, kein Datums-Stempel. Die Persona-Scoring-Matrix verlangt Quellen für >70 % der Positionen — hier sind es 0 %.

### K3 — Personalkosten nicht eingepreist

"Anteilige Arbeitszeit: 1,00–1,50 €" für eine 400g-Lasagne ist eine reine Schätzung. Fragen: Wer macht die Arbeit? Silvio selbst (Opportunitätskosten seines Restaurant-Stundensatzes)? Ein Minijobber (Personalkosten mit AG-Anteil)? Wie viele Einheiten pro Stunde? Ohne das ist die Arbeitskosten-Position Fiktion.

### K4 — Verderb nicht modelliert

Kein Posten für weggeworfene Ware. Bei 5–10 % Verderb (branchenüblich in der Frische-Produktion, insbesondere Phase 1 ohne Erfahrungswerte) sind das im realistischen Szenario ca. 1.170 €/Jahr reiner Rohstoff. Der Deckungsbeitrag sinkt um 5–10 Prozentpunkte.

### K5 — Gewerbesteuer fehlt

Stuttgart Hebesatz 420 %. Effektiver GewSt-Satz 14,7 %. Im realistischen Szenario (24.000 € Deckungsbeitrag minus Freibetrag 24.500 € bei Einzelunternehmen) fällt bei korrekter Rechnung möglicherweise keine GewSt an — aber genau das muss durchgerechnet werden, nicht einfach weggelassen. Im optimistischen Szenario (ca. 48.000 € DB) wäre es real relevant.

### K6 — Investitionstabelle unvollständig

Fehlende Positionen: Schockfroster/Schnellkühler (1.500–4.000 €, je nach Gerät — in Doc 05 als operativ notwendig identifiziert), Labor-Nährwertanalyse (320–600 € für 4 Produkte, SP-11), BAFA-Beratungskosten (anteilig), Erstbegehungs-Gebühren Vetamt, AGB-Erstellung durch Anwalt. Die Investitions-Spanne "3.000–4.500 €" ist unrealistisch niedrig — realistisch eher 5.500–9.000 €.

### K7 — Umsatzszenarien nicht sauber

- **Konservativ (20 Lasagne + 15 Ragù = 35 Stk):** Widerspricht Inconsistency #2 — Doc 13 plant mit 25–30/Woche
- **Realistisch (50 + 30 = 80 Stk):** Kein Beleg für die Nachfrage. Woher kommen 80 Portionen/Woche? Stammgast-Basis? Büro-Kunden?
- **Optimistisch (100 + 60 = 160 Stk):** 160 Portionen bei 5 Öffnungstagen = 32/Tag. Bei Abholzeitraum 17–22 Uhr = ca. 6 Abholungen/Stunde. Realistisch? Kühl-Lagerkapazität geprüft?
- Alle drei Szenarien rechnen nur mit Lasagne und Ragù — Sugo und Parmigiana sind nicht eingepreist

### K8 — Jahresbetrachtung nicht nachvollziehbar

"Umsatz ca. 54.000 €, Deckungsbeitrag ca. 24.000 €" — die Rechnung: 1.050 €/Woche × 52 = 54.600 €. Aber: Goldoni hat Mo/Di geschlossen und vermutlich Betriebsferien. Bei 46 Wochen (6 Wochen Ferien/Feiertage/Krankheit): 48.300 €. Das sind 10 % weniger. Der "Gewinnbeitrag 19.500–21.000 €" zieht nur Investitionskosten ab, keine laufenden Kosten (Verpackung, Etiketten, Verderb, Personal, Energie). Das ist kein Gewinn, das ist ein Rohertrag vor allen variablen und fixen Kosten.

### K9 — "Rohwareneinsatz ~25 %" — Rechencheck

Behauptung: Rohwareneinsatz bei Vollverkauf ~25 %. Rechnung: Rohware 182–225 € für 40 Lasagne + 20 Ragù. Umsatz bei Mittelwert: 40 × 13,50 + 20 × 9,00 = 720 €. Rohwareneinsatz: 203/720 = 28,2 %. Die 25 % stimmen nur am unteren Rand der Rohwaren-Spanne bei gleichzeitig oberem Rand der Verkaufspreise. "Sehr gut" ist eine Bewertung, keine Analyse.

### K10 — Keine Compliance-Kosten

Die Reviews der Gate-Docs haben erhebliche Compliance-Kosten identifiziert, die in Doc 02 nicht auftauchen:
- HACCP-Schulung und -Dokumentation (laufend)
- Chargen-Doku-System (Formularblock oder Digital)
- Rückstellproben-Lagerung (Kühlkapazität)
- Verpackungs-Konformitätserklärung (ab 12.8.2026, PPWR)
- Produkthaftpflicht-Versicherung (Aufpreis auf bestehende Gastro-Police)
- Regelmäßige Temperatur-Datenlogger (Kalibrierung + Batterie)

## Was fehlt

1. **Netto/Brutto-Deklaration** im Doc-Kopf (analog Doc 15 v2)
2. **Fixkosten-Allokation** mit transparenter Methodik (Vollkosten vs. Teilkosten, Prozentsatz-Schlüssel)
3. **Vollständige Produktpalette** (Sugo, Parmigiana ergänzen)
4. **Sensitivity-Analyse** (Break-Even bei 20/30/40/50/60 Einheiten, Wareneinsatz ±10 %)
5. **Verderb-Position** (5–10 % Schwund, Warenvernichtungsprotokoll-Kosten)
6. **Personalkosten-Block** (Minijob vs. Silvio-Eigenleistung vs. Ehegatten-Arbeitsvertrag, Stundensatz × Stunden/Woche)
7. **Gewerbesteuer-Rechnung** (Hebesatz 420 %, Freibetrag 24.500 € EU)
8. **Compliance-Kosten** (laufend + einmalig, siehe K10)
9. **Saisonalitäts-Anpassung** (Sommer = mehr Restaurantgäste oder weniger? Ferienzeiten?)
10. **Investitionstabelle erweitern** (Schockfroster, Labor, Anwalt, Vetamt-Gebühren)
11. **Break-Even-Rechnung** mit echten Zahlen statt pauschaler "unter 3 Monate"-Behauptung
12. **Abschreibungs-Tabelle** (aus Doc 15 v2 übernehmen: Vakuumierer 8 Jahre, Etikettendrucker 3 Jahre)

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich
- [ ] Stopp — geht so nicht live

**Begründung:** Das Dokument ist nicht falsch im Sinne von "die Grundlogik stimmt nicht" — der Aufbau (Investition → Stückkosten → Szenarien → Jahresbetrachtung) ist richtig. Aber es ist so unvollständig, dass keine belastbare Aussage möglich ist. Kein Steuerberater und keine Bank würde diese Rechnung ohne Rückfragen akzeptieren. Das Rework-Urteil (nicht Stopp) kommt daher, dass die Struktur steht und die Lücken alle füllbar sind — es fehlt Fleisch auf den Knochen, nicht das Skelett.

**Eskalations-Check:**
- Break-Even im realistischen Szenario → wahrscheinlich unter 12 Monate, aber nicht geprüft → kein Stopp
- MwSt geklärt (7 %) → kein Stopp
- Phase-1-Scope trägt die Wirtschaftlichkeit → nicht prüfbar ohne vollständige Kalkulation → Rework
- Wareneinsatz ohne Quelle bei >30 % der Positionen → **ja, 100 % ohne Quelle → Rework**
