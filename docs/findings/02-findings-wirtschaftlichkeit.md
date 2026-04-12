# Findings: Doc 02 – Wirtschaftlichkeitsrechnung

**Quelle:** [Lead-Review CFO](../reviews/02-wirtschaftlichkeit-cfo.md)
**Datum:** 2026-04-12
**Status:** Offen — v2-Plan ausstehend

Konsolidierte Findings aus dem CFO-Lead-Review. Jedes Finding benennt Auflösungs-Pfad, Owner und Impact. Findings sind die Grundlage für den späteren v2-Plan (`docs/plans/02-v2-plan.md`, noch nicht geschrieben).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **Netto/Brutto nirgends deklariert.** Alle Preise (VK, EK, Kosten) tragen kein Flag. Bei 7 % USt ca. 2.100 €/Jahr Verzerrung im realistischen Szenario. Gesamte Margen-Rechnung nicht interpretierbar. Propagation aus Doc 15 v2 ("Alle Preise sind Brutto inkl. 7 % USt"). | P1 | S | CFO | — | Offen | Ohne Deklaration ist jede Zahl im Doc ±6,5 % unsicher. Gate-Blocker für Steuerberater-Vorlage. |
| 2 | **Fixkosten-Allokation fehlt komplett.** "Energie + Overhead 0,30–0,50 €" ohne Herleitung. Keine anteilige Miete, Küchen-Abschreibung, Reinigung, Versicherung. Ohne Allokation subventioniert das Restaurant den Retail-Strang verdeckt. Methodik-Entscheidung (Vollkosten vs. Teilkosten) muss in v2 verankert werden. | P1 | M | CFO | Methodik-Entscheidung | Offen | Die zentrale Frage "Lohnt sich Retail?" ist nicht beantwortbar. Steuerberater und Bank brauchen mindestens eine Pro-forma-Allokation. |
| 3 | **Rohwaren-Tabelle widerspricht SP-19.** "Butter, Mehl, Milch — pauschal 12–16 €" sind Béchamel-Zutaten. SP-19-Arbeitsannahme: "ohne Béchamel, ohne Ei". Entweder Kalkulation oder Rezeptur-Annahme falsch. | P1 | XS | CFO + Küchenchef | SP-19-Bestätigung durch Silvio | Offen | Wareneinsatz Lasagne um ca. 1,50–2,00 € zu hoch oder zu niedrig, je nach Auflösung. Beeinflusst DB-Marge um 10–15 Prozentpunkte. |
| 4 | **Nur 2 von 4 Phase-1-Produkten kalkuliert.** Sugo Pomodoro und Parmigiana di Melanzane fehlen komplett. Kein Produkt-Mix, kein gewichteter DB, keine Kannibalisierungs-Prüfung. | P1 | M | CFO + Küchenchef | SP-19 (Rezepturen) | Offen | Ohne alle 4 Produkte ist der Gesamt-DB eine Schätzung. Sugo hat vermutlich höheren DB (weniger Arbeitszeit), Parmigiana niedrigeren (aufwendiger). |
| 5 | **Wareneinsatz-Preise ohne Quelle.** 100 % der Preisannahmen sind unbelegt. Kein Metro-Preis, kein Großhändler-Angebot, kein Datums-Stempel. Persona-Scoring verlangt Quellen für >70 %. | P1 | S | CFO | → Silvio-Paket (Metro/Lieferant-Preise) | Offen | Ohne Quellen ist die Kalkulation nicht vorzeigbar. Preisschwankungen (insbesondere Bio-Hackfleisch, Büffelmozzarella) können 15–20 % betragen. |
| 6 | **Personalkosten nicht eingepreist.** "Anteilige Arbeitszeit 1,00–1,50 €" ohne Herleitung. Unklar: wer arbeitet (Silvio, Minijob, Ehegatte), Stundensatz, Einheiten/Stunde. Querverbindung zu Doc 20 (Personal-Setup Retail). | P1 | M | CFO + Persona 11 | Doc 20 Persona-11-Review | Offen | Personalkosten sind nach Wareneinsatz der größte variable Kostenblock. Bei Minijob + AG-Pauschale ca. 15 €/Stunde statt Silvios impliziter "Gratisarbeit". |
| 7 | **Verderb nicht modelliert.** Kein Posten für Schwund, Ausschuss, Warenvernichtung. Bei 5–10 % (branchenüblich Frischeproduktion, insbes. Phase 1 ohne Erfahrungswerte) ca. 1.170 €/Jahr reiner Rohstoff im realistischen Szenario. | P1 | S | CFO | — | Offen | DB sinkt um 5–10 Prozentpunkte. Verderb-Buchung und Warenvernichtungsprotokoll → Doc 15 v2 (dort gelöst). |
| 8 | **Keine Sensitivity-Analyse.** Drei Punkt-Szenarien ohne Variation der Eingangsgrößen. Kein Break-Even-Chart, keine Wareneinsatz-Variation, keine Mengen-Sensitivity. | P2 | M | CFO | F1 (Netto/Brutto) | Offen | Ohne Sensitivity keine Risiko-Bewertung. Steuerberater/Bank erwartet mindestens Break-Even bei X Einheiten. |
| 9 | **Investitionstabelle unvollständig.** Fehlend: Schockfroster (1.500–4.000 €), Labor-Nährwertanalyse (320–600 €), Vetamt-Gebühren, Anwalts-AGB, BAFA-Beratung. Realistische Spanne: 5.500–9.000 € statt 3.000–4.500 €. | P2 | S | CFO | SP-01 (Vetamt), SP-11 (Labor), SP-15 (Anwalt) | Offen | Amortisationszeitraum verdoppelt sich möglicherweise. Break-Even-Aussage "unter 3 Monate" ist mit korrekter Investitionssumme nicht haltbar. |
| 10 | **Amortisations-Aussage irreführend.** "Unter 3 Monate bei 50 Einheiten/Woche" — das ist das realistische, nicht das konservative Szenario. Mit vollständiger Investitionssumme (F9) und konservativem Absatz: 6–12 Monate. | P2 | XS | CFO | F9 | Offen | Silvio und Steuerberater erhalten ein falsches Bild der Kapital-Rückfluss-Geschwindigkeit. |
| 11 | **Gewerbesteuer fehlt.** Stuttgart Hebesatz 420 %, effektiv 14,7 %. Freibetrag EU 24.500 €. Im realistischen Szenario (DB 24.000 €) vermutlich unter Freibetrag, im optimistischen relevant. Muss durchgerechnet werden. | P2 | S | CFO + Steuerberaterin | — | Offen | Im optimistischen Szenario ca. 3.500 €/Jahr GewSt. Auch wenn realistisch unter Freibetrag: die Rechnung muss stehen, damit Steuerberater sie verifizieren kann. |
| 12 | **Jahresbetrachtung rechnet mit 52 Wochen.** Kein Abzug für Betriebsferien, Feiertage, Krankheit. Realistisch: 44–46 Wochen. Differenz: 10–15 % weniger Umsatz. | P2 | XS | CFO | — | Offen | 54.000 € → 46.000–48.000 €. Verstärkt den Effekt von F7 (Verderb) und F2 (Fixkosten). |
| 13 | **"Gewinnbeitrag 19.500–21.000 €" ist kein Gewinn.** Zieht nur Investitionskosten ab, keine laufenden Kosten (Verpackung, Verderb, Personal, Energie, Compliance). Das ist ein Rohertrag, kein Gewinnbeitrag. Begrifflich und rechnerisch falsch. | P1 | S | CFO | F1, F2, F6, F7 | Offen | Silvio liest "19.500 € Gewinn" und plant damit. Die reale Zahl nach allen Kosten ist vermutlich 8.000–12.000 € (bei realistischem Szenario, vollständiger Kalkulation, ohne Fixkosten-Allokation). Mit Fixkosten-Allokation möglicherweise niedriger. |
| 14 | **Compliance-Kosten fehlen komplett.** HACCP-Schulung (laufend), Chargen-Doku-System, Rückstellproben-Lagerung, PPWR-Konformität (ab 12.8.2026), Produkthaftpflicht-Aufpreis, Datenlogger-Wartung. Schätzung: 800–1.500 €/Jahr laufend. | P2 | S | CFO + Lebensmittelrechtler | Gate-Doc-Reviews | Offen | Unsichtbare laufende Kosten, die den DB weiter drücken. Sind das Ergebnis der Gate-Doc-Reviews (Docs 03, 04, 05, 14) und müssen in Doc 02 zurückfließen. |
| 15 | **Umsatzszenarien ohne Nachfrage-Beleg.** Woher kommen 80 Portionen/Woche (realistisch)? Stammgast-Basis? Büro-Kundenpotential? Keine Marktforschung, kein Vergleichswert. 160/Woche (optimistisch) = 32/Tag = 6 Abholungen/Stunde bei 5h Öffnungszeit — Kühl-Lagerkapazität geprüft? | P2 | M | CFO + Gastronom-Praktiker | → Silvio-Paket (Stammgast-Schätzung) | Offen | Ohne Nachfrage-Beleg ist die gesamte Umsatzprojektion Wunschdenken. Pilot-Phase (Rollout-Plan Gate 6) wird die echten Zahlen liefern — aber Doc 02 muss die Unsicherheit benennen. |
| 16 | **Rohwareneinsatz "~25 %" rechnerisch falsch.** Nachrechnung: 203 € / 720 € = 28,2 %. 25 % nur bei unterem Rohwaren-Rand + oberem VK-Rand. Aussage "sehr gut" ist eine Bewertung ohne Benchmark. | P3 | XS | CFO | — | Offen | Kosmetisch, aber symptomatisch: wenn schon die einfache Division nicht stimmt, wie belastbar sind die komplexeren Rechnungen? |
| 17 | **Abschreibungs-Tabelle fehlt.** Doc 15 v2 hat die Rechnung (Vakuumierer 8 J., Etikettendrucker 3 J., Vorsteuer-Effekt). Muss nach Doc 02 propagiert werden, damit der Cash-Flow-Effekt sichtbar wird. | P3 | XS | CFO | — | Offen | Vorsteuer-Abzug aus Investitionen (285–665 €) ist Liquidität im Monat 1 — fehlt in der Cashflow-Betrachtung. |
| 18 | **Saisonalität nicht berücksichtigt.** Sommerterrasse = mehr Restaurant, weniger Retail? Oder umgekehrt (Büros bestellen im Winter mehr Comfort Food)? Weihnachts-/Ostergeschäft für Geschenkeboxen? | P3 | S | CFO + Gastronom-Praktiker | — | Offen | Ohne Saisonalität ist die Jahresbetrachtung eine Gleichverteilung, die es in der Gastronomie nicht gibt. |
| 19 | **Lieferdienst-Provision als Kostenblock fehlt (D-13).** Wolt/Uber nehmen 15–30 % Provision. Zwei Margen-Schienen nötig: Abholung (volle Marge) vs. Plattform-Lieferung (Marge minus Provision). Ohne Split ist der gewichtete DB falsch. Annahme für v2: 30 % der Bestellungen über Plattform, 70 % Abholung → gewichteter Provisions-Anteil ca. 4,5–9 % auf Gesamt-Umsatz. | P1 | S | CFO | D-13, SP-23 (Nachfrage-Split) | Offen | Bei 30 % Plattform-Anteil und 25 % Provision: ca. 4.000 €/Jahr weniger DB im realistischen Szenario. Verschärft den Effekt von F13 ("Gewinnbeitrag" ist kein Gewinn). |

