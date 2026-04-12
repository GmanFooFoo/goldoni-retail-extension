# Goldoni – HACCP-Erweiterung

> **Version:** v2 (2026-04-12). Rewrite auf Basis von 28 Findings aus Lead-Review Lebensmittelrechtler und Co-Reviews Behördenkontrolleur (+ Rule-9-Nachtrag), Küchenchef, Logistiker.
> **Scope:** Phase 1 — Vakuum, gekühlt, Abholung + Vorbestellung (D-12). Kein Tiefkühl (D-02).
> **Arbeitsannahme Rezeptur:** Lasagne **ohne Béchamel, ohne Ei** (SP-19). Listerien-Risiko sinkt gegenüber Béchamel-Variante, bleibt aber relevant (Ragù = Fleischprodukt + feuchtes Milieu).
> **Rückruf:** Doc 05 = **Hygiene-/Chargen-Prozess**. Doc 14 = Haftungs-/Krisen-Prozess. Beide verlinkt (D-09).

## Prozesskette

```
Rohware-Eingang → Eingangskontrolle → Kühllagerung → Zubereitung →
Abkühlung (CCP1) → Vakuumieren (CCP2) → Etikettierung + Los-Nr. →
Kühllager (CCP3) → Verkauf/Übergabe (CCP4) → Kunde
```

## Gefahrenanalyse

Fundament des HACCP-Konzepts (VO 852/2004 Art. 5 Abs. 2a). Jeder CCP muss aus der Gefahrenanalyse **begründet** sein, nicht behauptet.

| Prozess-Schritt | Gefahr | Ursache | Schwere | Wahrscheinlichkeit | CCP? |
|---|---|---|---|---|---|
| Rohware-Eingang | Pathogene in Rohware (Salmonellen, Listerien) | Lieferant, Transport-Temperatur | Hoch | Mittel | Vorkontrolle (kein CCP, aber Pflicht-Prüfung) |
| Zubereitung (Kochen) | Überleben von Pathogenen bei zu niedriger Kerntemperatur | Unzureichendes Erhitzen | Hoch | Niedrig (Standard-Kochen >75 °C) | Kein CCP (Kochen ist intrinsisch sicher bei Ragù/Sugo) |
| **Abkühlung** | **B. cereus, C. perfringens** Sporulation im Gefahrenbereich 10–60 °C | Zu langsame Abkühlung | Hoch | Mittel | **CCP1** |
| **Vakuumieren** | **C. botulinum** (anaerob, wächst im Vakuum) bei zu hoher Produkttemperatur | Warmes Produkt vakuumiert | Sehr hoch | Niedrig (wenn CCP1 eingehalten) | **CCP2** |
| **Kühllagerung** | Listerien-Wachstum bei Kühlketten-Bruch | Kompressor-Ausfall, Tür offen, Überfüllung | Hoch | Mittel | **CCP3** |
| **Verkauf/Übergabe** | Temperatur-Anstieg außerhalb des Kühlraums | Produkt steht an der Theke | Mittel | Mittel | **CCP4** |

## Kritische Kontrollpunkte (CCPs)

### CCP1 — Abkühlung nach Zubereitung

| Feld | Wert |
|---|---|
| **Gefahr** | B. cereus, C. perfringens — Sporen keimen im Bereich 10–60 °C |
| **Grenzwert** | **Zwei-Stufen-Regel:** 60 °C → 20 °C innerhalb 2 Stunden, dann 20 °C → ≤4 °C innerhalb weiterer 4 Stunden |
| **Überwachung** | Kerntemperatur messen (Einstechthermometer), Uhrzeit + Temperatur protokollieren |
| **Korrekturmaßnahme** | Bei Überschreitung des Zeitfensters: Produkt verwerfen |
| **Praxis-Hinweis** | GN-Behälter max. 4 cm Schichthöhe für Sugo/Ragù. Lasagne (ohne Béchamel): flache Portionierung in Einzelformen, Abkühlung realistisch in 4–5 Stunden ohne Schnellkühler. **Ohne Schockfroster in Phase 1:** Produktion morgens starten, Abkühlung über den Vormittag, Vakuumieren am frühen Nachmittag. |

