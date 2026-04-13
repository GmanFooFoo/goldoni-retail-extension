# Doc 11 — Lieferanten und Zutaten-Management

> **Version:** v2 (2026-04-13, Session 14)
> **Basis:** 11 Findings aus Thomas (Gastronom, Lead) + Pietro (Küchenchef, Co-Review).
> **Findings aufgelöst:** F-01 bis F-11 (alle 11). Siehe `docs/findings/11-findings-lieferanten.md`.
> **Scope:** Phase 1 — 5 Produkte (Lasagne Classica, Lasagne Verdure, Ragù Bolognese, Sugo Pomodoro, Parmigiana di Melanzane).
> **Preise:** Alle Einkaufspreise sind Schätzwerte [E] auf Basis von Premium-Großhandels-Niveau. Echte Preise mit Datums-Stempel stehen aus (SP-22). Die Schätzwerte sind konservativ (eher zu hoch), damit die Kalkulation bei echten Preisen eher besser als schlechter ausfällt.

## Lieferanten-Übersicht

| # | Lieferant | Standort | Sortiment | Modus | Status |
|---|---|---|---|---|---|
| 1 | **Di Gennaro Handelszentrum** | Von-Pistorius-Str. 1, 70188 Stuttgart-Ost | Premium-Import: Büffelmozzarella, Parmigiano 24M, San Marzano DOP, Olivenöl EV, frische Lasagneplatten | Lieferung oder Abholung [TBD-Silvio SP-22] | Bestandskunde |
| 2 | **Metro** | Weil im Dorf | Standard: Bio-Rinderhack, Gemüse, Kräuter, Verpackungsmaterial | Abholung (Selbstbedienung) | Bestandskunde |
| 3 | **Allfo.de** (Online) | Versand | Vakuumbeutel (250×350mm, 500er-Pack) | Online-Bestellung, Lieferung 2–3 Werktage | Neu, evaluiert |
| 4 | **Bos Food** (Backup) | Online, 24h-Lieferung | Premium-Notfall: Büffelmozzarella, Parmigiano, Spezialitäten | Online-Bestellung, Express möglich | Identifiziert, nicht aktiv |

**Seelgroß** (Feuerbach): In v1 als "zu prüfen" geführt. Kein Alleinstellungsmerkmal gegenüber Metro. Gestrichen. Falls Metro-Qualität nicht reicht, ist Transgourmet (Online-Großhandel) die Alternative, nicht Seelgroß.

### Backup-Strategie (Thomas F-02)

| Kern-Zutat | Primär-Lieferant | Backup | Umschaltzeit |
|---|---|---|---|
| Büffelmozzarella | Di Gennaro | **Bos Food** (Online, 24h Express) | 1 Tag |
| Parmigiano 24M | Di Gennaro | **Bos Food** oder Metro (niedrigere Qualitätsstufe) | 1 Tag |
| San Marzano DOP (Dosen) | Di Gennaro | **Metro** (DOP-Dosentomaten vorhanden) | sofort |
| Bio-Rinderhack | Metro | **Bio-Metzgerei Stuttgart** (Fettgehalt bestellbar) | 1–2 Tage |
| Frische Lasagneplatten | Di Gennaro | **Eigenherstellung** (Silvio kann Pasta machen) | gleicher Tag |
| Olivenöl EV | Di Gennaro | Metro oder Online (Gustini) | 2–3 Tage |

Ein Lieferant fällt aus → Plan B ist dokumentiert und aktivierbar. Kein Sprint zum Supermarkt.

## Zutaten-Steckbrief-Tabelle (Pietro-Empfehlung)

### Lasagne Classica (400g)

| Zutat | Lieferant | Menge/Portion | Preis/kg [E] | Qualitätskriterium | Haltbarkeit ab Einkauf | Backup |
|---|---|---|---|---|---|---|
| Bio-Rinderhack (mind. 15 % Fett) | Metro | 200g | 14,00 € | Fettgehalt 15–20 %, nicht unter 15 % (Ragù wird sonst trocken) | 2–3 Tage (Kühlware) | Bio-Metzgerei |
| San Marzano DOP Pelati | Di Gennaro | 100g | 5,00 € | DOP-Zertifikat auf der Dose, ganze geschälte Tomaten | 12+ Monate (Dosenware) | Metro |
| Frische Lasagneplatten | Di Gennaro | 80g | 6,00 € | Frisch, nicht getrocknet | 3–5 Tage | Eigenherstellung |
| Büffelmozzarella | Di Gennaro | 50g | 14,00 € | DOP oder Campana, **125g-Einzelportionen** (kein Großgebinde) | **3–5 Tage** — kritisch! | Bos Food Express |
| Parmigiano Reggiano 24M | Di Gennaro | 20g | 24,00 € | 24 Monate Reifung, DOP-Stempel | 4–6 Wochen (Stück, vakuumiert) | Bos Food |
| Soffritto (Zwiebel, Karotte, Sellerie) | Metro | 40g | 2,00 € | Frisch, nicht vorgeschnitten | 5–7 Tage | Jeder Supermarkt |
| Olivenöl EV | Di Gennaro | pauschal | 8,00 €/L | Extra Vergine, erste Pressung | 12+ Monate | Metro |

