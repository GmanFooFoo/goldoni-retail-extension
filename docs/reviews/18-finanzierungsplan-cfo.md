# Review: Doc 18 – Finanzierungsplan

**Reviewer:** Marcus (CFO / Zahlen-Realist, Persona 01)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Regulatorik-Nachtrag (Rule 9)

Übernommen aus Doc-02-Scan. Zusätzlich relevant: BAFA-Förderung (D-11, Doc 21) und L-Bank Beratungsgutschein BW (Doc 21). Keine Rechtsänderungen.

## Kurzurteil (1 Satz)

Das Dokument hat die richtige Grundhaltung ("Eigenkapital für Stufe 1–2, Fremdkapital nur für Skalierung"), aber die Zahlen sind veraltet, der Rentabilitäts-Check ist Wunschdenken, die BAFA-Förderung (D-11) fehlt, und die Stufen-Logik aus Doc 12 v1 wurde unkritisch übernommen.

## Scoring (1–5)

- **Fachliche Korrektheit:** 2 — Finanzierungsoptionen korrekt benannt (EK, KfW, Hausbank, L-Bank), aber Zahlen und Timeline falsch
- **Vollständigkeit:** 2 — BAFA-Förderung (bis 1.750 € Zuschuss, D-11) fehlt komplett, GewSt-Freibetrag als Cash-Effekt nicht erwähnt, Vorsteuer-Erstattung ignoriert
- **Umsetzbarkeit:** 3 — Empfehlung "EK für Stufe 1–2" ist richtig und direkt umsetzbar
- **Risiko-Abdeckung:** 1 — kein Worst Case, kein "was passiert wenn Stufe 1 scheitert", kein Liquiditäts-Puffer

## Red Flags

1. **Kapitalbedarf-Tabelle übernimmt Doc 12 v1-Zahlen.** Stufe 1: "1.500–2.200 €" — korrigiert in Doc 12 v2: **6.040 € brutto / 5.139 € netto**. Der Gesamtrahmen "6.100–10.600 €" ist ebenfalls falsch — realistisch (Phase 1 Stufe 1 + 2): **6.200–7.800 €**.

2. **"Break-even bei 50 Einheiten/Woche in unter 3 Monaten"** — übernimmt den falschen Wert aus Doc 02 v1. Korrigiert: **Break-Even Cashflow ca. Monat 12–13**, operativer Break-Even ab Monat 4.

3. **KfW-Mindestbetrag 25.000 €.** Doc 18 nennt KfW als Option für Stufe 3 (3.600–6.600 €). Aber KfW-Unternehmerkredite starten bei 25.000 € — das Investitionsvolumen liegt weit darunter. KfW ist für Goldoni **irrelevant**. Stattdessen: Mikrokredit-Programme (bis 25.000 €, z.B. über Bürgschaftsbank BW).

4. **BAFA-Förderung fehlt.** D-11 und Doc 21 haben eine BAFA-Förderung von bis zu 1.750 € identifiziert (50 % von max. 3.500 € Beratungskosten). Das ist der attraktivste Finanzierungs-Baustein — kein Kredit, sondern Zuschuss. Fehlt komplett.

## Fundierte Kritikpunkte

### K1 — Rentabilitäts-Check ist Phantasie

"Monat 1: Stufe 1 amortisiert" — bei 1.500 € Invest und 470 €/Woche DB wäre das in 3 Wochen. In der Realität (Doc 02 v2): Stufe 1 kostet 6.040 €, die ersten 2 Monate haben null Umsatz (Vorbereitung + Beschaffung), und der operative DB im Pilot-Monat ist ~114 €. Cashflow-Break-Even: Monat 12–13.

### K2 — Vorsteuer-Erstattung als Liquiditäts-Hebel ignoriert

901 € Vorsteuer kommen in der nächsten USt-Voranmeldung zurück — das ist ~15 % der Brutto-Investition, die innerhalb von 1–2 Monaten wieder auf dem Konto ist. In einem Finanzierungsplan muss das stehen, weil es den tatsächlichen Kapitalbedarf senkt.

### K3 — Kein Liquiditäts-Puffer

Doc 18 rechnet so, als ob jeder Euro genau dann reinkommt, wenn er gebraucht wird. Kein Puffer für: Verderb in der Pilotphase, verzögerte Vorsteuer-Erstattung, unvorhergesehene Kosten (z.B. Kasse SP-06). Empfehlung: **20 % Liquiditäts-Reserve auf Stufe 1** = ~1.200 €.

### K4 — Stufen-Logik passt nicht mehr

Doc 12 v2 hat die Stufen-Logik verändert: Stufe 1 ist jetzt 6.040 € statt 1.500–2.200 €, Stufe 2 ist 140–270 € (ohne Vitrine, die optional ist), Phase 2 ist separat. Die alte dreistufige Finanzierungslogik muss an Doc 12 v2 angepasst werden.

## Was fehlt

1. **BAFA-Förderung** (D-11, bis 1.750 € Zuschuss)
2. **L-Bank Beratungsgutschein BW** (Doc 21, bis 1.920 € Zuschuss)
3. **Vorsteuer-Erstattung** als Cash-Effekt (901 €)
4. **Korrigierte Zahlen** aus Doc 02 v2 und Doc 12 v2
5. **Liquiditäts-Reserve** (20 % Puffer)
6. **Worst-Case-Finanzierung** (was wenn Pilot scheitert, Kasse ersetzt werden muss)
7. **Cashflow-Projektion als Verweis** (existiert bereits in `docs/plans/02-cashflow-projektion-2026.md`)
8. **KfW streichen oder durch Mikrokredit ersetzen**

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich
- [ ] Stopp

**Begründung:** Die Grundhaltung (Eigenkapital first, Fremdkapital nur für Skalierung) bleibt richtig. Aber die Zahlen sind alle falsch und die BAFA-Förderung als stärkstes Finanzierungsinstrument fehlt. v2 ist im Wesentlichen ein Abgleich mit Doc 02 v2 + Doc 12 v2 + Doc 21 (Fördermittel).