> **Ohne Béchamel (SP-19):** Die Abkühlzeit ist kürzer als bei der Béchamel-Variante, weil kein dickflüssiger Milch-Kern die Wärme speichert. Trotzdem realistisch 3–4 Stunden für Lasagne-Portionen im Standard-Kühlschrank. Zwei-Stufen-Regel ist der saubere Standard.

### CCP2 — Vakuumieren

| Feld | Wert |
|---|---|
| **Gefahr** | C. botulinum (anaerob, wächst im Vakuum) |
| **Grenzwert** | Kerntemperatur **≤ +4 °C** vor dem Vakuumiervorgang |
| **Überwachung** | Kerntemperatur messen direkt vor dem Vakuumieren, protokollieren |
| **Korrekturmaßnahme** | Produkt über +4 °C: zurück in den Kühlraum bis Grenzwert erreicht. **Warme Produkte niemals vakuumieren.** |

### CCP3 — Kühllagerung

| Feld | Wert |
|---|---|
| **Gefahr** | Listerien-Wachstum, Kühlketten-Bruch |
| **Grenzwert** | Lagertemperatur **+2 bis +4 °C**. Warn-Schwelle: +5 °C. Alarm-Schwelle: +7 °C. |
| **Überwachung** | **Datenlogger mit WiFi und Alarm** (50–150 €, Doc 22). Min/Max-Aufzeichnung. Manuelle Kontrolle 1× täglich als Backup. |
| **Korrekturmaßnahme** | +5–7 °C: Ursache prüfen, Tür, Dichtung, Kompressor. > +7 °C: Produkte sperren, Techniker rufen. Wenn Dauer unbekannt (kein Logger): im Zweifel gesamte Ware entsorgen. |

### CCP4 — Verkauf/Übergabe (neu)

| Feld | Wert |
|---|---|
| **Gefahr** | Temperatur-Anstieg außerhalb des Kühlraums |
| **Grenzwert** | Max. **30 Minuten** außerhalb des Kühlraums bei Raumtemperatur |
| **Überwachung** | Produkte erst aus dem Kühlraum nehmen, wenn der Kunde da ist (oder unmittelbar vor Thekenauslage) |
| **Korrekturmaßnahme** | Produkt > 30 Min. außerhalb Kühlung: zurück in Kühlraum oder entsorgen |
| **Kunden-Hinweis** | "Gekühlt transportieren, innerhalb von 2 Stunden in den Kühlschrank" (Art. 25 LMIV). Optional: Isoliertasche als Service. |

## Rohware-Eingangskontrolle

Jede Lieferung prüfen:

| Prüfpunkt | Akzeptanz-Kriterium | Korrektur |
|---|---|---|
| Temperatur gekühlte Ware | ≤ +4 °C (Einstechthermometer) | Ware ablehnen bei > +7 °C |
| Verpackung | Unbeschädigt, kein Saftaustritt | Ware ablehnen bei Beschädigung |
| MHD | Mindestens 3 Tage Restlaufzeit | Ware ablehnen bei < 3 Tagen |
| Lieferschein | Vorhanden, vollständig, Lieferant identifizierbar | Nachfordern |

Lieferschein archivieren — Kopplung an Chargen-Protokoll für "one step up" Rückverfolgbarkeit (Art. 18 VO 178/2002).

## MHD-Richtwerte

| Produkt | Gekühlt vakuumiert | Validierungs-Status |
|---|---|---|
| Lasagne al forno (ohne Béchamel) | 7 Tage | [TBD — Haltbarkeitstest + Listerien-Nachweis nötig] |
| Ragù Bolognese | 8 Tage | [TBD — Haltbarkeitstest nötig] |
| Sugo | 10 Tage (Schätzung, Säure konserviert) | [TBD — Haltbarkeitstest nötig] |
| Parmigiana | 7 Tage | [TBD — Haltbarkeitstest nötig] |

**MHD-Validierung ist Pflicht vor erstem Verkauf.** Optionen:

