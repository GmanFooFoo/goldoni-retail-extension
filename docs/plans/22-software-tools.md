# Software & Tools — Goldoni Retail Extension

> **Datum:** 2026-04-12
> **Zweck:** Übersicht aller Software-Systeme und digitalen Tools, die für den Retail-Betrieb gebraucht werden. Getrennt nach Phase 1 (Theken-Verkauf) und Phase 2 (Fernabsatz/Online).

## Phase 1 — Theken-Verkauf (Minimum Viable)

| # | Tool | Zweck | Status | Kosten | Anmerkung |
|---|---|---|---|---|---|
| 1 | **Kassensystem (CRV)** | POS, Belegausgabe, TSE, Zwei-Steuersatz (7 %/19 %) | Im Einsatz, muss für Retail konfiguriert werden | Konfiguration: 0 € (wenn TSE-fähig), Nachrüstung: 300–3.000 € worst case | SP-06: TSE-Check offen. Neuer Artikel "Vakuum-Retail" mit 7 %-Steuerschlüssel anlegen. KassenSichV-konform. |
| 2 | **[Q4Me Qualitätsmanagement](https://www.q4me-qualitaetsmanagement.de)** | QM-System für HACCP-Dokumentation, Temperatur-Logs, Schulungsnachweise, Checklisten | Evaluiert 2026-04-14, 4-Wochen-Test empfohlen | 29,90 €/Monat (Nicht-Mitglied) oder 19,90 €/Monat (DEHOGA-Mitglied), netto, Ein-Preis-pro-Standort, 4 Wochen gratis | Details und Flowtify-Vergleich: siehe [Q4Me-Evaluation](./22-q4me-evaluation.md). Chargenprotokoll/Reinigungspläne und Datenlogger-Integration im Test explizit prüfen. DEHOGA-BW-Status → SP-25. |
| 3 | **WhatsApp Business** | Marketing-Kanal, Kunden-Kommunikation, Broadcast-Listen für Stammgäste | Vermutlich schon im Einsatz (Restaurant) | Kostenlos (WhatsApp Business App) | DSGVO-Einwilligung nach Art. 7 zwingend (Doc 14 DSGVO-Abschnitt). BfDI bewertet kritisch. Marketing- und Rückruf-Liste getrennt führen (zwei Rechtsgrundlagen). |
| 4 | **Etikettendrucker** | Etiketten-Druck für Vakuum-Produkte (LMIV-konform) | Noch nicht angeschafft | Brother QL-820NWB ~200 € oder Profidruck 0,05–0,10 €/Stück | GWG, sofort abzugsfähig (Doc 15 v2). |
| 5 | **Einstechthermometer** | Kerntemperatur-Messung CCP1/CCP2 | Vermutlich vorhanden (Restaurant-Küche) | ~30 €, jährliche Kalibrierung | Doc 05, Küchenchef-Finding. |
| 6 | **WiFi-Datenlogger** | Kontinuierliches Temperatur-Monitoring Kühlraum mit min/max und Alarm | Neu | 50–150 € | Doc 05 Finding 23 (Logistiker): Punktmessung 1×/Tag reicht nicht. |

## Phase 1 — Vorbestellung & Online-Bezahlung (D-12)

> Vorbestellungen gehören in Phase 1 (D-12). Die rechtliche Mehr-Komplexität ist minimal: Widerrufsrecht entfällt bei verderblicher Ware (§ 312g Abs. 2 Nr. 2 BGB — ein Satz), AGB und Datenschutzerklärung braucht Silvio ohnehin (SP-15), LMIV-Pflichtangaben existieren fürs Etikett und werden online gespiegelt. Der Umsatz-Hebel (bessere Produktionsplanung, Vorbestellungen = sichere Chargen) überwiegt den Aufwand.

| # | Tool | Zweck | Status | Kosten | Anmerkung |
|---|---|---|---|---|---|
| 7 | **Webshop** | Bestellungen entgegennehmen, Produktkatalog, Warenkorb, Checkout mit Bezahlung | Noch nicht vorhanden | Shopify ~30 €/Monat, WooCommerce ~0 € (Hosting ~10 €/Monat), oder Ecwid/Square | Muss LMIV-Pflichtangaben vor Kaufabschluss anzeigen (Art. 14 LMIV Fernabsatz). AGB + Widerrufsbelehrung einbinden. Impressum + Datenschutzerklärung. |
| 8 | **Stripe** | Online-Zahlungsabwicklung (Kreditkarte, SEPA, Apple Pay, Google Pay) | Konto noch nicht vorhanden | 1,5 % + 0,25 € pro Transaktion (EU-Karten) | Standard-Payment-Provider. Einfache Integration in alle gängigen Webshops. Deckt die meisten Zahlungsmethoden ab. |
| 9 | **PayPal Business** | Zusätzliche Zahlungsoption für Kunden, die kein Stripe nutzen wollen | Konto noch nicht vorhanden | 2,49 % + 0,35 € pro Transaktion | Stripe deckt PayPal **nicht** ab — wenn PayPal als Zahlungsmethode gewünscht ist, braucht Silvio ein eigenes PayPal-Business-Konto. Alternativ: Stripe allein reicht für die meisten Kunden. |
| 10 | **Domain / Hosting** | Landing Page oder Webshop unter eigener Domain | [TBD] — restaurante-goldoni.de existiert vermutlich schon | ~5–15 €/Monat | Wenn schon eine Website existiert, Webshop als Unterseite einbinden. |

## Querschnitt-Tools (Phase 1 + 2)

| # | Tool | Zweck | Status | Kosten | Anmerkung |
|---|---|---|---|---|---|
| 11 | **Canva** | Etikett-Design, Marketing-Material, Social-Media-Posts | Vermutlich nicht im Einsatz | Kostenlos (Basis) oder 12 €/Monat (Pro) | Doc 04: Etikett-Empfehlung. Für Prototypen-Design ausreichend. |
| 12 | **Google Workspace / E-Mail** | Geschäftliche E-Mail, Kalender, Dokumente | Vermutlich vorhanden | 0–6 €/Monat | Für Steuerberater-Briefing (SP-05), Anwalts-Kommunikation (SP-15), BAFA-Anträge. |

## Abhängigkeiten und Reihenfolge

```
Phase 1 (sofort):
  Kassensystem konfigurieren (SP-06) ──→ Erster Retail-Verkauf
  Q4Me evaluieren ──→ HACCP-Dokumentation digitalisieren
  WhatsApp DSGVO-Einwilligung ──→ Marketing starten
  Etikettendrucker + Thermometer ──→ Produktion starten
  Datenlogger ──→ Kühlketten-Monitoring

Phase 1 (parallel zum Theken-Start):
  Webshop aufsetzen ──→ Stripe-Konto ──→ ggf. PayPal
  AGB + Widerrufsbelehrung (SP-15) ──→ Webshop live
  LMIV Art. 14 Pflichtangaben ──→ Webshop live
```

## Offene Fragen

| # | Frage | Wer | Bezug |
|---|---|---|---|
| 1 | CRV-Kassensystem: TSE-fähig? Zwei Steuersätze? | Silvio (SP-06) | Doc 15 Finding 4 |
| 2 | Q4Me: Preismodell, Funktionsumfang, passt es zu Silvios Größe? | ✅ Erledigt 2026-04-14 → [Evaluation](./22-q4me-evaluation.md), offen: DEHOGA-Status (SP-25) | Doc 05 HACCP |
| 3 | Webshop: welche Plattform? (Shopify, WooCommerce, Ecwid, Square) | German + Silvio | D-12, Doc 22 |
| 4 | WhatsApp Business: hat Silvio das schon oder nutzt er privates WhatsApp? | Silvio | Doc 14 DSGVO |

---

[← Zurück zur Übersicht](../../README.md)
