# Q4Me QM-Software — Evaluation

> **Datum:** 2026-04-14
> **Auftrag:** Backlog #56 — Q4Me als QM-Software für die Retail-Extension evaluieren. Preismodell, Funktionsumfang, Eignung für einen Einzel-Gastronom.
> **Cross-Ref:** Doc 05 HACCP, Doc 22 Software-Tools, Doc 02 Wirtschaftlichkeit (Fixkosten-Position "HACCP-Dokumentation / QM-Software" 30 €/Monat).

## Kurzurteil

Q4Me ist für Silvio der pragmatische Default: ein Preis pro Standort (29,90 €/Monat nicht-Mitglied, 19,90 € DEHOGA-Mitglied, jeweils zzgl. MwSt.), 4 Wochen kostenlos, unbegrenzte Nutzer und Geräte, keine Einrichtungsgebühr. Deckt die fünf QM-Kern-Pflichten aus Doc 05 ab (Hygiene, Temperatur, Schulung, Checklisten, fälschungssichere Aufzeichnungen), kommt aber **ohne explizite Chargenprotokoll- und Reinigungsplan-Module** laut Haupt-Webseite. Flowtify ist technisch vergleichbar und hat ausgereiftere IoT-Integrationen (Temperatur-Sensoren), nennt aber keinen öffentlichen Preis und hat nur 14 Tage Testphase.

**Empfehlung:** 4-Wochen-Test Q4Me starten, parallel Flowtify-Angebot einholen, nach Test-Phase entscheiden. Keine Anschaffung vor Vakuum-Launch zwingend — Papier-Protokolle aus Doc 05 reichen formal. Digital macht erst ab Regelbetrieb mit 20+ Chargen/Woche echten Unterschied.

## Q4Me — Fakten

**Anbieter:** hoga service gmbh (Köln), info@hoga-service-gmbh.de.
**URL:** <https://www.q4me-qualitaetsmanagement.de>

### Preise (Stand 2026-04-14, Quelle: [q4me-qualitaetsmanagement.de/preise/](https://www.q4me-qualitaetsmanagement.de/preise/))

| # | Tarif | Preis/Monat (netto) | Kommentar |
|---|---|---|---|
| 1 | DEHOGA Nordrhein (Köln/Düsseldorf) | 12,90 € | Für Silvio nicht relevant (Stuttgart = DEHOGA Baden-Württemberg) |
| 2 | DEHOGA andere Landesverbände | 19,90 € | Gilt für Silvio, wenn er DEHOGA-BW-Mitglied ist → SP-25 klären |
| 3 | Nicht-Mitglieder | 29,90 € | Default, falls keine DEHOGA-Mitgliedschaft |

Alle Preise zzgl. 19 % MwSt. **Ein Preis pro Standort**, Nutzer- und Gerätezahl unlimitiert. Kündigungsfrist: 1 Monat zum Vertragsende. **Testphase: 4 Wochen gratis, ohne automatische Verlängerung.**

> Hinweis: Auf der Aktionsseite `/q4me-aktion/` wird zusätzlich mit "12 Monate kostenlos testen" geworben. Unklar, ob das eine laufende Promo oder Altbestand ist — im Test-Onboarding nachfragen, bevor man sich darauf verlässt.

### Funktionsumfang (laut Anbieter-Seite)

| # | Modul | Abgedeckt | Doc 05 Pflicht |
|---|---|---|---|
| 1 | Temperaturkontrolle (Echtzeit-Auswertung) | ✅ | CCP1 Kühlung, CCP2 Kerntemperatur |
| 2 | Mitarbeiterschulungen / Unterweisungsnachweise | ✅ | § 4 LMHV Schulungspflicht |
| 3 | Checklisten für Mitarbeiter | ✅ | Tagesroutine, Wareneingang |
| 4 | Fälschungssichere Aufzeichnungen | ✅ | Rückverfolgbarkeit, § 44 LFGB |
| 5 | Hygienemanagement (allgemein) | ✅ | HACCP-Konzept |
| 6 | Chargenprotokolle | ⚠️ | Nicht explizit genannt — im Test prüfen |
| 7 | Reinigungspläne | ⚠️ | Nicht explizit genannt — im Test prüfen |
| 8 | Datenlogger-Integration | ❌ | Doc 05 F23 (WiFi-Logger) — separat |
| 9 | Kassen-Integration | ❌ | Doc 15 (CRV) — separat |

