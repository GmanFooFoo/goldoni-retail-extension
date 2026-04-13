# Review: Doc 10 — Operative Umsetzung

**Reviewer:** Thomas (Gastronom-Praktiker, Persona 06)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Kurzurteil (1 Satz)

Solider Grundriss mit dem richtigen Instinkt (1× Mittwoch, lieber ausverkauft als Vernichtung, MHD-Restbestand als Tagesangebot), aber für 5 Produkte statt 2 komplett unterdimensioniert — und das gefährlichste Wort im ganzen Dokument ist "kein Zusatzpersonal".

## Scoring (1–5)

- Fachliche Korrektheit: 2 — Öffnungszeiten falsch (18:00 statt 17:00), Equipment-Preise veraltet, CCP-Nummerierung ohne Doc-05-Abgleich
- Vollständigkeit: 2 — kein Vertretungsplan, keine Einschwing-Phase, keine Skalierungs-Stufen, Personal-Realismus fehlt
- Umsetzbarkeit: 3 — Grundstruktur (Mittwoch-Produktion, Wochenrhythmus) ist praxisnah, aber die Zahlen tragen nicht
- Risiko-Abdeckung: 1 — SPOF Inhaber nicht adressiert, Service-Mehraufwand auf "0 Extraaufwand" geschätzt, keine Rückfallebene

## Red Flags

- **"Kein Zusatzpersonal" in Zeile 9** widerspricht dem gesamten Personal-Setup (Doc 20, Szenarien A/B/C) und dem Rollout-Plan (einfacher Koch vormittags). Das ist nicht konservativ, das ist falsch. Fünf Produkte in 4 Stunden vakuumieren, etikettieren, einlagern — alleine — ist physisch möglich, aber nur unter der Annahme, dass Silvio kein Restaurant-Prep für den Abend braucht, keine Lieferung annimmt und nicht telefoniert.
- **"Verkauf = 0 Extraaufwand"** (Zeile 72) ist eine Fantasie-Zahl. Service-Personal muss erklären, empfehlen, kassieren (zweiter Steuersatz), Kühlregal nachfüllen, Kunden-Rückfragen beantworten ("Wie wärme ich das auf?"). Erfahrungswert aus vergleichbaren Modellen: **15–30 Min./Abend** bei 5–10 verkauften Einheiten, nicht null.
- **SPOF Inhaber:** "Küchenchef / Inhaber" steht bei jeder Aufgabe. Wenn Silvio krank ist, eine Woche Urlaub macht oder einfach einen schlechten Tag hat — wer produziert? Kein Wort dazu.

## Fundierte Kritikpunkte

### F-01 — Öffnungszeiten falsch

Doc 10 sagt "18:00–22:30 Uhr". Die aktuelle Realität laut README und CLAUDE.md: **17:00–22:00 Uhr**. Eine Stunde früher öffnen heißt: das Produktionsfenster endet nicht um 15:00, sondern eher um **14:00** (Küche braucht ~3 Std. Vorlauf für Mise en Place). Das schrumpft das nutzbare Fenster von 6 auf 5 Stunden.

### F-02 — Nur 2 Produkte, aber 5 sind im Scope

Doc 10 plant mit Lasagne + Ragù. Seit Session 12 sind es 5 Produkte: **2× Lasagne (Classica/Verdure), Ragù, Sugo, Parmigiana**. Die Mengenplanung (30–40 Lasagne + 15–20 Ragù = max. 60 Einheiten) muss auf 5 Produkte verteilt werden. Die Produktionszeit steigt, weil Parmigiana (Auberginen frittieren) und Lasagne Verdure eigene Vorbereitungs-Schritte haben.

### F-03 — Personalaufwand "5–6 Std/Woche" ist für 5 Produkte unrealistisch

Für 2 Produkte war die Schätzung schon knapp. Für 5 Produkte mit unterschiedlichen Vorbereitungs-Profilen (Ragù: Schmoren 2–3 Std., Parmigiana: Frittieren + Schichten, Lasagne: Backen) rechne ich mit **8–12 Std./Woche** inklusive Vor-/Nachbereitung, Reinigung, Dokumentation. Das ist kein 1-Mann-Mittwoch mehr — das sind 2 Produktionstage oder 2 Personen an einem Tag.

### F-04 — Ablaufplan passt nicht zu den Abkühlzeiten

Der Zeitplan sagt "10:45 Abkühlung einleiten → 11:30 Vakuumieren (≤ 10 °C)". 45 Minuten von Backofen-/Herdtemperatur auf ≤ 10 °C ist in flachen GN-Behältern **physikalisch nicht machbar** ohne aktive Kühlung. HACCP-Vorgabe: von ≥ 60 °C auf ≤ 10 °C in **maximal 2 Stunden** (Doc 05 v2, CCP Abkühlung). Realistisch mit passiver Kühlung im Kühlraum: 90–120 Minuten. Der Zeitplan muss um mindestens 45 Minuten gestreckt werden — oder Silvio braucht einen Schnellkühler (Blast Chiller), was wiederum Invest bedeutet.

### F-05 — Equipment-Preise veraltet

Vakuumierer "1.200–1.800 €" — Doc 12 v2 korrigiert auf **2.500 €** für ein Profi-Kammergerät in Gastro-Größe. Kühlvitrine "optional" — für den Verkauf im Restaurant ist sie nicht optional, sondern **Pflicht** (Temperatur-Compliance, Sichtbarkeit, Hygiene). Gesamtkosten in Doc 10 sind ~2.200–3.700 €, Doc 12 v2 rechnet mit ~6.200 € Gesamtinvest. Die Lücke ist fast 100 %.

