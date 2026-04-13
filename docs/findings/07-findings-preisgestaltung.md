# Findings: Doc 07 – Preisgestaltung

**Quelle:** [Lead-Review CFO](../reviews/07-preisgestaltung-cfo.md)
**Datum:** 2026-04-12
**Status:** **Alle 17 Findings adressiert in v2** (2026-04-13, Session 14). **17 Findings** (12 Lead-Review + 5 Co-Review Claudia).

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **Netto/Brutto nicht deklariert.** Identisch mit Inconsistency #8 und Doc-02-Finding 1. Alle Preise in Doc 07 sind weder als netto noch als brutto ausgewiesen. Bei 7 % USt ~0,90 €/Stk Unklarheit. | P1 | XS | CFO | — | ✅ v2 | Ohne Deklaration kann kein Preis gegen die Kosten-Seite geprüft werden. |
| 2 | **Tiefkühl-Zeile im Scope (D-02-Verstoß).** "Tiefkühl-Lasagne 400g — 10–12 €" steht in der Preistabelle, obwohl Tiefkühl in Phase 1 ausgeschlossen ist. Muss gestrichen werden. | P1 | XS | CFO | — | ✅ v2 | Scope-Drift, verleitet Leser, Tiefkühl als Phase-1-Produkt zu lesen. |
| 3 | **Nur 2 von 4 Phase-1-Produkten bepreist.** Sugo Pomodoro und Parmigiana fehlen. Ohne vollständige Preisliste keine Gesamtkalkulation. | P1 | S | CFO + Küchenchef | SP-19 (Rezepturen) | ✅ v2 | Sugo hat vermutlich niedrigeren VK (einfacheres Produkt), Parmigiana höheren. Ohne beide keine realistische Umsatz-Prognose. |
| 4 | **Keine Margen-Prüfung.** Kein einziger Preis ist gegen die Kosten-Seite (Doc 02) gegengerechnet. DB-Marge unbekannt. Preise können unter Vollkosten liegen, ohne dass es auffällt. | P1 | M | CFO | Doc 02 v2 | ✅ v2 | Kernproblem: Preis und Kosten leben in getrennten Docs ohne Cross-Check. v2-Rewrite muss beides zusammenbringen. |
| 5 | **Mengenrabatt ohne Margen-Effekt.** "Domenica-Box: 34 € statt 40 € (6 € Rabatt)" — gibt 40–50 % des DB pro Stück weg. Kein Break-Even-Check für Kombis. | P2 | S | CFO | F4 (Margen erst bekannt nach Doc 02 v2) | ✅ v2 | Rabatt kann die Marge unter die Rentabilitätsschwelle drücken. Muss bewusst entschieden werden, nicht als "Hidden Champion" hingestellt. |
| 6 | **Keine zwei Preisschienen (Abholung vs. Plattform, D-13).** Wolt/Uber-Provision (15–30 %) drückt die Marge bei Plattform-Bestellungen. Entweder Preis-Aufschlag auf Plattform oder bewusst niedrigere Marge. Beide Optionen müssen in Doc 07 diskutiert werden. | P1 | S | CFO + Brand/Marketing | D-13 | ✅ v2 | Ohne Plattform-Schiene entscheidet Silvio unbewusst, ob er 15–30 % seiner Marge an Wolt/Uber abgibt. |
| 7 | **Restaurantpreis ungeprüft.** "16–18 € im Restaurant" als Preisanker — ist das der aktuelle Kartenpreis? Muss als [TBD-Silvio] markiert werden, nicht als Fakt. | P2 | XS | CFO | → Silvio-Paket | ✅ v2 | Wenn der Kartenpreis falsch ist, kippt der gesamte Preisanker. |
| 8 | **"Zutaten von Di Gennaro" — UWG/LMIV-Risiko.** Lieferanten-Name als Qualitäts-Argument auf dem Etikett ist potenziell irreführend (§ 5 UWG). Cross-Ref zu Inconsistency #13 (UWG-Claims). LMIV-Konformität ungeklärt. | P2 | XS | Lebensmittelrechtler + Brand/Marketing | — | ✅ v2 | Abmahn-Risiko 2.000–4.000 € (Doc 14 Finding 12). |
| 9 | **Saisonale Strategie ohne Zahlen.** "Natale-Box +2–3 € Aufpreis" vs. Geschenkkarton-Kosten "1,50–2,50 €" — DB positiv? Arbeitszeit für Zusammenstellen nicht eingepreist. Cross-Ref zu SP-20 (Geschenkebox) fehlt. | P3 | XS | CFO + Brand/Marketing | — | ✅ v2 | Guter Marketing-Gedanke, aber ohne Margen-Check kann das Geschenkebox-Geschäft negativ sein. |
| 10 | **Kein Wettbewerbs-Benchmark.** Doc 17 (Wettbewerbsanalyse) existiert, aber Doc 07 referenziert ihn nicht. "Premium" ist eine Behauptung ohne Marktkontext. | P3 | S | CFO + Brand/Marketing | Doc 17 Review | ✅ v2 | Ohne Benchmark kein Nachweis, dass die Preise im Markt bestehen können. |
| 11 | **Cross-Ref zu Doc 02 fehlt.** Preis und Kosten sind in getrennten Docs ohne Verlinkung. v2-Rewrite muss Doc 02 explizit als Kosten-Gegenpart referenzieren. | P2 | XS | CFO | — | ✅ v2 | Strukturelles Problem. Ohne Cross-Ref kann jedes Doc unabhängig geändert werden, ohne die Auswirkung auf das andere zu prüfen. |
| 12 | **Preisanker-Methode "80 % des Restaurantpreises" — nicht für alle Produkte anwendbar.** Ragù hat keinen Restaurantpreis (kein Einzelgericht auf der Karte), Sugo auch nicht. Die Methode funktioniert nur für Lasagne und ggf. Parmigiana. Für Ragù und Sugo braucht es eine andere Preislogik (Wettbewerb, Warenwert, Convenience-Premium). | P2 | S | CFO + Brand/Marketing | — | ✅ v2 | Zwei verschiedene Pricing-Logiken nötig: Preisanker (Lasagne, Parmigiana) und Standalone-Pricing (Ragù, Sugo). |
| 13 | **11,90 € für Lasagne fair, wenn Qualität stimmt.** Stammgast-Perspektive: Preis akzeptabel, solange Restaurant-Qualität erkennbar ist. Kein Preisproblem, sondern Erwartungs-Management. | P3 | XS | Stammgast (Claudia) | — | ✅ v2 | Bestätigung — kein Handlungsbedarf am Preis, aber am Qualitäts-Versprechen. |
| 14 | **Sugo 6,90 € zu günstig — 7,90 € realistischer.** Bei Premium-Zutaten (San Marzano, frisches Basilikum) erwartet Stammkundin höheren Preis. 6,90 € signalisiert "Supermarkt-Niveau". | P2 | XS | CFO + Stammgast (Claudia) | — | ✅ v2 | 1 €/Stk mehr = ~100 €/Monat Zusatz-DB bei 25 Stk/Woche. |
| 15 | **Parmigiana ist ein Schnäppchen.** Aufwändiges Gericht, im Restaurant 16–18 €. Vakuum-VK unter 12 € wird als "zu billig" wahrgenommen. Preis-Anker prüfen. | P2 | XS | CFO + Stammgast (Claudia) | — | ✅ v2 | Unterbewertung drückt wahrgenommene Qualität und verschenkt Marge. |
| 16 | **Portionsangabe fehlt auf Etikett und in Preisliste.** "Für wie viele Personen?" ist die erste Frage beim Kauf. Ohne Angabe kein Preis-Leistungs-Vergleich möglich. | P2 | XS | Brand/Marketing + Stammgast (Claudia) | — | ✅ v2 | Cross-Ref zu Doc 06 (Mockup) — Portionsangabe muss auf Etikett. |
| 17 | **Wolt-Preis max. +2 € über Abholpreis.** Stammkundin würde bei >2 € Aufschlag lieber abholen. Plattform-Preisschiene darf nicht zu weit vom Abholpreis abweichen. | P2 | XS | CFO + Stammgast (Claudia) | — | ✅ v2 | Deckel für Plattform-Aufschlag: max. 2 € über Abhol-VK. |

