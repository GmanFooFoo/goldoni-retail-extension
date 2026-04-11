# Findings: Doc 04 – LMIV-Kennzeichnung

**Quelle:** [Lead-Review Lebensmittelrechtler](../reviews/04-lmiv-lebensmittelrechtler.md) inkl. Regulatorik-Nachtrag Dr. Maldini (Persona 10)
**Datum:** 2026-04-11
**Status:** In Klärung — Co-Reviews durch Behördenkontrolleur und Küchenchef ausstehend.

Konsolidierte Findings analog `03-findings.md`, `15-findings.md` und `05-findings.md`. Gruppen-Logik einheitlich: A = Silvio/extern, B = eigenständige Arbeits-Blöcke im Repo, C = Doc-Rewrite.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | DVO (EU) 2018/775 Herkunftsangabe Primärzutat fehlt komplett — bei "Hergestellt in Deutschland" auf dem Etikett muss die Herkunft der primären Zutat zusätzlich angegeben werden, wenn sie abweicht. Lieferanten-Herkunft → Silvio-Paket SP-10. | P1 | M | Lebensmittelrechtler | Ja, vor erstem Etikett-Druck | Offen | Ohne diese Angabe ist das Etikett ordnungswidrig; LMIDV § 10 Bußgeldrahmen bis 50.000 €; aktive Prüfung durch Überwachungsbehörden in Stichproben. |
| 2 | Art. 22 LMIV QUID-Mengenangabe fehlt — bei hervorgehobener Zutat im Namen/Abbild muss der Mengenanteil in % ausgewiesen werden (Rindfleisch in "Lasagne mit Rindfleisch-Bolognese", Parmigiano in "Parmigiana"). | P1 | S | Lebensmittelrechtler + Küchenchef (Rezept-Daten) | Ja, vor erstem Etikett-Druck | Offen | Wenn Goldoni die Kern-Zutat im Namen nennt (Standard bei italienischen Gerichten), ist QUID nicht optional; ohne Zahlen ist das Etikett nicht druckreif. |
| 3 | Los-Kennzeichnung / Chargennummer nach LKV fehlt — separate Pflicht neben dem MHD, Entlastungs-Regel (MHD mit Tag+Monat ersetzt Los) nur bei einem Produkt pro Tag tragfähig. | P1 | S | Lebensmittelrechtler (Format) + Küchenchef (Prozess-Ankerung) | Ja, vor erstem Verkauf | Offen | Kopplung an Doc 05 HACCP-Eingangsprotokolle; Rückruf nach Finding 3 Doc 05 setzt eindeutige Los-Identifikation voraus. |
| 4 | LMIDV § 2 Pflichtsprache Deutsch nicht benannt — Bezeichnung italienisch erlaubt, aber Zutaten/Allergene/Zubereitung/Aufbewahrung deutsch zwingend. | P1 | XS | Lebensmittelrechtler (Doc-Zeile) | Ja, vor erstem Etikett-Druck | Offen | Trivial in der Umsetzung, aber ordnungswidrig bei Auslassung. |
| 5 | Hersteller-Anschrift unvollständig — "Reinsburgstraße, Stuttgart" ohne Hausnummer und PLZ; Art. 9 Abs. 1 lit. h LMIV fordert die vollständige Anschrift. Adress-Bestätigung → Silvio-Paket SP-09. | P1 | XS | Lebensmittelrechtler (Doc-Zeile) | Ja, vor erstem Etikett-Druck | Offen | [TBD-Silvio] Rule 8; echte Adresse bestätigen. |
| 6 | Art. 17 LMIV Verkehrsbezeichnung vs. Fantasiename nicht getroffen — "Lasagne al forno" ohne beschreibenden Zusatz ist wackelig. Saubere Lösung: Klammer-Zusatz "Nudelauflauf mit Rindfleisch-Bolognese und Béchamel". | P2 | XS | Lebensmittelrechtler (Formulierung) | — | Offen | Nimmt Diskussions-Raum mit Kontrolleur und Verbraucherschutz-Verbänden. |
| 7 | Nährwert-Toleranzbereich nach EU-Leitlinie Dezember 2012 nicht genannt; fddb.info allein ohne Labor-Validierung ist nicht prüfungsfest. Empfehlung: einmalige Labor-Analyse pro Produktlinie bei Rezept-Fixierung. Labor-Auftrag → Silvio-Paket SP-11. | P2 | S | Lebensmittelrechtler | — | Offen | Kosten: 80–150 € × 4 Produkte = 320–600 €. Danach fddb-Updates bei kleinen Variationen zulässig. |
| 8 | Sanktions-Schicht komplett unerwähnt — LMIDV § 10 (bis 50.000 €), § 58 LFGB, UWG-Abmahn-Risiko, Rückruf-Pflicht Art. 19 BasisVO 178/2002. | P2 | S | Lebensmittelrechtler (Kapitel) | — | Offen | Silvio braucht die Risiko-Dimension, sonst kann er Aufwand und Nutzen nicht einschätzen. |
| 9 | PPWR (VO EU 2025/40) ab 12. August 2026 nicht adressiert — Konformitätserklärung pro Verpackung, Piktogramm-Kennzeichnung, PFAS-Grenzwerte für Lebensmittelkontakt-Verpackungen. Beutel-Lieferanten-Anfrage → Silvio-Paket SP-12. | P2 | S | Lebensmittelrechtler | Ja, wenn Launch nach 12.8.2026 | Offen | Für PA/PE-Vakuumbeutel sind PFAS unkritisch, aber die Konformitätserklärung ist universell. Datums-Marker im Rollout-Plan zwingend. |
| 10 | Mindestschrift-Rechenweg nicht explizit — 80 × 120 mm = 96 cm² > 80 cm², damit 1,2-mm-Regel. Doc 04 nennt die Beziehung nicht. | P2 | XS | Lebensmittelrechtler (Doc-Korrektur) | — | Offen | Verhindert Missverständnis zwischen "80 cm²" und "80 × 120 mm". |
| 11 | Varianten-Logik fehlt — Lasagne klassisch vs. vegetarisch sind zwei Etiketten mit unterschiedlichen Zutaten, Allergenen, Nährwerten und QUID-Zahlen. | P2 | S | Lebensmittelrechtler (Kapitel) | — | Offen | Bei realer Speisekarte sind mehrere Etiketten pro Produkt der Standard, nicht die Ausnahme. |
| 12 | Prozess für Rezeptur-Änderungen fehlt — drei Trigger-Punkte: (a) Zutaten-Wechsel mit Allergen-Effekt, (b) Mengen-Verschiebung bei hervorgehobener Zutat (QUID neu), (c) Herkunfts-Wechsel der Primärzutat. | P2 | S | Lebensmittelrechtler + Küchenchef | — | Offen | In laufender Restaurant-Küche sind Zutaten-Änderungen saisonal und lieferanten-abhängig der Normalfall. |
| 13 | Kreuzkontaminations-Absicherung und Art. 36 freiwillige Spuren-Hinweise nicht behandelt. Cross-Ref Doc 05 HACCP. | P2 | S | Lebensmittelrechtler + Küchenchef | — | Offen | Bei gemischter Küche (Pizza, Pasta, vakuumierte Retail-Ware) reales Risiko; Spuren-Hinweis oder physisch-zeitliche Trennung. |
| 14 | Etikett-Mockup für Referenz-Produkt fehlt (Cross-Ref Doc 06) — kein vollständiges Zutatenverzeichnis, kein Layout, keine Checkliste für Silvio. | P2 | M | Lebensmittelrechtler + Brand/Jana (Co-Review Doc 06) | — | Offen | Ohne Mockup ist Doc 04 praxisuntauglich; Silvio kann die Pflichten nicht operationalisieren. |
| 15 | UWG / PAngV-Hinweis für freiwillige Claims ("hausgemacht", "traditionell") fehlt. Cross-Ref Dr. Maldini. | P3 | XS | Lebensmittelrechtler (Absatz) | — | Offen | Spätere Werbe-Aussagen müssen belegbar sein; vorbeugender Hinweis verhindert Abmahn-Risiko. |
| 16 | Cross-Refs zu Doc 05 (HACCP, Allergen-Management, CCP MHD), Doc 06 (Mockups), Doc 08 (Verpackung, PPWR), Doc 11 (Lieferanten, Primärzutat-Herkunft) fehlen. | P3 | XS | Lebensmittelrechtler (Doc-Ergänzung) | — | Offen | Reife-Problem; verhindert Doppel-Aufbau und erleichtert v2-Merge. |
| 17 | Nutri-Score neuer Algorithmus seit 1.1.2026 nicht erwähnt. Freiwillig, aber falls Goldoni später einsetzt, muss der neue Algorithmus rein. | P3 | XS | Lebensmittelrechtler (Hinweis-Absatz) | — | Offen | Reine Vorsorge-Notiz; kein Gate-Problem. |

