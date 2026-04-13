# Goldoni – Operative Umsetzung

> **Version:** v2 (2026-04-13, Session 13)
> **Änderungen gegenüber v1:** 5 Produkte statt 2, Öffnungszeiten korrigiert (17:00), Personalaufwand neu berechnet (8–12h statt 5–6h), Produktionsreihenfolge als Zeitstrahl, Abkühlzeit korrigiert (90–120 Min.), Equipment aus Doc 12 v2, Rollout an Rollout-Plan (10–12 Wochen) angepasst, Wolt/Uber-Logistik (D-13), Vorbestellungs-Management (D-12), HACCP-Hygiene-Overlay, Vertretungsplan, Einschwing-Phase, Delegierbarkeits-Matrix.
> **Findings aufgelöst:** 21 von 24 (Thomas 10/12, Pietro 5/5, Dr. Steiger 4/4, P11 2/3). Offen: F-05 Equipment-Detailpreise (→ SP-22), F-10 MHD-Restbestand-Strategie (v2 aufgewertet, aber Marketing-Integration erst mit Doc 09 v2), F-24 Ehefrau-Verfügbarkeit (→ Silvio-Paket).

## Rahmenbedingungen

- Öffnungszeiten: Mittwoch + Donnerstag–Sonntag, **17:00–22:00 Uhr**
- Ruhetage: Montag und Dienstag
- Kein Mittagsbetrieb
- Produktionsfenster: **09:00–14:00** (vor Mise-en-Place ab ~14:00)
- Personal: gemäß Doc 20 Szenarien A/B/C — Phase 1 startet als Szenario C (Silvio, 4–6 Wochen Pilot), dann Übergang zu A oder B

## Produktionsreihenfolge — Zeitstrahl (1 Produktionstag, 3 Produkte in Rotation)

Nicht alle 5 Produkte an einem Tag (Pietro: 5–6h reine Arbeitszeit + Abkühlung sprengt das Fenster für 1 Person). Stattdessen: **3 Produkte pro Tag in 2-Wochen-Rotation** (siehe Doc 19 v2).

Beispiel: Mittwoch, Rotation "Ragù + Sugo + Lasagne Classica":

```
08:45  Vor-Reinigung Produktionsbereich (Oberflächen, Geräte, Hände) — dokumentieren
09:00  Ragù ansetzen (Schmor-Start, 2–3 Std. passiv)
09:15  Sugo ansetzen (parallel, anderer Herd, 45–60 Min.)
10:00  Sugo fertig → in flache GN-Behälter (max. 4 cm) → Kühlraum
10:15  Lasagne-Vorbereitung (Nudeln kochen, Schichten vorbereiten)
11:00  Ragù fertig → GN-Behälter → Kühlraum
11:15  Lasagne schichten + in Ofen (45 Min.)
12:00  Lasagne raus → GN-Behälter → Kühlraum
        --- Abkühlphase: 90–120 Min. passiv im Kühlraum (Ziel: ≤ 10 °C) ---
12:15  Chargen-Verkostung Ragù + Sugo (Salz, Textur, Gargrad)
12:30  Sugo vakuumieren (≤ 10 °C erreicht) → Etikettieren → Einlagern
13:00  Ragù vakuumieren → Etikettieren → Einlagern
13:15  Rückstellproben entnehmen (1 Beutel pro Produkt, beschriftet, bis MHD + 1 Tag)
13:30  Lasagne vakuumieren (≤ 10 °C erreicht) → Etikettieren → Einlagern
13:45  Chargenprotokoll abschließen (Temperaturen, Mengen, Chargen-Nr.)
14:00  Nach-Reinigung Produktionsbereich
14:15  FERTIG — Küche frei für Restaurant-Mise-en-Place
```

**Gesamtdauer: ~5,5 Stunden** inkl. Abkühlpause und Reinigung. Der Engpass ist die Abkühlung, nicht die Garzeit.

## Wochenrhythmus

| Tag | Aktivität |
|---|---|
| Montag | Admin, Buchhaltung, Bestellung aufgeben (Metro + Di Gennaro), **Personalsuche starten wenn Szenario B** |
| Dienstag | Lieferung annehmen, Wareneingangskontrolle, Einlagerung. **Fallback:** Bei Lieferausfall → Ersatz-Einkauf Metro (Selbstabholung) |
| Mittwoch | 09:00–14:15 Produktion (3 Produkte Rotation), 17:00 Service. **Wolt/Uber-Bestellungen prüfen** |
| Do–So | Abendservice, Verkauf (Kühlvitrine), Tagesprotokoll Kühlung (Temperatur-Log), Wolt/Uber-Bestellungen abwickeln |

## Wolt/Uber-Logistik (D-13)

| Prozess-Schritt | Verantwortlich | Wann |
|---|---|---|
| Produkt-Listing auf Plattform (Fotos, Beschreibung, Preis) | German + Silvio | Einmalig vor Launch |
| Eingehende Bestellungen (Tablet/App) | Service-Personal | Während Öffnungszeiten |
| Produkt aus Kühlvitrine entnehmen, in Karton-Einlage packen | Service-Personal | Bei Bestell-Eingang |
| Übergabe an Fahrer (Isolier-Box neben Kasse als Puffer) | Service-Personal | Bei Fahrer-Ankunft |

