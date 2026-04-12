# v2-Plan: Doc 02 – Wirtschaftlichkeitsrechnung

**Datum:** 2026-04-12 (Session 11)
**Basis:** 22 Findings aus Lead-Review CFO + Co-Reviews Steuerberaterin + Persona 11
**Urteil:** Einstimmig Rework erforderlich
**Zielformat:** Vereinfachte EÜR-Struktur (Finding 20)

## Blocker vor Rewrite

| # | Blocker | Status | Ohne Blocker-Auflösung |
|---|---|---|---|
| 1 | **SP-19** — Rezepturen (Béchamel ja/nein, Gramm-Angaben) | Bei Silvio (WhatsApp 2026-04-12) | Rewrite mit Arbeitsannahme "ohne Béchamel" möglich, aber Wareneinsatz-Tabelle bleibt [A]-markiert |
| 2 | **SP-22** — Metro-/Lieferanten-Preise mit Datums-Stempel | Offen | Rewrite mit [E]-Spannen möglich, aber Quellen-Anforderung (Finding 5) nicht erfüllt |
| 3 | **SP-23** — Nachfrage-Schätzung von Silvio | Offen | Szenarien bleiben hypothetisch, Absatz-Zahlen nicht validiert |

**Empfehlung:** v2-Rewrite **jetzt mit Arbeitsannahmen und [E]/[A]-Markern** starten. Die Struktur und Logik sind das Wichtigste — Silvios Daten werden nachgezogen, sobald sie vorliegen. Jeder [E]/[A]-Marker ist ein Platzhalter mit definiertem Auflösungs-Pfad.

## Kapitelstruktur Doc 02 v2

### Kopf

```
> **Version:** v2 (YYYY-MM-DD). Rewrite auf Basis von 22 Findings.
> **Scope:** Phase 1 — Vakuum, gekühlt, 4 Produkte, Abholung + Plattform-Lieferung (D-13).
> **Netto/Brutto-Deklaration:** Alle Verkaufspreise Brutto inkl. 7 % USt.
>   Alle Kosten Netto (ohne USt), sofern nicht anders gekennzeichnet.
> **Basis-Szenario Personal:** Szenario B1 Minijob (externe Kraft, 13,90 €/h + AG-Pauschale).
```

### Kapitel 1 — Produkt-Mix und Stückpreise (→ F1, F3, F4, F5)

Alle vier Phase-1-Produkte mit:
- VK brutto + netto (F1)
- Wareneinsatz mit Quelle oder [E]-Marker (F5)
- Rezeptur-Annahme (F3, SP-19)
- Mix-Anteil (F4)

Löst: F1 (Netto/Brutto), F3 (Béchamel-Widerspruch), F4 (nur 2 Produkte), F5 (Quellen)

### Kapitel 2 — Variable Kosten pro Stück (→ F6, F22)

| Position | Herleitung |
|---|---|
| Wareneinsatz | Aus Kapitel 1 |
| Verpackung + Etikett | Spanne mit Quelle |
| Arbeitskosten | Drei Szenarien (A/B/C) aus Doc 20, Basis: B1 Minijob. Stundenlohn × AG-Pauschale ÷ Stk/h. Verweis auf Doc 20 für Details. |

Löst: F6 (Personalkosten), F22 (Herleitung)

### Kapitel 3 — Deckungsbeitrag und Abzüge (→ F7, F16, F19)

- DB/Stk vor Abzügen
- Verderb-Abzug (7,5 % Arbeitsannahme, mit Sensitivity 5/7,5/10 %) (F7)
- Plattform-Provision (D-13, 30 % Plattform-Anteil, 25 % Rate) (F19)
- Bereinigter DB/Stk
- Rohwareneinsatz-Quote korrekt berechnet (F16)

Löst: F7, F16, F19

### Kapitel 4 — Fixkosten Retail-Strang (→ F2, F14)

- Fixkosten-Allokation mit Methodik-Entscheidung: Teilkosten (Deckungsbeitrag ausweisen) oder Vollkosten (anteiliger Overhead) (F2)
- Compliance-Kosten laufend (F14): Versicherung, QM-Software, Datenlogger, HACCP-Doku
- Webshop-Hosting + Zahlungsanbieter
- Monatliche Fixkosten-Summe

Löst: F2, F14

### Kapitel 5 — Investitionen und Abschreibung (→ F9, F10, F17)

- Vollständige Investitionstabelle (Vakuumierer, Etikettendrucker, Labor, Anwalt, Vetamt, HACCP-Berater, Webshop-Setup, Versicherung Jahresprämie) (F9)
- Brutto / Netto / Vorsteuer-Erstattung pro Position
- AfA-Tabelle aus Doc 15 v2 (Vakuumierer 8 J., Drucker GWG) (F17)
- Amortisations-Rechnung mit konservativem Szenario (F10)

