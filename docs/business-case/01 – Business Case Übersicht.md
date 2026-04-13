# Doc 01 — Business Case Übersicht

> **Version:** v2 (2026-04-13, Session 14)
> **Zweck:** Dach-Dokument. Wer nur dieses Doc liest, soll in 2 Minuten verstehen: Was? Warum? Wie viel? Welche Risiken? Der Rest lebt in den Einzel-Docs.
> **Basis:** Propagation aus Doc 02 v2 (Wirtschaftlichkeit), Doc 12 v2 (Investitionsplan), Doc 13 v2 (Rollout), Doc 20 v2 (Personal). 10 Findings aufgelöst.
> **Alle Zahlen mit Quellen.** Kein Bauchgefühl.

## Ausgangssituation

**Ristorante Goldoni**, Stuttgart West. Eingesessenes, beliebtes italienisches Restaurant. Inhaber: Silvio [TBD-Silvio]. Öffnungszeiten: **Mi + Do–So, 17–22 Uhr**. Ruhetage: Montag und Dienstag.

**Vorhaben:** Selbst hergestellte Speisen vakuumverpackt und gekühlt an Restaurantgäste und über Lieferplattformen verkaufen. Produktion vormittags (9–14 Uhr) in der bestehenden Küche, außerhalb der Service-Zeiten.

**Phase 1 — nur Vakuum, gekühlt.** Kein Tiefkühl, kein Schockfroster, kein Paketversand. Tiefkühl ist auf Phase 2 vertagt (D-02), frühestens nach 6–12 Monaten stabilem Betrieb.

## Was wird verkauft? (5 Produkte)

| # | Produkt | Portion | VK brutto (inkl. 7 % USt) | DB/Stk | DB-Marge |
|---|---|---|---|---|---|
| 1 | Lasagne Classica (Ragù) | 400g | 13,50 € | 6,26 € | 46,4 % |
| 2 | Lasagne Verdure (Gemüse-Ricotta) | 400g | 12,00 € | 6,48 € | 54,0 % |
| 3 | Ragù Bolognese | 350g | 9,00 € | 4,65 € | 51,7 % |
| 4 | Sugo Pomodoro | 500g | 7,00 € | 4,03 € | 57,6 % |
| 5 | Parmigiana di Melanzane | 400g | 12,00 € | 7,16 € | 59,7 % |

Gewichteter Durchschnitt: **10,85 € VK, 5,72 € DB/Stk, 52,7 % DB-Marge brutto** (41,4 % bereinigt nach Plattform-Provision und Verderb). Quelle: Doc 02 v2.

## An wen und wie? (Vertriebskanäle)

| Stufe | Kanal | Zeitpunkt | Marge |
|---|---|---|---|
| 1 | **Abholung im Restaurant** (Stammgäste, Kellner-Empfehlung) | Tag 1 | Volle Marge |
| 2 | **Webshop-Vorbestellung** (Stripe, Abholung) + **Wolt/Uber Eats** | Woche 2–4 | Webshop: volle Marge. Plattform: −15–30 % Provision |
| 3 | **Abo-Modell** + ggf. Kooperationen | Monat 4–6 | Volle Marge |

Entscheidungen: D-12 (Vorbestellungen Phase 1), D-13 (Abholung + Wolt/Uber, kein Versand). Details: Doc 09 v2.

## Was kostet es?

### Einmalige Investition

| Position | Brutto | Netto (nach Vorsteuer) |
|---|---|---|
| Vakuumierer Kammer | 2.500 € [E] | 2.101 € |
| HACCP-Berater | 800 € | 672 € |
| Anwalt (AGB + DSGVO + Fernabsatz) | 1.000 € | 840 € |
| Labor-Nährwertanalyse (5 Produkte) | 500 € | 420 € |
| Etikettendrucker + Verpackung + Kleinmaterial | 640 € | 538 € |
| Webshop-Setup | 200 € | 168 € |
| Behörden (IfSG, Gewerbe) | 100 € | 100 € |
| Versicherung Produkthaftpflicht (1. Jahr) | 300 € | 300 € |
| **Gesamt** | **6.040 €** | **5.139 €** |

Falls Silvios vorhandener Henkelman ausreicht: **−2.500 € → Gesamt ~3.540 € brutto**.

Quelle: Doc 12 v2.

### Laufende Kosten

| Position | Monatlich |
|---|---|
| Personalkosten (Minijob, Szenario B1) | ~381 € |
| Fixkosten Retail (Versicherung, QM, Webshop, Allokation) | ~295 € |
| Compliance (HACCP-Schulung, IfSG, Kalibrierung) | ~28 € |
| **Gesamt laufend** | **~704 €/Monat** |

Quelle: Doc 02 v2, Doc 20 v2.

## Was bringt es?

### Drei Szenarien

| Szenario | Stk/Woche | Monatsumsatz brutto | Betriebsergebnis/Monat | Jahresergebnis |
|---|---|---|---|---|
| **Konservativ** | 25 | ~1.175 € | ~200 € | ~2.400 € |
| **Realistisch** | 50 | ~2.350 € | ~650 € | ~7.800 € |
| **Optimistisch** | 80 | ~3.760 € | ~1.200 € | ~14.400 € |

### Amortisation

- **Operativer Break-Even:** ab 15 Stk/Woche (Doc 02 v2)
- **Cashflow-Break-Even:** Monat 12–13 nach Start (realistisches Szenario, inkl. Ramp-Up)
- **Bei Abbruch nach Pilot:** Versunkene Kosten ~2.500–3.500 € (Vakuumierer-Restwert 50–70 %)