### Lasagne Verdure (400g)

| Zutat | Lieferant | Menge/Portion | Preis/kg [E] | Qualitätskriterium | Haltbarkeit ab Einkauf | Backup |
|---|---|---|---|---|---|---|
| Gemüse (Zucchini, Aubergine, Paprika, Spinat) | Metro | 180g | 4,00 € | Frisch, saisonal, keine Convenience-TK | 3–5 Tage | Jeder Großmarkt |
| Ricotta | Di Gennaro oder Metro | 80g | 8,00 € | Frisch, Fettgehalt 10–15 % | 5–7 Tage | Metro |
| San Marzano DOP Pelati | Di Gennaro | 80g | 5,00 € | Wie Classica | 12+ Monate | Metro |
| Frische Lasagneplatten | Di Gennaro | 80g | 6,00 € | Wie Classica | 3–5 Tage | Eigenherstellung |
| Büffelmozzarella | Di Gennaro | 50g | 14,00 € | Wie Classica | **3–5 Tage** | Bos Food Express |
| Parmigiano Reggiano 24M | Di Gennaro | 20g | 24,00 € | Wie Classica | 4–6 Wochen | Bos Food |

### Ragù Bolognese (350g)

| Zutat | Lieferant | Menge/Portion | Preis/kg [E] | Qualitätskriterium | Haltbarkeit ab Einkauf | Backup |
|---|---|---|---|---|---|---|
| Bio-Rinderhack (mind. 15 % Fett) | Metro | 150g | 14,00 € | **Fettgehalt fixieren:** 15–20 %. Metro-Bio variiert (10–20 %). Bei Produktwechsel: Rezeptur testen. | 2–3 Tage | Bio-Metzgerei (Fettgehalt bestellbar) |
| San Marzano DOP Pelati | Di Gennaro | 120g | 5,00 € | Wie Classica | 12+ Monate | Metro |
| Soffritto | Metro | 50g | 2,00 € | Frisch | 5–7 Tage | Jeder Supermarkt |
| Olivenöl, Rotwein, Kräuter | Di Gennaro / Metro | pauschal | — | EV Olivenöl, trockener Rotwein zum Kochen | Wochen–Monate | — |

### Sugo Pomodoro (500g)

| Zutat | Lieferant | Menge/Portion | Preis/kg [E] | Qualitätskriterium | Haltbarkeit ab Einkauf | Backup |
|---|---|---|---|---|---|---|
| San Marzano DOP Pelati | Di Gennaro | 350g | 5,00 € | Ganze geschälte Tomaten, kein Passata | 12+ Monate | Metro |
| Zwiebel, Knoblauch | Metro | 30g | 2,00 € | Frisch | 1–2 Wochen | Jeder Supermarkt |
| Olivenöl EV | Di Gennaro | 20ml | 8,00 €/L | Extra Vergine | 12+ Monate | Metro |
| **Basilikum frisch** | Metro oder eigene Pflanze | 5–10g | saisonal | **Frisch, nicht getrocknet!** Hält 2–3 Tage, wird im Kühlschrank schwarz. Dienstag kaufen, Mittwoch komplett verarbeiten. Winter: Gewächshaus-Basilikum oder eigene Pflanze in der Küche (~3 €, hält Wochen). | **2–3 Tage** | Eigene Pflanze / TK-Basilikum (Notfall) |

### Parmigiana di Melanzane (400g)

