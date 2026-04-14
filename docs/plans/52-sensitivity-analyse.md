# Sensitivity-Analyse Doc 02 — Break-Even bei 30/40/50/60 Einheiten/Woche

> **Datum:** 2026-04-14
> **Auftrag:** Backlog #52 — Absatz-Sensitivity für die Retail-Extension. Wie verhalten sich operatives Ergebnis und Amortisations-Dauer bei unterschiedlichen Absatz-Szenarien?
> **Basis:** [Cashflow-Projektion 2026](./02-cashflow-projektion-2026.md), DB-Kennzahlen aus Doc 02 v2.
> **Cross-Ref:** Doc 02 F18 (Saisonalität), Backlog-Blocker #31 (MwSt 7 % vs. 19 %).

## Kurzurteil

**Das Geschäft trägt sich operativ schon ab 16 Stück/Woche.** Die wirkliche Frage ist nicht "lohnt sich der Betrieb", sondern "wie lange dauert die Amortisation der 5.277 € Netto-Invest". Bei 30 Stück/Woche (pessimistisches Szenario) braucht Silvio **21 Monate** Regelbetrieb. Bei 55 (Baseline) **acht**. Bei 60+ weniger als sieben. **Die 30-Stück-Linie ist der kritische Kipppunkt** — darunter wird das Projekt zum mehrjährigen Mini-Nebenverdienst ohne klaren Break-Even-Horizont.

**Empfehlung:** Das 30-Stück-Szenario als Go/No-Go-Schwelle nach 6 Monaten Regelbetrieb etablieren. Wenn Silvio Ende Q1 2027 nicht 40+ Stück/Woche stabil verkauft, ist eine ehrliche Stop/Rework-Entscheidung fällig, nicht ein "weitermachen und hoffen".

## Basis-Kennzahlen (aus [Cashflow-Projektion](./02-cashflow-projektion-2026.md))

| Kennzahl | Wert | Herkunft |
|---|---|---|
| Gewichteter VK brutto/Stk | 10,45 € | Mix Lasagne/Ragù/Sugo/Parmigiana |
| Gewichteter VK netto/Stk (7 % USt) | 9,77 € | |
| Variable Kosten/Stk | 5,03 € | Wareneinsatz + Verpackung + Arbeit |
| **Bereinigter DB/Stk** (nach Plattform 30 % + Verderb 6 %) | **4,23 €** | |
| Fixkosten Retail/Monat (ab August, mit Webshop) | 295 € | |
| Einmal-Invest brutto | 6.190 € | |
| **Einmal-Invest netto (nach Vorsteuer)** | **5.277 €** | |
| Operativer Break-Even | 16 Stk/Woche | 70 Stk/Monat |

Monat = 4,3 Wochen (Standard-Konvention dieses Plans).

## Szenario-Matrix — Operatives Monatsergebnis

| # | Stk/Woche | Stk/Monat | Op. Ergebnis/Mo | Delta zu Baseline | Kommentar |
|---|---|---|---|---|---|
| 1 | **15** | 65 | **−20 €** | −727 € | Unter Break-Even, monatlicher Mini-Verlust |
| 2 | **20** | 86 | **+69 €** | −638 € | Knapp über Null, kein Amortisations-Pfad |
| 3 | **30** | 129 | **+251 €** | −456 € | Pessimistisch, Amortisation > 1½ Jahre |
| 4 | **40** | 172 | **+432 €** | −275 € | Unterkonservativ, tragbar |
| 5 | **50** | 215 | **+614 €** | −93 € | Konservativ, gut |
| 6 | **55** | 237 | **+707 €** | Baseline | Aktuelle Projektion (Doc 02 v2) |
| 7 | **60** | 258 | **+796 €** | +89 € | Optimistisch, klarer Pfad |
| 8 | **70** | 301 | **+978 €** | +271 € | Best Case, Produktions-Obergrenze bei 1 Person |

Formel: Op. Ergebnis = Stk/Monat × 4,23 € − 295 €.

## Amortisations-Matrix — Wie lange bis der Invest drin ist?

Netto-Invest: 5.277 €. Annahme: Regelbetrieb setzt ab September 2026 ein (Monat 5). Das Teiljahr Mai–Dez 2026 endet kumulativ bei −3.113 € (Baseline 55 Stk/W). Alternative Szenarien skalieren das operative Ergebnis der Regelbetriebs-Monate (Sep–Dez).

| # | Stk/Woche | Monate Regelbetrieb bis Invest amortisiert | Kalender-Monat | Einschätzung |
|---|---|---|---|---|
| 1 | 20 | 76 Monate | 2033 (!) | Projekt operativ lebensfähig, aber kein Invest-Return. Rote Flagge. |
| 2 | 30 | 21 Monate | ~Juni 2028 | Sehr lange Amortisation, Gebrauchsverschleiß der Geräte rückt näher. |
| 3 | 40 | 12,2 Monate | ~Sep 2027 | Akzeptabel, entspricht ca. 16 Monaten ab Launch. |
| 4 | 50 | 8,6 Monate | ~Mai 2027 | Gut, 12 Monate ab Launch. |
| 5 | **55** | **7,5 Monate** | **~Apr 2027** | **Baseline Doc 02 v2** |
| 6 | 60 | 6,6 Monate | ~März 2027 | Besser als geplant. |
| 7 | 70 | 5,4 Monate | ~Feb 2027 | Best Case, Vakuumierer-AfA nachteilig ausgereizt. |