### F-06 — 8-Wochen-Rollout: dritte Zahl, dritter Widerspruch

Doc 13 sagt 6 Wochen (CFO-Stopp-Urteil). Der Rollout-Plan sagt 10–12 Wochen mit Gates. Doc 10 sagt 8 Wochen. Das macht drei verschiedene Timelines in drei Dokumenten. Der Rollout-Plan ist die führende Quelle — Doc 10 muss sich daran ausrichten. Cross-Ref: inconsistency #1.

### F-07 — Keine Einschwing-Phase nach Launch

Der Plan springt von "Soft Launch Woche 4" direkt zu "voller Launch Woche 7–8". Aus meiner Erfahrung mit vergleichbaren Modellen: die ersten 4–6 Wochen nach dem ersten echten Verkauf sind Chaos. Prozesse sitzen nicht, Etikettierung dauert doppelt so lang, ein Beutel platzt, ein Kunde beschwert sich. Eine explizite **Einschwing-Phase von 4–6 Wochen** mit reduzierter Menge und wöchentlicher Retro gehört in den Plan. Erst danach skalieren.

### F-08 — Delegierbarkeit nicht adressiert

Welche Aufgaben kann Silvio ab Tag 1 delegieren? Etikettieren und Einlagern: ja, das kann eine Küchenhilfe. Vakuumieren: ja, nach Einweisung. Chargenprotokoll: bedingt, wenn das Formular klar ist. Qualitätskontrolle (Sensorik, Temperatur-Check): nein, das bleibt beim Verantwortlichen. Der Plan unterscheidet nicht zwischen "muss Silvio" und "kann delegiert werden".

### F-09 — "Montag: Bestellung aufgeben" ohne Wareneingangskontrolle-Prozess

Der Wochenrhythmus sagt "Dienstag: Lieferung annehmen, Wareneingangskontrolle, Einlagerung". Gut. Aber: was, wenn die Lieferung Dienstag nicht kommt? Was, wenn die Tomaten nicht die Qualität haben? Kein Plan B, kein Ersatz-Lieferant-Ablauf. In der Praxis passiert das alle 2–3 Wochen. Dann steht Silvio Mittwoch morgens ohne Ware da — und hat 20 vorbestellte Portionen. → Puffer-Bestellung oder Dienstag-Vorabend-Fallback nötig.

### F-10 — MHD-Restbestand-Regel ist eine der besten Ideen im ganzen Repo

"Produkte 2 Tage vor MHD als Tagesangebot ins Restaurant" — das ist genau die richtige Denkweise. Kein Abfall, kein Verlust, stattdessen ein Marketing-Moment ("Heute als Tagesempfehlung: unsere vakuumierte Parmigiana, frisch aufgewärmt"). Das sollte im v2 als bewusste Strategie ausgebaut werden, nicht als Fußnote.

### F-11 — CCP-Nummerierung ohne Cross-Reference zu Doc 05

Der Ablaufplan markiert "CCP 1" (Abkühlung), "CCP 2" (Vakuumieren ≤ 10 °C), "CCP 3" (Einlagerung). Doc 05 v2 hat eine eigene CCP-Struktur mit definierten Grenzwerten und Korrekturmaßnahmen. Ob die Nummern übereinstimmen, ist nicht geprüft — und sie müssen übereinstimmen, weil das Vetamt eine konsistente Dokumentation verlangt.

### F-12 — Wolt/Uber-Logistik fehlt komplett

Seit D-13 ist Plattform-Lieferung ein Phase-1-Vertriebsweg. Doc 10 kennt nur Abholung ("Einlagerung Kühlvitrine / Kühlschrank"). Für Wolt/Uber braucht Silvio: Verpackung mit Transport-Sicherung, Übergabe-Prozess an den Fahrer, Tablet/App-Management für eingehende Bestellungen, Preis-Differenzierung (Abholung vs. Lieferung wegen Provision). Das ist ein eigener Abschnitt im operativen Ablauf, der komplett fehlt.

## Was fehlt

1. **Vertretungsplan** bei Krankheit/Urlaub Silvio (SPOF)
2. **Einschwing-Phase** 4–6 Wochen nach Pilot mit reduzierter Menge
3. **Skalierungs-Stufen:** Was passiert bei 20 → 40 → 80 Stk/Woche? Wann braucht Silvio den zweiten Produktionstag?
4. **Plattform-Lieferung** als operativer Prozess (D-13)
5. **Vorbestellungs-Management** als Tagesablauf-Element (D-12)
6. **Mise-en-Place-Budget** — wie viel der regulären Restaurantvorbereitung fällt weg oder verschiebt sich durch die Vakuum-Produktion?
7. **Chargenprotokoll-Vorlage** oder zumindest Verweis auf Doc 05

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich
- [ ] Stopp — geht so nicht live

**Begründung:** Die Grundidee stimmt (Mittwoch-Produktion, Wochenrhythmus, MHD-Restbestand-Regel), aber das Dokument beschreibt einen 2-Produkt-1-Mann-Betrieb, während der aktuelle Scope 5 Produkte und ein Personal-Setup vorsieht. Die Lücke zwischen Plan und Realität ist zu groß für eine Auflagen-Freigabe — das muss neu geschrieben werden.
