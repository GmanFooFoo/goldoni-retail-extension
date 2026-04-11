# Findings: Doc 15 – Steuerliche Behandlung

**Quelle:** [Lead-Review Steuerberaterin](../reviews/15-steuer-steuerberaterin.md)
**Datum:** 2026-04-11
**Status:** In Klärung — Co-Review durch CFO offen. Findings 1 und 9 wurden nach Bekanntwerden des Steueränderungsgesetzes 2025 (7 % auf Speisen in Gastronomie seit 1.1.2026) auf "aufgelöst — Silvio-Verifikation offen" umgestellt. Die Nebenpunkte bleiben unverändert gültig.

> **Nachtrag 2026-04-11:** Seit 1. Januar 2026 gilt laut Steueränderungsgesetz 2025 ein dauerhafter 7 %-Umsatzsteuersatz auf Speisen in der Gastronomie (Bundestag 04.12.2025). Das löst die MwSt-Kernfrage aus Finding 1 und die Quantifizierungs-Frage aus Finding 9 auf. Die beiden Einträge stehen weiter in der Tabelle, sind aber als "aufgelöst, Silvio-Verifikation beim Steuerberater-Kontakt" markiert, damit die Historie nachvollziehbar bleibt. Die übrigen Findings (Gewerbeanzeige, KassenSichV, Kontenrahmen, Abschreibung, Verderb-Buchung, Vorsteuer, Cross-Refs) sind nicht betroffen.

