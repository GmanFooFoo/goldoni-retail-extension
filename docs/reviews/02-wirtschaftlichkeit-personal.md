# Co-Review: Doc 02 – Wirtschaftlichkeitsrechnung

**Reviewer:** Persona 11 (Personal-Markt & Arbeitsrecht Retail)
**Datum:** 2026-04-12
**Doc-Version:** v1
**Typ:** Co-Review (Lead: CFO Marcus)

## Regulatorik-Nachtrag (aktualisierte Arbeitsmarkt-Daten)

| Kennzahl | Wert 2026 | Quelle |
|---|---|---|
| Gesetzlicher Mindestlohn | **13,90 €/h** (seit 1.1.2026) | [BMAS](https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/mindestlohn-steigt-zum-ersten-januar-2026.html) |
| Minijob-Verdienstgrenze | **603 €/Monat** (7.236 €/Jahr) | [Minijob-Zentrale](https://magazin.minijob-zentrale.de/minijob-2026-aenderungen/) |
| Midijob-Untergrenze | 603,01 €/Monat | — |
| Mindestlohn 2027 (Ausblick) | 14,60 €/h | [Bundesregierung](https://www.bundesregierung.de/breg-de/aktuelles/mindestlohn-steigt-2391010) |

> **Korrektur Doc 20:** Die dort genannte Minijob-Grenze von "556 €" ist veraltet (Stand 2025). Seit 1.1.2026 gilt 603 €/Monat. Wird im Anschluss an diesen Review in Doc 20 korrigiert.

## Kurzurteil (1 Satz)

Doc 02 behandelt Personalkosten als einzeilige Schätzung ("Anteilige Arbeitszeit 1,00–1,50 €") ohne jede Herleitung — wer arbeitet, zu welchem Stundensatz, in welcher rechtlichen Form und mit welchen AG-Nebenkosten ist komplett offen.

## Scoring (1–5)

- **Fachliche Korrektheit:** 1 — "1,00–1,50 €" ist eine Phantasie-Zahl ohne Bezug zu Mindestlohn, AG-Kosten oder Produktivität
- **Vollständigkeit:** 1 — kein Szenario, keine Nebenkosten, keine rechtliche Form
- **Umsetzbarkeit:** 2 — die Grundstruktur (Arbeitszeit als Kostenposition) ist richtig, aber inhaltlich leer
- **Risiko-Abdeckung:** 1 — Ausfall-Risiko, Ein-Personen-Abhängigkeit, Scheinselbständigkeit nicht erwähnt

## Kernanalyse: Was kostet eine Produktionsstunde wirklich?

### Rechnung bei externer Kraft (Szenario B aus Doc 20)

| Position | Wert | Rechnung |
|---|---|---|
| Bruttolohn (Mindestlohn) | 13,90 €/h | Gesetzlich ab 1.1.2026 |
| Realistischer Lohn einfacher Koch Stuttgart | 14,50–16,00 €/h [E] | Marktüblich, Vormittags-Zuschlag für Verfügbarkeit |
| AG-Nebenkosten SV-pflichtig (~20 %) | +2,90–3,20 €/h | KV, RV, AV, PV, U1, U2, Insolvenzumlage |
| **AG-Gesamtkosten/Stunde** | **17,40–19,20 €/h** | |

### Produktivität (Einheiten pro Stunde)

| Produkt | Stk/Stunde [E] | Begründung |
|---|---|---|
| Lasagne 400g | 6–8 | Komplex: Schichten, Käse, Ofen, Abkühlen, Vakuumieren |
| Ragù 350g | 15–20 | Batch-Kochen, nur Portionieren + Vakuumieren |
| Sugo 500g | 20–25 | Einfachster Prozess, nur Kochen + Abfüllen + Vakuumieren |
| Parmigiana 400g | 6–8 | Komplex: Auberginen frittieren, Schichten, Ofen |
| **Gewichteter ⌀** | **~12 Stk/h** | Mix-gewichtet (30/25/25/20) |

### Arbeitskosten pro Stück (nach Szenario)

| Szenario | AG-Kosten/h | ÷ 12 Stk/h | Arbeitskosten/Stk |
|---|---|---|---|
| A — Ehefrau (Ehegatten-AV, Fremdvergleich) | ~17,00 €/h | ÷ 12 | **1,42 €** |
| B — Externe Kraft (SV-pflichtig) | ~18,30 €/h | ÷ 12 | **1,53 €** |
| C — Silvio selbst | 0 € explizit | — | **0 € (aber Opportunitätskosten)** |
| **Doc 02 v1** | **nicht herleitbar** | — | **1,00–1,50 € (geraten)** |

Die Spanne in Doc 02 v1 (1,00–1,50 €) trifft zufällig den richtigen Bereich für Szenario A, liegt aber für Szenario B zu niedrig. Und die Herleitung fehlt — was bedeutet, dass die Zahl jederzeit angezweifelt werden kann.

### Minijob-Check

Bei 20 h/Woche × 13,90 €/h = **1.112 €/Monat** — deutlich über der Minijob-Grenze (603 €). Ein Minijob funktioniert nur bei maximal **10 h/Woche** (603 € ÷ 13,90 € ÷ 4,3 Wochen). Das reicht für ~520 Stk/Monat (bei 12/h) — unterhalb der Regelbetrieb-Planung (237 Stk/Monat lt. Cashflow-Projektion).

Warte: 10 h/Woche × 12 Stk/h = 120 Stk/Woche? Nein — 10 h/Woche × 12 = 120 Stk/Woche ist unrealistisch. Richtig: 10 h/Woche × 4,3 Wochen = 43 h/Monat × 12 Stk/h = 516 Stk/Monat. Das übertrifft die geplante Produktion (237 Stk/Monat im Regelbetrieb). **Minijob reicht also volumenmäßig aus** — wenn die 12 Stk/h stimmen.

Korrektur: Bei 237 Stk/Monat ÷ 12 Stk/h = 19,75 Stunden/Monat = ~4,6 h/Woche. Das ist **gut unter der Minijob-Grenze** (4,6 h × 13,90 € × 4,3 = 275 €/Monat < 603 €).

**Ergebnis: Minijob ist möglich**, solange die Produktion bei ≤237 Stk/Monat bleibt und die Produktivität bei ~12 Stk/h liegt.

### AG-Kosten bei Minijob

| Position | Satz |
|---|---|
| Pauschale KV | 13 % |
| Pauschale RV | 15 % |
| Umlage U1 | 1,1 % |
| Umlage U2 | 0,22 % |
| Insolvenzumlage | 0,06 % |
| Pauschale LSt | 2 % |
| **Gesamt AG-Pauschale** | **~31,4 %** |

Bei 275 €/Monat Bruttolohn: AG-Kosten 86 €/Monat → **Gesamtkosten 361 €/Monat** für die Produktion.

Das sind **1,52 €/Stk** bei 237 Stk/Monat — fast identisch mit dem SV-pflichtigen Szenario, weil die geringere Stundenzahl den höheren Pauschalsatz kompensiert.

## Monatliche Personalkosten-Szenarien (bei 237 Stk/Monat Regelbetrieb)

| # | Szenario | Stunden/Monat | AG-Gesamtkosten/Monat | Pro Stk |
|---|---|---|---|---|
| A | Ehefrau (Minijob) | ~20 h | ~335 € | 1,41 € |
| B1 | Externe Kraft (Minijob) | ~20 h | ~361 € | 1,52 € |
| B2 | Externe Kraft (SV-Teilzeit) | ~20 h | ~366 € | 1,54 € |
| C | Silvio selbst | ~20 h | 0 € | 0 € |

**Fazit:** Der Unterschied zwischen Minijob und SV-Teilzeit ist bei diesem Volumen marginal (~5 €/Monat). Die echte Entscheidung ist A/B vs. C — also "zahle ich jemanden ~350 €/Monat oder mache ich es selbst?"

## Was Doc 02 v2 braucht

1. **Personalkosten-Block mit allen drei Szenarien** als Sensitivity-Tabelle (nicht eine Zeile mit "1,00–1,50 €")
2. **Explizite Angabe, welches Szenario die Basis-Rechnung unterstellt** (Empfehlung: Szenario B1 Minijob als Basis, Szenario C als Sensitivity-Variante)
3. **Verweis auf Doc 20** für die Herleitungen und Risiko-Abwägungen
4. **Opportunitätskosten Szenario C** zumindest benennen — nicht beziffern, aber als "versteckte Kosten" markieren

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich (bestätigt Lead-Urteil)
- [ ] Stopp

Der Personalkosten-Block ist der zweitgrößte variable Kostenposten nach dem Wareneinsatz. Ihn als Einzeiler ohne Herleitung zu führen macht die gesamte Wirtschaftlichkeitsrechnung angreifbar.