1. **Laborgestützter Haltbarkeitstest** (empfohlen): Proben an Tag 0, Mitte MHD, Ende MHD auf Keimzahl, Listerien, Sensorik prüfen lassen. Kosten: 200–500 € pro Produkt.
2. **Dokumentierter Eigentest** mit Sensorik-Protokoll (Aussehen, Geruch, Textur, Geschmack an Tag 0, 3, 5, 7) — günstiger, aber weniger belastbar.

### Listerien-Grenzwert ab 1. Juli 2026

> **Rule-9-Fund:** Ab 1.7.2026 gilt für verzehrfertige Lebensmittel auf Handelsebene: Listeria monocytogenes **"nicht nachweisbar in 25g in jeder von 5 Proben"** bis Ende des MHD. Der bisherige Toleranzwert (100 KBE/g) entfällt auf Handelsebene.

Ohne Béchamel ist das Listerien-Risiko **niedriger** als bei der Béchamel-Variante, aber nicht null — Ragù (Fleischprodukt) und Lasagne (feuchtes Milieu mit Käse) bleiben in der Risiko-Kategorie. **MHD-Validierung muss den Listerien-Nachweis am Ende des MHD einschließen**, wenn der Launch nach dem 1.7.2026 liegt.

## Vormittags-Produktionsfenster

Retail-Produktion im **Vormittags-Fenster** (ca. 9–14 Uhr), getrennt vom Restaurant-Vorlauf (ab ca. 15 Uhr Mise en place). Das schafft:

- Zeitliche Trennung Retail/Restaurant → Kreuzkontaminations-Schutz
- Reinigung zwischen den beiden Nutzungen
- Nutzung der Küche in ihrer produktivsten Leerlaufzeit

| Uhrzeit | Aktivität |
|---|---|
| 09:00–10:00 | Rohware-Eingang + Eingangskontrolle |
| 10:00–12:00 | Zubereitung (Kochen) |
| 12:00–14:00 | Abkühlung (CCP1 Zwei-Stufen-Regel) |
| 14:00–14:30 | Vakuumieren (CCP2) + Etikettierung |
| 14:30–15:00 | Reinigung Küche (Übergang Restaurant) |
| Ab 15:00 | Restaurant Mise en place |

## FIFO-Regelung

Ältere Chargen nach vorne, MHD-Datum sichtbar auf jeder Packung. Bei Entnahme aus dem Kühlraum: MHD prüfen. Produkte, die ihr MHD am selben Tag erreichen, morgens aus dem Verkauf nehmen.

## Rückstellproben

Pro Charge mindestens **eine Rückstellprobe** aufbewahren:
- Gekühlt bei ≤ +4 °C
- Beschriftet mit Charge-Nr., Produktionsdatum, MHD
- Aufbewahrung: **7 Tage über MHD hinaus** (also bis Tag 14)
- Zweck: Gegenprobe bei Reklamation oder Rückruf

## Reinigungsplan

| Was | Wann | Womit | Wer | Dokumentation |
|---|---|---|---|---|
| Arbeitsflächen Retail-Produktion | Nach jeder Produktionseinheit, vor Restaurant-Übergang | Lebensmittelgeeigneter Reiniger + Desinfektionsmittel | Retail-Koch / Silvio | Reinigungsprotokoll (Datum, Uhrzeit, Kürzel) |
| Vakuumierer (Kammer + Schweißleiste) | Nach jeder Nutzung | Feuchtes Tuch, Herstelleranleitung | Retail-Koch | Reinigungsprotokoll |
| Kühlraum | 1× wöchentlich komplett, täglich Sichtkontrolle | Lebensmittelgeeigneter Reiniger | Küchenpersonal | Reinigungsprotokoll |
| Handwaschbecken | Permanent verfügbar | Seife + Einweg-Handtücher | Alle | — |

## Chargenprotokoll (Muster)

| Charge-Nr. | Datum | Produkt | Menge | MHD | Temp. bei Vakuum | Lieferschein-Ref. | Rückstellprobe | Freigabe | Kürzel |
|---|---|---|---|---|---|---|---|---|---|
| L2026-097-01 | 07.04.2026 | Lasagne al forno | 20 × 400g | 14.04.2026 | +3,8 °C | LS-2026-04-001 | Ja, Pos. 3 | ✅ | MA |
| L2026-097-02 | 07.04.2026 | Ragù Bolognese | 15 × 350g | 15.04.2026 | +3,5 °C | LS-2026-04-001 | Ja, Pos. 8 | ✅ | MA |