Konsolidierte Findings aus dem Lead-Review. Format und Struktur analog `03-findings.md`. Jedes Finding benennt Auflösungs-Pfad, Owner und Impact. Findings sind die Grundlage für den späteren v2-Plan (`docs/plans/15-v2-plan.md`, noch nicht geschrieben) und für Cross-Drift-Einträge in `inconsistencies.md`.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | ~~MwSt-Einordnung (7 % vs. 19 %) ist nicht prüfungsfest. Pfad zur verbindlichen Auskunft nach § 89 Abs. 2 AO fehlt.~~ **Aufgelöst durch Steueränderungsgesetz 2025 — 7 % auf Speisen in Gastronomie seit 1.1.2026, gilt auch für Retail-Mitnahme.** | P1 → ✅ | — | Silvio-Verifikation beim nächsten Steuerberater-Kontakt | — | Aufgelöst, Silvio-Verifikation offen | Der größte Gate-Blocker nach Rollout-Schritt 1 ist weg. |
| 2 | Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) erwähnen MwSt nicht. Netto/Brutto ist nirgends fixiert. | P1 | S | Steuerberaterin + CFO (Cross-Review) | Ja, Voraussetzung für belastbare Margen-Rechnung | Offen | Jede Margen-Aussage im Business-Case ist ohne diese Klarheit unbelastbar. |
| 3 | Gewerbeanzeige nach § 14 GewO nicht adressiert. Retail ist Einzelhandel mit Lebensmitteln, nicht Gaststättenerlaubnis. | P1 | XS | Silvio (Gewerbeamt Stuttgart) | Pflicht vor erstem Verkauf | Offen | Ohne Erweiterung läuft der Retail-Umsatz ordnungsrechtlich nicht sauber; Risiko Bußgeld und Umsatzsperre. |
| 4 | KassenSichV / TSE-Pflicht nicht geprüft. Kann Silvios Kasse zwei Steuersätze nebeneinander und ist sie TSE-zertifiziert? | P1 | XS | Silvio (Kassenhersteller oder Handbuch) | Ja, bei "Nein" Stopp bis System-Update | Offen | Bei Kassen-Nachschau hart geprüft; fehlende TSE ist Bußgeld-bewehrt. |
| 5 | Trennung Erlöskonten nicht operationalisiert. Kein Anker im Kontenrahmen (SKR 03 / SKR 04). | P2 | S | Steuerberater (legt Konten an) | — | Offen | Ohne saubere Trennung Jahresabschluss nicht nachvollziehbar; Betriebsprüfungs-Risiko. |
| 6 | Tiefkühl-Lasagne-Zeile in der Einordnungstabelle widerspricht D-01 (Phase 1 nur Vakuum gekühlt). | P2 | XS | Steuerberaterin (Doc-Korrektur) | — | Offen | Drift zu D-01; verleitet Leser, Tiefkühl als Phase-1-Option zu lesen. |
| 7 | Briefing-Text an den Steuerberater ist zu kurz. Vier Kern-Fragen fehlen (Kombi-Beleg, Aufwärm-Empfehlung, verbindliche Auskunft, Gewerbeanzeige-Pflicht). | P2 | S | Steuerberaterin (Ausformulierung) | — | Offen | Voraussetzung für Finding 1. Ohne vollständiges Briefing läuft der Steuerberater-Kontakt nicht in einem Zug. |
| 8 | Abschreibung Vakuumierer nicht konkret durchgerechnet. Anschaffungswert, Vorsteuer, AfA-Nutzungsdauer, jährliche AfA fehlen. | P2 | XS | Steuerberaterin (Rechenbeispiel) | — | Offen | Vorsteuer aus Vakuumierer-Kauf (285–665 €) ist Liquidität, die im Rollout-Plan-Budget nicht gegengerechnet ist. |
| 9 | ~~Quantifizierung des MwSt-Risikos fehlt. Was bedeutet eine rückwirkende Umstufung auf 19 % für die Marge?~~ **Entfällt — keine rückwirkende Umstufung auf 19 % mehr möglich, weil es keinen 19 %-Satz für Speisen mehr gibt.** | P2 → ✅ | — | — | — | Aufgelöst | — |
| 10 | Vorsteuer-Zuordnung für Retail-spezifische Einkäufe (Beutel, Etiketten, Labor, Schulung) nicht operationalisiert. | P3 | XS | Steuerberater (Konten-Anker) | — | Offen | Mit Finding 5 zusammen lösbar. Praktisch relevant bei der ersten Umsatzsteuer-Voranmeldung. |
| 11 | Umgang mit Verderb / Entsorgung abgelaufener Ware fehlt als Standard-Prozess (Warenvernichtungsprotokoll, Buchungssatz, USt-Effekt). | P3 | XS | Steuerberaterin (Standard-Prozess beschreiben) | — | Offen | Bei 5–10 % Verderb laufender Buchungsvorgang. Klärt sich mit Finding 5 im selben Konten-Konzept. |
| 12 | Cross-Refs zu Doc 14 (Recht, § 58 LFGB) und Doc 03 (Vetamt, § 42/43 IfSG-Belehrung) fehlen. | P3 | XS | Steuerberaterin (Doc-Ergänzung) | — | Offen | Reife-Problem, kein Gate-Problem. Verhindert Doppel-Aufbau von Doku-Pflichten. |
| 13 | Fernabsatz / Onlineversand nicht explizit als "nicht in Phase 1" markiert. | P3 | XS | Steuerberaterin (Doc-Ergänzung) | — | Offen | Konsistenz mit `rollout-plan.md`; verhindert falsche Übertragung der 7-%-Einordnung auf einen hypothetischen Versand. |

## Auflösungs-Gruppen

Die 13 Findings zerfallen in drei Gruppen, die unterschiedliche Arbeits-Stränge auslösen. Die Zuordnung folgt der gleichen Logik wie bei Doc 03 (`03-findings.md`), damit Session 5+ die Gruppen repo-weit einheitlich handhabt.

**Gruppe A — Silvio-Aktionen (extern, außerhalb des Repos):** Findings 1, 2 (indirekt), 3, 4, 7 (Ausführung), 8 (Input). Konkret drei Handlungen:

1. **E-Mail an den Steuerberater** mit dem vollständigen Briefing-Text (Ergebnis aus Gruppe C, Finding 7). Enthält die vier Kern-Fragen, bittet um schriftliche Stellungnahme, fragt nach Notwendigkeit einer verbindlichen Auskunft nach § 89 Abs. 2 AO. Klärt Findings 1, 5 (Konten), 8 (Abschreibung), 10, 11 in einem Zug.
2. **Anruf beim Kassenhersteller oder Blick ins Kassen-Handbuch.** Klärt Finding 4: TSE ja/nein, Zwei-Steuersatz-Fähigkeit ja/nein. Zehn Minuten Aufwand.
3. **Gewerbeanzeige-Erweiterung beim Gewerbeamt Stuttgart.** Klärt Finding 3. Kann parallel zu 1 passieren, weil sie nicht vom Steuerberater-Ergebnis abhängt. Kosten 15–60 €, Bearbeitungsdauer wenige Tage.

