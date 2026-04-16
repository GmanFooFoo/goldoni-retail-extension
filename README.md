# Goldoni Retail Extension

Arbeits-Repo für den Business Case **Retail-Extension für das Ristorante Goldoni Stuttgart** (Vakuumierte Gerichte aus der laufenden Küche für den Außer-Haus-Verkauf). Inhaber: Silvio Brunetti. Freundschaftsprojekt, kein Beratungsmandat. Owner: German Rauhut.

Dieses README ist die Arbeits-Übersicht für German selbst. Nicht Silvio-facing. Silvio liest das Repo nicht direkt — Silvio-Ableitungen entstehen ad-hoc, wenn konkret gebraucht (D-06, Variante B).

## Phase

**Phase A — aktiv** (D-08). Business-Case-Reviews, Scope-Schärfung, Rollout-Vorbereitung bis Silvio eine Entscheidung trifft (Ja / Nein / Später). Hoher Session-Takt zulässig.

Nach Silvios Entscheidung: Phase B (reduziert aktiv, Pilot-Begleitung) oder Phase C (Kontext-Speicher, keine Weiterentwicklung). Jede Maßnahme in diesem Repo muss die Frage bestehen: *"Brauchen wir das in der aktuellen Phase?"*

## Scope

Phase 1 des Produkts: **nur Vakuum, gekühlt, eine Woche Haltbarkeit**. Keine Tiefkühlung, kein Schockfroster, keine MAP/Schutzgas. Tiefkühl steht als mögliche Phase 2 auf der Roadmap (D-02), ist aber bewusst nicht im Launch-Scope.

Zielkanal: **Abholung im Restaurant + Plattform-Lieferung** (Wolt/Uber Eats) innerhalb Stuttgart (D-13). Kein Paketversand, keine Lieferung über Stadtgrenzen. Webshop zum Vorbestellen ab Phase 1 (D-12). Zielgruppe: Stammgäste, Büros im Stuttgarter Westen, Familien mit Convenience-Bedarf. Öffnungszeiten Goldoni: Mi + Do–So, 17–22 Uhr (zwei Küchen-Leerlauf-Tage Mo/Di als produktives Zeitfenster).

## Repo-Map

