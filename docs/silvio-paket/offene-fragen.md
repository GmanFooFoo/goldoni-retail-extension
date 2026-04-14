# Silvio-Paket — Offene Fragen & Aktionen

**Zweck:** Zentrale, einzige Liste aller Realwelt-Aktionen, die Silvio erledigen muss, damit die Review-Findings aus `docs/findings/*` aufgelöst werden können. **Silvio fasst dieses Repo nicht an.** Diese Datei ist der **Ausgang** von German an Silvio: German liest sie, bereitet die Gespräche/Anrufe/Termine vor, bringt Silvios Antworten zurück — als GitHub-Issue mit Label `feedback-silvio` oder direkt als Eintrag in die `Ergebnis`-Spalte, wenn German die Rückmeldung in der laufenden Session verarbeitet.

**Aktualisierung:** Nach jedem Lead-Review, der neue Silvio-Aktionen erzeugt, wird diese Datei erweitert, **nicht** die `Wer`-Spalte der jeweiligen Findings-Datei.

**Warum nicht in die Findings-Tabelle?** Weil Silvio kein Reviewer ist. Reviewer sind Personas mit Fach-Lead. Silvio ist der Realwelt-Adressat, der außerhalb des Repos handelt. Die Findings-Tabelle gehört den Review-Personas; diese Datei gehört Silvio.

## Status-Legende

- **Offen** — noch nicht angesprochen
- **In Vorbereitung** — German bereitet das Gespräch/Dokument vor (Hand-Out, Briefing-Text, Fragenliste)
- **Bei Silvio** — Silvio weiß Bescheid, Antwort ausstehend
- **Zurück** — Silvio hat geantwortet, aber Verarbeitung im Repo noch nicht abgeschlossen
- **Erledigt** — Ergebnis im Repo eingearbeitet, Referenz-Commit in der `Ergebnis`-Spalte

## Blöcke

Die Silvio-Aktionen sind nach Kontext gruppiert, damit ein Gespräch/Telefonat mehrere Einträge auf einmal abräumen kann. Innerhalb eines Blocks ist die Reihenfolge egal.

### Block 1 — Behörden & Verbände (Vetamt, IHK, Gewerbeamt)

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-01 | Vetamt Stuttgart anrufen: realistische Timings Erstkontakt → Bescheid (3–8 Wochen?), Gebühren für Registrierung / Erstbegehung / Nachbegehung / Laboranalyse, Klärung "Luca-Portal: Pflicht oder Option?". | Doc 03 F4, F5, F7 | P2 | Offen | — |
| SP-02 | IHK Stuttgart Gastronomie-Erstberatungs-Termin buchen — als Schritt 0 vor dem Vetamt-Kontakt, Risiko-Reduktion. | Doc 03 F11 | P3 | Offen | — |
| SP-03 | Gewerbeanzeige-Erweiterung beim Gewerbeamt Stuttgart (§ 14 GewO, Einzelhandel Lebensmittel zusätzlich zur Gaststättenerlaubnis). Kosten 15–60 €, wenige Tage Bearbeitungsdauer. | Doc 15 F3 | P1 | Offen | — |
| SP-04 | Gesundheitsamt Stuttgart: Termin für § 43 IfSG Erstbelehrung für Silvio und das Personal, das am Vakuum arbeitet. Folgebelehrung jährlich. | Doc 05 F12 | P1 | Offen | — |

### Block 2 — Steuerberater & Kasse

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-05 | E-Mail an den Steuerberater mit strukturiertem Briefing. **Fünf Kern-Fragen:** (a) 7%-USt-Verifikation für Retail-Mitnahme ab 1.1.2026 (Steueränderungsgesetz 2025), (b) Abschreibung Vakuumierer (Anschaffungswert, Nutzungsdauer, AfA), (c) Trennung Erlöskonten und Kontenrahmen-Anker (SKR 03 / SKR 04), (d) Verderb / Entsorgungs-Buchung, **(e) USt-Einstufung Geschenkebox** (7 % Gesamtsatz über Hauptleistungs-Prinzip oder Split 7 %/19 %, siehe [docs/plans/54-geschenkebox-konzept.md](../plans/54-geschenkebox-konzept.md)). Zusätzlich: Notwendigkeit einer verbindlichen Auskunft nach § 89 Abs. 2 AO? **Hand-Out:** [`sp-05-briefing-steuerberater.md`](sp-05-briefing-steuerberater.md). | Doc 15 F1, F5, F8, F10, F11; Backlog #54 | P1 | Bei Silvio (Hand-Out wird um Geschenkebox-Frage ergänzt) | — |
| SP-06 | Kassenhersteller anrufen oder Handbuch lesen: Ist die Kasse TSE-zertifiziert (KassenSichV)? Kann sie zwei Steuersätze parallel (7 % und 19 %, z. B. für Getränke)? Zehn Minuten Aufwand. | Doc 15 F4 | P1 | Offen | — |

