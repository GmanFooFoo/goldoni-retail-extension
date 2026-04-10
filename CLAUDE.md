# CLAUDE.md — Goldoni Retail Extension

## Project

German bereitet einen Business Case für seinen Freund **Silvio** auf, den Inhaber des italienischen Restaurants **Goldoni** in Stuttgart. Es geht um eine Retail-Extension: vakuumierte Gerichte (Lasagne, Sugo, Ragù, Parmigiana) aus der laufenden Küche für den Außer-Haus-Verkauf.

Das ist **kein Kundenauftrag** und **kein Beratungsmandat**. Silvio und German sind Freunde. German macht das, weil er die Idee spannend findet und Silvio dabei helfen will, sie sauber aufzusetzen. Silvio soll am Ende etwas in der Hand haben, das er seinem Steuerberater, seiner Bank oder dem Veterinäramt vorlegen kann, ohne dass jemand die Augenbrauen hochzieht.

- **Inhaber:** Silvio `[TBD-Nachname]`
- **Adresse:** `[TBD-Silvio]`
- **Öffnungszeiten:** Mi + Do–So, 17–22 Uhr
- **Zielkanal:** Abholung im Restaurant + ggf. lokale Lieferung
- **Zielgruppe:** Stammgäste, Büros im Stuttgarter Westen, Familien mit Convenience-Bedarf

## Deine Rolle (Claude)

Du bist Claude. Du unterstützt German beim Aufbereiten, Strukturieren und Prüfen der Dokumente in diesem Repo. Du bist **kein eigenständiger Berater, kein Marcello, keine Persona**. Der menschliche Projekt-Owner ist German, und die Arbeit erscheint Silvio gegenüber als Germans Arbeit.

Der Ton in Silvio-gerichteten Texten (README, docs/index, Brief-Passagen) ist **freundschaftlich**, nicht beratend. Keine Deadlines, keine Forderungen, keine Consulting-Terminologie. German und Silvio sind befreundet; du schreibst in Germans Namen und Stimme.

**Vorbilder für die analytische Schärfe** (aber ohne Berater-Pose): Marty Cagan (Product Discovery), Ray Dalio (Principles), Andy Grove (OKR-Klarheit).

## Rules

1. **Jede Zahl braucht eine Quelle** oder `[TBD-Silvio]` / `[TBD-Recherche]`-Marker. Keine erfundenen Werte.
2. **Widersprüche** zwischen Dokumenten sofort in `docs/findings/inconsistencies.md` protokollieren.
3. **Silvio-freundliche Sprache.** Der Mann ist Gastronom, kein Jurist und kein BWLer. Glossar in `docs/glossary.md` verlinken, Fachbegriffe erklären.
4. **Review-Output** immer im Standard-Format (siehe unten).
5. **Commit nach jedem Work-Block**, nicht erst am Session-Ende.
6. **Kein v2-Rewrite** der 19 Original-Docs ohne vorherige Findings + Plan.
7. **README.md ist Silvios Seite.** Sie bleibt in Silvio-freundlicher Sprache (ELI12, Brief-Ton, Navigations-Zentrale) und wird **nach jedem Work-Block aktualisiert** (neuer Status, neue Links, neue Findings, neue Fragen an Silvio). Technische Details gehören in diese `CLAUDE.md`, nicht in `README.md`.
8. **Echter Name:** In den Mockups steht "Marco Antonelli". Silvios echter Name und Adresse sind `[TBD-Silvio]` — bis er sie bestätigt.

## Review Standard-Format

Jede Persona-Review folgt diesem Schema:

```markdown
# Review: [Doc-Nummer] – [Doc-Titel]
**Reviewer:** [Persona-Name]
**Datum:** YYYY-MM-DD
**Doc-Version:** v1

## Kurzurteil (1 Satz)

## Scoring (1–5)
- Fachliche Korrektheit:
- Vollständigkeit:
- Umsetzbarkeit:
- Risiko-Abdeckung:

## Red Flags
- ...

## Fundierte Kritikpunkte
- ...

## Was fehlt
- ...

## Empfehlung
- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [ ] Rework erforderlich
- [ ] Stopp — geht so nicht live
```

## Structure

- `docs/business-case/` — die 19 Original-Dokumente (v1, unberührt)
- `docs/personas/` — 9 rollenbasierte Review-Personas (Marcus, Dr. Steiger, Frau Keller, Inspektor Vogel, Bruno, Thomas, Pietro, Jana, Claudia) + `assignments.md` Matrix
- `docs/findings/inconsistencies.md` — Widersprüche zwischen Dokumenten
- `docs/plans/rollout-plan.md` — Phase 1/2 Scope + Zeitplan
- `docs/backlog/repo-backlog.md` — Status-Tabelle
- `docs/glossary.md` — Fachbegriffe
- `docs/session-handoff.md` — wie Sessions gestartet und sauber geschlossen werden
- `docs/reports/` — Session-Reports (angelegt nach Bedarf)

Später, sobald Reviews starten:

- `docs/reviews/` — Persona-Reviews pro Doc
- `docs/findings/[doc-nummer]-findings.md` — konsolidierte Findings pro Doc
- `docs/plans/[doc-nummer]-v2-plan.md` — Revisionspläne pro Doc

## Keine Reader-Site

Wir arbeiten direkt mit **GitHub + lokalen Verzeichnissen**. Kein MkDocs,
kein Vercel, kein Static-Site-Builder. Alle Markdown-Dateien sind auf
GitHub direkt lesbar. Falls später eine Silvio-freundliche Web-Ansicht
gebraucht wird, entscheiden wir das neu.

## Session Discipline

- **Commit nach jedem Work-Block.**
- **Backlog und session-state.md** nach jedem Block aktualisieren.
- **Status-Tabellen** in MASCHIN-Format: `# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`.
- **T-Shirt-Effort:** XS (<30min) / S (1–2h) / M (halber Tag) / L (ganzer Tag) / XL (mehrere Tage).
- **Completion:** "in-review" ≠ "done". Done = von zweiter Instanz geprüft (in diesem Projekt: Silvio bestätigt oder nächste Persona-Cross-Review).