Löst: F9, F10, F17

### Kapitel 6 — Absatz-Szenarien (→ F8, F12, F15)

Drei Szenarien mit Herleitung:

| Szenario | Stk/Woche | Basis |
|---|---|---|
| Konservativ | 25 | Pilot-Minimum (≈ Break-Even operativ) |
| Realistisch | 50 | [A] oder SP-23-Ergebnis |
| Optimistisch | 80 | Regelbetrieb + Plattform-Effekt |

- Betriebswochen/Jahr: 46 (nicht 52) (F12)
- Nachfrage-Basis benennen (Stammgäste, Büros, Plattform-Laufkundschaft) (F15)
- Sensitivity-Tabelle: Break-Even bei X Stk/Woche (F8)

Löst: F8, F12, F15

### Kapitel 7 — Monats-P&L und Cashflow (→ F13)

Verweis auf die Cashflow-Projektion (`docs/plans/02-cashflow-projektion-2026.md`) oder integrierte Version davon. Zeigt:
- Monatliches Betriebsergebnis (nicht "Gewinnbeitrag") (F13)
- Kumulierter Cashflow
- Break-Even-Monat

Löst: F13

### Kapitel 8 — Steuerliche Eckdaten (→ F11, F20, F21)

- Gewerbesteuer-Check (Hebesatz 420 %, Freibetrag 24.500 €) (F11)
- EÜR-Zusammenfassung (F20)
- USt-Voranmeldung als Prozess (F21)
- Verweis auf Doc 15 v2 für Details

Löst: F11, F20, F21

### Kapitel 9 — Saisonalität und Risiken (→ F18)

- Saisonale Anpassung (Sommer/Winter, Ferien, Feiertage) (F18)
- Top-5-Risiken mit Kosteneffekt
- Verweis auf Doc 16 (Risiken) für die Gesamtliste

Löst: F18

### Kapitel 10 — Cross-Referenzen

Tabelle mit Verweisen auf Doc 07, 12, 15, 18, 20 und relevante Findings-Dateien.

## Finding-zu-Kapitel-Matrix

| Finding | Kapitel | Status nach v2 |
|---|---|---|
| F1 Netto/Brutto | 1 (Kopf + Tabelle) | Aufgelöst |
| F2 Fixkosten-Allokation | 4 | Aufgelöst (mit Methodik-Entscheidung) |
| F3 Béchamel-Widerspruch | 1 | Aufgelöst wenn SP-19 bestätigt, sonst [A] |
| F4 Nur 2 Produkte | 1 | Aufgelöst |
| F5 Wareneinsatz ohne Quelle | 1 | Offen bis SP-22 |
| F6 Personalkosten | 2 | Aufgelöst |
| F7 Verderb | 3 | Aufgelöst |
| F8 Sensitivity | 6 | Aufgelöst |
| F9 Investitionstabelle | 5 | Aufgelöst |
| F10 Amortisation | 5 | Aufgelöst |
| F11 Gewerbesteuer | 8 | Aufgelöst |
| F12 52 Wochen | 6 | Aufgelöst |
| F13 "Gewinnbeitrag" | 7 | Aufgelöst |
| F14 Compliance-Kosten | 4 | Aufgelöst |
| F15 Nachfrage-Beleg | 6 | Offen bis SP-23 |
| F16 Rohwareneinsatz % | 3 | Aufgelöst |
| F17 Abschreibung | 5 | Aufgelöst |
| F18 Saisonalität | 9 | Aufgelöst (qualitativ) |
| F19 Plattform-Provision | 3 | Aufgelöst |
| F20 EÜR-Struktur | 8 (+ Gesamt-Aufbau) | Aufgelöst |
| F21 USt-VA | 8 | Aufgelöst |
| F22 Personal-Herleitung | 2 | Aufgelöst |

**Bilanz: 19 von 22 Findings im v2 auflösbar. 3 bleiben offen bis Silvio-Input (SP-19, SP-22, SP-23).**

## Effort-Schätzung

| Block | Effort |
|---|---|
| v2-Rewrite Doc 02 (mit [A]/[E]-Markern) | M (halber Tag) |
| v2-Rewrite Doc 02 (nach SP-19/22/23 — Marker auflösen) | S (1–2h) |
| Cashflow-Projektion aktualisieren (nach v2-Zahlen) | XS |

## Empfehlung

v2-Rewrite in der **nächsten Session** starten — die Kapitelstruktur steht, die Logik ist klar, und 19 von 22 Findings sind ohne Silvio-Input auflösbar. Die drei offenen Findings werden als saubere [A]/[E]-Marker geführt, die Silvio-Paket-Einträge SP-19/22/23 sind der definierte Auflösungs-Pfad.