## Auflösungs-Gruppen

### Gruppe A — Silvio-Paket (Aktionen, die Silvio selbst ausführen muss)

Finding 5 (Wareneinsatz-Preise → Metro/Lieferant-Preise einholen) und Finding 15 (Nachfrage-Schätzung → Stammgast-Einschätzung) erfordern Input von Silvio. Wird im Silvio-Paket als neue SP-Einträge eingetragen.

### Gruppe B — Propagation aus anderen Docs

Findings 1 (Netto/Brutto aus Doc 15 v2), 7 (Verderb-Kosten aus Doc 15 v2), 11 (Gewerbesteuer aus Doc 15 v2), 17 (Abschreibung aus Doc 15 v2), 14 (Compliance-Kosten aus Gate-Doc-Reviews), 6 (Personal aus Doc 20) — diese Findings sind in anderen Docs bereits gelöst oder angelegt und müssen nach Doc 02 v2 propagiert werden.

### Gruppe C — Doc-02-eigene Arbeit

Findings 2 (Fixkosten-Allokation), 4 (fehlende Produkte), 8 (Sensitivity), 9 (Investitionstabelle), 10 (Amortisation), 12 (Wochen-Korrektur), 13 (Gewinn-Begriff), 15 (Nachfrage-Beleg), 16 (Rohwareneinsatz-Korrektur), 18 (Saisonalität) — das sind Ergänzungen und Korrekturen, die im v2-Rewrite von Doc 02 passieren.

