# Goldoni – Steuerliche Behandlung

> **Version:** v2 (2026-04-12). Rewrite auf Basis von 16 Findings aus Lead-Review Steuerberaterin und Co-Review CFO.
> **Scope:** Phase 1 — nur Vakuum, gekühlt, Abholung im Restaurant. Kein Tiefkühl, kein Fernabsatz, kein Onlineversand (D-02).
> **Netto/Brutto-Deklaration:** Alle Preise in diesem Dokument und in Doc 02/07 sind **Brutto-Verkaufspreise inkl. 7 % USt**, sofern nicht ausdrücklich anders gekennzeichnet.

## Umsatzsteuer: 7 % auf Retail-Mitnahme

Seit 1. Januar 2026 gilt laut **Steueränderungsgesetz 2025** (Bundestag-Beschluss 04.12.2025) ein dauerhafter **7 %-Umsatzsteuersatz auf Speisen in der Gastronomie**. Das gilt für Restaurant-Verzehr und für Retail-Mitnahme gleichermaßen. Getränke bleiben bei 19 %.

Für Goldonis vakuumierte Gerichte bedeutet das: **7 % USt, keine Ausnahme**, solange das Produkt ohne weitere Serviceleistung (Bedienung, Besteck, Tisch) verkauft wird — reine Mitnahme.

### Einordnungstabelle

| Produkt | Einordnung | USt |
|---|---|---|
| Vakuum-Lasagne (gekühlt, zum Mitnehmen) | Lebensmittel, reine Mitnahme | 7 % |
| Vakuum-Ragù (gekühlt, zum Mitnehmen) | Lebensmittel, reine Mitnahme | 7 % |
| Vakuum-Sugo (gekühlt, zum Mitnehmen) | Lebensmittel, reine Mitnahme | 7 % |
| Vakuum-Parmigiana (gekühlt, zum Mitnehmen) | Lebensmittel, reine Mitnahme | 7 % |
| Restaurant-Essen (Verzehr vor Ort) | Restaurantleistung | 7 % (seit 1.1.2026) |
| Getränke (Verzehr vor Ort oder Mitnahme) | Getränke | 19 % |

### Fallstricke

1. **Aufwärmservice:** Wenn Silvio das Vakuumprodukt im Restaurant aufwärmt und auf einem Teller serviert → 7 % (seit 2026 kein Unterschied mehr zwischen Vor-Ort und Mitnahme bei Speisen), aber die Zubereitungsanleitung auf dem Etikett darf nicht als Aufwärm-Service durch das Restaurant missverstanden werden.
2. **Gemischte Rechnung:** Wenn ein Kunde gleichzeitig im Restaurant isst und ein Vakuumprodukt kauft, müssen beide Positionen auf dem Beleg getrennt ausgewiesen werden — auch wenn beide 7 % haben. Getränke (19 %) immer separat.
3. **Kein Fernabsatz in Phase 1:** Onlineversand, Vorbestellung per WhatsApp mit Lieferung oder Click-and-Collect sind in Phase 1 nicht vorgesehen. Sollte Phase 2 einen Fernabsatz-Kanal einführen, kommen zusätzliche steuerliche und rechtliche Pflichten hinzu (Cross-Ref Doc 14, Finding 3).

### Verbindliche Auskunft

Eine verbindliche Auskunft nach § 89 Abs. 2 AO beim Finanzamt ist **nicht mehr erforderlich**, weil das Steueränderungsgesetz 2025 die 7-%-Frage gesetzlich geklärt hat. Silvio sollte die Anwendung auf seinen Retail-Fall beim nächsten Steuerberater-Kontakt bestätigen lassen (→ SP-05).

## Gewerbeanzeige

Der Verkauf vakuumierter Fertiggerichte ist **Einzelhandel mit Lebensmitteln** und damit ein zweiter Gewerbe-Zweig neben dem Gaststättengewerbe. Silvio muss die **Gewerbeanzeige nach § 14 GewO** erweitern, bevor der erste Retail-Verkauf stattfindet.