| Ordner / Datei | Inhalt |
|---|---|
| `docs/business-case/` | Die 20 Dokumente (19 Original + Doc 20 Personal-Setup). **Alle 20 auf v2** (Session 13–15). |
| `docs/personas/` | 12 rollenbasierte Review-Personas als Analyse-Linsen (00 Silvio Übersetzungs-Schicht, 01 CFO, 02 Lebensmittelrecht, 03 Steuer, 04 Behördenkontrolleur, 05 Logistiker, 06 Gastronom, 07 Küchenchef, 08 Brand/Marketing, 09 Stammkundin, 10 Dr. Maldini Regulatorik-Scout, 11 Personal-Markt & Arbeitsrecht Retail). |
| `docs/personas/assignments.md` | Matrix: welche Persona reviewt welches Doc. |
| `docs/findings/decisions.md` | Entscheidungs-Log D-01 bis D-13. Grundlegend für Scope- und Ton-Fragen. Neu Session 11: D-11 (BAFA), D-12 (Vorbestellungen Phase 1), D-13 (Vertriebskanal Abholung + Wolt/Uber). |
| `docs/findings/inconsistencies.md` | 17 Widersprüche, davon **16 aufgelöst**. **1 offen:** #2 (Launch-Mengen, Präzisierung). #16 aufgelöst in Session 16 durch Geschenkebox-Konzept, #17 aufgelöst in Session 18 (Öffnungszeiten in Doc 01 v2 und Doc 10 v2 bereits auf 17–22). |
| `docs/reviews/` | Persona-Reviews im Standard-Format. **Alle 20 Docs lead-reviewt.** Gate-Docs (03/04/05/14/15): Lead + Co fertig. Doc 02: Lead + 2 Co fertig. Session 13: 8 Lead-Reviews + 14 Tier-1-Co-Reviews. **45 Reviews gesamt.** |
| `docs/findings/` | Konsolidierte Findings pro Doc. **20 Findings-Dateien:** 01 Übersicht (10), 02 Wirtschaftlichkeit (22), 03 Vetamt (16), 04 LMIV (23), 05 HACCP (28), 06 Mockups (12), 07 Preisgestaltung (17), 08 Verpackung (14), 09 Verkaufsstrategie (12), 10 Operative Umsetzung (24), 11 Lieferanten (11), 12 Investitionsplan (9), 13 Rollout (17), 14 Recht (25), 15 Steuer (16), 16 Risiken (17), 17 Wettbewerb (7), 18 Finanzierungsplan (8), 19 Sortiment (11), 20 Personal-Setup (9). Gesamt: **308 Findings**. |
| `docs/silvio-paket/offene-fragen.md` | **Zentrales Artefakt für Silvio-Aktionen.** 26 Einträge SP-01 bis SP-26 in acht Blöcken. Neu Session 16: SP-25 (DEHOGA-BW-Mitgliedschaft), SP-26 (Produkthaftpflicht Handelsware Rummo). SP-19 (Béchamel) bei Silvio seit 2026-04-12. |
| `docs/plans/` | v2-Pläne und Themen-Analysen. Doc-bezogen: `02-v2-plan.md`, `02-cashflow-projektion-2026.md`, `03-v2-plan.md`, `20-personal-setup-retail.md`, `21-foerdermittel.md`, `22-q4me-evaluation.md`, `22-software-tools.md`. Themen: `52-sensitivity-analyse.md` (Break-Even-Matrix 15–70 Stk/W, Go/No-Go-Checkpoints), `54-geschenkebox-konzept.md` (LMIV + Kalkulation, VK 19,90/22,90 €). Rollout-Plan: `rollout-plan.md`. |
| `docs/silvio-derivatives/` | Silvio-facing Ableitungen. Persona-00-Gesamtüberblick (`gesamt-ueberblick.md`), Silvio-Paket-Hand-Outs (`silvio-paket-1-anrufe-und-termine.md`), YAML-getriebener PPTX-Generator (`slides-content.yaml`, `goldoni-retail-ueberblick.pptx`), Pitch-Variante (`pitch-content.yaml`, `goldoni-retail-pitch.pptx`). |
| `scripts/` | Hilfs-Skripte. `create-slides.py` rendert PPTX aus YAML-Content (13 Slides, Goldoni-Farbschema). `create-label-mockup.py` rendert Etikett-Platzhalter-Mockups (80×120 mm, 300 DPI) für alle 5 Phase-1-Produkte als PNG nach `docs/silvio-derivatives/labels/`. |
| `docs/glossary.md` | Fachbegriffe (HACCP, LMIV, CCP, Vakuum vs. Schutzgas, Schockfroster, Vetamt). Primär als Silvio-Hilfe gedacht, auch für Germans Cross-Reference nützlich. |
| `docs/backlog/repo-backlog.md` | Status-Tabelle aller Arbeitspakete im MASCHIN-Format. |
| `docs/session-handoff.md` | Wie Sessions gestartet und geschlossen werden, Feedback-Workflow über GitHub-Issues. |
| `docs/reports/` | Session-Reports (chronologisch). |
| `session-state.md` | Aktueller Stage-Fortschritt und Phase. |
| `SESSION-PROMPT-NEXT.md` | Konkreter Auftrag für die nächste Session. |

## Entscheidungen

Voller Log in [`docs/findings/decisions.md`](docs/findings/decisions.md). Tragend für aktuelle Arbeit:

- **D-02** — Phase 1 nur Vakuum, Tiefkühl vertagt.
- **D-06** — Repo-Ton ist Germans Arbeits-Level. Silvio-facing Texte als explizite Ableitung.
- **D-10** — Silvio ist kein Reviewer. Aktionen im Silvio-Paket (SP-XX).
- **D-11** — BAFA-Förderung für Germans Beratungsleistung (formales Mandat neben Freundschaft).
- **D-12** — Vorbestellungen ab Phase 1 (Webshop + Stripe, Fernabsatz kein separater Scope-Block).
- **D-13** — Vertriebskanal: Abholung + Wolt/Uber innerhalb Stuttgart, kein Paketversand.

## Personas

Analyse-Linsen, keine Narrative. Neue Personas rollen-basiert ohne Personennamen (Persona 11 ist der erste Fall). Jede Persona hat eine eigene Datei in `docs/personas/` mit Haltung, Fokus-Fragen, Red-Flags-Katalog. Die 12 Rollen decken: Zahlen (CFO), Lebensmittelrecht, Steuern, Küche, Gastronom (peer), Stammkundin, Brand/Marketing, Logistik, Amt (adversarial), Regulatorik-Scout (Dr. Maldini, horizontal), Personal-Markt & Arbeitsrecht Retail (neu Session 9), Silvio (Übersetzungs-Schicht, horizontal).