> **Hinweis zur Lesart:** "Monate Regelbetrieb" meint zusätzliche Monate nach dem Ende des operativen Break-Even-Jahres 2026 (kumulierter Cashflow −3.113 €). Die Amortisations-Rechnung ist nur Operativ-Sicht — Silvios Opportunitätskosten (seine Arbeitszeit, falls er selbst produziert) sind separat und senken die echte Marge.

## Was kippt bei MwSt 19 % statt 7 %?

Backlog-Blocker #31 ist ungeklärt: die Retail-Mitnahme könnte nach Steuerberater-Entscheidung (SP-05) mit 19 % statt 7 % USt belastet werden. Delta-Analyse:

| Kennzahl | 7 % USt (Annahme) | 19 % USt (Worst Case) | Delta |
|---|---|---|---|
| VK netto/Stk | 9,77 € | 8,78 € | −0,99 € |
| Bereinigter DB/Stk | 4,23 € | 3,33 € | −0,90 € |
| Op. Ergebnis/Mo bei 55 Stk/W | +707 € | +493 € | −214 € |
| Amortisation bei 55 Stk/W | 7,5 Monate | 10,7 Monate | +3,2 Monate |
| Op. Break-Even | 16 Stk/W | 21 Stk/W | +5 Stk/W |
| Op. Break-Even bei 30 Stk/W | +251 € | +135 € | −116 € |

**Interpretation:** MwSt-Wechsel verschlechtert alle Szenarien um ca. 30 % beim operativen Ergebnis und verlängert die Amortisation um ~3 Monate. Das Geschäft kippt nicht — aber das 30-Stück-Szenario wird zum echten Risiko-Szenario (+135 € statt +251 €). **Priorität von SP-05 / Backlog #31 bleibt hoch.**

## Kombi-Risiko — Pessimistisch × MwSt

Wenn beide Negativ-Faktoren zusammentreffen (Silvio erreicht nur 30 Stk/Woche **und** MwSt wird 19 %):

| Kennzahl | Wert |
|---|---|
| Op. Ergebnis/Mo | +135 € |
| Amortisations-Dauer | 39 Monate Regelbetrieb (~3,2 Jahre) |

Das ist kein Kipp-Szenario im Sinne "operativ defizitär", aber ein Szenario, in dem die Investition über die wirtschaftliche Nutzungsdauer des Vakuumierers (AfA 8 Jahre) gerade so eingefahren wird. **Marketing-erhöhend gegen-steuern** wäre dann nötig, um auf 40+ Stk/Woche zu kommen.

## Go/No-Go-Entscheidungspunkte (Vorschlag)

Die Sensitivity macht erst operativ nützlich, wenn sie in Entscheidungsregeln übersetzt wird. Vorschlag für Silvios Entscheidungs-Checkpoints:

| # | Zeitpunkt | Soll-Wert | Reaktion bei Unterschreitung |
|---|---|---|---|
| 1 | Ende Pilot Juli 2026 | ≥ 15 Stk/Woche | Prozess-Audit mit Pietro (Rezeptur? Preis? Sichtbarkeit?). Kein Abbruch. |
| 2 | Ende Ramp-Up August | ≥ 25 Stk/Woche | Marketing-Offensive (Jana-Paket, Instagram, Büro-Samples) vor September. |
| 3 | Ende Q3 (September) | ≥ 40 Stk/Woche | Ehrlich: wenn hier weniger, ist Regelbetrieb vermutlich ≤ 30. Invest-Amortisation hinterfragen. |
| 4 | Ende Q4 2026 | ≥ 40 Stk/Woche Durchschnitt | Baseline bestätigt oder Korrektur nach unten (Reduktion auf 2 Produkte statt 4, weniger Produktionstage). |
| 5 | **Ende Q1 2027** | **≥ 40 Stk/Woche stabil** | **Kritische Schwelle. Unterhalb: Stop-Rework-Entscheidung — entweder Phase-2-Verschiebung oder Restwert-Verkauf Vakuumierer.** |
| 6 | Mitte 2027 | ≥ 50 Stk/Woche | Tiefkühl-Invest-Gespräch kann geführt werden (Phase 2 Roadmap). |

Diese Checkpoints sind **keine Schnell-Abbruch-Regeln** — Gastronomie braucht Geduld. Aber sie geben Silvio und German eine gemeinsame Sprache, um Enttäuschung und zu langes Durchhalten zu vermeiden.

## Offene Punkte / Folge-Arbeit

| # | Punkt | Status |
|---|---|---|
| 1 | Baseline 55 Stk/W braucht Silvios Absatz-Schätzung (SP-23) | Offen |
| 2 | Wareneinsatz-Sensitivity bereits in [02-cashflow-projektion-2026.md](./02-cashflow-projektion-2026.md) enthalten, nicht dupliziert | — |
| 3 | Geschenkebox-Upside (Konzept [54-geschenkebox-konzept.md](./54-geschenkebox-konzept.md)) könnte +900 €/Jahr DB netto bringen, nicht eingerechnet | Later |
| 4 | MwSt-Entscheidung Steuerberater (SP-05, Backlog #31) | Offen |
| 5 | Sensitivity in Doc 02 v2 selbst verlinken (Cross-Ref in "Was kippt?"-Abschnitt) | Wird in nächstem Doc-02-Touch ergänzt |

---

[← Zurück zu Doc 02 Cashflow](./02-cashflow-projektion-2026.md) · [← Zurück zu Doc 02 v2](../business-case/02%20%E2%80%93%20Wirtschaftlichkeitsrechnung.md) · [← Übersicht](../../README.md)
