# Goldoni – Risiken & Gegenmaßnahmen

> **Version:** v2 (2026-04-13, Session 13)
> **Änderungen gegenüber v1:** Risiko-Register mit 10 Einträgen (Impact × Wahrscheinlichkeit, Euro-Beträge), regulatorische Stichtage, Behörden-Risiko-Budget, SPOF quantifiziert, Qualitäts-Drift, Kannibalisierung, Verderb bei 5 Produkten, Einschwing-Chaos, Reputations-Risiko.
> **Findings aufgelöst:** F-01 bis F-08 (CFO), CF-01 bis CF-05 (Thomas), CF-01 bis CF-04 (Inspektor Vogel). 17 von 17.

## Goldene Regel

**Im Zweifel nicht verkaufen.** Lieber eine Charge vernichten als einen Kunden enttäuschen oder ein Hygiene-Risiko eingehen. Silvios Ruf wiegt mehr als der Deckungsbeitrag einer Woche.

## Risiko-Register

| # | Risiko | W'keit | Impact (€) | Prio | Gegenmaßnahme |
|---|---|---|---|---|---|
| R-01 | **Nachfrage bleibt aus.** Stammgäste kaufen nicht. Neugier-Phase endet nach 4 Wochen ohne Wiederkauf. | Mittel | 3.100–4.600 € versunken | **P1** | Pilot 15 Stk/Woche, Gate nach 6 Wochen (Wiederkauf ≥ 30 %), bei Nicht-Erreichen: reduzieren oder stoppen |
| R-02 | **SPOF Silvio.** Krankheit/Urlaub = Produktion + Restaurant fallen gleichzeitig aus. | Hoch | 500–800 €/Woche + Vertrauensverlust | **P1** | Vertretungsplan (Doc 10 v2), Misch-Modell M (Doc 20), Wolt/Uber bei Ausfall offline |
| R-03 | **Qualitäts-Drift ab Monat 3.** Routine → nachlassende Kontrolle → Portionen ungenau, Protokolle oberflächlich. | Hoch | Wiederkaufrate sinkt, Ruf-Schaden | **P1** | Monatliche Stichproben-Verkostung (30 Min.), Chargenprotokoll-Audit alle 4 Wochen |
| R-04 | **Behördliche Beanstandung bei Erstbegehung.** Lückenhaftes HACCP, fehlende Protokolle. | Mittel | 50–150 € Nachkontrolle. Worst Case: Betriebsuntersagung Retail. | **P1** | Dry Run 2 Wochen vor Vetamt-Termin: HACCP-Ordner, Chargenprotokoll-Muster, 7-Tage-Temperatur-Log simulieren |
| R-05 | **Verderb bei 5 Produkten.** Nachfrage verteilt sich dünn (5 Stk/Produkt/Woche). | Mittel | ~25–50 €/Woche Abschrift | **P2** | MHD-Restbestand als Tagesangebot, Produkt-Rotation, Bereinigung nach 8 Wochen |
| R-06 | **Regulatorik-Stichtage verpasst.** Listerien 01.07., PPWR 12.08., ProdHaftG 09.12.2026. | Niedrig | Bußgeld bis 50.000 € (LFGB), Rückruf, neue Haftung | **P1** | SP-13 Launch-Timing entscheiden, Kalender-Reminder, PPWR: Beutel-Konformitätserklärung (SP-12) |
| R-07 | **Probennahme — mikrobiologisch auffällig.** Keimzahl über Grenzwert, Listerien-Nachweis. | Niedrig | Rückruf, Chargen-Sperrung, ggf. § 58 LFGB (strafrechtlich ab 01.07.2026) | **P1** | Rückstellproben, lückenlose Chargen-Doku, Versicherung mit Rückruf-Baustein (SP-16) |
| R-08 | **Kannibalisierung Restaurant ↔ Retail.** Kunden kaufen vakuumiert statt Restaurantbesuch. | Niedrig | Wahrnehmungs-Risiko | **P3** | Kommunikation: "Inspiriert von unserer Küche" (nicht "genau wie"). Preisspreizung 25–30 % |
| R-09 | **Einschwing-Chaos Wochen 1–6.** Prozesse sitzen nicht, Etiketten falsch, Beutel-Probleme. | Hoch (Gewissheit) | Stress + Ruf-Risiko bei zu früher Skalierung | **P2** | Reduzierte Mengen, wöchentliche Retro, erst nach 4 stabilen Wochen skalieren |
| R-10 | **Reputations-Schaden durch Einzelfall.** Ein viraler Negativ-Post auf Google/Instagram. | Mittel | Retail-Strang in Anlaufphase gefährdet | **P2** | Reklamations-QR-Code, sofortiger Umtausch, persönliche Antwort auf jede Bewertung |

## Regulatorische Stichtage 2026

| Datum | Regelwerk | Wirkung auf Phase 1 |
|---|---|---|
| **01.07.2026** | Listerien-Grenzwert verschärft | "Nicht nachweisbar in 25g" — relevant bei Büffelmozzarella |
| **12.08.2026** | PPWR (Verpackung) | Konformitätserklärung Pflicht |
| **09.12.2026** | ProdHaftG-Novelle | 25-Jahre-Haftung, Chargen-Doku als Beweismittel |

## Behörden-Risiko-Budget

| Posten | Kosten |
|---|---|
| Erstbegehung Vetamt | 50–150 € |
| Nachkontrolle bei Beanstandung | 50–150 € |
| Amtliche Probe + Labor (bei Beanstandung) | 100–400 € |
| Rückruf direkt (Ware + Kommunikation) | 50–200 € + 30 Min. |
| Rückruf indirekt (Reputation) | nicht bezifferbar |

## Bestehende Risiken aus v1 (überarbeitet)

### Kühlkettenunterbrechung
Ursachen: Kühlschrankausfall, Tür offen, Stromausfall. Maßnahmen: Tagesprotokoll Kühlung, Alarmtemperatur einstellen, bei >7 °C für >2 Std.: gesamte Charge sperren und verwerfen, Techniker-Notfallnummer.

### Vakuumiergerät-Ausfall
Servicenummer griffbereit, Garantie kennen, bei Ausfall Produktionstag verschieben (nicht improvisieren). Zweites Gerät erst Phase 2.

### Lieferengpass Rohwaren
Backup-Lieferant identifizieren (Bos Food für Premium, Metro für Standard). Di-Gennaro-Ausfall = Mittwochs-Produktion gefährdet. Fallback: Dienstagabend Ersatz-Einkauf Metro.

## Versicherungs-Anforderungen

Deckungssumme mind. 2,5 Mio. € pauschal, Rückrufkosten-Baustein, Rechtsschutz für Straf-/Bußgeldverfahren. → SP-16.

---

[← Zurück zur Übersicht](../../README.md)