### Block 3 — Hygiene & Sicherheit

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-07 | HACCP-Beauftragten selbst benennen — Silvio persönlich oder eine andere verantwortliche Person aus der Küche. Namentlich in der Vetamt-Unterlage. | Doc 03 F2, Doc 05 F15 | P1 | Offen | — |
| SP-08 | Bestehenden Schädlingsbekämpfungsvertrag klären: Deckt er die Retail-Erweiterung mit ab oder braucht er einen Nachtrag? | Doc 05 F14 | P3 | Offen | — |

### Block 4 — Etikett-Vorbereitung (LMIV)

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-09 | Echte Hersteller-Anschrift bestätigen: vollständige Adresse mit Hausnummer und PLZ für das Etikett nach Art. 9 Abs. 1 lit. h LMIV. `[TBD-Silvio]` laut CLAUDE.md Rule 8. | Doc 04 F5 | P1 | Offen | — |
| SP-10 | Primärzutat-Herkunft je Phase-1-Produkt klären (DVO EU 2018/775): woher kommen Hartweizen (Lasagne-Nudeln), Tomaten (Sugo), Rindfleisch (Ragù), Auberginen und Käse (Parmigiana)? Silvio liefert die Lieferanten-Daten, German formuliert die Etikett-Pflichtzeile. | Doc 04 F1 | P1 | In Vorbereitung (Hand-Out aus Gruppe B Block 1 folgt) | — |
| SP-11 | Labor-Nährwertanalyse pro Produktlinie beauftragen (320–600 € gesamt bei 80–150 € × 4 Produkte). Einmalig bei Rezept-Fixierung. | Doc 04 F7 | P2 | Offen | — |
| SP-12 | Beutel-Lieferanten nach PPWR-Konformitätserklärung (VO EU 2025/40) und PFAS-Nachweis fragen. PA/PE-Beutel sind praktisch unkritisch bei PFAS, aber die Konformitätserklärung ist ab 12.8.2026 universelle Pflicht. | Doc 04 F9 | P2 | Offen | — |

### Block 5 — Recht & Versicherung

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-13 | Launch-Timing-Entscheidung: **vor 12.8.2026** (keine PPWR, kein neues ProdHaftG für Start-Chargen), **nach 9.12.2026** (beide neue Regime sauber von Tag eins) oder **dazwischen** (Doppel-Stack). **Hand-Out:** [`sp-13-launch-timing-entscheidung.md`](sp-13-launch-timing-entscheidung.md). Persona-00-Einschätzung: Option C sauberer, Option A realistisch, Option B nicht empfohlen. | Doc 14 F1 | P1 | Bei Silvio (Hand-Out bereit) | — |
| SP-14 | ~~Scope-Entscheidung Phase 1: mit oder ohne Vorbestellung.~~ **Revidiert (D-12):** Vorbestellungen gehören in Phase 1. Die rechtliche Mehr-Komplexität ist minimal (ein Satz Widerrufs-Ausschluss + LMIV-Daten online, AGB und Datenschutzerklärung sind ohnehin nötig). Der Umsatz-Hebel ist real. Kein separater Entscheidungs-Punkt mehr — Webshop + Vorbestellung wird direkt mitgeplant. | Doc 14 F3 | — | Aufgelöst (D-12) | Vorbestellungen ab Phase 1. |
| SP-15 | Auf Gastronomie und Lebensmittelrecht spezialisierten Anwalt in Stuttgart beauftragen für: AGB-Paket (mit Fernabsatz-Variante, wenn SP-14 so entschieden), Datenschutzerklärung inkl. WhatsApp-Einwilligung, einseitiges Krisen-Prozess-Notfall-Blatt. Budget 800–1.500 € einmalig (Weg 1) oder 150–300 € + Muster-Anpassung (Weg 2 IHK/DEHOGA). **Hand-Out:** [`sp-15-anwalts-auftrag.md`](sp-15-anwalts-auftrag.md). | Doc 14 F5, F11 | P1 | Bei Silvio (Hand-Out bereit) | — |
| SP-16 | Zwei Versicherungs-Angebote parallel einholen: (a) bestehender Gastro-Haftpflicht-Makler mit Anfrage zur Erweiterung um "Verkauf verpackter Lebensmittel an Endverbraucher", (b) Food-Spezialist (foodsurance.de, FMP Fuchs, Bernhard Assekuranz). Anforderungs-Profil aus Gruppe B Block 3 (Versicherungs-Deckungs-Kapitel): Deckungssumme mind. 2,5 Mio. € pauschal, Rückrufkosten-Baustein, Rechtsschutz für Straf-/Bußgeldverfahren. | Doc 14 F9, F10 | P1 | In Vorbereitung (Anforderungs-Profil folgt) | — |
| SP-17 | Krisen-Telefonliste an die Küche hängen: (a) Vetamt Stuttgart Notfall-Nummer, (b) Versicherungs-Notfall-Hotline (aus SP-16-Ergebnis), (c) Strafverteidiger-Kontakt mit Schwerpunkt Lebensmittelstrafrecht (aus SP-15-Anwalts-Empfehlung). | Doc 14 F16 | P2 | Offen (abhängig von SP-15, SP-16) | — |
| SP-18 | Rechtsform-Entscheidung Einzelunternehmer vs. GmbH/UG als Haftungsbeschränkung. Entscheidung zusammen mit dem Steuerberater im Rahmen von SP-05. Bei Einzelunternehmer greift die Haftung auf Privatvermögen — nach ProdHaftG-Novelle 9.12.2026 ohne 85-Mio-Cap. | Doc 14 F20 | P2 | Offen (koppelt an SP-05) | — |