## Auflösungs-Gruppen

**Gruppe A — Aktionen im Silvio-Paket** (`docs/silvio-paket/offene-fragen.md`, Block 4 Etikett-Vorbereitung): Findings 5 → SP-09 (Hersteller-Anschrift), 7 → SP-11 (Labor-Nährwertanalyse), 9 → SP-12 (PPWR-Konformitätserklärung vom Beutel-Lieferanten). Finding 1 (Primärzutat-Herkunft) ist ein hybrides A/B-Finding: Lieferanten-Daten → SP-10, Dokumentations-Arbeit im Repo als Gruppe-B-Block.

**Gruppe B — Eigenständige Arbeits-Blöcke im Repo:** Findings 1 (Primärzutat-Herkunft als eigenes Kapitel inkl. Produkt-Tabelle für alle Phase-1-Produkte), 2 (QUID-Kapitel mit drei Beispielen), 3 (Los-Kennzeichnungs-Format und Kopplung an HACCP-Eingangsprotokolle aus Doc 05), 8 (Sanktions-Kapitel), 11 (Varianten-Logik-Kapitel), 14 (Etikett-Mockup für Lasagne als Referenz-Template, Cross-Ref Doc 06). Reihenfolge:

1. **Primärzutat-Herkunft (Finding 1)** zuerst — sie hängt an Lieferanten-Daten und setzt die Grundlage für die Etikett-Pflicht-Felder. Arbeits-Block mit Kommissions-Auslegung, Produkt-Tabelle und Hand-Out für Silvio zum Lieferanten-Gespräch.
2. **QUID (Finding 2)** kann parallel laufen, sobald die Rezepte fixiert sind. Abhängig von Küchen-Daten, die aus Doc 07 und Doc 11 kommen.
3. **Los-Kennzeichnung (Finding 3)** als operativer Block mit Format-Vorschlag ("L2026-097" = Tag des Jahres) und Kopplung an das Chargen-Protokoll aus Doc 05 Finding 11.
4. **Etikett-Mockup (Finding 14)** ist das Referenz-Artefakt, aus dem sich alle Detail-Fragen lösen. Cross-Ref Doc 06 Mockups — die dort vorhandenen Mockups werden im Doc-06-Review gespiegelt und als Grundlage genommen. Vermutlich eigener Arbeits-Block nach Doc 06 Review.
5. **Sanktions-Kapitel (Finding 8)** und **Varianten-Logik (Finding 11)** sind Text-Arbeiten, die nach den strukturellen Blöcken in Doc 04 v2 einfließen.