- **Stelle:** Gewerbeamt Stuttgart
- **Kosten:** 15–60 € (gebührenabhängig)
- **Dauer:** wenige Tage Bearbeitungszeit
- **Folge bei Unterlassung:** Der Retail-Umsatz läuft ordnungsrechtlich nicht sauber; Bußgeld und Umsatzsperre möglich.
- **Silvio-Aktion:** → SP-03

## Kassensystem und KassenSichV

### Pflichten

Seit 2020 gilt die **Kassensicherungsverordnung (KassenSichV)**:

1. **TSE-Pflicht:** Jede elektronische Registrierkasse muss eine zertifizierte technische Sicherheitseinrichtung (TSE) haben.
2. **Belegausgabepflicht:** Für jede Transaktion muss ein Beleg erstellt werden (Papier oder digital).
3. **Z-Bon-Archivierung:** Tagesabschlüsse müssen 10 Jahre aufbewahrt werden.
4. **Zwei-Steuersatz-Fähigkeit:** Die Kasse muss 7 % und 19 % parallel verarbeiten können (für Speisen vs. Getränke).

### Silvio-Check

[TBD-Silvio] Welches Kassensystem hat Silvio? Ist es TSE-zertifiziert? Kann es zwei Steuersätze parallel? (→ SP-06, ein Anruf beim Kassenhersteller oder Blick ins Handbuch)

**Worst-Case-Kosten** bei nicht-TSE-fähiger Kasse:

| Szenario | Kosten |
|---|---|
| TSE-Nachrüstung (Software-Update + TSE-Modul) | 300–500 € |
| Kassen-Komplettersatz mit TSE | 1.500–3.000 € |

Diese Kosten müssen im Investitionsplan (Doc 12) als Budgetposition geführt werden, falls SP-06 "nicht TSE-fähig" ergibt. Bei einem "Nein" ist das ein **Stopper für den Rollout**.

## Buchhalterische Trennung

### Erlöskonten

Restaurant-Umsatz und Retail-Umsatz müssen auf **getrennten Erlöskonten** laufen. "Gesondert erfassen" reicht nicht — es braucht eine Verankerung im Kontenrahmen.

**Beispiel SKR 03:**

| Konto | Bezeichnung | Steuersatz |
|---|---|---|
| 8300 | Erlöse 7 % (Restaurant — Speisen) | 7 % |
| 8301 | Erlöse 7 % (Retail — Vakuumprodukte) | 7 % |
| 8400 | Erlöse 19 % (Getränke) | 19 % |

**Beispiel SKR 04:** 4300 / 4301 / 4400 analog.

[TBD-Silvio] Welchen Kontenrahmen nutzt Silvios Steuerberater? (→ SP-05)

### Wareneinsatz Retail

Retail-spezifische Einkäufe (Vakuumbeutel, Etiketten, Labor-Nährwertanalyse, Schulungskosten) müssen als **eigene Kostenstelle** oder zumindest auf einem separaten Aufwandskonto gebucht werden, damit die Retail-Wirtschaftlichkeit isoliert berechenbar ist.

### Vorsteuer-Zuordnung

Silvio ist umsatzsteuerlicher Regelbesteuerer (Kleinunternehmer-Grenze durch Restaurant-Umsatz längst überschritten). Vorsteuer aus Retail-spezifischen Einkäufen ist **sofort abzugsfähig** in der nächsten Umsatzsteuer-Voranmeldung:

- Vakuumbeutel, Etiketten, Drucker-Verbrauchsmaterial
- Labor-Nährwertanalyse (80–150 € × 4 Produkte)
- Schulungskosten (IfSG-Belehrung, HACCP-Schulung)
- Anwaltskosten (AGB, Datenschutzerklärung)
- Versicherungsprämie Produkthaftpflicht

## Investitionsabschreibung Vakuumierer

Der Vakuumierer ist das zentrale Investitionsgut für Phase 1. Konkrete Rechnung:

| Position | Wert |
|---|---|
| Netto-Kaufpreis (Spanne laut Rollout-Plan) | 1.260–2.941 € |
| + 19 % USt | 239–559 € |
| = Brutto-Kaufpreis | 1.500–3.500 € |
| **Vorsteuer-Erstattung** (nächste VA) | **239–559 €** |
| Effektive Anfangsinvestition | 1.260–2.941 € |

**Abschreibung:**

- **GWG-Grenze 800 € netto** (§ 6 Abs. 2 EStG) → Vakuumierer liegt **über** der Grenze → **Aktivierungspflicht**.
- **AfA-Nutzungsdauer:** 8 Jahre (AfA-Tabelle "Gastgewerbe", Gruppe "Maschinen und Geräte")
- **Jährliche AfA:** 158–368 € (linear)

Der **Cash-Flow-Effekt** ist real: Silvio zahlt den Brutto-Preis, bekommt die Vorsteuer (239–559 €) in der nächsten Voranmeldung zurück, und mindert über 8 Jahre seinen Gewinn um die jährliche AfA. Die effektive Belastung im ersten Jahr ist der Netto-Preis minus Vorsteuer-Erstattung — also ca. 16 % weniger als der Brutto-Preis suggeriert.

**Etikettendrucker** (Brother QL-820NWB, ca. 200 € netto): unter GWG-Grenze → **sofort abzugsfähig** als Betriebsausgabe im Anschaffungsjahr.

## Gewerbesteuer-Effekt

Der Retail-Gewinn erhöht Silvios Gesamtgewinn und damit die Gewerbesteuer-Last.

| Position | Wert |
|---|---|
| Hebesatz Stuttgart | 420 % |
| Geschätzter Retail-Gewinn erstes volles Jahr | 10.000–15.000 € |
| Zusätzliche Gewerbesteuer (Schätzung) | ca. 550–825 € |
| Anrechnung auf Einkommensteuer (§ 35 EStG) | mindert die Doppelbelastung |

Kein Stopper, aber ein Posten, der in die Wirtschaftlichkeitsrechnung (Doc 02) gehört und die Gewerbesteuer-Vorauszahlung beeinflusst. Silvios Steuerberater sollte die Vorauszahlungen nach dem ersten Quartal Retail-Umsatz anpassen.

## Fixkosten-Allokation

Die Retail-Produktion nutzt Silvios bestehende Infrastruktur: Küche, Strom, Kühlschrank, Miete, Wasser. Wenn der Retail-Strang **keinen anteiligen Fixkosten-Block** trägt, subventioniert das Restaurant den Retail-Verkauf verdeckt.

Für die **steuerliche** Seite ist das kein Problem (alles derselbe Betrieb, eine Gewinnermittlung). Für die **betriebswirtschaftliche** Entscheidung "Lohnt sich Retail?" ist es entscheidend: ein Retail-Strang, der nur auf variable Kosten gerechnet wird, sieht immer profitabel aus — selbst wenn er bei Vollkosten-Betrachtung Verlust macht.

**Empfehlung:** In Doc 02 (Wirtschaftlichkeit) eine Methodik-Entscheidung treffen — Vollkosten oder Teilkosten? Bei Teilkosten den Deckungsbeitrag ausweisen, bei Vollkosten den anteiligen Overhead (Miete, Strom, Versicherung) als festen Block einrechnen. Beide Varianten haben ihre Berechtigung; die Entscheidung muss dokumentiert sein.

## Umgang mit Verderb und Entsorgung

Bei einer konservativen Annahme von 5–10 % Verderb in der Pilot-Phase (Doc 16 Risiken) ist das ein **laufender Buchungsvorgang**:

1. **Warenvernichtungsprotokoll:** Datum, Produkt, Charge, Menge, Grund (MHD überschritten / Kühlketten-Bruch / Qualitätsmangel), Unterschrift.
2. **Buchungssatz:** Wareneinsatz / Warenbestand (Aufwand, nicht Umsatzkorrektur). Die USt auf den Wareneinsatz bleibt als Vorsteuer abzugsfähig — der Verderb ändert die Vorsteuer nicht, weil die Ware zum Zeitpunkt des Einkaufs für den steuerpflichtigen Umsatz bestimmt war.
3. **Kostenblock:** Bei 50 Einheiten/Woche, 4,50 € Wareneinsatz und 10 % Verderb: ca. **22,50 €/Woche / 1.170 €/Jahr** reiner Rohstoff-Verlust (ohne Arbeitskosten). Dieser Block gehört als feste Position in die Wirtschaftlichkeitsrechnung (Doc 02), nicht als Risiko-Fußnote.