### Block 6 — Rezepturen & Produktlinie

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-19 | **Rezeptur-Klärung Phase-1-Produkte:** (a) ~~Hat die Goldoni-Lasagne Béchamel oder nicht?~~ **Arbeitsannahme: ohne Béchamel, ohne Ei** (German, 2026-04-12). Lasagne = Ragù + Pasta + Käse. Listerien-Risiko sinkt, Abkühlzeit entschärft, Allergen Ei entfällt. Bestätigung durch Silvio steht noch aus. (b) Genaue Rezepturen aller vier Phase-1-Produkte in Gramm-Angaben fixieren — weiterhin offen, aber v2-Rewrites können jetzt auf Basis der Arbeitsannahme laufen. | Doc 04 F18, Doc 05 F2/F18/F20, alle Béchamel-Referenzen in Reviews | P1 | Bei Silvio (WhatsApp 2026-04-12), Arbeitsannahme gesetzt | Ohne Béchamel, ohne Ei. Gramm-Angaben offen. |
| SP-20 | **Geschenkebox "Sugo + Rummo-Nudeln" — Silvio-Entscheidungen:** Konzept vollständig durchgeplant in [docs/plans/54-geschenkebox-konzept.md](../plans/54-geschenkebox-konzept.md) (LMIV, Haftung, Kalkulation, Verpackung). Empfohlen: Standard-Box 19,90 €, Premium 22,90 €. **Silvio-Fragen:** (a) Grundsätzliches OK für das Produkt? (b) Rummo-Sorte (Spaghetti No. 3 / Penne Rigate No. 66 / Pappardelle)? (c) Ist der Rummo-EK von 2 € netto/500g realistisch oder hat Silvio einen besseren Lieferanten-Preis? (d) Premium-Variante (Geschenkkarton + Karte) ab Launch oder erst zu Weihnachten 2026? (e) Launch in Monat 4 des Retail-Rollouts OK? | Doc 04, Doc 08, Backlog #54, Inconsistency #16 | P2 | Offen (Konzept bereit) | — |