Reviews folgen dem Standard-Format aus [`CLAUDE.md`](CLAUDE.md#review-standard-format). Alle 20 Docs durchlaufen: Lead-Review → Findings → v2-Rewrite. Gate-kritische Sequenz (5 Docs) zusätzlich mit Co-Reviews abgesichert. Tier-2-Co-Reviews für verbleibende Docs optional.

## Stand pro Dokument

Pipeline: **v1** (Original) → **Lead-Review** → **Co-Reviews** → **Findings** → **v2-Plan** → **v2-Rewrite** → ✅

| # | Dokument | Lead | Co | Findings | v2 | Status |
|---|---|---|---|---|---|---|
| 01 | Business Case Übersicht | ✅ Thomas | 🔲 | 10 | ✅ | Dach-Propagation aller v2-Docs |
| 02 | Wirtschaftlichkeitsrechnung | ✅ CFO | ✅ Steuer, Personal | 22 (19 gelöst) | ✅ | SP-19/22/23 offen ([E]-Marker) |
| 03 | Veterinäramt Stuttgart | ✅ Lebensmittelrecht | ✅ Behörde + R9 | 16 (14 gelöst) | ✅ | — |
| 04 | LMIV-Kennzeichnung | ✅ Lebensmittelrecht + R9 | ✅ Behörde, Küche | 23 (19 gelöst) | ✅ | SP-10 (Herkunftsdaten) |
| 05 | HACCP-Erweiterung | ✅ Lebensmittelrecht | ✅ Behörde, Küche, Logistik + R9 | 28 (24 gelöst) | ✅ | — |
| 06 | Etikett-Spezifikation (ex Mockups) | ✅ Jana | ✅ Lebensmittelrecht | 12 (11 gelöst) | ✅ | Platzhalter-Mockup (5 PNG) in `docs/silvio-derivatives/labels/`. Druckfertiger Entwurf wartet weiter auf SP-09/10/11/19 |
| 07 | Preisgestaltung | ✅ CFO | 🔲 | 17 | ✅ | Margen-Tabelle + 2 Preisschienen |
| 08 | Verpackungsstrategie | ✅ Jana | ✅ Pietro, Bruno | 14 (14 gelöst) | ✅ | — |
| 09 | Verkaufsstrategie | ✅ Jana | 🔲 | 12 | ✅ | 3-Stufen-Kanal-Modell |
| 10 | Operative Umsetzung | ✅ Thomas | ✅ Pietro, Steiger, P11 | 24 (21 gelöst) | ✅ | SP-22, MHD-Strategie, Ehefrau offen |
| 11 | Lieferanten Stuttgart | ✅ Thomas | 🔲 | 11 | ✅ | Zutaten-Steckbriefe + Backup |
| 12 | Investitionsplan | ✅ CFO | 🔲 | 9 (7 gelöst) | ✅ | SP-06/22 offen |
| 13 | Rollout-Plan | ✅ CFO | 🔲 | 17 | ✅ | 10–12 Wochen, gate-basiert |
| 14 | Rechtliche Absicherung | ✅ Lebensmittelrecht + R9 | ✅ Behörde, Steuer | 25 (22 gelöst) | ✅ | — |
| 15 | Steuerliche Behandlung | ✅ Steuer | ✅ CFO | 16 (15 gelöst) | ✅ | — |
| 16 | Risiken & Gegenmaßnahmen | ✅ CFO | ✅ Thomas, Vogel | 17 (17 gelöst) | ✅ | — |
| 17 | Wettbewerbsanalyse | ✅ CFO | 🔲 | 7 | ✅ | 3-Ebenen + Substitut-Analyse |
| 18 | Finanzierungsplan | ✅ CFO | 🔲 | 8 (8 gelöst) | ✅ | BAFA/L-Bank, KfW gestrichen |
| 19 | Produktsortiment-Erweiterung | ✅ Jana | ✅ Pietro | 11 (10 gelöst) | ✅ | Polpette Phase-2-Roadmap |
| 20 | Personal-Setup Retail | ✅ P11 | 🔲 | 9 (8 gelöst) | ✅ | IfSG Ehefrau offen (SP-04) |

**Legende:** ✅ erledigt, 🔲 offen, R9 = Rule-9-Regulatorik-Nachtrag

**Aggregate:** **20/20 Docs lead-reviewt, 20/20 auf v2.** 308 Findings, davon ~260 in v2-Rewrites adressiert. 45 Reviews (31 Lead + 14 Tier-1-Co). 16/17 Inconsistencies aufgelöst, 1 offen (#2).

### Silvio-Paket

26 Einträge (SP-01 bis SP-26) in acht Blöcken. Gate-kritisch offen:

| SP | Thema | Status | Blockiert |
|---|---|---|---|
| SP-09 | Vollständige Anschrift (Hausnr. + PLZ) | Offen | Doc 06 Etikett druckfertig |
| SP-11 | Labor-Nährwertanalyse (400–750 €) | Offen | Doc 06 Nährwerttabelle |
| SP-19 | Rezeptur (ohne Béchamel, Gramm-Angaben) | Bei Silvio (WhatsApp 12.04.) | Doc 02/04/05/06 |
| SP-20 | Geschenkebox OK + Rummo-Sorte | Offen (Konzept bereit) | Doc 07/19, Launch-Plan |
| SP-22 | Metro-/Lieferanten-Preise | Offen | Doc 02/07/11 [E]-Marker |
| SP-23 | Nachfrage-Schätzung | Offen | Doc 02 Absatz-Szenarien |
| SP-24 | Aktuelle Kartenpreise | Offen | Doc 07 Preisanker |
| SP-25 | DEHOGA-BW-Mitgliedschaft | Offen | Q4Me-Preis in Doc 22, Cashflow |
| SP-26 | Produkthaftpflicht Handelsware Rummo | Offen | Geschenkebox-Launch |

### Cashflow-Projektion

Hypothetisch bei Start Mai 2026: Invest ~6.200 €, Ende 2026 kumuliert −3.100 €, operativ ab August positiv (~650 €/Monat), Cashflow-Break-Even Mai/Juni 2027. Realer Gewinnbeitrag: **7.000–9.000 €/Jahr** (nicht 19.500 € wie Doc 02 v1). Details: [`docs/plans/02-cashflow-projektion-2026.md`](docs/plans/02-cashflow-projektion-2026.md).

### Rechts-Stichtage H2/2026

| Datum | Regelwerk | Wirkung |
|---|---|---|
| 1.7.2026 | Listerien-Grenzwert verschärft | "nicht nachweisbar in 25g" — durch Arbeitsannahme ohne Béchamel (SP-19) entschärft, Büffelmozzarella bleibt Substrat |
| 12.8.2026 | PPWR (Verpackung) | Konformitätserklärung Pflicht |
| 9.12.2026 | ProdHaftG-Novelle | 25-Jahre-Haftung, Chargen-Doku als Beweismittel |

## Working Rules

Siehe [`CLAUDE.md`](CLAUDE.md) für das vollständige Projekt-Regelwerk (Review-Format, Session-Disziplin, Commit-Rhythmus, Pushback-Erwartung, MASCHIN-Tabellenformat). Kernpunkte:

- Jede Zahl mit Quelle oder `[TBD-Silvio]` / `[TBD-Recherche]`-Marker.
- Commit nach jedem Work-Block.
- Plain Markdown, keine Static-Site-Builder, keine Hard-Wraps im Fließtext.
- Review → Findings → Plan → v2. Nie v1 → v2 direkt.
- Completion zweistufig: "in-review" ≠ "done".

## Nicht im Scope dieses Repos

- Keine Real-World-Ausführung (Anrufe, Termine, E-Mails) — das macht German außerhalb des Repos.
- Keine rechtliche oder steuerliche Zusicherung — Personas geben Einschätzungen, kein Gutachten. Vor Livegang echter Anwalt / Steuerberater.
- Kein Code-Produkt. Docs-only. Kein Shop, keine App.
- Keine Ersetzung von Silvios Entscheidungen (Preise, Mengen, Lieferanten, Termin).

## Kontakt

- Projekt-Owner: German Rauhut (GmanFooFoo).
- Zielperson: Silvio Brunetti, Inhaber Ristorante Goldoni Stuttgart. Freund, kein Kunde.
- Planning-Instanz außerhalb dieses Repos: MASCHIN in `~/Developer/projects/OMNIXIS-planning/` — nur für strukturelle Fragen, nicht für Tagesarbeit.
