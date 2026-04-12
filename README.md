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
| `docs/business-case/` | Die 19 Original-Dokumente (v1) — Küche, Zahlen, Recht, Verpackung, Verkauf, Logistik. Gate-kritische Sequenz 03 → 15 → 05 → 04 → 14 lead-reviewt (Stufe 3). |
| `docs/personas/` | 12 rollenbasierte Review-Personas als Analyse-Linsen (00 Silvio Übersetzungs-Schicht, 01 CFO, 02 Lebensmittelrecht, 03 Steuer, 04 Behördenkontrolleur, 05 Logistiker, 06 Gastronom, 07 Küchenchef, 08 Brand/Marketing, 09 Stammkundin, 10 Dr. Maldini Regulatorik-Scout, 11 Personal-Markt & Arbeitsrecht Retail). |
| `docs/personas/assignments.md` | Matrix: welche Persona reviewt welches Doc. |
| `docs/findings/decisions.md` | Entscheidungs-Log D-01 bis D-10. Grundlegend für Scope- und Ton-Fragen. |
| `docs/findings/inconsistencies.md` | 16 Widersprüche zwischen den 19 Original-Docs. #5 aufgelöst (7 %-USt), #11 aufgelöst (Schreibort Rückruf). #7 MHD/Los/Chargen-Doku-als-Beweismittel, #12/13/14 aus Doc-14-Review. #15 Béchamel-Annahme ungeprüft (SP-19, bei Silvio). #16 Geschenkebox Sugo+Nudeln LMIV-Frage (SP-20). |
| `docs/reviews/` | Persona-Reviews im Standard-Format. **Lead-Reviews:** Doc 03 (Lebensmittelrechtler), Doc 15 (Steuerberaterin), Doc 05 (Lebensmittelrechtler HACCP), Doc 04 (Lebensmittelrechtler LMIV mit Rule 9), Doc 14 (Lebensmittelrechtler Recht mit Rule 9). **Co-Reviews (Session 10):** Doc 15 (CFO), Doc 03 (Behördenkontrolleur + Rule-9-Nachtrag), Doc 14 (Behördenkontrolleur + Steuerberaterin), Doc 04 (Behördenkontrolleur + Küchenchef), Doc 05 (Behördenkontrolleur + Küchenchef + Logistiker + Rule-9-Nachtrag). |
| `docs/findings/03-findings-veterinaeramt.md`, `04-findings-lmiv.md`, `05-findings-haccp.md`, `14-findings-recht-haftung.md`, `15-findings-steuer.md` | Konsolidierte Findings pro Doc, mit Auflösungs-Gruppen A (Silvio-Paket-Verweis), B (Repo-Arbeit), C (Doc-Rewrite). **109 Findings gesamt** (82 Lead + 27 Co-Review). |
| `docs/silvio-paket/offene-fragen.md` | **Zentrales Artefakt für Silvio-Aktionen.** 20 Einträge SP-01 bis SP-20 in sechs Blöcken (Behörden, Steuer/Kasse, Hygiene, Etikett, Recht/Versicherung, Rezepturen & Produktlinie). SP-19 (Béchamel-Frage) bei Silvio seit 2026-04-12. Silvio fasst das Repo nicht an — dieses Dokument ist der Ausgang, GitHub-Issues mit Label `feedback-silvio` sind der Eingang. |
| `docs/plans/03-v2-plan.md` | v2-Plan-Skizze Doc 03. Weitere v2-Pläne folgen nach Co-Reviews und Silvio-Rückmeldungen. |
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
- **D-03** — Keine Marcello-Persona. Das Repo ist Germans Arbeit an Silvios Case, kein Berater-Framing.
- **D-05** — Keine Easter Eggs in Reports. Stattdessen "Leitsatz der Session".
- **D-06** — Repo-Ton ist Germans Arbeits-Level. Silvio-facing Texte entstehen als explizite Ableitung, nicht als Default.
- **D-07** — Kein Investment. Bei Umsetzung: Aufwandsentschädigung auf Selbstkosten-Basis, transparent vor Silvios erstem Euro. Haltung in Persona 99 verankert.
- **D-08** — Phase A/B/C-Lebenszyklus.
- **D-09** — Rückruf-Prozess zweigeteilt: Doc 14 = Haftung/Krise, Doc 05 = Hygiene/Chargen, gegenseitig verlinkt.
- **D-10** — Silvio ist kein Reviewer. Aktionen in `docs/silvio-paket/offene-fragen.md` (SP-XX), Rückmeldungen über GitHub-Issues mit Label `feedback-silvio`.

