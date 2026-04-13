# Goldoni Retail Extension

Arbeits-Repo für den Business Case **Retail-Extension für das Ristorante Goldoni Stuttgart** (Vakuumierte Gerichte aus der laufenden Küche für den Außer-Haus-Verkauf). Inhaber: Silvio `[TBD-Nachname]`. Freundschaftsprojekt, kein Beratungsmandat. Owner: German Rauhut.

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
| `docs/business-case/` | Die 19 Original-Dokumente (v1) — Küche, Zahlen, Recht, Verpackung, Verkauf, Logistik. Gate-kritische Sequenz 03 → 15 → 05 → 04 → 14 lead-reviewt (Stufe 3). |
| `docs/personas/` | 12 rollenbasierte Review-Personas als Analyse-Linsen (00 Silvio Übersetzungs-Schicht, 01 CFO, 02 Lebensmittelrecht, 03 Steuer, 04 Behördenkontrolleur, 05 Logistiker, 06 Gastronom, 07 Küchenchef, 08 Brand/Marketing, 09 Stammkundin, 10 Dr. Maldini Regulatorik-Scout, 11 Personal-Markt & Arbeitsrecht Retail). |
| `docs/personas/assignments.md` | Matrix: welche Persona reviewt welches Doc. |
| `docs/findings/decisions.md` | Entscheidungs-Log D-01 bis D-13. Grundlegend für Scope- und Ton-Fragen. Neu Session 11: D-11 (BAFA), D-12 (Vorbestellungen Phase 1), D-13 (Vertriebskanal Abholung + Wolt/Uber). |
| `docs/findings/inconsistencies.md` | 16 Widersprüche, davon **4 aufgelöst** (#5 USt, #11 Rückruf-Schreibort, #14 Aufbewahrungs-Fristen, #15 Béchamel-Arbeitsannahme). 12 offen. #2 und #8 mit Cross-Refs zu Doc-02-Findings ergänzt (Session 11). |
| `docs/reviews/` | Persona-Reviews im Standard-Format. **Gate-Docs (03/04/05/14/15):** Lead + Co fertig. **Doc 02 (Session 11):** Lead CFO + Co Steuerberaterin + Co Persona 11 fertig. |
| `docs/findings/` | Konsolidierte Findings pro Doc. **6 Findings-Dateien:** 03 Vetamt (16), 04 LMIV (23), 05 HACCP (28), 14 Recht (25), 15 Steuer (16), **02 Wirtschaftlichkeit (22, Session 11)**. Gesamt: **131 Findings**. |
| `docs/silvio-paket/offene-fragen.md` | **Zentrales Artefakt für Silvio-Aktionen.** 24 Einträge SP-01 bis SP-24 in acht Blöcken. Neu Session 11: SP-22 (Metro-Preise), SP-23 (Nachfrage-Schätzung), SP-24 (Kartenpreise). SP-19 (Béchamel) bei Silvio seit 2026-04-12. |
| `docs/plans/02-v2-plan.md` | v2-Plan Doc 02 — 10 Kapitel, Finding-zu-Kapitel-Matrix, 19 von 22 Findings im v2 auflösbar. |
| `docs/plans/02-cashflow-projektion-2026.md` | Monats-P&L Mai–Dez 2026 (hypothetisch bei Start Mai). Invest ~6.200 €, operativ ab August positiv, Cashflow-Break-Even Mai/Juni 2027. |
| `docs/plans/03-v2-plan.md` | v2-Plan-Skizze Doc 03. |
| `docs/plans/rollout-plan.md` | Phase-1-Scope und Rollout-Reihenfolge. Wird in dieser Session ebenfalls auf Germans Arbeits-Level gezogen (Stufe 6 / 2b). |
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

Reviews folgen dem Standard-Format aus [`CLAUDE.md`](CLAUDE.md#review-standard-format). Gate-kritische Sequenz (5 Docs, 14 Reviews, 109 Findings) Lead + Co fertig + v2-Rewrites fertig. **Doc 02 Wirtschaftlichkeit** (Session 11): Lead + 2 Co fertig, 22 Findings, Cashflow-Projektion, v2-Plan. Sekundär-Reviews Doc 01/06–13/16–19 stehen aus.

## Stand pro Dokument

Pipeline: **v1** (Original) → **Lead-Review** → **Co-Reviews** → **Findings** → **v2-Plan** → **v2-Rewrite** → ✅

| # | Dokument | Lead | Co | Findings | v2-Plan | v2 | Blocker |
|---|---|---|---|---|---|---|---|
| 01 | Business Case Übersicht | 🔲 | — | — | — | — | — |
| **02** | **Wirtschaftlichkeitsrechnung** | **✅ CFO** | **✅ Steuer, Personal** | **22 (19 gelöst)** | **✅** | **✅** | SP-19/22/23 offen |
| 03 | Veterinäramt Stuttgart | ✅ Lebensmittelrecht | ✅ Behörde + R9 | 16 | ✅ | ✅ (14 gelöst) | — |
| 04 | LMIV-Kennzeichnung | ✅ Lebensmittelrecht + R9 | ✅ Behörde, Küche | 23 | — | ✅ (19 gelöst) | SP-10 |
| 05 | HACCP-Erweiterung | ✅ Lebensmittelrecht | ✅ Behörde, Küche, Logistik + R9 | 28 | — | ✅ (24 gelöst) | — |
| 06 | Mockups | 🔲 | — | — | — | — | — |
| **07** | **Preisgestaltung** | **✅ CFO** | **🔲** | **12** | **🔲** | **🔲** | Doc 02 v2 erst |
| 08 | Verpackungsstrategie | 🔲 | — | — | — | — | — |
| 09 | Verkaufsstrategie | 🔲 | — | — | — | — | — |
| 10 | Operative Umsetzung | 🔲 | — | — | — | — | — |
| 11 | Lieferanten Stuttgart | 🔲 | — | — | — | — | — |
| **12** | **Investitionsplan** | **✅ CFO** | **🔲** | **9** | **🔲** | **🔲** | Doc 02 v2 Propagation |
| 13 | 6-Wochen-Rollout-Plan | 🔲 | — | — | — | — | — |
| 14 | Rechtliche Absicherung | ✅ Lebensmittelrecht + R9 | ✅ Behörde, Steuer | 25 | — | ✅ (22 gelöst) | — |
| 15 | Steuerliche Behandlung | ✅ Steuer | ✅ CFO | 16 | — | ✅ (15 gelöst) | — |
| 16 | Risiken & Gegenmaßnahmen | 🔲 | — | — | — | — | — |
| 17 | Wettbewerbsanalyse | 🔲 | — | — | — | — | — |
| 18 | Finanzierungsplan | 🔲 | — | — | — | — | Doc 02 erst |
| 19 | Produktsortiment-Erweiterung | 🔲 | — | — | — | — | — |
| 20 | Personal-Setup Retail (Plan) | 🔲 P11 | — | — | — | — | — |

**Legende:** ✅ erledigt, ⚠️ in Arbeit, 🔲 offen, R9 = Rule-9-Regulatorik-Nachtrag

**Aggregate:** 8 von 20 Docs lead-reviewt (40 %). 152 Findings. 6 v2-Rewrites fertig. 19 Reviews gesamt.

### Silvio-Paket

23 Einträge (SP-01 bis SP-23) in acht Blöcken. Gate-kritisch offen:

| SP | Thema | Status | Blockiert |
|---|---|---|---|
| SP-19 | Rezeptur (Béchamel, Gramm-Angaben) | Bei Silvio (WhatsApp 12.04.) | Doc 02/04/05 v2-Finishing |
| SP-22 | Metro-/Lieferanten-Preise | Offen | Doc 02 v2 (Quellen-Anforderung) |
| SP-23 | Nachfrage-Schätzung | Offen | Doc 02 v2 (Absatz-Szenarien) |
| SP-05 | Steuerberater-Briefing | Hand-Out bereit | Steuer-Verifikation |
| SP-13 | Launch-Timing | Hand-Out bereit | Rollout-Kalender |

### Cashflow-Projektion

Hypothetisch bei Start Mai 2026: Invest ~6.200 €, Ende 2026 kumuliert −3.100 €, operativ ab August positiv (~650 €/Monat), Cashflow-Break-Even Mai/Juni 2027. Realer Gewinnbeitrag: **7.000–9.000 €/Jahr** (nicht 19.500 € wie Doc 02 v1). Details: [`docs/plans/02-cashflow-projektion-2026.md`](docs/plans/02-cashflow-projektion-2026.md).

### Rechts-Stichtage H2/2026

| Datum | Regelwerk | Wirkung |
|---|---|---|
| 1.7.2026 | Listerien-Grenzwert verschärft | "nicht nachweisbar in 25g" — relevant bei Béchamel |
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
- Zielperson: Silvio `[TBD-Nachname]`, Inhaber Ristorante Goldoni Stuttgart. Freund, kein Kunde.
- Planning-Instanz außerhalb dieses Repos: MASCHIN in `~/Developer/projects/OMNIXIS-planning/` — nur für strukturelle Fragen, nicht für Tagesarbeit.
