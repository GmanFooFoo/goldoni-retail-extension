# Software & Tools — Goldoni Retail Extension

> **Datum:** 2026-04-12
> **Zweck:** Übersicht aller Software-Systeme und digitalen Tools, die für den Retail-Betrieb gebraucht werden. Getrennt nach Phase 1 (Theken-Verkauf) und Phase 2 (Fernabsatz/Online).

## Phase 1 — Theken-Verkauf (Minimum Viable)

| # | Tool | Zweck | Status | Kosten | Anmerkung |
|---|---|---|---|---|---|
| 1 | **Kassensystem (CRV)** | POS, Belegausgabe, TSE, Zwei-Steuersatz (7 %/19 %) | Im Einsatz, muss für Retail konfiguriert werden | Konfiguration: 0 € (wenn TSE-fähig), Nachrüstung: 300–3.000 € worst case | SP-06: TSE-Check offen. Neuer Artikel "Vakuum-Retail" mit 7 %-Steuerschlüssel anlegen. KassenSichV-konform. |
| 2 | **[Q4Me Qualitätsmanagement](https://www.q4me-qualitaetsmanagement.de)** | QM-System für HACCP-Dokumentation, Chargen-Protokolle, Temperatur-Logs, Reinigungspläne, Schulungsnachweise | Neu, noch nicht im Einsatz | [TBD-Recherche] Preismodell prüfen | Könnte die Papier-Protokolle aus Doc 05 (Tagesprotokoll Kühlung, Chargenprotokoll) digitalisieren. Erfüllt ggf. auch die BAFA-Berater-Anforderung an ein QM-System. Passt zum Datenlogger-Thema (Doc 05 Finding 23). |
| 3 | **WhatsApp Business** | Marketing-Kanal, Kunden-Kommunikation, Broadcast-Listen für Stammgäste | Vermutlich schon im Einsatz (Restaurant) | Kostenlos (WhatsApp Business App) | DSGVO-Einwilligung nach Art. 7 zwingend (Doc 14 DSGVO-Abschnitt). BfDI bewertet kritisch. Marketing- und Rückruf-Liste getrennt führen (zwei Rechtsgrundlagen). |
| 4 | **Etikettendrucker** | Etiketten-Druck für Vakuum-Produkte (LMIV-konform) | Noch nicht angeschafft | Brother QL-820NWB ~200 € oder Profidruck 0,05–0,10 €/Stück | GWG, sofort abzugsfähig (Doc 15 v2). |
| 5 | **Einstechthermometer** | Kerntemperatur-Messung CCP1/CCP2 | Vermutlich vorhanden (Restaurant-Küche) | ~30 €, jährliche Kalibrierung | Doc 05, Küchenchef-Finding. |
| 6 | **WiFi-Datenlogger** | Kontinuierliches Temperatur-Monitoring Kühlraum mit min/max und Alarm | Neu | 50–150 € | Doc 05 Finding 23 (Logistiker): Punktmessung 1×/Tag reicht nicht. |

## Phase 2 — Fernabsatz / Online (abhängig von SP-14 Scope-Entscheidung)

> **Achtung:** Diese Tools setzen voraus, dass Silvio Vorbestellungen annimmt und/oder online verkauft. Das ist ein **Fernabsatzvertrag** nach § 312c BGB und zieht AGB, Widerrufsbelehrung, vorvertragliche Informationspflichten und LMIV Art. 14 nach sich (Doc 14, Findings 3–5). SP-14 (Scope-Entscheidung) muss vorher fallen.

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

Phase 2 (nach SP-14 Scope-Entscheidung):
  Webshop aufsetzen ──→ Stripe-Konto ──→ ggf. PayPal
  AGB + Widerrufsbelehrung (SP-15) ──→ Webshop live
  LMIV Art. 14 Pflichtangaben ──→ Webshop live
```

## Offene Fragen

| # | Frage | Wer | Bezug |
|---|---|---|---|
| 1 | CRV-Kassensystem: TSE-fähig? Zwei Steuersätze? | Silvio (SP-06) | Doc 15 Finding 4 |
| 2 | Q4Me: Preismodell, Funktionsumfang, passt es zu Silvios Größe? | German (Recherche) | Doc 05 HACCP |
| 3 | Webshop: welche Plattform? Abhängig von SP-14 | German + Silvio | Doc 14 Finding 3 |
| 4 | WhatsApp Business: hat Silvio das schon oder nutzt er privates WhatsApp? | Silvio | Doc 14 DSGVO |

---

[← Zurück zur Übersicht](../../README.md)
