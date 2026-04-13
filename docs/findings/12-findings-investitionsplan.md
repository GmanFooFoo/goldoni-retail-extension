# Findings: Doc 12 – Investitionsplan & Geräteausstattung

**Quelle:** [Lead-Review CFO](../reviews/12-investitionsplan-cfo.md)
**Datum:** 2026-04-13
**Status:** Offen — v2-Rewrite als nächster Schritt (S-Effort, koppelt an Doc 02 v2).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **Netto/Brutto nicht deklariert.** Alle Preise ohne Flag. Differenz bei Vakuumierer allein 200–340 € Vorsteuer. | P1 | XS | CFO | — | Offen | Effektive Investition nicht berechenbar. |
| 2 | **Nicht-Geräte-Investitionen fehlen (~2.900 €).** Anwalt, Labor, HACCP-Berater, Versicherung, Webshop, Gebühren. Doc 02 v2 hat die vollständige Liste (Kapitel 5). | P1 | S | CFO | — | Offen | Investitions-Gesamtrahmen um ~50 % zu niedrig. Steuerberater/Bank sieht unvollständige Planung. |
| 3 | **Vakuumierer-Preis zu niedrig.** 1.200–1.800 € vs. 1.500–3.500 € in Doc 02 v2 / Rollout-Plan. 1.200 € ist Haushalts-Niveau, nicht Restaurant-Kammer. | P1 | XS | CFO | SP-22 (Metro-Angebote) | Offen | Unterschätzt die Startinvestition um 700–1.700 €. |
| 4 | **Tiefkühl in Stufe 3 widerspricht D-02.** Tiefkühler und Schockfroster als Phase-1-Skalierung — D-02 schließt Tiefkühl aus Phase 1 aus. | P1 | XS | CFO | — | Offen | Scope-Drift. Muss in separaten "Phase 2"-Block verschoben werden. |
| 5 | **Kassensystem fehlt als Risiko-Position.** SP-06 (TSE-Check) kann 0 € (alles OK) oder 1.500–3.000 € (Komplettersatz) bedeuten. Muss als bedingte Position stehen. | P2 | XS | CFO | SP-06 | Offen | Ungeplanter Capex-Block, wenn Kasse nicht TSE-fähig. Stopper für Rollout. |
| 6 | **Keine AfA-Tabelle.** GWG vs. Aktivierung, Nutzungsdauer, jährlicher AfA-Betrag. Steuerberater braucht das. Daten existieren in Doc 15 v2. | P2 | XS | CFO | — | Offen | Propagation aus Doc 15 v2. |
| 7 | **Vorsteuer-Erstattung nicht berücksichtigt.** 901 € Erstattung bei 6.040 € brutto Invest. Cashflow-Effekt im ersten Monat. | P2 | XS | CFO | — | Offen | Propagation aus Doc 02 v2. |
| 8 | **Kühlvitrine fraglich.** 800–1.500 € "Komfort"-Investition — braucht Silvio das bei Plattform-Lieferung (D-13)? Verändert Restaurant-Ambiente. Silvio-Entscheidung, nicht CFO-Empfehlung. | P3 | XS | Gastronom-Praktiker | — | Offen | Optionaler Invest, der vorschnell als "Stufe 2" eingeordnet ist. |
| 9 | **Bezugsquellen ohne Preisvergleich.** Keine konkreten Angebote, nur Hersteller-Namen und Großhändler. Für Steuerberater/Bank: 2–3 Angebote nötig. | P3 | S | CFO | SP-22 | Offen | Glaubwürdigkeit der Kalkulation. |

## Auflösungs-Gruppen

**Gruppe A — Propagation aus Doc 02 v2:** Findings 1, 2, 3, 6, 7 — alle Daten existieren bereits in Doc 02 v2 (Kapitel 5) und Doc 15 v2. Einfache Übernahme.

**Gruppe B — Scope-Korrektur:** Findings 4 (Tiefkühl raus), 8 (Kühlvitrine hinterfragen) — strukturelle Anpassungen.

**Gruppe C — Silvio-Input:** Findings 5 (SP-06 Kasse), 9 (SP-22 Angebote) — braucht Silvios Daten.

## Nächste Schritte

1. [ ] v2-Rewrite Doc 12 — weitgehend ein Abgleich mit Doc 02 v2 Kapitel 5 + AfA/Vorsteuer aus Doc 15 v2. Effort: S (1–2h).
2. [ ] Co-Review Bruno (Logistiker) lt. assignments.md — Geräte-Praxistauglichkeit.