> **Korrektur zu v1:** "Amortisation unter 3 Monate" war um Faktor 4 zu optimistisch. Basierte auf unvollständiger Investitionstabelle und überschätztem Absatz.

## Wie lange dauert es?

**10–12 Wochen** vom Silvio-Ja bis zum Launch (Worst Case 14–16 bei Iterationsschleifen). Vier Phasen, gate-basiert:

| Phase | Dauer | Gate |
|---|---|---|
| I — Fundament (Behörden, Beschaffung, Personal) | Woche 1–4 | Vetamt positiv, Geräte bestellt |
| II — Produktion & Test (Rezeptur, MHD, Labor) | Woche 3–8 | Mind. 3/5 Produkte tragen 7 Tage |
| III — Pilot (Stammgäste, begrenztes Volumen) | Woche 8–10 | Nachkauf-Rate > 50 %, Beutelschäden < 2/50 |
| IV — Launch (Regelbetrieb) | ab Woche 10–12 | — |

Kritischer Pfad: **Vetamt** (4–8 Wochen) → **Haltbarkeitstests** (3–5 Wochen) → **Labor** (2–3 Wochen). Details: Doc 13 v2.

## Personal

Pilot: **Silvio selbst** (Szenario C, 4–6 Wochen). Dauerbetrieb: **Ehefrau oder externe Kraft** (Szenario A oder B, 690–1.000 €/Monat). Personalsuche startet in Woche 1–2, nicht nach dem Pilot. Details: Doc 20 v2.

## Top-5-Risiken

| # | Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|---|
| 1 | **Nachfrage bleibt unter Break-Even** (< 15 Stk/Woche) | Mittel | Retail-Strang defizitär | Pilot-Gate (Doc 13 v2): < 30 % Nachkauf → Stopp |
| 2 | **Vetamt verlangt Küchen-Umbau** | Niedrig–Mittel | Invest-Sprung oder Stopp | Gate I: Voranfrage vor jeder Investition |
| 3 | **SPOF Silvio** — Inhaber ist einziger Wissensträger | Hoch | Restaurant + Retail fallen gleichzeitig aus | Misch-Modell M (Doc 20 v2): Ablösung ab Monat 2 |
| 4 | **Regulatorik-Stichtage** (Listerien 01.07., PPWR 12.08., ProdHaftG 09.12.2026) | Sicher (Gesetz) | Compliance-Anforderungen ändern sich | Launch-Timing-Entscheidung (SP-13), PPWR-konforme Beutel von Anfang an |
| 5 | **Haltbarkeit reicht nicht** (< 7 Tage bei einem Produkt) | Mittel | Sortiment-Reduktion oder MHD-Verkürzung | Haltbarkeitstests mit 2–3 Iterationen (Doc 13 v2 Phase II) |

Details: Doc 16 v2 (Risiko-Register mit Euro-Beträgen).

## Stärken des Modells

1. **Bestehende Küche + Lieferanten** — keine Infrastruktur-Investition (außer Vakuumierer)
2. **Stammkunden-Vertrauen** — 25 Jahre Beziehung, kein Kaltstart (aber: Stammgäste ≠ automatische Käufer, Nachfrage-Aufbau nötig)
3. **Freie Vormittags-Kapazität** — Küche steht 9–14 Uhr leer, Produktion stört den Service nicht
4. **Niedriges Risiko-Kapital** — max. ~5.000 € netto, davon ~2.500 € versunken bei Abbruch
5. **First Mover in Stuttgart** — kein identifizierter Wettbewerber für vakuumierte Restaurant-Gerichte (Doc 17 v2)

## Offene Entscheidungen (Silvio)

| # | Entscheidung | Referenz | Impact |
|---|---|---|---|
| 1 | Grundsatz-Ja zur Retail-Extension | SP-13 | Ohne Ja kein Start |
| 2 | Launch-Timing (vor/nach PPWR 12.08.2026) | SP-13 | Compliance-Anforderungen |
| 3 | Personal-Szenario (Ehefrau / extern / selbst) | Doc 20 v2, SP-04 | Kosten 0–1.000 €/Monat |
| 4 | Vakuumierer: vorhandener Henkelman ausreichend? | SP-22 | Invest ±2.500 € |

## Dokument-Navigation

| Doc | Thema | Version |
|---|---|---|
| **02** | Wirtschaftlichkeitsrechnung | v2 |
| **04** | LMIV-konforme Etikettierung | v2 |
| **05** | HACCP-Konzept | v2 |
| **07** | Preisgestaltung | v2 |
| **08** | Verpackungsstrategie | v2 |
| **09** | Verkaufsstrategie | v2 |
| **10** | Operative Umsetzung | v2 |
| **11** | Lieferanten und Zutaten | v2 |
| **12** | Investitionsplan | v2 |
| **13** | Rollout-Plan und Meilensteine | v2 |
| **16** | Risiko-Management | v2 |
| **17** | Wettbewerbsanalyse | v2 |
| **19** | Sortimentserweiterung | v2 |
| **20** | Personal-Setup | v2 |
| 03 | Veterinäramt / Registrierung | v1 |
| 06 | Mockups / Etikett-Entwurf | v1 (visuell ausstehend) |
| 14 | Recht und Haftung | v2 |
| 15 | Steuerliche Einordnung | v2 |
| 18 | Finanzierungsoptionen | v2 |

---

[Zurück zur Übersicht](../../README.md)
