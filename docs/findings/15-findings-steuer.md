# Findings: Doc 15 – Steuerliche Behandlung

**Quelle:** [Lead-Review Steuerberaterin](../reviews/15-steuer-steuerberaterin.md)
**Datum:** 2026-04-11
**Status:** **Doc 15 v2 geschrieben** (2026-04-12). Von 16 Findings sind 13 in Doc 15 v2 aufgelöst, 2 waren vorher schon aufgelöst (F1 Steueränderungsgesetz, F9 MwSt-Risiko entfällt), 1 offen (F2 Netto/Brutto-Propagation in Doc 02/07). Drei Findings (F14, F15, F16) sind in Doc 15 adressiert, müssen aber in Doc 02, Doc 12, Doc 18 propagiert werden. Findings 1 und 9 wurden nach Bekanntwerden des Steueränderungsgesetzes 2025 (7 % auf Speisen in Gastronomie seit 1.1.2026) auf "aufgelöst — Silvio-Verifikation offen" umgestellt. Die Nebenpunkte bleiben unverändert gültig.

> **Nachtrag 2026-04-11:** Seit 1. Januar 2026 gilt laut Steueränderungsgesetz 2025 ein dauerhafter 7 %-Umsatzsteuersatz auf Speisen in der Gastronomie (Bundestag 04.12.2025). Das löst die MwSt-Kernfrage aus Finding 1 und die Quantifizierungs-Frage aus Finding 9 auf. Die beiden Einträge stehen weiter in der Tabelle, sind aber als "aufgelöst, Silvio-Verifikation beim Steuerberater-Kontakt" markiert, damit die Historie nachvollziehbar bleibt. Die übrigen Findings (Gewerbeanzeige, KassenSichV, Kontenrahmen, Abschreibung, Verderb-Buchung, Vorsteuer, Cross-Refs) sind nicht betroffen.

