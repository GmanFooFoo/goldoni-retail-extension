# Findings: Doc 18 – Finanzierungsplan

**Quelle:** [Lead-Review CFO](../reviews/18-finanzierungsplan-cfo.md)
**Datum:** 2026-04-13
**Status:** Offen — v2-Rewrite ausstehend (S-Effort, Propagation aus Doc 02/12/21).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **Kapitalbedarf-Zahlen veraltet.** Stufe 1 "1.500–2.200 €" → korrigiert 6.040 € brutto / 5.139 € netto (Doc 12 v2). Gesamtrahmen falsch. | P1 | XS | CFO | — | Offen | Gesamte Finanzierungslogik basiert auf falschen Eingangswerten. |
| 2 | **Break-Even falsch.** "Unter 3 Monate" → korrigiert Monat 12–13 Cashflow-BEP (Doc 02 v2). | P1 | XS | CFO | — | Offen | Silvio plant mit falscher Kapital-Rückfluss-Geschwindigkeit. |
| 3 | **BAFA-Förderung fehlt.** Bis 1.750 € Zuschuss (50 % von max. 3.500 €). Stärkstes Finanzierungsinstrument — kein Kredit, sondern Zuschuss. | P1 | S | CFO | D-11, SP-21 | Offen | Senkt Silvios Eigenkapitalbedarf um bis zu 1.750 €. |
| 4 | **L-Bank Beratungsgutschein BW fehlt.** Bis 1.920 € Zuschuss (80 % von 2.400 €). Kumulierbar mit BAFA. | P1 | XS | CFO | Doc 21 | Offen | Bis zu 3.670 € Förderpotential insgesamt. |
| 5 | **Vorsteuer-Erstattung ignoriert.** 901 € kommen in 1–2 Monaten zurück. Senkt effektiven Kapitalbedarf auf 5.139 €. | P2 | XS | CFO | — | Offen | Liquiditäts-Effekt im ersten Monat. |
| 6 | **KfW irrelevant.** Mindestbetrag 25.000 € — Goldoni liegt weit darunter. Stattdessen: Mikrokreditprogramme (Bürgschaftsbank BW). | P2 | XS | CFO | — | Offen | Falsche Option suggeriert unnötige Komplexität. |
| 7 | **Kein Liquiditäts-Puffer.** 20 % Reserve auf Stufe 1 = ~1.200 € empfohlen. Deckt: Verderb Pilotphase, verzögerte VSt, SP-06 Kasse. | P2 | XS | CFO | — | Offen | Ohne Puffer kann eine einzige ungeplante Ausgabe den Cashflow kippen. |
| 8 | **Rentabilitäts-Check ist Phantasie.** "Monat 1 amortisiert" vs. Realität (erste 2 Monate null Umsatz). Verweis auf Cashflow-Projektion nötig. | P2 | XS | CFO | — | Offen | Falsches Timing erzeugt falsche Erwartungen bei Silvio. |

## Nächste Schritte

1. [ ] v2-Rewrite Doc 18 — Propagation aus Doc 02 v2, Doc 12 v2, Doc 21. Effort: S.
2. [ ] Co-Review Steuerberaterin (lt. assignments.md) — Fördermittel-Perspektive, Liquiditäts-Planung.