| Zutat | Lieferant | Menge/Portion | Preis/kg [E] | Qualitätskriterium | Haltbarkeit ab Einkauf | Backup |
|---|---|---|---|---|---|---|
| Aubergine | Metro | 200g | 3,00 € | Fest, glänzend, keine Druckstellen. Saison Mai–Oktober. Winter: Gewächshaus, Preis +30–50 %. | 3–5 Tage | Jeder Großmarkt |
| San Marzano DOP Pelati | Di Gennaro | 100g | 5,00 € | Wie oben | 12+ Monate | Metro |
| Büffelmozzarella | Di Gennaro | 60g | 14,00 € | **125g-Einzelportionen** | **3–5 Tage** | Bos Food Express |
| Parmigiano Reggiano 24M | Di Gennaro | 25g | 24,00 € | Wie oben | 4–6 Wochen | Bos Food |
| Olivenöl (zum Frittieren) | Di Gennaro / Metro | 50ml | 8,00 €/L | EV für Premium-Frittierung, Rauchpunkt beachten | 12+ Monate | — |
| Basilikum frisch | Metro | 5g | saisonal | Wie Sugo | **2–3 Tage** | Eigene Pflanze |

## Einkaufsrhythmus und Mengenlogik

### Wochenrhythmus

| Tag | Aktion | Wer | Dauer |
|---|---|---|---|
| **Montag** | Bestellung aufgeben: Di Gennaro (Lieferung oder Abholung Di) + Metro-Einkaufsliste | Silvio / Produktionskraft | 15 Min. |
| **Dienstag** | Ware annehmen, Wareneingangskontrolle (Temperatur, Zustand, MHD), Einlagerung mit Chargen-Markierung "Retail [Datum]" | Silvio / Produktionskraft | 30–60 Min. (inkl. Metro-Fahrt falls Abholung) |
| **Mittwoch** | Produktion mit frischer Ware (09:00–14:00) | Silvio / Produktionskraft | 5–8 Stunden |

**Metro-Fahrt:** Metro Weil im Dorf ist Selbstbedienung (keine Lieferung). Fahrtzeit ab Stuttgart West: ~25 Min. einfach. Personalaufwand: 1–1,5 Stunden inkl. Einkauf. Alternativ: Dienstag Morgen vor der Di-Gennaro-Lieferung.

**Di Gennaro Liefermodus:** [TBD-Silvio SP-22] — klären: Liefert Di Gennaro Großhandel an Gastro-Kunden, oder muss Silvio in die Von-Pistorius-Straße fahren? Bei Lieferung: Mindestbestellwert? Liefertag?

### Bestellmengen-Formel (Thomas F-04)

Bestellmenge pro Zutat = Wochenplanung × Portionsgröße × Verlustfaktor

| Parameter | Wert | Quelle |
|---|---|---|
| Wochenplanung (Stückzahl) | 25 Stk/Woche (realistisches Szenario) bis 60 Stk/Woche (optimistisch) | Doc 02 v2 |
| Portionsgröße | siehe Zutaten-Steckbriefe oben | Doc 02 v2 Rezepturen |
| Verlustfaktor | 1,10 (10 % Schwund/Verderb/Testchargen) | Doc 02 v2 Annahme |

**Beispiel Büffelmozzarella (25 Stk/Woche, Mix-gewichtet):**
- Classica: 7,5 Stk × 50g = 375g
- Verdure: 3,75 Stk × 50g = 188g
- Parmigiana: 3,75 Stk × 60g = 225g
- Gesamt: ~788g × 1,10 = **~870g/Woche** = 7 × 125g-Portionen

### Chargen-Kennzeichnung statt Rohwaren-Trennung (Thomas F-05)

Separate Bestellung und Lagerung für Retail ist in Phase 1 unrealistisch (eine Küche, ein Kühlraum). Stattdessen: **chargenweise Kennzeichnung**. Kiste oder Behälter mit Aufkleber "Retail [Datum] [Charge-Nr.]". Das reicht für HACCP-Dokumentation und Rückverfolgbarkeit, ohne den Bestellaufwand zu verdoppeln.

## Saisonalität und Preisvolatilität (Thomas F-07)

| Zutat | Saison | Preis-Schwankung | Impact |
|---|---|---|---|
| Büffelmozzarella | Ganzjährig (Büffelmilch leicht saisonal: mehr im Frühjahr) | ±10–15 % | Gering — Grundlage stabil |
| San Marzano DOP (Dosen) | Ganzjährig (Ernte Jul–Sep, Rest Dosenware) | Stabil: 2,50–3,50 €/Dose 400g | Minimal |
| Bio-Rinderhack | Ganzjährig | ±15–20 % (Marktpreis-schwankend) | Mittel — teuerste Zutat im Ragù |
| Aubergine | Mai–Oktober frisch, Winter Gewächshaus | **+30–50 % im Winter** | Hoch — Parmigiana-Marge sinkt im Winter |
| Basilikum frisch | Juni–September optimal | +50–100 % im Winter (Gewächshaus) | Gering (kleine Mengen) |
| Gemüse (Zucchini, Paprika, Spinat) | Saisonal unterschiedlich | ±20–30 % | Mittel — Verdure betroffen |