## Geschwollener Beutel — richtige Reaktion

Ein geschwollener Beutel ist ein Anzeichen für **Clostridium-Wachstum** (anaerob, produziert Gas). Die korrekte Reaktion:

1. **Nicht nur den einen Beutel entsorgen** — die gesamte **Charge sperren**
2. Rückstellproben der Charge prüfen (Sichtkontrolle, ggf. Labor)
3. Ursache klären: Prozess-Fehler (CCP1/CCP2 nicht eingehalten)? Rohware-Problem? Verpackungsfehler?
4. Wenn weitere Beutel der Charge im Verkauf sind: **Rückruf einleiten** (Cross-Ref Doc 14 Rückruf-Prozess)
5. Vetamt informieren, wenn Verdacht auf Gesundheitsgefährdung (Art. 19 VO 178/2002 — niedrige Schwelle)

## Strom-Ausfall-Plan

| Dauer | Kühlraum-Temperatur (geschätzt) | Aktion |
|---|---|---|
| < 2 Stunden | Bleibt unter +7 °C (Tür geschlossen) | Tür geschlossen lassen, Datenlogger prüfen, Produkte OK |
| 2–4 Stunden | Steigt auf +8–12 °C | Datenlogger-Max prüfen. Wenn > +7 °C: Produkte sperren, Sichtkontrolle, ggf. entsorgen |
| > 4 Stunden | > +12 °C möglich | Gesamte Ware entsorgen (ohne Datenlogger-Nachweis kein Beweis für Sicherheit) |

**Kontakt Kältetechniker:** [TBD-Silvio]

## Lagerkapazitäts-Rechnung

| Position | Wert |
|---|---|
| Tages-Produktion (Ziel) | 20–30 Portionen |
| MHD-Spanne | 7 Tage |
| Max. Lagerbestand (worst case, langsamer Abverkauf) | ~150 Portionen ≈ 60 kg |
| Parallel: Restaurant-Vorräte | [TBD-Silvio] |

[TBD-Silvio] Reicht der bestehende Kühlraum für beides? Wenn nicht: zweiter Kühlschrank (500–1.500 €) oder Tages-Menge reduzieren.

## Schulungsnachweise

| Schulung | Rechtsgrundlage | Frequenz | Dokumentation |
|---|---|---|---|
| IfSG-Erstbelehrung | § 43 Abs. 1 IfSG | Einmalig vor Arbeitsbeginn | Bescheinigung Gesundheitsamt (SP-04) |
| IfSG-Folgebelehrung | § 43 Abs. 4 IfSG | Alle 2 Jahre durch Arbeitgeber | Datum, Name, Unterschrift |
| HACCP-Unterweisung Vakuum | LMHV § 4 | Bei Arbeitsbeginn + jährlich | Datum, Inhalt, Name, Unterschrift |

## Tägliche 3-Minuten-Kontrolle

1. Datenlogger-App prüfen: min/max letzte 24h OK?
2. MHD aller Produkte prüfen — abgelaufene sofort entnehmen
3. Vakuumbeutel visuell prüfen — **geschwollene Beutel: Charge sperren** (nicht nur entsorgen)

## Cross-Referenzen

| Verweis | Thema | Richtung |
|---|---|---|
| Doc 03 Vetamt | Erstbegehungs-Checkliste, Unterlagen-Anforderungen | Doc 05 → Doc 03 |
| Doc 04 LMIV | Los-Kennzeichnung (Chargen-Kopplung), Allergen-Management, MHD auf Etikett | Doc 05 ↔ Doc 04 |
| Doc 14 Recht | Rückruf Haftungs-/Krisen-Seite (D-09), § 58 LFGB, Aufbewahrungs-Fristen | Doc 05 ↔ Doc 14 |
| Doc 22 Software-Tools | Q4Me QM, Datenlogger, Einstechthermometer | Doc 05 → Doc 22 |

---

[← Zurück zur Übersicht](../../README.md)