### Gruppe D — Abhängig von SP-19

Finding 3 (Béchamel-Widerspruch) und Finding 4 (fehlende Produkte) hängen von Silvios Rezeptur-Bestätigung ab. Ohne SP-19-Auflösung kann Doc 02 v2 nur mit Arbeitsannahmen geschrieben werden.

## Cross-Drift in inconsistencies.md

1. **Inconsistency #8 (Netto/Brutto):** Finding 1 bestätigt den bestehenden Eintrag. Status bleibt offen bis Doc 02 v2.
2. **Inconsistency #2 (Launch-Mengen):** Finding 15 verschärft: nicht nur 25–30 vs. 20, sondern auch kein Nachfrage-Beleg für irgendeine Zahl.
3. **Neuer Drift:** Rohwaren-Tabelle listet Béchamel-Zutaten, SP-19 sagt "ohne Béchamel". Eintrag in inconsistencies.md empfohlen, wenn SP-19 bestätigt wird.

## Nächste Schritte

1. [ ] Silvio-Paket erweitern: SP-22 (Metro-/Lieferanten-Preise für alle 4 Produkte) und SP-23 (Stammgast-/Nachfrage-Schätzung)
2. [ ] inconsistencies.md: aufgelöste Einträge (#5, #11, #14, #15) formell markieren, #8 und #2 mit Querverweis auf diese Findings aktualisieren
3. [ ] v2-Plan-Skizze `docs/plans/02-v2-plan.md` — Kapitelstruktur für Doc 02 v2 mit Zuordnung Finding → Kapitel
4. [ ] Doc 02 v2-Rewrite — frühestens nach SP-19-Bestätigung (Rezepturen) und SP-22 (Preise). Mit Arbeitsannahmen möglich, aber dann mit [TBD]-Markern.