## Auflösungs-Gruppen

### Gruppe A — Silvio-Paket

Finding 7 (Restaurantpreis) → neuer SP-Eintrag (SP-24: aktuelle Kartenpreise Lasagne, Parmigiana).

### Gruppe B — Kopplung an Doc 02

Findings 1, 4, 5, 6 — können erst im v2 aufgelöst werden, wenn Doc 02 v2 die Kosten-Seite liefert. **Doc 07 v2 und Doc 02 v2 sollten zusammen geschrieben werden** oder Doc 07 v2 nach Doc 02 v2.

### Gruppe C — Doc-07-eigene Arbeit

Findings 2 (Tiefkühl streichen), 3 (fehlende Produkte), 8 (Di Gennaro UWG), 9 (Saisonale Zahlen), 10 (Benchmark), 11 (Cross-Refs), 12 (Pricing-Logik Split) — im v2-Rewrite von Doc 07.

## Cross-Drift in inconsistencies.md

- **#8 (Netto/Brutto):** Finding 1 bestätigt erneut — Doc 07 hat dasselbe Problem wie Doc 02.
- **#3 (Tiefkühl im Scope):** Finding 2 ist ein weiterer Fall — Doc 07 hat eine Tiefkühl-Zeile trotz D-02.
- **#13 (UWG-Claims):** Finding 8 ("Di Gennaro"-Referenz) ist ein neuer UWG-Risiko-Punkt.

## Nächste Schritte

1. [x] Silvio-Paket: SP-24 (aktuelle Kartenpreise Lasagne/Parmigiana) — referenziert als [TBD-Silvio SP-24] in v2
2. [x] v2-Rewrite auf Basis Doc 02 v2 — Margen-Tabelle, zwei Preisschienen, Mengenrabatt-Check. Erledigt in Session 14.
3. [ ] Co-Reviews: Brand/Marketing (Jana) lt. assignments.md — Claudia Co-Review eingeflossen (siehe Findings 13–17)
