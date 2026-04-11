# Goldoni Retail Extension

Arbeits-Repo für den Business Case **Retail-Extension für das Ristorante Goldoni Stuttgart** (Vakuumierte Gerichte aus der laufenden Küche für den Außer-Haus-Verkauf). Inhaber: Silvio `[TBD-Nachname]`. Freundschaftsprojekt, kein Beratungsmandat. Owner: German Rauhut.

Dieses README ist die Arbeits-Übersicht für German selbst. Nicht Silvio-facing. Silvio liest das Repo nicht direkt — Silvio-Ableitungen entstehen ad-hoc, wenn konkret gebraucht (D-06, Variante B).

## Phase

**Phase A — aktiv** (D-08). Business-Case-Reviews, Scope-Schärfung, Rollout-Vorbereitung bis Silvio eine Entscheidung trifft (Ja / Nein / Später). Hoher Session-Takt zulässig.

Nach Silvios Entscheidung: Phase B (reduziert aktiv, Pilot-Begleitung) oder Phase C (Kontext-Speicher, keine Weiterentwicklung). Jede Maßnahme in diesem Repo muss die Frage bestehen: *"Brauchen wir das in der aktuellen Phase?"*

## Scope

Phase 1 des Produkts: **nur Vakuum, gekühlt, eine Woche Haltbarkeit**. Keine Tiefkühlung, kein Schockfroster, keine MAP/Schutzgas, kein Versand. Tiefkühl steht als mögliche Phase 2 auf der Roadmap (D-02), ist aber bewusst nicht im Launch-Scope.

Zielkanal: Abholung im Restaurant. Zielgruppe: Stammgäste, Büros im Stuttgarter Westen, Familien mit Convenience-Bedarf. Öffnungszeiten Goldoni: Mi + Do–So, 17–22 Uhr (zwei Küchen-Leerlauf-Tage Mo/Di als produktives Zeitfenster).

## Repo-Map

| Ordner / Datei | Inhalt |
|---|---|
| `docs/business-case/` | Die 19 Original-Dokumente (v1) — Küche, Zahlen, Recht, Verpackung, Verkauf, Logistik. Deep Review steht aus (Stufe 3, Backlog). |
| `docs/personas/` | 9 rollenbasierte Review-Personas als Analyse-Linsen (CFO, Lebensmittelrecht, Steuer, Koch, Gastronom, Stammkundin, Marketing, Logistik, Amt). Nicht Silvio-facing — Arbeitsmaterial. |
| `docs/personas/assignments.md` | Matrix: welche Persona reviewt welches Doc. |
| `docs/findings/decisions.md` | Entscheidungs-Log D-01 bis D-08. Grundlegend für Scope- und Ton-Fragen. |
| `docs/findings/inconsistencies.md` | 5 Widersprüche zwischen den 19 Original-Docs (aus MASCHIN-Voranalyse). |
| `docs/plans/rollout-plan.md` | Phase-1-Scope und Rollout-Reihenfolge. Wird in dieser Session ebenfalls auf Germans Arbeits-Level gezogen (Stufe 6 / 2b). |
| `docs/glossary.md` | Fachbegriffe (HACCP, LMIV, CCP, Vakuum vs. Schutzgas, Schockfroster, Vetamt). Primär als Silvio-Hilfe gedacht, auch für Germans Cross-Reference nützlich. |
| `docs/beteiligung.md` | Gerüst für die Frage "wer darf in welcher Form mitmachen" (D-07, offene Beteiligung). Inhaltlich leer, vier offene Fragen an German. |
| `docs/backlog/repo-backlog.md` | Status-Tabelle aller Arbeitspakete im MASCHIN-Format. |
| `docs/session-handoff.md` | Wie Sessions gestartet und geschlossen werden, Feedback-Workflow über GitHub-Issues. |
| `docs/reports/` | Session-Reports (chronologisch). |
| `session-state.md` | Aktueller Stage-Fortschritt und Phase. |
| `SESSION-PROMPT-NEXT.md` | Konkreter Auftrag für die nächste Session. |

## Entscheidungen

Voller Log in [`docs/findings/decisions.md`](docs/findings/decisions.md). Tragend für aktuelle Arbeit:

- **D-02** — Phase 1 nur Vakuum, Tiefkühl vertagt.
- **D-03** — Keine Marcello-Persona. Das Repo ist Germans Arbeit an Silvios Case, kein Berater-Framing.
- **D-05** — Keine Easter Eggs in Reports. Stattdessen "Leitsatz der Session".
- **D-06** — Repo-Ton ist Germans Arbeits-Level. Silvio-facing Texte entstehen als explizite Ableitung, nicht als Default.
- **D-07** — Offene Beteiligung: externe Personen können grundsätzlich beitragen, Form offen (siehe `docs/beteiligung.md`).
- **D-08** — Phase A/B/C-Lebenszyklus.

## Personas

Analyse-Linsen, keine Narrative. Keine Namen — nur Rollen. Jede Persona hat eine eigene Datei in `docs/personas/` mit Haltung, Fokus-Fragen, Red-Flags-Katalog. Die 9 Rollen decken: Zahlen (CFO), Lebensmittelrecht, Steuern, Küche (traditionell), Gastronom (peer), Stammkundin, Marken-/Marketing, Logistik, Amt.

Reviews folgen dem Standard-Format aus [`CLAUDE.md`](CLAUDE.md#review-standard-format). Deep Review der 19 Business-Case-Docs steht aus (Stufe 3, Backlog).

## Stand

| Stufe | Thema | Status |
|---|---|---|
| 1 | Repo-Setup, plain markdown, GitHub | ✅ Done |
| 2 | 9 Personas + Ton-Reset + Marcello-Streichung | ✅ Done |
| 3 | Deep Review der 19 Business-Case-Docs | 🔲 Backlog |
| 4 | Session-1-Wrap-up | ✅ Done |
| 5 | MASCHIN-Review + Maßnahmen 1/3/4 | ✅ Done |
| 6 | Repo-Zweck-Umschwung (Germans Arbeits-Level) | ⚠️ In Progress |

Operative Blocker bei Silvio (nicht vom Repo lösbar):

- MwSt-Einstufung durch Silvios Steuerberater.
- Vetamt-Voranfrage Stuttgart.
- Echter Nachname, Restaurant-Adresse, vorhandene Gerätebasis (Vakuumierer-Typ).
- Großhandels-Konditionen (Metro / Di Gennaro).

Siehe `docs/session-handoff.md` für den GitHub-Issue-Workflow zur Einspeisung von Silvio-Feedback.

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
