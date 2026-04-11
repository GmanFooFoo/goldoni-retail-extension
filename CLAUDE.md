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
9. **Regulatorik-Aktualität vor jedem Legal/Tax/Tech-Review (Dr. Maldini, Persona 10).** Bevor ein Lead-Review eines Docs mit Rechts-, Steuer-, KassenSichV-, DSGVO- oder Fernabsatz-Bezug geschrieben wird (mindestens Doc 02, 03, 04, 05, 06, 07, 13, 14, 15, 18), läuft eine aktive WebSearch auf den aktuellen Stand der betroffenen Rechtsgebiete. Das Ergebnis wird als **Regulatorik-Nachtrag** im Kopf des Reviews festgehalten, im Template aus `docs/personas/Persona 10 – Dr. Maldini – Fachanwalt Gastro Food Tech.md`. Begründung: Claudes Wissens-Cutoff ist vor dem aktuellen Jahr; ohne aktive Suche wird eine seit dem Cutoff geänderte Norm übersehen. Der 7%-USt-Fall 2026 in Doc 15 ist die Lehre, aus der die Regel entstanden ist.
10. **Silvio ist kein Reviewer — Silvio-Paket als Artefakt.** Silvio steht nie in der `Wer`-Spalte von Findings- oder Inconsistency-Tabellen. Die `Wer`-Spalte ist Review-Personas vorbehalten (CFO, Lebensmittelrechtler, Steuerberaterin, Behördenkontrolleur, Logistiker, Gastronom-Praktiker, Küchenchef, Brand & Marketing, Stammgast, Dr. Maldini). Jede Aktion, die Silvio selbst ausführen muss — Telefonate, E-Mails, Entscheidungen, Termine mit Behörden/Beratern/Lieferanten — wird als Eintrag `SP-XX` im zentralen Artefakt `docs/silvio-paket/offene-fragen.md` geführt. In Findings und Inconsistencies erscheint stattdessen ein Verweis `→ Silvio-Paket SP-XX`. Ausgang (Claude → German → Silvio) läuft über das Silvio-Paket; Eingang (Silvio → German → Repo) läuft über GitHub-Issues mit Label `feedback-silvio`. Begründung: Silvio ist der Kunde der Review-Arbeit, nicht ihr Mitarbeiter. Der Strukturfehler ist in Session 7 aufgefallen, nachdem Silvio systematisch in Wer-Spalten geschrieben worden war — das Silvio-Paket existierte nur als Prosa, nicht als Artefakt.
11. **AskUserQuestion bei 2+ Optionen Pflicht.** Sobald Claude German eine Auswahl zwischen zwei oder mehr Optionen präsentiert, wird das **AskUserQuestion**-Tool benutzt — nicht eine nummerierte Liste im Chat-Text. Das gilt auch für Varianten-Auswahl, Reihenfolge-Entscheidungen, Ton-Abstimmungen, Tool-Wahl und "jetzt A oder B?"-Fragen. Ausnahmen: (a) reine Rückfragen zu einem einzigen Punkt (Ja/Nein reicht), (b) bei Freitext-Antworten, die keine vorgegebenen Optionen haben. Begründung: German will per Tastendruck entscheiden können, nicht im Fließtext nach der Option suchen. Memory-Eintrag `feedback_askuserquestion_preferred.md` existiert seit früh, wird hier als Projekt-Rule festgezurrt.
12. **Eine Frage nach der anderen.** Bei interaktiven Befragungen, Klärungs-Dialogen oder Deep-Dives (zum Beispiel Persona-Kalibrierung, Interview-artige Gespräche zwischen German und Claude) wird **genau eine Frage pro Nachricht** gestellt. Keine Listen mit 3–10 Fragen auf einmal, auch wenn sie thematisch gruppiert sind. Begründung: Mehrfach-Fragen überfordern, zerschneiden den Gedanken und führen dazu, dass einzelne Punkte oberflächlich bleiben. Die Antwort auf Frage 1 verändert oft, wie Frage 2 überhaupt gestellt werden sollte — also erst antworten lassen, dann weiterfragen. Ausnahmen: Tabellen oder Checklisten, die German asynchron ausfüllt (z. B. ein Frage-Dokument zum Anhaken), sind erlaubt, müssen aber explizit so benannt sein.

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
- `docs/personas/` — 11 rollenbasierte Review-Personas: Persona 00 Silvio (Übersetzungs-Schicht, horizontal), 01 Marcus CFO, 02 Dr. Steiger Lebensmittelrechtler, 03 Frau Keller Steuerberaterin, 04 Inspektor Vogel Behördenkontrolleur, 05 Bruno Logistiker, 06 Thomas Gastronom-Praktiker, 07 Pietro Küchenchef, 08 Jana Brand & Marketing, 09 Claudia Stammgast, 10 Dr. Maldini Fachanwalt Gastro/Food/Tech (Regulatorik-Scout, Co-Reviewer auf allen Rechts/Steuer/Tech-Docs) + `assignments.md` Matrix
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