## Personas

Analyse-Linsen, keine Narrative. Neue Personas rollen-basiert ohne Personennamen (Persona 11 ist der erste Fall). Jede Persona hat eine eigene Datei in `docs/personas/` mit Haltung, Fokus-Fragen, Red-Flags-Katalog. Die 12 Rollen decken: Zahlen (CFO), Lebensmittelrecht, Steuern, Küche, Gastronom (peer), Stammkundin, Brand/Marketing, Logistik, Amt (adversarial), Regulatorik-Scout (Dr. Maldini, horizontal), Personal-Markt & Arbeitsrecht Retail (neu Session 9), Silvio (Übersetzungs-Schicht, horizontal).

Reviews folgen dem Standard-Format aus [`CLAUDE.md`](CLAUDE.md#review-standard-format). Gate-kritische Sequenz (5 Docs, 14 Reviews, 109 Findings) ist vollständig reviewt (Lead + Co). v2-Rewrites und Sekundär-Reviews stehen aus.

## Stand

| Stufe | Thema | Status |
|---|---|---|
| 1 | Repo-Setup, plain markdown, GitHub | ✅ Done |
| 2 | 9 Personas + Ton-Reset + Marcello-Streichung | ✅ Done |
| 3 | Deep Review der 19 Business-Case-Docs | ⚠️ In Progress — **Gate-kritische Sequenz 03/15/05/04/14: Lead-Reviews + Co-Reviews abgeschlossen** (109 Findings, 14 Reviews). Rule-9-Nachzug Doc 03/05 erledigt. v2-Rewrites + Sekundär-Reviews Doc 06–19 stehen aus. **Blocker:** SP-19 (Béchamel-Rezeptur) vor v2-Rewrites klären. |
| 4 | Session-1-Wrap-up | ✅ Done |
| 5 | MASCHIN-Review + Maßnahmen 1/3/4 | ✅ Done |
| 6 | Repo-Zweck-Umschwung (Germans Arbeits-Level) | ✅ Done |

**Silvio-Paket:** Operative Aktionen für Silvio sind konsolidiert in [`docs/silvio-paket/offene-fragen.md`](docs/silvio-paket/offene-fragen.md) mit 20 Einträgen (SP-01 bis SP-20) in sechs Blöcken: Behörden, Steuer/Kasse, Hygiene, Etikett, Recht/Versicherung, Rezepturen & Produktlinie. SP-19 (Béchamel-Frage, P1-Blocker) ist bei Silvio seit 2026-04-12. SP-20 (Geschenkebox Sugo + Rummo-Nudeln) ist offen.

**Rule-9-Funde (Session 10):** Zwei neue Rechts-Stichtage entdeckt: (1) verschärfter **Listerien-Grenzwert ab 1.7.2026** — "nicht nachweisbar in 25g" statt bisheriger 100 KBE/g auf Handelsebene, direkt relevant für Béchamel-Produkte. (2) **Registrierungs-Portal-Korrektur** — "Luca-Portal" in Doc 03 ist falsch, richtig ist service-bw.de. Zusammen mit PPWR (12.8.2026) und ProdHaftG (9.12.2026) aus früheren Sessions gibt es jetzt **drei harte Rechts-Stichtage im zweiten Halbjahr 2026**.

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