**Gruppe C — Doc-Rewrite:** Findings 4 (Pflichtsprache-Zeile), 6 (Art. 17 Klammer-Zusatz), 7 (Nährwert-Toleranz-Hinweis), 10 (Rechenweg Etikett-Größe), 12 (Rezeptur-Änderungs-Prozess mit drei Triggern), 13 (Kreuzkontaminations-Absatz und Art. 36 Spuren-Hinweis, Cross-Ref Doc 05), 15 (UWG/PAngV-Absatz), 16 (Cross-Refs zu Doc 05/06/08/11), 17 (Nutri-Score-Hinweis). Text- und Tabellen-Arbeit, sinnvoll als letzter Schritt nach Gruppe B, weil sie auf den neuen Kapiteln aus Gruppe B aufsetzen.

## Cross-Drift in inconsistencies.md

Zwei Verbindungen:

1. **Finding 3 (Los-Kennzeichnung)** koppelt an den bestehenden Eintrag **#7 (MHD-Validierung Doc 03 / 04 / 05)**, weil das Chargen-Protokoll aus Doc 05 und die Los-Kennzeichnung aus Doc 04 denselben Datensatz betreffen. Eintrag #7 muss um "Doc 04 Finding 3 — Los-Kennzeichnung als eigenes Feld zusätzlich zum MHD" erweitert werden.
2. **Finding 1 (Primärzutat-Herkunft)** schafft einen neuen Cross-Ref **Doc 04 ↔ Doc 11 Lieferanten**, weil die Herkunft der Kern-Zutaten aus den Lieferanten-Daten folgt. Neuer Eintrag #9 in inconsistencies: "Doc 04 LMIV erwartet Primärzutat-Herkunft, Doc 11 Lieferanten listet keine Herkunftsdaten — fehlende Kopplung".
3. **Finding 14 (Etikett-Mockup)** schafft einen zweiten neuen Cross-Ref **Doc 04 ↔ Doc 06 Mockups**, weil das Etikett-Layout dort angesiedelt ist, aber Doc 04 die Pflichtfelder vorgibt. Ggf. als zweiter neuer Eintrag #10 — oder als Kommentar in #9, falls das zusammengehört. Entscheidung im inconsistencies-Update.

Präzisierung von #7 und mindestens ein neuer Eintrag (#9), optional zwei (#9, #10). Effort: XS, wird in einem Durchgang committed.

## Nächste Schritte

1. [ ] inconsistencies.md aktualisieren: #7 um Doc-04-Los-Kennzeichnung erweitern, #9 Doc 04 ↔ Doc 11 Lieferanten-Herkunft neu, #10 Doc 04 ↔ Doc 06 Mockups neu.
2. [ ] Silvio-Paket um vierten Block "Etikett-Vorbereitung" erweitern (Adresse, Labor, Beutel-Lieferant). Wird in der späteren Silvio-Paket-Konsolidierung (Variante C einer Folge-Session) konsumiert.
3. [ ] Gruppe B Block 1 (Primärzutat-Herkunft-Kapitel) als erste Maßnahme nach Doc 14 Review — oder vorgezogen, wenn Silvio Lieferanten-Gespräche plant und ein Hand-Out braucht.
4. [ ] Gruppe B Block 4 (Etikett-Mockup) nach Doc-06-Review koppeln.
5. [ ] Gruppe C (Doc 04 v2) nicht vor Gruppe B Block 1–3.
6. [ ] Sequenz-Fortschritt: 03 ✓ 15 ✓ 05 ✓ **04 ✓** 14 offen. Nächstes und letztes Doc in der Gate-kritischen Sequenz: Doc 14 Rechtliche Absicherung & Haftung. Dort greift Rule 9 mit erweitertem Scan (BasisVO 178/2002, ProdHaftG, § 58 LFGB, aktuelle Urteile).