Konsolidierte Findings aus dem Lead-Review. Format und Struktur analog `03-findings-veterinaeramt.md`. Jedes Finding benennt Auflösungs-Pfad, Owner und Impact. Findings sind die Grundlage für den späteren v2-Plan (`docs/plans/15-v2-plan.md`, noch nicht geschrieben) und für Cross-Drift-Einträge in `inconsistencies.md`.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | ~~MwSt-Einordnung (7 % vs. 19 %) ist nicht prüfungsfest. Pfad zur verbindlichen Auskunft nach § 89 Abs. 2 AO fehlt.~~ **Aufgelöst durch Steueränderungsgesetz 2025 — 7 % auf Speisen in Gastronomie seit 1.1.2026, gilt auch für Retail-Mitnahme.** Verifikation Teil von Silvio-Paket SP-05 (Steuerberater-Briefing). | P1 → ✅ | — | Steuerberaterin (nach Rückmeldung) | — | Aufgelöst, Verifikation offen | Der größte Gate-Blocker nach Rollout-Schritt 1 ist weg. |
| 2 | ~~Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) erwähnen MwSt nicht. Netto/Brutto ist nirgends fixiert.~~ **In Doc 15 v2 aufgelöst:** Netto/Brutto-Deklaration im Doc-Kopf verankert ("Alle Preise sind Brutto inkl. 7 % USt"). Doc 02 und Doc 07 müssen im v2-Rewrite dieselbe Deklaration übernehmen. | P1 → ⚠️ | S | CFO (Doc-02/07-Rewrite) | — | In Doc 15 gelöst, in Doc 02/07 offen | Deklaration existiert, muss in die anderen Docs propagiert werden. |
| 3 | ~~Gewerbeanzeige nach § 14 GewO nicht adressiert.~~ **In Doc 15 v2 eigener Abschnitt.** Silvio-Aktion SP-03 bleibt offen. | P1 → ✅ | XS | — | — | In Doc gelöst, SP-03 offen | Ohne Erweiterung läuft der Retail-Umsatz ordnungsrechtlich nicht sauber; Risiko Bußgeld und Umsatzsperre. |
| 4 | ~~KassenSichV / TSE-Pflicht nicht geprüft.~~ **In Doc 15 v2 eigener Abschnitt mit Worst-Case-Kosten.** Silvio-Aktion SP-06 bleibt offen. | P1 → ✅ | XS | — | SP-06 offen | In Doc gelöst, SP-06 offen | Bei Kassen-Nachschau hart geprüft; fehlende TSE ist Bußgeld-bewehrt. |
| 5 | ~~Trennung Erlöskonten nicht operationalisiert.~~ **In Doc 15 v2 mit SKR-03/04-Beispiel und Briefing-Text.** SP-05 bleibt offen (Steuerberater bestätigt konkreten Kontenrahmen). | P2 → ✅ | — | — | SP-05 offen | In Doc gelöst. | Ohne saubere Trennung Jahresabschluss nicht nachvollziehbar; Betriebsprüfungs-Risiko. |
| 6 | ~~Tiefkühl-Lasagne-Zeile in der Einordnungstabelle widerspricht D-01.~~ **In Doc 15 v2 entfernt.** Tabelle zeigt nur Phase-1-Produkte. | P2 → ✅ | — | — | — | Gelöst. | Drift zu D-01; verleitet Leser, Tiefkühl als Phase-1-Option zu lesen. |
| 7 | ~~Briefing-Text an den Steuerberater ist zu kurz.~~ **In Doc 15 v2 vollständig ausformuliert** — vier Kern-Fragen plus Abschreibungs- und Vorsteuer-Bitte. Copy-paste-fähig. | P2 → ✅ | — | — | — | Gelöst. | Voraussetzung für Finding 1. Ohne vollständiges Briefing läuft der Steuerberater-Kontakt nicht in einem Zug. |
| 8 | ~~Abschreibung Vakuumierer nicht konkret durchgerechnet.~~ **In Doc 15 v2 mit vollständiger Rechnung** (Netto/Brutto/Vorsteuer/AfA 8 Jahre/Cash-Flow-Effekt). | P2 → ✅ | — | — | — | Gelöst. | Vorsteuer aus Vakuumierer-Kauf (285–665 €) ist Liquidität, die im Rollout-Plan-Budget nicht gegengerechnet ist. |
| 9 | ~~Quantifizierung des MwSt-Risikos fehlt. Was bedeutet eine rückwirkende Umstufung auf 19 % für die Marge?~~ **Entfällt — keine rückwirkende Umstufung auf 19 % mehr möglich, weil es keinen 19 %-Satz für Speisen mehr gibt.** | P2 → ✅ | — | — | — | Aufgelöst | — |
| 10 | ~~Vorsteuer-Zuordnung für Retail-spezifische Einkäufe nicht operationalisiert.~~ **In Doc 15 v2 als Liste in Abschnitt "Vorsteuer-Zuordnung".** | P3 → ✅ | — | — | — | Gelöst. | Mit Finding 5 zusammen lösbar. Praktisch relevant bei der ersten Umsatzsteuer-Voranmeldung. |
| 11 | ~~Umgang mit Verderb / Entsorgung abgelaufener Ware fehlt.~~ **In Doc 15 v2 eigener Abschnitt** mit Warenvernichtungsprotokoll, Buchungssatz, Kostenblock-Rechnung. | P3 → ✅ | — | — | — | Gelöst. | Bei 5–10 % Verderb laufender Buchungsvorgang. Klärt sich mit Finding 5 im selben Konten-Konzept. |
| 12 | ~~Cross-Refs zu Doc 14 und Doc 03 fehlen.~~ **In Doc 15 v2 Cross-Referenzen-Tabelle** mit 7 Verweisen (Doc 02, 03, 07, 10, 12, 14, 18). | P3 → ✅ | — | — | — | Gelöst. | Reife-Problem, kein Gate-Problem. Verhindert Doppel-Aufbau von Doku-Pflichten. |
| 13 | ~~Fernabsatz / Onlineversand nicht explizit als "nicht in Phase 1" markiert.~~ **In Doc 15 v2 im Scope-Header und unter "Fallstricke" Punkt 3.** | P3 → ✅ | — | — | — | Gelöst. | Konsistenz mit `rollout-plan.md`; verhindert falsche Übertragung der 7-%-Einordnung auf einen hypothetischen Versand. |
| 14 | Fixkosten-Allokation Retail-Strang fehlt — ohne anteiligen Overhead sieht jede variable Kalkulation profitabel aus. **In Doc 15 v2 als Hinweis-Abschnitt mit Methodik-Empfehlung (Vollkosten vs. Teilkosten).** Muss als Methodik-Entscheidung in Doc 02 verankert werden. | P2 | S | CFO (Doc-02-Lead-Review) | — | In Doc 15 adressiert, in Doc 02 offen | Ohne Allokation subventioniert das Restaurant den Retail-Strang verdeckt — die betriebswirtschaftliche Antwort "lohnt sich Retail?" ist dann nicht beantwortbar. |
| 15 | ~~Gewerbesteuer-Effekt nicht modelliert.~~ **In Doc 15 v2 eigener Abschnitt mit Hebesatz-Rechnung.** Muss in Doc 02 und Doc 18 übernommen werden. | P3 → ✅ | — | — | — | In Doc 15 gelöst, Propagation in Doc 02/18 offen. | Kein Stopper, aber ein Posten in der Wirtschaftlichkeitsrechnung; beeinflusst Gewerbesteuer-Vorauszahlung. |
| 16 | ~~Kassensystem-worst-case-Kosten nicht als Budgetposition.~~ **In Doc 15 v2 im KassenSichV-Abschnitt mit Kosten-Tabelle.** Muss in Doc 12 als Budgetposition übernommen werden. | P2 → ✅ | — | — | SP-06 offen | In Doc 15 gelöst, Propagation in Doc 12 offen. | Wenn Kasse nicht TSE-fähig: Stopper für Rollout, plus ungeplanter Capex-Block. |