### Block 8 — Preise & Kalkulation (aus CFO-Lead-Reviews Doc 02 + Doc 07)

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-22 | **Metro-/Lieferanten-Preise für alle 4 Phase-1-Produkte.** Für den v2-Rewrite von Doc 02 brauchen wir echte Einkaufspreise mit Datums-Stempel statt Spannen-Schätzungen. Ideal: Metro-Rechnung oder Online-Preisliste für Bio-Hackfleisch, San-Marzano-Tomaten, Büffelmozzarella, Parmigiano, Auberginen, Lasagneplatten, Olivenöl. | Doc 02 F5 | P1 | Offen | — |
| SP-23 | **Stammgast-/Nachfrage-Schätzung.** Wie viele Portionen pro Woche hält Silvio für realistisch? Basis: Anzahl Stammgäste, Büro-Kunden im Stuttgarter Westen, Erfahrung mit Außer-Haus-Verkauf. Ohne Silvios Einschätzung sind die Absatz-Szenarien in Doc 02 unbelegt. | Doc 02 F15 | P2 | Offen | — |
| SP-24 | **Aktuelle Kartenpreise Lasagne und Parmigiana.** Doc 07 nutzt "16–18 € im Restaurant" als Preisanker für den Retail-VK. Stimmt das mit der aktuellen Speisekarte überein? Falls Silvio die Preise kürzlich geändert hat, muss der Retail-VK nachziehen. | Doc 07 F7 | P2 | Offen | — |
| SP-25 | **DEHOGA-Baden-Württemberg-Mitgliedschaft.** Ist Silvio bereits Mitglied? Falls ja, kostet Q4Me QM-Software 19,90 € statt 29,90 € netto/Monat (Ersparnis ~120 €/Jahr, siehe [Q4Me-Evaluation](../plans/22-q4me-evaluation.md)). Falls nein, DEHOGA-BW-Jahresbeitrag separat prüfen und Mitgliedschafts-Nutzen gesamthaft bewerten (QM-Rabatt, Rechtsberatung, Tarif-Infos). | Doc 22 Software-Tools | P3 | Offen | — |
| SP-26 | **Produkthaftpflicht-Erweiterung um Handelsware (Rummo-Nudeln) für Geschenkebox.** Beim bestehenden/geplanten Produkthaftpflicht-Versicherer anfragen, ob Handelsware Rummo-Pasta im Rahmen der Goldoni-Police automatisch mitversichert ist oder als eigenes Produkt-Portfolio gemeldet werden muss. Haftungsrisiko für Händler ist niedrig (ProdHaftG § 4 Abs. 3, Hersteller Rummo klar identifizierbar), aber sauberes Vorgehen erfordert Versicherer-Freigabe vor Launch. | Konzept [docs/plans/54-geschenkebox-konzept.md](../plans/54-geschenkebox-konzept.md), Cross-Ref SP-16 | P3 | Offen | — |

### Block 7 — Fördermittel

| # | Frage/Aktion | Quelle | Prio | Status | Ergebnis |
|---|---|---|---|---|---|
| SP-21 | **BAFA-Antrag vor nächstem Beratertermin stellen:** Vor dem Steuerberater-Termin (SP-05) oder dem Anwalts-Termin (SP-15) den BAFA-Förderantrag online stellen. Reihenfolge zwingend: erst Antrag, dann Beratung. Prüfen, ob Silvios Steuerberater/Anwalt BAFA-registriert ist. Zuschuss: bis 50 % der Beratungskosten, max. 1.750 €. Programm läuft bis 31.12.2026. | Doc 21 Fördermittel | P1 | In Vorbereitung (German recherchiert BAFA-Berater-Status) | — |

## Workflow

**Eingang (Silvio → German → Repo):**

1. German spricht mit Silvio. Silvio liefert Antwort, Daten, Entscheidung.
2. German legt ein GitHub-Issue mit Label `feedback-silvio` und Referenz auf die SP-Nummer(n) an (oder trägt das Ergebnis direkt in die `Ergebnis`-Spalte dieser Datei ein, wenn die laufende Session das Thema sofort aufnimmt).
3. Die nächste Session arbeitet offene `feedback-silvio`-Issues und zieht die Ergebnisse in die entsprechenden Findings-Dateien, Pläne und Doc-Rewrites ein. Status hier wird auf `Erledigt` gesetzt mit Commit-Ref in der `Ergebnis`-Spalte.

**Ausgang (Claude → German → Silvio):**

1. Bei jedem Lead-Review, der Silvio-Aktionen erzeugt, wird **diese Datei** erweitert, nicht die `Wer`-Spalte der Findings-Datei.
2. Wenn eine Session ein Silvio-Gespräch vorbereiten soll, wird das Hand-Out (Briefing-Text, Entscheidungs-Grundlage, Fragenliste) als eigenes Dokument in `docs/silvio-paket/` mit einem sprechenden Dateinamen abgelegt (z. B. `silvio-paket/SP-05-briefing-steuerberater.md`, `silvio-paket/SP-13-launch-timing-entscheidung.md`).
3. Der SP-Eintrag in dieser Datei verweist auf das Hand-Out, wenn eins existiert.

**Was diese Datei nicht ist:**

- Kein Silvio-facing Text (das macht die Persona-00-Schicht in `docs/silvio-derivatives/`, wenn irgendwann gewünscht). Die Sprache hier ist Germans interne Arbeits-Sprache.
- Kein Ersatz für Findings-Dateien. Die Findings bleiben in `docs/findings/*`, werden nur in der `Wer`-Spalte ohne Silvio-Erwähnung geführt, mit Verweis "→ Silvio-Paket SP-XX".
- Keine Issue-Liste — Issues sind im GitHub-Repo, diese Datei ist der strukturierte Zustand der offenen Silvio-Fragen.