**Preis-Differenzierung:** VK auf Plattform = Restaurant-VK + max. 2 € (Claudia-Finding: mehr fühlt sich nach Abzocke an). Rest der Provision als Kosten einpreisen.

## Vorbestellungs-Management (D-12)

Webshop-Bestellungen bis Dienstag 22:00 → fließen in die Mittwochs-Produktionsplanung. Silvio weiß morgens, wie viel er vakuumieren muss. Vorbestellte Ware wird separat etikettiert ("Bestellt für: [Name]") und bei Abholung oder per Wolt zugestellt.

## Mengenplanung

| Szenario | Stück/Woche | Produkte/Tag | Produktionstage |
|---|---|---|---|
| Start (Pilot) | 15–20 | 3 (Rotation) | 1 (Mittwoch) |
| Regelbetrieb | 25–35 | 3 (Rotation) | 1 (Mittwoch) |
| Skalierung | 40–60 | 5 | 2 (Dienstag + Mittwoch) |

**Lieber ausverkauft als Vernichtung.** Ausverkauft schafft Dringlichkeit und Wahrnehmung. Vernichtung kostet Geld und Moral.

## MHD-Restbestand-Strategie

Produkte 2 Tage vor MHD noch im Regal: **als Tagesangebot ins Restaurant** — aufgewärmt, zum reduzierten Preis oder als Amuse-Bouche. Kein Abfall, kein Verlust, stattdessen ein Marketing-Moment: "Heute als Empfehlung: unsere vakuumierte Parmigiana, frisch aufgewärmt."

## Delegierbarkeits-Matrix

| Aufgabe | Muss Silvio (Qualität) | Kann delegiert werden |
|---|---|---|
| Rezeptur-Entscheidung, Chargen-Abnahme (Verkostung) | ✓ | — |
| Temperatur-Kontrolle (CCP-Messung) | — | ✓ (nach Einweisung, klares Protokoll) |
| Vakuumieren | — | ✓ |
| Etikettieren | — | ✓ |
| Einlagern | — | ✓ |
| Chargenprotokoll ausfüllen | — | ✓ (wenn Formular klar) |
| Wolt/Uber-Bestellungen | — | ✓ (Service-Personal) |
| Monatliche Stichproben-Verkostung | ✓ | — |

## Personalaufwand

| Aufgabe | Wer (Doc 20 Szenario) | Zeit/Woche |
|---|---|---|
| Produktion + Abkühlung + Vakuumieren | A, B oder C | 5–6 Std. |
| Vor-/Nach-Reinigung + Dokumentation | A, B oder C | 1–2 Std. |
| Chargenprotokoll + Temperatur-Log | A, B oder C | 30 Min. |
| Verkauf + Wolt/Uber-Übergabe | Service-Personal | 15–30 Min./Abend |
| **Gesamt Produktion** | | **8–10 Std./Woche** |

## Vertretungsplan (SPOF-Mitigation)

| Ausfall | Dauer | Maßnahme |
|---|---|---|
| Silvio 1–3 Tage | Kurzfristig | Produktion pausieren, bestehende Ware verkaufen (MHD reicht), Wolt/Uber offline setzen |
| Silvio 1–2 Wochen | Mittelfristig | Szenario A/B-Person übernimmt, Silvio-Qualitätskontrolle per Foto/Video |
| Silvio > 2 Wochen | Langfristig | Retail-Strang pausieren, Ware bis MHD abverkaufen, Wolt/Uber deaktivieren |

## Einschwing-Phase (Wochen 1–6 nach erstem Verkauf)

Die ersten 6 Wochen sind **Chaos by Design**:
- Mengen auf 50 % des Ziel-Volumens begrenzen
- Wöchentliche Retro (15 Min., Silvio + Koch): Was lief? Was nicht? Was ändern?
- Feedback-Kanal für Kunden (QR → WhatsApp)
- Erst nach stabilen 4 Wochen: Menge erhöhen, zweites Produkt in Rotation aufnehmen

## HACCP-Cross-Reference

Die CCPs in diesem Ablaufplan müssen **identisch** mit Doc 05 v2 HACCP-Plan sein — gleiche Nummerierung, gleiche Grenzwerte, gleiche Korrekturmaßnahmen. Bei einer Vetamt-Begehung wird verglichen. Diskrepanz = sofortiger Befund.

| CCP | Grenzwert | Messung | Korrektur | Doc 05 v2 Ref |
|---|---|---|---|---|
| Abkühlung | ≤ 10 °C in max. 2 Std. | Kernthermometer, digital | Ware verwerfen | CCP Abkühlung |
| Vakuumieren | Produkt ≤ 10 °C vor Versiegelung | Kernthermometer | Nachkühlen, nicht vakuumieren bei >10 °C | CCP Vakuum |
| Einlagerung | Kühlvitrine 2–7 °C, täglich Temperatur-Log | Vitrine-Thermometer | Bei >7 °C: Ware prüfen, Techniker rufen | CCP Lagerung |

---

[← Zurück zur Übersicht](../../README.md)