**Schwelle für Preis-Reaktion:** Wenn der Wareneinsatz eines Produkts um > 15 % steigt, DB-Marge prüfen. Fällt die Marge unter 40 % → Preis anpassen oder Zutat temporär substituieren (z.B. Parmigiana im Winter pausieren, Doc 19 v2 Rotation).

## Herkunftsdaten für LMIV (Inconsistency #9)

DVO (EU) 2018/775 verlangt die Herkunftsangabe der primären Zutat, wenn sie vom Herkunftsort des Lebensmittels abweicht. "Hergestellt in Deutschland" auf dem Etikett + italienische Tomaten = Angabepflicht.

| Zutat | Herkunft | Pflichtangabe nötig? |
|---|---|---|
| San Marzano DOP | Italien (Kampanien) | Ja — DOP impliziert Herkunft, aber explizite Angabe auf dem Etikett prüfen |
| Büffelmozzarella | Italien (Kampanien, DOP wenn Campana) | Ja |
| Bio-Rinderhack | Deutschland [E] | Nein (gleicher Herkunftsort) |
| Aubergine | Saison: DE/NL/ES, Winter: ES/IT | Ja, wenn nicht-DE |
| Parmigiano Reggiano | Italien (Emilia-Romagna) | Ja — DOP |

Konkrete Herkunfts-Dokumentation pro Lieferant: SP-10 (Silvio-Paket). Lebensmittelrechtler muss die Etiketten-Formulierung prüfen (Doc 04 v2).

## "Di Gennaro" als Markenname

In v1 stand: "Zutaten von Di Gennaro auf dem Etikett rechtfertigt den Preispunkt". Das ist aus drei Gründen problematisch:

1. **UWG-Risiko:** Lieferanten-Name als Qualitäts-Claim auf dem Etikett ist potenziell irreführend (§ 5 UWG, inconsistency #13)
2. **LMIV-Konformität:** Auf dem Etikett steht der Hersteller (Goldoni / Silvio), nicht der Lieferant
3. **Reichweite:** Di Gennaro ist in der Stuttgarter Markthallen-Szene bekannt, aber kein überregionaler Qualitätsbeweis

**Entscheidung v2:** Kein Lieferanten-Name auf dem Etikett. Stattdessen: Qualitäts-Claims über nachprüfbare Angaben ("San Marzano DOP", "Büffelmozzarella", "Parmigiano Reggiano 24 Monate"). Die DOP-Zertifikate sprechen für sich. Di Gennaro kann im Kellner-Skript oder auf der Webshop-Seite als Lieferant genannt werden — aber nicht auf dem regulierten Etikett.

## Verpackungsmaterial

| Material | Lieferant | Spezifikation | Menge (25 Stk/Woche) | Preis [E] |
|---|---|---|---|---|
| Vakuumbeutel 250×350mm | Allfo.de | PA/PE, 90µ, -30 bis +100 °C | 500er-Pack (reicht ~20 Wochen) | ~45–60 € / 500 Stk |
| Etiketten (Brother DK-Rolle) | Amazon / Bürobedarf | 62mm breit, kompatibel mit QL-820NWB | 800er-Rolle (reicht ~16 Wochen pro Produkt) | ~15–20 € / Rolle |

**PPWR-Hinweis (ab 12.08.2026):** Beutel-Spezifikation muss Rezyklat-Anforderungen erfüllen. Allfo-Sortiment prüfen, ggf. auf PPWR-konforme Beutel wechseln. Konformitätserklärung vom Lieferanten anfordern (Doc 08 v2).

## Verweise

- `docs/business-case/02 – Wirtschaftlichkeitsrechnung.md` (v2) — Wareneinsatz-Kalkulation mit [E]-Preisen
- `docs/business-case/07 – Preisgestaltung.md` (v2) — VK-Preise, Margen-Tabelle
- `docs/business-case/10 – Operative Umsetzung.md` (v2) — Wochenrhythmus, Produktionsplanung
- `docs/business-case/19 – Sortimentserweiterung.md` (v2) — Produkt-Rotation, Saisonalität
- `docs/findings/inconsistencies.md` — #9 (Primärzutat-Herkunft), #13 (UWG-Claims)
- `docs/silvio-paket/offene-fragen.md` — SP-10 (Herkunftsdaten), SP-22 (Metro-/Lieferanten-Preise)

---

[Zurück zur Übersicht](../../README.md)