**Technik:** Cloud-basiert, iOS- und Android-App verfügbar ([App Store](https://apps.apple.com/de/app/q4me/id1145814077), [Google Play](https://play.google.com/store/apps/details?id=de.hogaservicegmbh.q4me)). Zugriff von Büro, zuhause, unterwegs. Fälschungssicherheit über revisionssichere Protokollierung.

**Support:** 3 Video-Tutorials öffentlich, E-Mail-Support. Kein dokumentiertes Onboarding-Paket, kein explizites SLA.

## Alternativen-Kurzcheck

| # | Tool | Preis transparent? | Testphase | Stärken | Schwächen |
|---|---|---|---|---|---|
| 1 | **Q4Me** | ✅ Ja (29,90 € / 19,90 €) | 4 Wochen | DEHOGA-Kooperation, einfaches Preismodell, deutsche Oberfläche | Chargen/Reinigung nicht explizit beworben, keine IoT-Integration |
| 2 | **Flowtify** | ❌ Nein (Anfrage) | 14 Tage | >1.500 Kunden, IoT-Sensoren (flowtify IoT), EU VO 852/2004 explizit | Preis intransparent, kürzere Testphase, Pricing skaliert mit Standorten/Geräten |
| 3 | **HACCP Digital** | [TBD] | [TBD] | Explizit Eigendokumentation für Kleingastronomie | Nicht geprüft |
| 4 | **Papier-Protokolle** (Doc 05 Status-quo) | 0 € | — | Kein Vendor-Lock-in, rechtlich ausreichend bei sorgfältiger Führung | Zeitaufwand, Lesbarkeit bei Kontrolle, Archivierung 2 Jahre |

Flowtify hat das stärkere Produkt, aber ohne öffentlichen Preis bleibt es bei "anfragen, vergleichen". Für einen Ein-Küchen-Betrieb wie Goldoni ist der Funktions-Overkill wahrscheinlich nicht gerechtfertigt — außer Silvio steigt später in Temperatur-Sensorik mit Vendor-Integration ein.

## Eignung für Silvio

**Passt gut:**

- Ein Standort, klare Preis-Landing → keine Rahmenvertrags-Gespräche
- Italienisch-deutsche Küche, überschaubares Produkt-Sortiment (4 Vakuum-SKUs Phase 1) → Q4Me-Feature-Tiefe reicht
- Mitarbeiter-App-Modell passt zum tatsächlichen Betrieb (Silvio + Koch + Service)
- 4 Wochen Gratis-Test deckt den gesamten Doc-05-Setup-Zeitraum ab → "Testen, dann entscheiden" ohne finanzielles Risiko

**Risiken / offene Punkte:**

1. **Chargenprotokoll:** Pflicht für Vakuum-Produkte mit MHD. Muss im Test explizit gegen Doc 05 geprüft werden. Falls Q4Me das nur über freie Checklisten abbildet, ist das formal OK, aber weniger komfortabel als ein dediziertes Modul.
2. **Datenlogger-Integration:** Q4Me bietet laut Webseite keine automatische Übernahme von WiFi-Logger-Werten. Heißt: Silvio oder ein Mitarbeiter trägt Temperatur-Werte manuell ein (oder nimmt den Logger-Export getrennt in die Doku). Flowtify IoT würde das lösen — für 20+ Öffnungs-Tage/Monat ist das ein realer Zeit-Delta.
3. **12-Monate-Gratis-Aktion:** Widersprüchlich zur 4-Wochen-Angabe auf der Preis-Seite. Bei Test-Anmeldung klären.
4. **DEHOGA-Mitgliedschaft:** Silvio zahlt 19,90 € statt 29,90 €, wenn er bereits DEHOGA-BW-Mitglied ist. Jahres-Delta: 120 € netto → prüfen lohnt sich. Siehe SP-25.

## Entscheidung

**Empfehlung — nicht zwingend vor Vakuum-Launch anschaffen.** Die Papier-Protokolle aus Doc 05 sind rechtlich ausreichend für den Start. Software lohnt, sobald der Regelbetrieb läuft und die Chargen-Frequenz 20+/Woche übersteigt. Empfohlener Pfad:

| # | Schritt | Wann | Wer |
|---|---|---|---|
| 1 | DEHOGA-BW-Mitgliedschaft prüfen (SP-25) | Vor Test-Anmeldung | Silvio |
| 2 | Q4Me 4-Wochen-Test starten, Chargen/Reinigung/Datenlogger explizit testen | In Phase 1 Rollout-Woche 3–6 | German + Silvio |
| 3 | Flowtify-Angebot parallel einholen (Preis, IoT-Module) | Gleiche Zeit wie Q4Me-Test | German |
| 4 | Entscheidung Q4Me / Flowtify / Papier nach Test-Ende | Ende Test-Phase | Silvio |

**Cashflow-Annahme beibehalten:** Die in Doc 02 gesetzten 30 €/Monat für "HACCP-Dokumentation / QM-Software" decken den Q4Me-Non-Member-Preis fast exakt. Kein Update der Wirtschaftlichkeitsrechnung nötig. Sollte Silvio DEHOGA-Mitglied sein, entsteht eine kleine Puffer-Reserve von ~10 €/Monat.

## Offene Fragen (→ Silvio-Paket)

- **SP-25 (neu):** Ist Silvio DEHOGA-Baden-Württemberg-Mitglied? Falls ja → Q4Me 19,90 € statt 29,90 € netto/Monat. Falls nein → Kosten-Nutzen einer Mitgliedschaft separat prüfen (Jahresbeitrag DEHOGA BW ca. [TBD-Recherche] vs. QM-Ersparnis).

## Quellen

- Q4Me Preisseite: <https://www.q4me-qualitaetsmanagement.de/preise/> (abgerufen 2026-04-14)
- Q4Me Haupt-Webseite: <https://www.q4me-qualitaetsmanagement.de> (abgerufen 2026-04-14)
- Q4Me Aktionsseite: <https://www.q4me-qualitaetsmanagement.de/q4me-aktion/> (abgerufen 2026-04-14)
- Flowtify: <https://flowtify.de/home-en/> (abgerufen 2026-04-14)

---

[← Zurück zu Doc 22](./22-software-tools.md) · [← Übersicht](../../README.md)