## Auflösungs-Gruppen

Die 16 Findings (13 aus Lead-Review + 3 aus CFO-Co-Review) zerfallen in drei Gruppen, die unterschiedliche Arbeits-Stränge auslösen. Die Zuordnung folgt der gleichen Logik wie bei Doc 03 (`03-findings-veterinaeramt.md`), damit Session 5+ die Gruppen repo-weit einheitlich handhabt.

**Gruppe A — Aktionen im Silvio-Paket** (`docs/silvio-paket/offene-fragen.md`, Block 2): Findings 1/5/8/10/11 → SP-05 (Steuerberater-Briefing per E-Mail mit vier Kern-Fragen, Konten, Abschreibung, Vorsteuer, Verderb), 4 → SP-06 (Kassenhersteller-Check TSE + Zwei-Steuersatz), 3 → SP-03 (Gewerbeanzeige-Erweiterung Stuttgart). Finding 7 (Briefing-Text) ist eine Vor-Arbeit von Gruppe C (Claude), die den Input für SP-05 liefert.

**Gruppe B — CFO-Cross-Review und Doc-02/Doc-07-Drift:** Findings 2, 9, **14, 15, 16** (drei neue aus CFO-Co-Review). Doc 02 (Wirtschaftlichkeit) und Doc 07 (Preisgestaltung) müssen im CFO-Review ausdrücklich auf Netto/Brutto und MwSt-Behandlung geprüft werden. Finding 9 (Quantifizierung des MwSt-Risikos) ist inhaltlich ein CFO-Thema, weil es um Sensitivität geht, nicht um Steuerrecht. Finding 14 (Fixkosten-Allokation) und 15 (Gewerbesteuer) gehören in den Doc-02-Lead-Review, Finding 16 (Kassen-Kosten) in den Doc-12-Lead-Review. Empfehlung: alle fünf als explizite Prüfkriterien in die jeweiligen CFO-Lead-Reviews einziehen.

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