Diese drei Aktionen sind **nicht-Session-gebunden**. Silvio macht sie, Ergebnisse kommen als [TBD-Silvio]-Nachträge in den v2-Plan. Empfehlung: analog zu Doc 03 Gruppe A parallel zu den Vetamt/IHK-Anrufen abarbeiten — beide Gruppen A (Doc 03 + Doc 15) bilden zusammen das **Silvio-Aufgaben-Paket für die nächsten 1–2 Wochen**.

**Gruppe B — CFO-Cross-Review und Doc-02/Doc-07-Drift:** Findings 2, 9. Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) müssen im CFO-Review ausdrücklich auf Netto/Brutto und MwSt-Behandlung geprüft werden. Finding 9 (Quantifizierung des MwSt-Risikos) ist inhaltlich ein CFO-Thema, weil es um Sensitivität geht, nicht um Steuerrecht. Empfehlung: Finding 9 wandert in den späteren Doc-02-Review (CFO-Lead) als explizites Prüfkriterium.

**Gruppe C — Doc-Rewrite-Arbeit:** Findings 5, 6, 7 (Text-Ausformulierung), 10, 11, 12, 13. Korrekturen und Ergänzungen, die in Doc 15 v2 gehören. Klein bis mittel — aber nur sinnvoll, wenn Gruppe A Ergebnisse geliefert hat. Sonst werden die Lücken mit neuen [TBD]-Markern überschrieben statt gefüllt. Finding 7 (Briefing-Text) ist der einzige Punkt aus Gruppe C, der **vor** Gruppe A passieren muss, weil er den Input für die Silvio-E-Mail an den Steuerberater liefert.

## Cross-Drift in inconsistencies.md

Zwei Findings wirken auf `docs/findings/inconsistencies.md`:

1. **Finding 1 (MwSt-Einordnung)** präzisiert den bestehenden Eintrag #5 (MwSt 7 % vs. 19 %). Der Eintrag existiert bereits, aber er benennt weder den Pfad (verbindliche Auskunft) noch den Gate-Status (Rollout-Schritt 1). Präzisierung erfolgt im nächsten Work-Block.
2. **Finding 2 (Doc 02 / Doc 07 ohne MwSt-Erwähnung)** ist **neuer** Drift und rechtfertigt einen eigenen Eintrag: `#8 — Netto/Brutto-Kennzeichnung fehlt in Doc 02 und Doc 07`. Wird im nächsten Work-Block als Eintrag #8 angelegt.

## Nächste Schritte

1. [ ] `inconsistencies.md` aktualisieren: Eintrag #5 präzisieren, Eintrag #8 neu anlegen.
2. [ ] Gruppe A (Silvio-Aktionen): wenn Session 5 Variante C später angegangen wird oder als asynchrones Silvio-Paket, die drei Handlungen mit den Doc-03-Gruppe-A-Handlungen zusammenziehen (ein gemeinsames Briefing für Silvio).
3. [ ] Gruppe B (CFO-Cross): in den Doc-02-Review als Lead-Kriterium einziehen, wenn Doc 02 ansteht (Sequenz: nicht in der Gate-kritischen 03 → 15 → 05 → 04 → 14, sondern danach).
4. [ ] Gruppe C (Doc-Rewrite): v2-Plan-Skizze `docs/plans/15-v2-plan.md` erst nach Gruppe-A-Ergebnissen. Nicht in Session 5.
5. [ ] Finding 7 (Briefing-Text) — optionales Vor-Ausliefern als Textbaustein, damit Silvio die E-Mail an den Steuerberater sofort verschicken kann, ohne auf v2 zu warten. Könnte Teil der kombinierten Silvio-Briefing-Notiz werden (analog Doc 03 Variante C aus Session 4).