## Briefing-Text für den Steuerberater

Silvio kann diesen Text als E-Mail 1:1 an seinen Steuerberater verschicken (→ SP-05). **Hand-Out mit erweitertem Briefing:** [`sp-05-briefing-steuerberater.md`](../silvio-paket/sp-05-briefing-steuerberater.md).

> Betreff: Erweiterung Goldoni um Retail-Verkauf — steuerliche Klärung
>
> Hallo [Steuerberater-Name],
>
> wir planen, ab [Monat] selbst hergestellte vakuumierte Fertiggerichte (Lasagne, Ragù, Sugo, Parmigiana) direkt im Restaurant zur Mitnahme zu verkaufen — ohne Serviceleistung, reine Abholung. Kein Onlineversand, keine Lieferung.
>
> Vier Fragen, die ich gerne in einem Termin oder per E-Mail klären würde:
>
> 1. **USt-Satz:** Seit 1.1.2026 gilt 7 % auf Speisen. Gilt das auch für unseren Retail-Mitnahme-Fall ohne Einschränkung?
> 2. **Kombi-Bestellung:** Wenn ein Gast im Restaurant isst (7 %) und gleichzeitig ein Vakuumprodukt kauft (7 %) und ein Getränk bestellt (19 %) — wie muss der Beleg aussehen?
> 3. **Gewerbeanzeige:** Muss ich die Gewerbeanzeige um "Einzelhandel mit Lebensmitteln" erweitern? Machen Sie das mit oder gehe ich selbst zum Gewerbeamt?
> 4. **Kontenrahmen:** Welche Erlöskonten sollen wir für den Retail-Umsatz anlegen, damit die Buchführung sauber getrennt ist?
>
> Zusätzlich hätte ich gerne eine kurze Einschätzung zur Abschreibung des Vakuumierers (Anschaffungswert ca. [X] € netto) und zur Vorsteuer-Behandlung der Retail-spezifischen Einkäufe (Beutel, Etiketten, Labor-Analyse).
>
> Vielen Dank und Grüße,
> Silvio

## Cross-Referenzen

| Verweis | Thema | Richtung |
|---|---|---|
| Doc 02 Wirtschaftlichkeit | Netto/Brutto-Deklaration, Fixkosten-Allokation, Verderb-Kostenblock, Gewerbesteuer | Doc 15 → Doc 02 |
| Doc 03 Vetamt | IfSG-Belehrung als Betriebsausgabe, Vetamt-Gebühren | Doc 15 → Doc 03 |
| Doc 07 Preisgestaltung | Netto/Brutto-Deklaration | Doc 15 → Doc 07 |
| Doc 10 Operative Umsetzung | Kassensystem-Konfiguration, Belegausgabe | Doc 15 → Doc 10 |
| Doc 12 Investitionsplan | Vakuumierer-AfA, Kassensystem-worst-case-Kosten | Doc 15 → Doc 12 |
| Doc 14 Recht | § 58 LFGB und Dokumentations-Pflichten, Aufbewahrungs-Fristen, AGB-Kosten als Betriebsausgabe | Doc 15 ↔ Doc 14 |
| Doc 18 Finanzierungsplan | Gewerbesteuer-Vorauszahlungs-Anpassung | Doc 15 → Doc 18 |

## Hinweis

Diese Einschätzung ersetzt keine Steuerberatung. Silvio sollte den Briefing-Text (oben) an seinen Steuerberater schicken und die vier Kern-Fragen klären, bevor der erste Retail-Verkauf stattfindet.

---

[← Zurück zur Übersicht](../../README.md)
